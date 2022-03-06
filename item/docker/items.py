from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Item(db.Model):
    __tablename__ = 'item'

    ItemID = db.Column(db.Integer, primary_key=True, nullable=False)
    ItemName = db.Column(db.String(64), nullable=False)
    UserID_Seller = db.Column(db.Integer, nullable=False)
    QtyAvail = db.Column(db.Integer, nullable=False)
    ItemDesc = db.Column(db.String(64), nullable=False)
    Reviews = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.Integer, nullable=False)

    def __init__(self, ItemID, ItemName, UserID_Seller, QtyAvail, ItemDesc, Reviews, Price):
        self.ItemID = ItemID
        self.ItemName = ItemName
        self.UserID_Seller = UserID_Seller
        self.QtyAvail = QtyAvail
        self.ItemDesc = ItemDesc
        self.Reviews = Reviews
        self.Price = Price

    def json(self):
        return {"ItemID": self.ItemID, 
                "ItemName": self.ItemName, 
                "UserID_Seller": self.UserID_Seller, 
                "QtyAvail": self.QtyAvail, 
                "ItemDesc": self.ItemDesc, 
                "Reviews": self.Reviews, 
                "Price": self.Price}


@app.route("/item")
def get_all():
    itemlist = Item.query.all()
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
            "message": "There are no items on sale."
        }
    ), 404


@app.route('/Item/<string:ItemID>')
def searchItemID(ItemID):
    item =Item.query.filter_by(ItemID=ItemID).first()
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
            'message': 'Book not found'
        }
    ), 404


@app.route("/Item/<string:ItemID>", methods=['POST'])
def createItem(ItemID):
    if (Item.query.filter_by(ItemID=ItemID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "ItemID": ItemID
                },
                "message": "Item is already on sale."
            }
        ), 400

    data = request.get_json()
    item = Item(Item, **data)

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
                "message": "An error occurred when listing the item."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": item.json()
        }
    ), 201


if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
