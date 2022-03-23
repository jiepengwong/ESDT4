from invokes import invoke_http

# TBC, to check on invoking of js microservice and mongo/postgres database
order_id = 2
offer_details = { 
      "price": 100.50,
      "itemname": "Test item 7",
      "itemid": "1234567897",
      "buyerid": "",
      "sellerid": "9234567897",
      }
create_results = invoke_http(
        "http://localhost:5000/offer/" + str(order_id), method='POST', 
        json=order_id
    )

print()
print(create_results)
