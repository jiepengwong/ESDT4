from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment'
    seller_id = db.Column(db.String(10))
    buyer_id = db.Column(db.String(10), primary_key=True)
    price = db.Column(db.Float(precision=2), nullable=False)
    payment_id = db.Column(db.String(10))
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
                "payment_status": self.payment_status, 
                "payment_id": self.payment_id}

#step 1: get seller id, buyer id, price
#step 2: auto create random payment id then go to external API

#fields: sellerid, buyerid, price, paymentid, paymentstatus
#db = SQLAlchemy(app)
'''
class payment():
    buyer_id = '12345678'
    seller_id = '87654321'
    payment_id = '21436587'
    payment_status = False
'''
@app.route("/payment")
def getdetails(): #get sellerid, buyerid, price from accept offer microservice
    #pass   
    payments = Payment.query.all() 
    if len(payments):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment": [payment.json() for payment in payments]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Unable to get payment details."
        }
    ), 404
"""
def create_paymentID():
    payment_id = uuid.uuid4 () 
    print(payment_id)
    return jsonify(
            {
                "code": 200,
                "paymentid": payment.json()
            })
"""

def create_paymentStatus():
    pass

#port number should update
if __name__ == '__main__': 
    app.run(port=5000, debug=True)


