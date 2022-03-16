from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ, terminal_size
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/item'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Item(db.Model):
    __tablename__ = 'item'

    ItemID = db.Column(db.String(10), primary_key=True, nullable=False)
    ItemName = db.Column(db.String(64), nullable=False)
    Seller_ID = db.Column(db.String(10), nullable=False)
    ItemDesc = db.Column(db.String(64), nullable=False)
    Category = db.Column(db.String(64), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ItemStatus = db.Column(db.String(64), nullable=False)

    def __init__(self, ItemID, ItemName, Seller_ID, ItemDesc, Category, Price, ItemStatus):
        self.ItemID = ItemID
        self.ItemName = ItemName
        self.Seller_ID = Seller_ID
        self.ItemDesc = ItemDesc
        self.Category = Category
        self.Price = Price
        self.ItemStatus = ItemStatus

    def json(self):
        return {"ItemID": self.ItemID, 
                "ItemName": self.ItemName, 
                "Seller_ID": self.Seller_ID, 
                "ItemDesc": self.ItemDesc, 
                "Category": self.Category, 
                "Price": self.Price, 
                "ItemStatus": self.ItemStatus}

# GET: item list
@app.route("/item")
def get_all():
    itemlist = Item.query.all()
    if len(itemlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "item": [item.json() for item in itemlist]
                },
                'message': 'All listed items have been successfully retreived.'
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no items currently on sale."
        }
    ), 404

# GET: particular item
@app.route('/item/<string:ItemID>')
def searchItemID(ItemID):
    item = Item.query.filter_by(ItemID=ItemID).first()
    if item:
        return jsonify(
            {
                'code': 200,
                'data': item.json(),
                'message': 'Item has been successfully retreived.'
            }
        )
    return jsonify(
        {
            'code': 404,
            'message': 'Item not found (Invalid ItemID). Please enter a valid ItemID.'
        }
    ), 404

# POST: create new item
@app.route("/item/<string:ItemID>", methods=['POST'])
def createItem(ItemID):
    if (Item.query.filter_by(ItemID=ItemID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "ItemID": ItemID
                },
                "message": "Item already exist and an error occurred while listing the item. Please try again."
            }
        ), 400

    data = request.get_json()
    item = Item(ItemID, **data)

    try:
        db.session.add(item)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while listing the item. Please try again."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": item.json()
        }
    ), 201

# DELETE: delete item
@app.route("/item/<string:ItemID>", methods=['DELETE'])
def deleteItem(ItemID):
    item = Item.query.filter_by(ItemID=ItemID).first()
    if (item):
        db.session.delete(item)
        db.session.commit()
        return jsonify(
            {
                'code': 200,
                'message': 'Item has been deleted.'
            }
        )

    return jsonify(
        {
            'code': 404,
            'message': 'An error occurred while deleting the item. Please try again.'
        }
    ), 404

# PUT: update existing item
@app.route("/item/<string:ItemID>", methods=['PUT'])
def updateItem(ItemID):
    if (Item.query.filter_by(ItemID=ItemID).first()):
        db.session.delete(Item.query.filter_by(ItemID=ItemID).first())
        db.session.commit()

        data = request.get_json()
        item = Item(ItemID, **data)
        db.session.add(item)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": item.json(),
                "message": "Item has been successfully updated."
            }
        ), 200

    return jsonify(
        {
            'code': 404,
            'message': 'An error occurred while updating the item. Please try again.'
        }
    ), 404


if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

# terminal: cd C:\wamp64\www\IS213\ESDT4\docker\item

# set dbURL=mysql+mysqlconnector://root@localhost:3306/item
# python item.py
# python -m pip freeze

# docker build -t limyuxuan/item:1.0 ./
# docker images

# docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/item limyuxuan/item:1.0
# http://127.0.0.1:5000/item
# docker ps
# docker stop <containerid> / docker start <containerid>
# docker logs 681cfd451376

# on 2 seperate cmd lines
# docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/item limyuxuan/item:1.0
# docker run -p 5100:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/item limyuxuan/item:1.0
# docker stop 437e19267ec9 681cfd451376
# docker rm 437e19267ec9 681cfd451376