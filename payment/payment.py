from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment'
    seller_id = db.Column(db.String(10), nullable=False)
    buyer_id = db.Column(db.String(10),  nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    payment_id = db.Column(db.String(10), primary_key=True)
    payment_status = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, seller_id, buyer_id, price, payment_id, payment_status):
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.price = price
        self.payment_id = payment_id
        self.payment_status = payment_status
    
    def json(self):
        return {"seller_id": self.seller_id,
                "buyer_id": self.buyer_id, 
                "price": self.price,
                "payment_id": self.payment_id,
                "payment_status": self.payment_status}

#GET sellerid, buyerid, price from "Accept Offer" microservice
@app.route("/payment")
def getdetails():
     
    payments = Payment.query.all() 
    if len(payments):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment": [payment.json() for payment in payments]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "Unable to get payment details."
        }
    ), 404


#create unique ID for payment transaction
@app.route("/payment", methods=['POST'])
def createPayment():
    payment_id = secrets.token_urlsafe(22)
    if (Payment.query.filter_by(payment_id=payment_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "payment_id": payment_id
                },
                "message": "Item already exist and an error occurred while listing the item. Please try again."
            }
        ), 400

    data = request.get_json()
    payment = Payment(payment_id, **data)

    try:
        db.session.add(payment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "payment_id": payment_id
                },
                "message": "An error occurred while listing the item. Please try again."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": Payment.json()
        }
    ), 201

#update payment status
@app.route("/payment/<string:payment_id>", methods=['PUT'])
def updatePaymentStatus(payment_id):
    
    if (Payment.query.filter_by(payment_id=payment_id).first()):
        db.session.delete(Payment.query.filter_by(payment_id=payment_id).first())
        db.session.commit()

        data = request.get_json()
        payment_id = Payment(payment_id, **data)
        db.session.add(payment_id)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment_id": Payment.json(),
                },
                "message": "Payment status has been successfully updated."
            }
        ), 200
    return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "An error occurred while updating the payment status. Please try again."
                }
            }
        ), 404


if __name__ == '__main__': 
    app.run(port=5000, debug=True)
