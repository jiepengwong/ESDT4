from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

# make sure the following microservices are running:
# offer_URL = "http://localhost:5000/offer"
item_URL = "http://localhost:5000/item" # need to change port for multiple URLs (?)
# error_URL = "http://localhost:5004/error"
# notificatio_URL = "http://localhost:5004/notification" # requires AMQP


@app.route("/accept_offer", methods=['POST'])
def accept_offer():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            offer = request.get_json()
            print("\nReceived an offer in JSON:", offer)

            # do the actual work
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
                "message": "accept_offer.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processAcceptOffer(offer):

    # TBC on the logical flow

    # 1. Send the offer info {items}
    # Invoke the offer microservice
    # print('\n-----Invoking offer microservice-----')
    # offer_result = invoke_http(offer_URL, method='POST', json=offer)
    # print('offer_result:', offer_result)

    # 2. Record new offer (if we are doing an activity log microservice)
    # record the activity log anyway
    # print('\n\n-----Invoking activity_log microservice-----')
    # invoke_http(activity_log_URL, method="POST", json=offer_result)
    # print("\nOffer sent to activity log.\n")
    # - reply from the invocation is not used;
    # continue even if this invocation fails

    # 3. Check the offer result (AMQP?); if a failure, send it to the error microservice.
    # code = offer_result["code"]
    # if code not in range(200, 300):
        # Inform the error microservice
        # print('\n\n-----Invoking error microservice as offer fails-----')
        # invoke_http(error_URL, method="POST", json=offer_result)
        # - reply from the invocation is not used; 
        # continue even if this invocation fails
        # print("Offer status ({:d}) sent to the error microservice:".format(
        #     code), offer_result)

        # 7. Return error
        # return {
        #     "code": 500,
        #     "data": {"offer_result": offer_result},
        #     "message": "Offer creation failure sent for error handling."
        # }

    # 5.Check the offer result (AMQP?); if success/fail, Send this notification result to BUYER [make offer complex ms]
    # Invoke the notification microservice - need to check AMQP
    # print('\n\n-----Invoking notification microservice-----')
    # notification_result = invoke_http(
    #     notification_URL, method="POST", json=offer_result['data'])
    # print("notification_result:", notification_result, '\n')


    # 7. Return created offer, notification of result
    # return {
    #     "code": 201,
    #     "data": {
    #         "offer_result": offer_result,
    #         "notification_result": notification_result
    #     }
    # }
    return {} # to remove



# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
