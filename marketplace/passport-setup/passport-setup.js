// Explanation of the Code, creating this will allow for passing variable things into Google.
const passport = require('passport')

const GoogleStrategy = require( 'passport-google-oauth2' ).Strategy;

// Read 9mins 30 sec for why the codes is important 

passport.serializeUser(function(user,done) {
    done(null,user.id);
});

passport.deserializeUser(function(id,done) {
    // This is for Database Connection 
    User.findById(id, function(err,user){
        done(null,user);
    })
});


passport.use(new GoogleStrategy({
    clientID:     "616186403576-ii3mdj1ujr9f8s8srnfa1q5mtgq3o1pm.apps.googleusercontent.com",
    clientSecret: "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",
    callbackURL: "http://localhost:3000/auth/google/callback",
    passReqToCallback   : true
  },
  function(request, accessToken, refreshToken, profile, done) {
    // Use the profile info (mainly profile id) to check if the user is registered in your db [THIS IS FOR DATABASE!!]
    User.findOrCreate({ googleId: profile.id }, function (err, user) {
      return done(err, user);
    });
  }
));