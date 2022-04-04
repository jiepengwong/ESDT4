from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

# input JSON:
# accept = 
# {
#   "item_id": "XXXXXXXX" 
# } 

# Make sure the following microservices are running:
# profile.py        # load profile.sql data
# item.js           # node installed + MongoDB database
# error_new.py          # AMQP routing_key = 'error.*'
# twilio_notifs.py  # AMQP routing_key = 'notify.*' 

profile_URL =  "http://localhost:5000/profile/" # requires :user_id
item_URL = "http://localhost:5001/items/" # requires :item_id


@app.route("/accept_offer", methods=['POST'])
def accept_offer(): # SELLER invokes this complex microservice to accept an offer, request = {accept} 
    # Check that input format of the request is in JSON
    if request.is_json:
        try:
            accepted = request.get_json()
            print("\nReceived accepted item in JSON:", accepted)

            # 1. Send accepted item info {accept}
            result = processAcceptOffer(accepted)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "accept_offer.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processAcceptOffer(accepted):  # process the json input of /accept_offer

    # 2.  Invoke the item microservice to update item_status ['PUT']
    item_id = accepted['item_id']
    print('\n-----Invoking item microservice to update item status-----')
    accepted_details = {"item_status": 'accepted'}
    accept_result = invoke_http(item_URL + item_id, method='PUT', json=accepted_details)
    print('\nItem status:', accept_result)

    # 5. Return error if invocation fails
    code = accept_result["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"accept_result": accept_result},
            "message": "Unable to update/accept item."
        }



    # 3. Check if acceptance of item failed [AMQP]
        # a. Send the error to the error microservice to log this failure (routing_key = 'error.*' )

    code = accept_result["code"]
    message = json.dumps(accept_result)

    if code not in range(200, 300):
        # Inform the error microservice 
        print('\n\n-----Publishing the failed accept offer error message with routing_key= error.accept-----')
        amqp_setup.check_setup()
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="error.accept", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2)
        ) 
        # message is persistent within the matching queues until received by notification.py        
        print("\n Item accept failure ({:d}) published to the RabbitMQ Exchange:".format(code), accept_result)

        # 5. Return error and end here
        return {
            "code": 500,
            "data": {"accept_result": accept_result},
            "message": "Accept offer failure is sent for error handling."
        }



    # Publish to twilio_notifs only when there is no error in accepting offer 
    else: 
        # 4. Send accept offer success to twilio_notifs [AMQP]
            # a. Send the message and buyer mobile number to the notification microservice to inform seller of accepted offer (routing_key = 'notify.*' )
        
        buyer_mobile = accept_result['Success']['buyer_mobile']
        seller_name = accept_result['Success']['seller_name']
        item_name = accept_result['Success']['item_name']
        
        data = {
            "mobile": buyer_mobile,
            "message": f"Your offer for '{item_name}' has been accepted by {seller_name}. Please check your offers under 'My Offers' page in Henesys to view the confirmed details." # collection date, time, location, price will be displayed there
            }
        
        message = json.dumps(data)
        print('The following message will be sent:' + message)   # for debugging, to remove
        print('\n\n-----Publishing the successful accepted offer message with routing_key=notify.accept-----')    
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="notify.accept", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2) # message is persistent within the matching queues until received by twilio_notifs.py 
        )
        
        print(message)
        print("\nOffer acceptance ({:d}) published to the RabbitMQ Exchange:".format(code), accept_result)



    # 5. Return the details of accepted offer if successful
    return {
        "code": 201,
        "data": {
            f"accept_result:": accept_result, # confirmation for seller
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an accepted...")
    app.run(host="0.0.0.0", port=5300, debug=True)

