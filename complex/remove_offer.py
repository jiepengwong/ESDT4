from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http


app = Flask(__name__)
CORS(app)

# input JSON:
# remove = 
# {
#   "item_id": "XXXXXXXX" 
# } 

# Make sure the following microservices are running:
# profile.py        # load profile.sql data
# item.js           # node installed + MongoDB database


profile_URL =  "http://localhost:5000/profile/" # requires :user_id
item_URL = "http://localhost:5001/items/" # requires :item_id


@app.route("/remove_offer", methods=['POST'])
def remove_offer(): # SELLER invokes this complex microservice to reject an offer, request = {reject} 
    #  Check that input format of the request is in JSON
    if request.is_json:
        try:
            remove = request.get_json()
            print("\nReceived removed offer details in JSON:", remove)

            # 1. Send rejected item info {reject}
            result = processRemoveOffer(remove)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "remove_offer.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processRemoveOffer(remove):  # process the json input of /remove_offer

    # 2.  Invoke the item microservice to update item_status ['PUT']
    item_id = remove['item_id']
    removed_details = {
        "item_status": 'open',
        "buyer_id": None, # reset to null
        "buyer_name": None,
        "buyer_mobile": None,
        "price": None
        }
    print('\n-----Invoking item microservice to update item status-----')
    remove_result = invoke_http(item_URL + item_id, method='PUT', json=removed_details)
    print('\nItem details has been reset to remove buyer offer. Item status changed back to open:', remove_result)

    # 5. Return the details of rejected offer if successful
    return {
        "code": 201,
        "data": {
            f"remove_result": remove_result, # confirmation for seller
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for removing an offer...")
    app.run(host="0.0.0.0", port=5600, debug=True)
    