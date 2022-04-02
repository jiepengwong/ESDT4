import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/profile'
# The SQLAlchemy Database URI format is: dialect+driver://username:password@host:port/database

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
CORS(app)

class Profile(db.Model):
    __tablename__ = "Profile_details"

    user_id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(8), nullable=False)
    ratings = db.Column(db.Float(precision=2), nullable = True)

    def __init__(self,user_id,name,email,mobile,ratings):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.ratings = ratings

    def json(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email, "mobile": self.mobile,"ratings":self.ratings}
        

# We need to get /profile/:id, this is to get the profile details of the user 
@app.route("/profile/<string:profile_ID>")
def find_by_profile_ID(profile_ID):
    profile = Profile.query.filter_by(user_id=profile_ID).first()
    if profile:
        return jsonify({
            "code":200,
            "data": profile.json()
        }),200
    return jsonify({
        "code":404,
        "message": "User has yet to register"
    }),404

# We need to update profile/rating/:id, this is to update the profile ratings of the user
@app.route("/profile/ratings/<string:Profile_Id>", methods=["PUT"])
def update_ratings(Profile_Id):
    if (Profile.query.filter_by(user_id=Profile_Id).first()):

        data = request.get_json()
        profile = Profile.query.filter_by(user_id=Profile_Id).first()
        print(profile.mobile)
        profile.ratings = data['ratings']
        db.session.commit()
        return jsonify({
                "code":200,
                "data":profile.json(),
                "message":"Profile's ratings has been updated."
            },200
        )
    return jsonify({
        "code":404,
        "message":"An error occured while updating the profile ratings.Please try again."
    })

# WE NEED TO UPDATE THE PROFILE 
@app.route("/profile/mobile/<string:Profile_Id>", methods=["PUT"])
def update_number(Profile_Id):
    if (Profile.query.filter_by(user_id=Profile_Id).first()):

        data = request.get_json()
        profile = Profile.query.filter_by(user_id=Profile_Id).first()
        print(profile.mobile)
        profile.mobile = data['mobile']
        db.session.commit()
        return jsonify({
                "code":200,
                "data":profile.json(),
                "message":"Profile's number has been updated."
            },200
        )
    return jsonify({
        "code":404,
        "message":"An error occured while updating the profile number.Please try again."
    })



# We need to post /profile/register/, this is to register new user everytime they login with google 
@app.route("/profile/register/<string:Profile_Id>", methods=["POST"])
def create_account(Profile_Id):
    if (Profile.query.filter_by(user_id=Profile_Id).first()):
        return jsonify({
            "code":400,
            "data": {
                "user_id" : Profile_Id
            },
            "message": "User has already registered"
        }), 400
    
    data = request.get_json()
    profile = Profile(Profile_Id, **data)

    try:
        db.session.add(profile)
        db.session.commit()
    
    except:
        return jsonify({
            "code":500,
            "data":{
                "user_id": Profile_Id
            },
            "message": "An error occured creating a new account"
        }), 500
    
    return jsonify({
        "code":200,
        "data":profile.json()
    })


if __name__ == "__main__":
    app.run(port=5000, debug = True)
