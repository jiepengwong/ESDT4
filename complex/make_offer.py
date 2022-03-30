from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

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
notification_URL = "http://localhost:5002/notification" # requires AMQP
error_URL = "http://localhost:5001/error" # AMQP 
# need to change port for multiple services

@app.route("/make_offer", methods=['POST'])
def make_offer(): # BUYER invokes this complex microservice, requests using offer details 
    # First check if input format and data of the request are JSON
    if request.is_json:
        try:
            offer = request.get_json() 
            print("\nReceived an offer in JSON:", offer)

            # # do the actual work
            # # 1. Send offer info {offer details}
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

    # 0. (REMOVED as this is the json input) Get information of items requested in offer (GET one item)
    # Invoke the item microservice
    # print('\n-----Invoking item microservice-----')
    # item_result = invoke_http(item_URL, method='GET', json=offer)
    # print('item_result:', item_result)

    # 1. Invoke the profile microservice to GET full profile 
        # a. request profile_id
        # b. return mobile   
    print('\n\n-----Invoking profile microservice-----')
    profile_result = invoke_http(profile_URL, method="POST", json=offer)
    print("\nnew order created:", offer_result)


    # 2. Check the offer creation result (AMQP?) - if failure:
        # a. send the error to the error microservice to inform of failure
        # b. return message about error

    # code = offer_result["code"]
    # if code not in range(200, 300):
        # Inform the error microservice
        # print('\n\n-----Invoking error microservice as offer fails-----')
        # invoke_http(error_URL, method="POST", json=offer_result)
        # - reply from the invocation is not used; 
        # continue even if this invocation fails
        # print("Offer status ({:d}) sent to the error microservice:".format(
        #     code), offer_result)

        # 6/7.Return error
        # return {
        #     "code": 500,
        #     "data": {"offer_result": offer_result},
        #     "message": "Offer creation failure sent for error handling."
        # }

    # 3. Record new offer in notification (AMQP route to notification)
    # log information for notification
    print('\n\n-----Invoking notification microservice-----')
    invoke_http(notification_URL, method="POST", json=offer_result)
    print("\nOffer sent to notification microservice.\n")
    # the reply/result from this invocation is not used;
    # continue even if this invocation fails

    # The below might only be applicable for seller side accept
    # X. Check the offer result (AMQP?); if success/fail, Send this notification result to BUYER [make offer complex ms]
    # Invoke the notification microservice - need to check AMQP
    # print('\n\n-----Invoking notification microservice-----')
    # notification_result = invoke_http(
    #     notification_URL, method="POST", json=offer_result['data'])
    # print("notification_result:", notification_result, '\n')

    # 4. Invoke Payment Mircoservice module
    # return {} # to remove

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

    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
