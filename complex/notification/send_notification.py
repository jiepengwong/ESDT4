# TBC - requires notification + invoking thru AMQP 
from invokes import invoke_http

# invoke item microservice to get all items
result = invoke_http("http://localhost:5000/notification", method='GET')

print(result)