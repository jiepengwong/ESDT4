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

    paymentID = db.Column(db.String(10), primary_key=True, nullable=False)
    sellerID = db.Column(db.String(10), nullable=False)
    buyerID = db.Column(db.String(10),  nullable=False)
    price = db.Column(db.Integer, nullable=False)
    paymentStatus = db.Column(db.String(64), nullable=False)

    def __init__(self, paymentID, sellerID, buyerID, price, paymentStatus):
        self.paymentID = paymentID
        self.sellerID = sellerID
        self.buyerID = buyerID
        self.price = price
        self.paymentStatus = paymentStatus

    def json(self):
        return {"paymentID": self.paymentID,
                "sellerID": self.sellerID,
                "buyerID": self.buyerID,
                "price": self.price,
                "paymentStatus": self.paymentStatus}

#GET sellerid, buyerid, price from "Accept Offer" microservice
@app.route("/payment")
def getdetails(): 
    #pass   

#step 1: get seller id, buyer id, price
#step 2: auto create random payment id then go to external API

#fields: sellerid, buyerid, price, paymentid, paymentstatus
#db = SQLAlchemy(app)

#GET: all payments (only for checking purposes)
def get_all():
    paymentlist = Payment.query.all()
    if len(paymentlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment": [paymentlist.json() for payment in paymentlist]
                },
                'message': 'All payments listed - only for checking purposes'
            }

        ), 200
        
    return jsonify(
        {
            "code": 404,
            "message": "Payments cannot be retreived - only for checking purposes"
        }
    ), 404

# GET: particular payment record
@app.route('/payment/<string:paymentID>')
def searchpaymentID(paymentID):
    payment = Payment.query.filter_by(paymentID=paymentID).first()
    if payment:
        return jsonify(
            {
                'code': 200,
                'data': payment.json(),
                'message': 'Payment record has been successfully retreived.'
            }
        )
    return jsonify(
        {
            'code': 404,
            'message': 'Payment record not found (Invalid paymentID). Please enter a valid paymentID.'
        }
    ), 404

# POST: create new payment + unique paymentID
@app.route("/payment", methods=['POST'])
def createPayment():
    paymentID = secrets.token_urlsafe(22)
    if (Payment.query.filter_by(paymentID=paymentID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "paymentID": paymentID
                },
                "message": "Payment record already exist and an error occurred while creating a new payment record under this paymentID. Please try again."
            }
        ), 400

    data = request.get_json()
    payment = Payment(paymentID, **data)

    try:
        db.session.add(payment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "paymentID": paymentID
                },
                "message": "An error occurred while creating the payment record. Please try again."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": payment.json()
        }
    ), 201

# redone until here - yu xuan
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
