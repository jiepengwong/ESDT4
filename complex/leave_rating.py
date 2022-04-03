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
# rate = 
# {
#   "item_id": "XXXXXXXX"   # item being reviewed
#   "ratings": 4             # input 1-5
# } 

# Make sure the following microservices are running:
# profile.py        # load profile.sql data

rate_profile_URL =  "http://localhost:5000/profile/ratings/" # requires :seller_id
item_URL = "http://localhost:5001/items/" # requires :item_id

@app.route("/leave_rating", methods=['POST'])
def leave_rating(): # BUYER invokes this complex microservice to review seller of item, request = {rate} 
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            rate = request.get_json()
            print("\nReceived input in JSON:", rate)

            # 1. Send item and rating info {rate}
            result = processLeaveRating(rate)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "leave_rating.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processLeaveRating(rate):  # process the json input of /leave_rating

    # 2.  Invoke the item microservice to get item details ['GET']
    item_id = rate['item_id']
    print('\n-----Invoking item microservice to get item details-----')
    item_result = invoke_http(item_URL + item_id)

    # store seller_id for updating profile later
    seller_id = item_result['Success']['seller_id']



    # 3.  Invoke the profile microservice to update rating ['PUT']
    ratings = rate['ratings']
    rating_details = { 
        "ratings": ratings
        }
    
    print('\n-----Invoking profile microservice to update overall ratings of seller-----')
    rating_result = invoke_http(rate_profile_URL + seller_id, method='PUT', json=rating_details)
    print('\nProfile has been updated with new average rating:', rating_result)



    # 4. Return the details of leave review if successful
    return {
        "code": 201,
        "data": {
            f"Rating has been given for the seller.": rating_result, # confirmation for seller
        }
    }



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 