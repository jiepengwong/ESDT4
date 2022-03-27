# from tokenize import String
# from matplotlib import collections

#connecting to mongoDB

# from hashlib import new
# from sqlite3 import Date
import pymongo
from pymongo import MongoClient
from datetime import datetime, timezone
# from datetime import timedelta

#defining the connection to the database/cluster
cluster = pymongo.MongoClient("mongodb+srv://tingz:rS21GYaQ7snuxaTK@wtesd.azs8r.mongodb.net/ESDnotifs?retryWrites=true&w=majority")


#picking which db we want 
db = cluster["ESDnotifs"]
collection = db['notifications']


# user_schema = {  #this needs to be in the savetoDB function

#        "Notification_ID":  {
#             'type': 'String',
#             'required': True
#         },

#         "Seller_ID": {
#             'type': 'Number',
#             'required': True
#         },

#         "Buyer_ID": {
#             'type': 'Number',
#             'required': True
#         },

#         "Status": {
#             'type': 'String',
#             'required': True
#         },

#         "Message": {
#             'type': 'String',
#             'required': True
#         },

#         # "DateTimeSQL": datetime.today()

#         "DateTimeSQL": {
#             'type': 'Date',
#             'required': True
#         }

# }

# collection.insert_one(user_schema)

##how to add to db  - hardcoded into db
# collection.insert_one({
    
#     "Notification_ID": '11',
#     "Seller_ID": "1",
#     "Buyer_ID": "1",
#     "Status": "1",
#     "Message": "1",
#     "DateTimeSQL": "1"

#     })


#amqp notificatiions 

import json
import os
import amqp_setup
import requests
import secrets
from flask import Flask, app, request, jsonify
from os import environ
from flask_cors import CORS



notifsBindingKey = 'notify.*'

app = Flask(__name__)
CORS(app)


def receiveNotification():

    amqp_setup.check_setup()
    queue_name = 'Notify'
    channel = amqp_setup.channel
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def callback(channel, method, properties, body): 

    print("\nReceived a notifcation by " + __file__)
    processNotifs(json.loads(body))
    saveToDatabase(body)
    print() # print a new line feed


@app.route("/notifs/<string:Notification_ID>") 
def processNotifs(Msg):
    print("Printing the notification message:")
    try: 
        notifs = json.loads(Msg) 
        print(notifs)
        # print("--JSON:", notifs
        #to insert into DB here 

        # data = request.get_json()
        # notifications_msg = Notifications(Notification_ID, **data)
        # db.session.add(notifs)
        # db.session.commit()

    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", Msg)
    print()

def saveToDatabase(successMsg):
    successMsg = json.loads(successMsg)
    # query = 'mutation MyMutation {insert_Activity(objects: {Description: "'+successMsg["message"]+'"}){affected_rows}}'

    #query for mongodb -- need find how to do 
    
    # url = 'https://esd-healthiswell-69.hasura.app/v1/graphql'

    # url: collection

    #need to fetch the data from the complex micro and insert into the db 

    one_notif = {

        "Notification_ID": secrets.token_urlsafe(16),
        "Seller_ID": "1",
        "Buyer_ID": "1",
        "Status": "1",
        "Message":successMsg,
        "DateTimeSQL": datetime.today()
    }

    ##Insert "one notif' object directly into MongoDB via insert_one
    result = collection.insert_one(one_notif)

    ## checking 
    print('print to console the object ID of the new document (a row in sql)'.format(result.inserted_id))

    # secret_ID = collection._id
    # myobj = {collection._id}
    # myobj = {'x-hasura-admin-secret': 'Qbbq4TMG6uh8HPqe8pGd1MQZky85mRsw5za5RNNREreufUbTHTSYgaTUquaKtQuk',
    #         'content-type': 'application/json'}
    # r = requests.post(url, headers={'Content-type': 'application/json'}, json={'query': query})

    #not sure if i need this ... 
    r = requests.post(url, headers={'Content-type': 'application/json'}, json={'query': query})


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')  same exchange different binding key 
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(notifsBindingKey, amqp_setup.exchangename)) 
    receiveNotification()




