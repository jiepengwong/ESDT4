from invokes import invoke_http

# invoke item microservice to get all items
results = invoke_http("http://localhost:5000/item", method='GET')

print( type(results) )
print()
print( results )
 