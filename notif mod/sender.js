//fire and forget

var amqp = require('amqplib/callback_api');

/* Step 1: Create connection
and by sending a callback with an error and return a connection*/
amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) { //after creating the connection, check if theres a connection error which return an error
        throw error0;
    }
    // Step 2: Create a channel (if theres no error in connection)
    connection.createChannel(function(error1, channel) {
        if (error1) { // error in channel
            throw error1;
        }
        //Step 3: Assert Queue (Check if the queue is present)
        // if queue is not present, it will create 
        var queue = 'hello';
        var msg = 'Hello World!';

        channel.assertQueue(queue, {
            durable: false
        });
        channel.sendToQueue(queue, Buffer.from(msg));

        console.log(" [x] Sent %s", msg);
    });
    setTimeout(function() {
        connection.close();
        process.exit(0);
    }, 500);
});