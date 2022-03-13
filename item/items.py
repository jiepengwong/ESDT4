from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class item(db.Model):
    __tablename__ = 'item'

    ItemID = db.Column(db.Integer, primary_key=True, nullable=False)
    ItemName = db.Column(db.String(64), nullable=False)
    Seller_ID = db.Column(db.Integer, nullable=False)
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
    itemlist = item.query.all()
    if len(itemlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "item": [item.json() for item in itemlist]
                }
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
    item =item.query.filter_by(ItemID=ItemID).first()
    if item:
        return jsonify(
            {
                'code': 200,
                'data': item.json()
            }
        )
    return jsonify(
        {
            'code': 404,
            'message': 'Item is not found.'
        }
    ), 404

# POST: create new item
@app.route("/item/<string:ItemID>", methods=['POST'])
def createItem(ItemID):
    if (item.query.filter_by(ItemID=ItemID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while listing the item. Please try again."
            }
        ), 400

    data = request.get_json()
    item = item(item, **data)

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
@app.route("/item/<string:ItemID>", methods=['Delete'])
def deleteItem(ItemID):
    if (item.query.filter_by(ItemID=ItemID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while deleting the item. Please try again."
            }
        ), 400

    data = request.get_json()
    item = item(item, **data)

    try:
        db.session.delete(item)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while deleting the item. Please try again."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": item.json()
        }
    ), 201

# PUT: edit item
@app.route("/item/<string:ItemID>", methods=['PUT'])
def editItem(ItemID):
    if (item.query.filter_by(ItemID=ItemID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while editing the item details. Please try again."
            }
        ), 400

    data = request.get_json()
    item = item.filter_by(item, **data)

    try:
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "ItemID": ItemID
                },
                "message": "An error occurred while editing the item details. Please try again."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": item.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5000, debug=True)