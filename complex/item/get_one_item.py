# invoke item microservice to get ONE item
from invokes import invoke_http

# TBC - hardcoded for now
ItemId = 1234567891

get_result = invoke_http(
        "http://localhost:5000/item/" + str(ItemId), method='GET'
    )

print(get_result)