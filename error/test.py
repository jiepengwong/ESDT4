import pymongo

print("Mongo version",pymongo.__version__)
from pymongo import MongoClient

cluster = pymongo.MongoClient("mongodb+srv://tingz:C1e3RbVUrvmAkDzl@wtesd.azs8r.mongodb.net/ESDnotifs?retryWrites=true&w=majority")

db = cluster["ESDnotifs"]
collection = db['error_micro']

collection.insert_one({
    
    "Notification_ID": '11',
    "Seller_ID": "1",
    "Buyer_ID": "1",
    "Status": "1",
    "Message": "1",
    "DateTimeSQL": "1"

    })
    
print("hELLO world")

