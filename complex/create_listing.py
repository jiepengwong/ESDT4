from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json
from types import SimpleNamespace

# import amqp_setup
# import pika
# import json

app = Flask(__name__)
CORS(app)

create_item_URL = "http://localhost:5000/createitems"
profile_URL =  "http://localhost:5001/profile/" # requires /:id

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
profile = json.loads(listing, object_hook=lambda d: SimpleNamespace(**d))
id = profile.user_id


profile_details = invoke_http(
    profile_URL + id, method='GET', 
    )

# to remove
print( "----- invoking profile microservice to get profile details -----" )
print (profile_details)

profile_details = json.loads(listing, object_hook=lambda d: SimpleNamespace(**d))