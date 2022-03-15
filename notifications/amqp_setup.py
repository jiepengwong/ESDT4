import pika
from os import environ

#prolly need to add in environ for more scalablit

#How notification is sent --> notification microservice will have its own DB with the standardised messages that will be sent. When buyer press on "Make an Offer"button, the notification microservice will send a message to the seller's queue. The seller will have to open the queue and listen to the message  and then send back message to the buyer's queue via a button. The buyer will have to open the queue and listen to the message and then send the message to the seller's queue. (Qns: Will we then need two queue? One for buyer and one for user? Or will we just have one queue for both? ) 

#Notifications will be routing to the Order microservice - need to include a message field in for the messages that will be sent to the order microservice.


hostname = environ.get('rabbit_host') or 'localhost'
port = environ.get('rabbit_port') or 5672
# connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port,
        heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
)) 

channel = connection.channel()

exchangename="notify_topic"
exchangetype="topic"
channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

# notify queue 

queue_name = 'Notify'
channel.queue_declare(queue=queue_name, durable=True) 

# bind Notify queue
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='notify')
    # bind the queue to the exchange via the key
    # any routing_key with 'notify' will be matched

"""
This function in this module sets up a connection and a channel to a local AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""
def check_setup():
    # The shared connection and channel created when the module is imported may be expired, 
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)


def is_connection_open(connection):
    # For a BlockingConnection in AMQP clients,
    # when an exception happens when an action is performed,
    # it likely indicates a broken connection.
    # So, the code below actively calls a method in the 'connection' to check if an exception happens
    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False