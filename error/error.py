import pymongo
from pymongo import MongoClient


#defining the connection to the database/cluster
# cluster = pymongo.MongoClient("mongodb+srv://tingz:rS21GYaQ7snuxaTK@wtesd.azs8r.mongodb.net/ESDnotifs?retryWrites=true&w=majority")

cluster = pymongo.MongoClient("mongodb+srv://tingz:C1e3RbVUrvmAkDzl@wtesd.azs8r.mongodb.net/ESDnotifs?retryWrites=true&w=majority")

# cluster = MongoClient("mongodb+srv://tingz:C1e3RbVUrvmAkDzl@wtesd.azs8r.mongodb.net/ESDnotifs?retryWrites=true&w=majority")

db = cluster["ESDnotifs"]
collection = db['error_micro']

import json
import os
import amqp_setup


errorBindingKey = 'error.*'


def receiveError():

    amqp_setup.check_setup()
    queue_name = 'Error'
    channel = amqp_setup.channel
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming() 


def callback(channel, method, properties, body): 

    print("\nReceived a error by " + __file__)
    processErrors(json.loads(body))
    saveToDatabase(body)
    print() # print a new line feed


def processErrors(Msg):
    print("Printing the error message:")
    try: 

        errors = Msg
        # print(notifs)
        print(errors)
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

def saveToDatabase(errorMsg):
    errorMsg = json.loads(errorMsg)

    #need to edit the field for error

    one_error = {
        "code": errorMsg["code"],
        "message": errorMsg["message"]
    }

    ##Insert "one notif' object directly into MongoDB via insert_one
    result = collection.insert_one(errorMsg)

    ## checking 
    print('print to console the object ID of the new document (a row in sql)'.format(result.inserted_id))



if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')  same exchange different binding key 
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(errorBindingKey, amqp_setup.exchangename)) 
    receiveError()




