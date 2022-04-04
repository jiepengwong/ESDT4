from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import json
import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

# input JSON:
# rate = 
# {
#   "item_id": "XXXXXXXX"   # item being reviewed
#   "rating": 4             # input 1-5
# } 

# Make sure the following microservices are running:
# profile.py        # load profile.sql data
# item.js           # node installed + MongoDB database

rate_profile_URL =  "http://profile:5000/profile/ratings/" # requires :seller_id
item_URL = "http://item:5001/items/" # requires :item_id

@app.route("/leave_rating", methods=['POST'])
def leave_rating(): # BUYER invokes this complex microservice to review seller of item, request = {rate} 
    # Check that input format of the request is in JSON
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


def processLeaveRating(rate):  # Process the JSON input of /leave_rating

    # 2.  Invoke the item microservice to get the item's seller details ['GET']
    item_id = rate['item_id']
    print('\n-----Invoking item microservice to get seller details of item-----')
    item_result = invoke_http(item_URL + item_id)
    print('\nItem result:', item_result)
    
    # 5. Return error if invocation fails
    code = item_result["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"item_result": item_result},
            "message": "Unable to get item details."
        }
    
    # If success, store seller_id for updating profile later
    seller_id = item_result['Success']['seller_id']
    print('\nseller_id retrieved:', seller_id)



    # 3.  Invoke the profile microservice to update rating ['PUT']
    ratings = rate['rating']
    rating_details = { 
        "ratings": ratings
        }
    
    print('\n-----Invoking profile microservice to update overall ratings of seller-----')
    rating_result = invoke_http(rate_profile_URL + seller_id, method='PUT', json=rating_details)
    print('\nProfile update result:', rating_result)

    # 5. Return error if invocation fails
    code = rating_result["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"rating_result": rating_result},
            "message": "Unable to update profile rating."
        }



    # 4.  Invoke the item microservice to update item_status ['PUT']
    print('\n-----Invoking item microservice to update item status-----')
    new_status = {
        "item_status": "closed"
    }
    item_update = invoke_http(item_URL + item_id, method='PUT', json=new_status)
    print('\nItem update result:', item_update)

    # 5. Return error if invocation fails
    code = item_update["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"item_update": item_update},
            "message": "Unable to update item."
        }



    # 5. Return the details of leave_rating if successful
    return {
        "code": 201,
        "data": {
            "rating_result": rating_result,
        }
    }



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for leaving a review...")
    app.run(host="0.0.0.0", port=5500, debug=True) 