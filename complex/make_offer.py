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
# offer =
# {
#   "item_id": this.results.item_id,    # based on item selected
#   "price": this.price,                # input by buyer on UI 
#   "buyer_id": this.buyer_id             # stored on the browser (user_id)
# }

# Make sure the following microservices are running:
# profile.py        # load profile.sql data
# item.js           # node installed + MongoDB database
# error_new.py          # AMQP routing_key = 'error.*'
# twilio_notifs.py  # AMQP routing_key = 'notify.*' 

profile_URL =  "http://localhost:5000/profile/" # requires :user_id
item_URL = "http://localhost:5001/items/" # requires :item_id

@app.route("/make_offer", methods=['POST']) # pass in offer details
def make_offer(): # BUYER invokes this complex microservice, request = {offer} 
    # First check if input format and data of the request are JSON
    if request.is_json:
        try:
            offer = request.get_json() 
            print("\nReceived an offer in JSON:", offer)

            # 1. Send offer info {offer} to processMakeOffer to do the work
            result = processMakeOffer(offer)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "make_offer.py internal error: " + ex_str
            }), 500

    # if reached here, means input was not a JSON request to begin with (refer to next comment)
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def processMakeOffer(offer): # process the json input of /make_offer (BUYER)

    # 2. Invoke the profile microservice to retrieve mobile number to send messgage thru notification ['GET']
        # a. Send user_id
        # b. Return name, mobile / error

    user_id = offer['buyer_id']
    print('\n\n-----Invoking profile microservice-----')
    profile_results = invoke_http(profile_URL + user_id, method="GET")
    name = profile_results['data']['name']
    mobile = profile_results['data']['mobile']
    print("\nRetrieved name:", profile_results['data']['name'])
    print("\nRetrieved mobile:", profile_results['data']['mobile'])

    code = profile_results["code"]


    # 6. Return error if profile not retrieved
    if code not in range(200, 300):
        return {
            "code": 404,
            "data": {"profile_results": profile_results},
            "message": "Error while trying to retrieve profile information"
        }



    # 3. Update item details (mobile, buyer_id) ['PUT']
        # Invoke the item microservice
        # a. Send offer_details (buyer_id, buyer_name, buyer_mobile, item_status)
        # b. Return offer_result / error

    item_id = offer['item_id']
    price = offer['price']
    print('\n-----Invoking item microservice to update offer details-----')
    offer_details = { 
        "buyer_id": user_id, 
        "buyer_name": name, 
        "buyer_mobile": mobile, 
        "item_status": 'pending', 
        "price": price
        }
    offer_result = invoke_http(item_URL + item_id, method='PUT', json=offer_details)
    print("\nItem has been updated with buyer information:", offer_details)
    print("\nOffer result:", offer_result)




    # 4. Check if the item update failed [AMQP]
        # a. Send the error to the error microservice to log failure (routing_key = 'error.*' )

    code = offer_result["code"]
    message = json.dumps(offer_result)

    print('This is the message to error')
    print(type(message))

    if code not in range(200, 300):
        # Inform the error microservice 
        print('\n\n-----Publishing the failed offer error message with routing_key= error.offer-----')
        amqp_setup.check_setup()
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="error.offer", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2) # message is persistent within the matching queues until received by error_new.py 
        ) 
        
        print("\nOffer failure ({:d}) published to the RabbitMQ Exchange:".format(code), offer_result)


        # 6. Return error and end here
        return {
            "code": 500,
            "data": {"offer_result": offer_result},
            "message": "Make offer failure is sent for error handling."
        }


    # Publish to twilio_notifs only when there is no error in making offer 

    else: 
        # 5. Send offer success to twilio_notifs [AMQP]
            # a. Send the message and seller mobile number to the notification microservice to inform seller of offer (routing_key = 'notify.*' )
        
        seller_mobile = offer_result['Success']['seller_mobile']
        item_name = offer_result['Success']['item_name']

        data = {
            'mobile': seller_mobile,
            'message': f"You have a new offer for '{item_name}'. Please check your listings under 'My Listings' in Henesys to accept or reject the offer." 
            }
        
        message = json.dumps(data)
        print('This is the message to notif')
        print(type(message))

        print('The following message will be sent:' + message)
        print('\n\n-----Publishing the successful offer message with routing_key=notify.offer-----')  
        amqp_setup.check_setup()
        amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="notify.offer", 
        body=message, 
        properties=pika.BasicProperties(delivery_mode = 2) # message is persistent within the matching queues until received by twilio_notifs.py 
        )
        
        print(message)
        print("\nOffer success ({:d}) published to the RabbitMQ Exchange:".format(code), offer_result)



    # 6. Return the updated offer (item) details if successful
    return {
        "code": 201,
        "data": {
            "offer_result": offer_result,
        }
    }

# Execute this program if it is run as a main script and not by 'import'
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for making an offer...")
    app.run(host="0.0.0.0", port=5200, debug=True) 