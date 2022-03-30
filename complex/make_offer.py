from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
import json
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
#   "buyerid": this.buyerid             # stored on the browser (user_id)
# }

# make sure the following microservices are running:
profile_URL =  "http://localhost:5000/profile/" # requires :user_id
item_URL = "http://localhost:5000/items/" # requires :item_id
notification_URL = "http://localhost:5002/notification" # AMQP routing_key = 'notify.*' 
error_URL = "http://localhost:5001/error" # AMQP routing_key = 'error.*'
# need to change port for multiple services

@app.route("/make_offer", methods=['POST']) # pass in offer details
def make_offer(): # BUYER invokes this complex microservice, request = offer 
    # First check if input format and data of the request are JSON
    if request.is_json:
        try:
            offer = request.get_json() 
            print("\nReceived an offer in JSON:", offer)

            # 1. Send offer info {offer details}
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

    # 1. Invoke the profile microservice to retrieve mobile number to send messgage thru notification
        # a. request user_id
        # b. return name, mobile  
    user_id = offer['buyerid']
    print('\n\n-----Invoking profile microservice-----')
    profile_details = invoke_http(profile_URL + user_id, method="GET")
    name = profile_details['name']
    mobile = profile_details['mobile']
    print("\nname:", profile_details['name'])
    print("\nmobile number:", profile_details['mobile'])

    # 2. Update item details (mobile, buyerid) using PUT to add new offer details
        # Invoke the item microservice
        # a. PUT offer_details (buyer_id, buyer_name, buyer_mobile, item_status)
        # b. return offer_result
    print('\n-----Invoking item microservice-----')
    offer_details = { "buyer_id": user_id, "buyer_name": name, "buyer_mobile": mobile, "item_status": 'pending'}
    offer_result = invoke_http(item_URL, method='PUT', json=offer_details)
    print("\nitem updated with buyer information:", offer)

    # 3. Check the item update result succeeded 
        # if failure:       
            # a. send the error to the error microservice to inform of failure
            # b. return error message
    code = offer["code"]
    if code not in range(200, 300):
        # Inform the error microservice (AMQP routing_key = 'error.*' )
        print('\n\n-----Invoking error microservice as offer fails-----')
        invoke_http(error_URL, method="POST", json=offer_result)
        # result from the invocation is not used
        # continue even if this invocation fails
        print("Offer status ({:d}) sent to the error microservice:".format(code), offer) #tbc

        # Return error
        return {
            "code": 500,
            "data": {"offer_result": offer_result},
            "message": "Offer creation failure is sent for error handling."
        }

    # 4. Record new offer in notification (AMQP routing_key = 'notify.*' )
    # Send information to notification
    print('\n\n-----Invoking notification microservice-----')
    invoke_http(notification_URL, method="POST", json=offer_result)
    print("\nOffer sent to notification microservice.\n")
    code = offer["code"]
    if code not in range(200, 300):
        # Inform the error microservice (AMQP routing_key = 'error.*' )
        print('\n\n-----Invoking error microservice as offer fails-----')
        invoke_http(error_URL, method="POST", json=offer_result)
        # result from the invocation is not used
        # continue even if this invocation fails

    # 5. Return created offer + notification of result
    return {
        "code": 201,
        "data": {
            "offer_result": offer_result,
        #     "notification_result": notification_result
        }
    }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 