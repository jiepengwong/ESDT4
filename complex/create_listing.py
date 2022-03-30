from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json
from types import SimpleNamespace

app = Flask(__name__)
CORS(app)

profile_URL =  "http://localhost:5000/profile/" # requires /:id
create_item_URL = "http://localhost:5001/createitem"

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

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 