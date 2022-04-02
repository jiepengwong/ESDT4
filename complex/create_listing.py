from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json
from types import SimpleNamespace

app = Flask(__name__)
CORS(app)

# input JSON:
# listing = 
# {
#     "seller_id": this.user_id,             # user_id stored on the browser (user_id)
#     "item_details": {                      # field input from user from create page
#         "item_name": "Bag of Carrots ",
#         "category": "Vegetables",
#         "description": "Unused packet of carrots. Expires 3 May.",
#         "location": "80 Kallang Rd #03-26",
#         "date_time": 2022-04-13 16:30:00
#     }
# } 

profile_URL =  "http://localhost:5000/profile/" # requires /:id
create_item_URL = "http://localhost:5001/createitem"

@app.route("/create_listing", methods=['POST'])
def create_listing():
    # Check if input format and data of the request are in JSON format
    if request.is_json:
        try:
            listing = request.get_json()
            print("\nReceived a valid request in JSON:", listing)

            # 1. Send the item information and user ID - {seller_id}, {item_details}
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

    # 2. Invoke the profile microservice to retrieve seller details ['GET'] 
        # a. Send user_id
        # b. Return name, mobile  

    user_id = listing['seller_id']
    print('\n\n-----Invoking profile microservice-----')
    profile_details = invoke_http(profile_URL + user_id, method="GET")
    name = profile_details['data']['name']
    mobile = profile_details['data']['mobile']
    print("\nname:", profile_details['data']['name'])
    print("\nmobile number:", profile_details['data']['mobile'])

    item_details = listing['item_details']

    # 3. Invoke the item microservice ['POST']
        # a. Send the item information, change status and mobile {item}, {mobile}
        # b. Return 
    # POST back new item_num
    # GET new item_num

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

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 