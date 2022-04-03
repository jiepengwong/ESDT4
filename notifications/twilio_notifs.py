import json
import os
import amqp_setup
import twilio
from twilio.rest import Client
from dotenv import load_dotenv
from pathlib import Path

notifsBindingKey = 'notify.*'

def receiveNotification():

    amqp_setup.check_setup()
    queue_name = 'Notify'
    channel = amqp_setup.channel
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def callback(channel, method, properties, body): 

    # print("\nReceived a notifcation by " + __file__)
    processNotifs(json.loads(body))
    print() # print a new line feed

def processNotifs(Msg):
    print("Printing the notification message:")
    try: 

        # data = json.loads(Msg) 

        data = Msg 


        #complex must send over as     
        # notification_json = {
        # 'noti_message': noti_message,
        # 'user_phone': user_phone
        # } 

        # dotenv_path = Path('marketplace/.env')
        # load_dotenv(dotenv_path=dotenv_path)


        # load_dotenv()

        load_dotenv('../.env')
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')


        noti_message = data['message']
        mobile_number = f"+65{data['mobile']}"

        # account_sid = 'TWILIO_ACCOUNT_SID'
        # auth_token = 'TWILIO_AUTH_TOKEN'
        client = Client(account_sid, auth_token) 

        message = client.messages.create( 
                                        from_='whatsapp:+14155238886',  
                                        body=noti_message,     
                                        # to=user_phone 
                                        to= 'whatsapp:' + mobile_number
                                        ) 

        print(message.sid)

        # print(data)
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

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')    
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(notifsBindingKey, amqp_setup.exchangename))
    receiveNotification()


# from twilio.rest import Client 

# account_sid = 'ACc2ba82a67c14ae8f185741f5aafc560a' 
# auth_token = '[AuthToken]' 
# client = Client(account_sid, auth_token) 

# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Your order has been accepted. Please make your payment. ',      
#                               to='whatsapp:+6591127531' 
#                           ) 

# print(message.sid)


###Response Message

# {
#     "sid": "SM973362362fb142fa9ff6c16776460401",
#     "date_created": "Fri, 25 Mar 2022 17:49:03 +0000",
#     "date_updated": "Fri, 25 Mar 2022 17:49:03 +0000",
#     "date_sent": null,
#     "account_sid": "ACc2ba82a67c14ae8f185741f5aafc560a",
#     "to": "whatsapp:+6591127531",
#     "from": "whatsapp:+14155238886",
#     "messaging_service_sid": null,
#     "body": "Your order has been accepted. Please make your payment. ",
#     "status": "queued",
#     "num_segments": "1",
#     "num_media": "0",
#     "direction": "outbound-api",
#     "api_version": "2010-04-01",
#     "price": null,
#     "price_unit": null,
#     "error_code": null,
#     "error_message": null,
#     "uri": "/2010-04-01/Accounts/ACc2ba82a67c14ae8f185741f5aafc560a/Messages/SM973362362fb142fa9ff6c16776460401.json",
#     "subresource_uris": {
#         "media": "/2010-04-01/Accounts/ACc2ba82a67c14ae8f185741f5aafc560a/Messages/SM973362362fb142fa9ff6c16776460401/Media.json"
#     }
# } 