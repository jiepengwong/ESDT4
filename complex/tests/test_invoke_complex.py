from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json
from types import SimpleNamespace

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

profile_URL =  "http://localhost:5000/profile/" # requires /:id
create_item_URL = "http://localhost:5001/createitem"
item_URL = "http://localhost:5000/items/" # requires :item_id

@app.route("/create_listing", methods=['POST'])
def create_listing():
    # Check if input format and data of the request are in JSON format
    if request.is_json:
        try:
            listing = request.get_json()
            print("\nReceived a valid request in JSON:", listing)

            # 1. Send the item information and profile ID - {item}, {user_id}
            result = processCreateListing(listing)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "create_listing.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def processCreateListing(listing):

# invoke profile microservice to create a book

#stringify JSON request
    # listing_details = json.load(listing_json, object_hook=lambda d: SimpleNamespace(**d))
    # id = listing_details.user_id
    # print (id)
    id = listing['user_id']


    profile_details = invoke_http(
        profile_URL + id, method='GET', 
        )

    # to remove
    print( "----- invoking profile microservice to get profile details -----" )
    # print (profile_details)

    # profile_details = json.loads(listing, object_hook=lambda d: SimpleNamespace(**d))

    return {
        "code": 201,
        "data": {
            "result": profile_details,
        }
    }


        # HTTP Version (Old)
        # print('\n\n-----Invoking error microservice as offer fails-----')
        # invoke_http(error_URL, method="POST", json=offer_result)
        # # result from the invocation is not used
        # # continue even if this invocation fails
        # print("Offer status ({:d}) sent to the error microservice:".format(code), offer) #tbc

        # HTTP below
        # print('\n\n-----Invoking notification microservice-----')
        # invoke_http(notification_URL, method="POST", json=offer_result)
        # print("\nOffer sent to notification microservice.\n")
        # if code not in range(200, 300):
    #     # Inform the error microservice (AMQP routing_key = 'error.*' )
    #     print('\n\n-----Invoking error microservice as offer fails-----')
    #     invoke_http(error_URL, method="POST", json=offer_result)
    #     # result from the invocation is not used
    #     # continue even if this invocation fails

    # profile_details = json.loads(listing, object_hook=lambda d: SimpleNamespace(**d))


    
    # @app.route('/')
    # def healthcheck():
    #     return 'Accept Offer is up and running!';

    #wt: tHE following is used for testing 

    # @app.route('/test')
    # def test():
    #     one_notif = {
    #         "Notification_ID": 12345,
    #         "Seller_ID": "1",
    #         "Buyer_ID": "1",
    #         "Status": "1",
    #         "Message": "I am ok",
    #         "DateTimeSQL": 12345
    #     }
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.error", 
    #     body=one_notif, properties=pika.BasicProperties(delivery_mode = 2)) 


    """A simple wrapper for requests methods.
       url: the url of the http service;
       method: the http method;
       data: the JSON input when needed by the http method;
       return: the JSON reply content from the http service if the call succeeds;
            otherwise, return a JSON object with a "code" name-value pair.
    """

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
