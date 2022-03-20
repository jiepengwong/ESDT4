const express = require("express")
const app = express()
const cors = require("cors")
const bodyParser = require("body-parser")
const passport = require("passport")
const cookieSession = require('cookie-session')
require('./passport-setup')

app.use(cors())

// Parse Application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false}))

// parse application/json
app.use(bodyParser.json())

const isLoggedIn = (req, res, next) => {
    if (req.user) {
        next()
    }
    else {
        res.sendStatus(401);
    }
}

app.use(cookieSession({
    name: 'Esd-session',
    keys: ['key1','key2']
}))


app.use(passport.initialize());
// use this session to authenticate. 
app.use(passport.session());


app.get('/failed', (req, res) => res.send("You are not logged in "))
app.get('/good',isLoggedIn, (req, res) => res.send(`Welcome Mr $(req.user)!`))


app.get('/google',
  passport.authenticate('google', { scope: [ 'email', 'profile' ] }
));

// This is the callback url. 
app.get( '/google/callback',
    passport.authenticate( 'google', {successRedirect: '/good',failureRedirect: '/failed'}),
    function(req, res) {
        res.redirect("/good");
    }

    );

app.get('/logout', (req,res)=> {
    req.session = null;
    req.logOut();
    res.redirect("/");

})

app.listen(3000, () => console.log("Example app listening on port $(3000)"))