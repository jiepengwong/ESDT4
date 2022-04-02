from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import update

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/profile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app) 

class Profile(db.Model):
    __tablename__ = 'profile_details'

    user_id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(8), nullable=False)
    ratings = db.Column(db.Float(precision=2), nullable = True)
    counts = db.Column(db.String(64), nullable=False)
    temp = db.Column(db.String(64), nullable=False)

    def __init__(self, user_id, name, email, mobile, ratings, counts, temp):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.ratings = ratings
        self.counts = counts
        self.temp = temp

    def json(self):
        return {"user_id": self.user_id, 
                "name": self.name, 
                "email": self.email,
                "mobile": self.mobile,
                "ratings": self.ratings,
                "counts": self.counts,
                "temp": self.temp,
                }

#Receive the rating and do the average
@app.route("/profile", methods=['POST'])
def aggregate_rating():
    #fetch data from UI
    data = request.getjson()
    details = Profile.query.get() 

    #post in the newly entered review number into the temp field
    details.temp = data
    db.session.commit() #save the changes
    
    if len(details):
        details = Profile.query.get()
        aggregated_rating = (((details.counts-1) * details.rating) + details.temp)/details.counts
        details.ratings = aggregated_rating
        db.session.commit()#save the changes
        details.temp = ""
        return jsonify({
            "code": 201,
                "data": {
                    "ratings": details.ratings  
                },
                "message": "Rating already exist and an error occurred while creating a rating. Please try again."
        }), 201
    return jsonify(
            {
                "code": 500,
                "data": {
                    "ratings": details.ratings
                },
                "message": "An error occurred while creating a rating. Please try again."
            }
        ), 500
    '''
    if (Profile.query.filter_by(user_id=user_id).first()):
        return jsonify({
            "code": 201,
                "data": {
                    "ratings": ratings  
                },
                "message": "Rating already exist and an error occurred while creating a rating. Please try again."
        }), 201'''
            
    '''
    update_review = (
        update(Rating).
        where(Rating == data).
        values(temp = data)
    )
    '''

    #the complex will update the ratings and count in the db
    #aggregate the total average 
    #(((count-1) * rating) + temp)/count

if __name__ == '__main__':
    app.run(port=5000, debug=True)



