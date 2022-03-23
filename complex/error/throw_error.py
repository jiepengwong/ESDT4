# TBC, need error microservice to be up and running
from invokes import invoke_http

# invoke error microservice to get all errors
result = invoke_http("http://localhost:5000/error", method='GET')

print(result)