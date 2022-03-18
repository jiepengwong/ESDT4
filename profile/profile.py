import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/profile'
# The SQLAlchemy Database URI format is: dialect+driver://username:password@host:port/database


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Profile(db.Model):
    __tablename__ = "Profile"

    userId = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), nullable=False)
    ratings = db.Column(db.Float(precision=2), nullable = True)

    def __init__(self,userId,name,email,ratings):
        self.userId = userId
        self.name = name
        self.email = email
        self.ratings = ratings

    def json(self):
        return {"userId": self.userId, "name": self.name, "email": self.email, "ratings":self.ratings}

# We need to get /profile/:id, this is to get the profile details of the user 
@app.route("/profile/rating/<string:profile_ID>")
def find_by_profile_ID(profile_ID):
    profile = Profile.query.filter_by(userId=profile_ID).first()
    if profile:
        return jsonify({
            "code":200,
            "data": profile.json()
        }),200
    return jsonify({
        "code":404,
        "message": "User has yet to register"
    })

# We need to update profile/rating/:id, this is to update the profile ratings of the user
@app.route("/profile/rating/<")


# We need to post /profile/register/, this is to register new user everytime they login with google 
@app.route("/profile/<string:Profile_Id", methods=["POST"])
def create_account(Profile_Id):
    if (Profile.query.filter_by(userId=Profile_Id).first()):
        return jsonify({
            "code":400,
            "data": {
                "userId" : Profile_Id
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
                "userId": Profile_Id
            },
            "message": "An error occured creating a new account"
        }), 500
    
    return jsonify({
        "code":201,
        "data":profile.json()
    })


if __name__ == "__main__":
    app.run(port=5000, debug = True)
