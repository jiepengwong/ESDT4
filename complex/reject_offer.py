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
# reject = 
# {
#   "item_id": "XXXXXXXX" 
# } 

# Make sure the following microservices are running:
# item.js           # node installed + MongoDB database
# error_new.py          # AMQP routing_key = 'error.*'
# twilio_notifs.py  # AMQP routing_key = 'notify.*' 

item_URL = "http://item:5001/items/" # requires :item_id


@app.route("/reject_offer", methods=['POST'])
def reject_offer(): # SELLER invokes this complex microservice to reject an offer, request = {reject} 
    #  Check that input format of the request is in JSON
    if request.is_json:
        try:
            rejected = request.get_json()
            print("\nReceived rejected item in JSON:", rejected)

            # 1. Send rejected item info {reject}
            result = processRejectOffer(rejected)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "reject_offer.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processRejectOffer(rejected):  # process the json input of /reject_offer

    # 2.  Invoke the item microservice to get item details ['GET']
    item_id = rejected['item_id']
    print('\n-----Invoking item microservice to get item details-----')
    item_result = invoke_http(item_URL + item_id)

    # store item details for notification later
    buyer_mobile = item_result['Success']['buyer_mobile']
    price = item_result['Success']['price']

    # 6. Return error if invocation fails
    code = item_result["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"item_result": item_result},
            "message": "Unable to get item details."
        }



    # 3.  Invoke the item microservice to update item_status ['PUT']
    rejected_details = {
        "item_status": 'open',
        "buyer_id": None, # reset to null
        "buyer_name": None,
        "buyer_mobile": None,
        "price": None
        }
    print('\n-----Invoking item microservice to update item status-----')
    reject_result = invoke_http(item_URL + item_id, method='PUT', json=rejected_details)
    print('\nItem details has been reset to remove buyer offer. Item status changed back to open:', reject_result)



    # 4. Check if the reject of item has failed [AMQP]
        # a. Send the error to the error microservice to log this failure (routing_key = 'error.reject')

    code = reject_result["code"]
    message = json.dumps(reject_result)

    if code not in range(200, 300):
        # Inform the error microservice 
        print('\n\n-----Publishing the failed reject offer error message with routing_key= error.reject-----')
        amqp_setup.check_setup()
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="error.reject", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2)
        ) 
        # message is persistent within the matching queues until received by notification.py        
        print("\n Item reject failure ({:d}) published to the RabbitMQ Exchange:".format(code), reject_result)

        # 6. Return error and end here
        return {
            "code": 500,
            "data": {"reject_result": reject_result},
            "message": "reject offer failure is sent for error handling."
        }


    # Publish to twilio_notifs only when there is no error in rejecting offer 

    else: 
        # 5. Send reject offer success to twilio_notifs [AMQP]
            # a. Send the message and buyer mobile number to the notification microservice to inform buyer of rejected offer (routing_key = 'notify.reject')
        
        seller_name = reject_result['Success']['seller_name']
        item_name = reject_result['Success']['item_name']
        
        data = {
            "mobile": buyer_mobile,
            "message": f"Your offer for '{item_name}' has been rejected by {seller_name}. Your previous offer was ${price}.\n\nPlease make another offer for the item in Henesys if it is still available." # item is placed back to catalogue
            }
        
        message = json.dumps(data)
        print('The following message will be sent:' + message)
        print('\n\n-----Publishing the successful rejected offer message with routing_key=notify.reject-----')    
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="notify.reject", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2) # message is persistent within the matching queues until received by twilio_notifs.py 
        )
        
        print(message)
        print("\nOffer rejectance ({:d}) published to the RabbitMQ Exchange:".format(code), reject_result)



    # 6. Return the details of rejected offer if successful
    return {
        "code": 201,
        "data": {
            f"reject_result": reject_result, # confirmation for seller
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for rejecting an offer...")
    app.run(host="0.0.0.0", port=5400, debug=True)
    