#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script


#for amqp 
import json
import os
import amqp_setup
import requests

#for linking to DB
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/notifications'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299} #what is this for?

db = SQLAlchemy(app)
CORS(app)

class Notifications(db.Model):
    __tablename__ = 'notifications'

    Notification_ID = db.Column(db.Integer, nullable=False)
    Seller_ID = db.Column(db.Integer, nullable=False)
    Buyer_ID = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(10), nullable=False)
    Message = db.Column(db.String(64), nullable=False)
    DateTimeSQL = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, Seller_ID, Buyer_ID, Status, Message):
        self.Notification_ID = secrets.token_urlsafe(16)
        self.Seller_ID = Seller_ID
        self.Buyer_ID = Buyer_ID
        self.Status = Status
        self.Message = Message 
        self.DateTimeSQL = datetime.now()

    def json(self):
        return {"Notification_ID": self.Notification_ID,
                "Seller_ID": self.Seller_ID, 
                "Buyer_ID": self.Buyer_ID, 
                "Status": self.Status, 
                "Message": self.Message,
                "DateTimeSQL": self.DateTimeSQL}


#consume from queue and then insert to DB

#for the amqp portion

import amqp_setup

notifsBindingKey = 'notify.*'

# acceptBindingKey = '*.accept'
# rejectBindingKey = '*.reject'

def receiveNotification():

    ##refer to this instead of the below ones##

    amqp_setup.check_setup()
    queue_name = 'Notify'

    channel = amqp_setup.channel
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

    ######################## Old Code below##############################


    #one channel one queue
    
    # amqp_setup.check_setup()
    # queue_nameA = 'NotifyAccept'

    # set up a consumer and start to wait for coming messages

    # channelA = amqp_setup.channel
    # channelA.basic_consume(queue=queue_nameA, on_message_callback=callback, auto_ack=True)
    # channelA.start_consuming()

    # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it. 

    # queue_nameR = 'NotifyReject'
    # channelR = amqp_setup.channel
    # channelR.basic_consume(queue=queue_nameR, on_message_callback=callback, auto_ack=True)

    # channelR.start_consuming()

def callback(channel, method, properties, body): # required signature for the callback; no return

    #this is what we want to do with the message - dont need to touch for now 
    print("\nReceived a notifcation by " + __file__)
    processNotifs(json.loads(body))
    saveToDatabase(body)
    print() # print a new line feed


@app.route("/notifications/<string:Notification_ID>")
def processNotifs(Msg):
    print("Printing the notification message:")
    try: 
        notifs = json.loads(Msg) 
        print(notifs)
        # print("--JSON:", notifs
        #to insert into DB here 

        data = request.get_json()
        # notifications_msg = Notifications(Notification_ID, **data)
        db.session.add(notifs)
        db.session.commit()

    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", Msg)
    print()

def saveToDatabase(successMsg):
    successMsg = json.loads(successMsg)
    query = 'mutation MyMutation {insert_Activity(objects: {Description: "'+successMsg["message"]+'"}){affected_rows}}'
    # url = 'https://esd-healthiswell-69.hasura.app/v1/graphql'  #need to add own mongodb url - see jp's 
    myobj = {'x-hasura-admin-secret': 'Qbbq4TMG6uh8HPqe8pGd1MQZky85mRsw5za5RNNREreufUbTHTSYgaTUquaKtQuk',
            'content-type': 'application/json'}
    r = requests.post(url, headers=myobj, json={'query': query})


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')  same exchange different binding key 
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(notifsBindingKey, amqp_setup.exchangename)) #WHERE TO PUT THIS rejectBindingKey
    # print(": monitoring routing key '{}' in exchange '{}' ...".format(rejectBindingKey, amqp_setup.exchangename))
    receiveNotification()


# def receive_notification(queue_name, binding_key):
#     """
#     This function receives a notification from the broker and prints it to the console.
#     """
#     channel = amqp_setup.channel
#     channel.basic_consume(queue=queue_name, on_message_callback=on_message,
#                           auto_ack=True,
#                           arguments={'x-match': 'all',
#                                      'key': binding_key})
#     channel.start_consuming()


    