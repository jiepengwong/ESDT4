const express = require('express')
const mongoose = require('mongoose')
const Order = require("./models/orders")


const app = express()
// Takes URL encoded data and parses it into a JavaScript object on express server
app.use(express.urlencoded({extended:true}))

// Connection to the mongoDB
const dbURI = "mongodb+srv://esdt4:esdt4@nodejstutoriallearning.xssjk.mongodb.net/orderdb?retryWrites=true&w=majority"
// Use mongoose to connect to the database (ASYNC function)
mongoose.connect(dbURI,{useNewUrlParser:true,useUnifiedTopology:true})
.then((res)=>{
    console.log("Connected to the database")
    // Listen only when connection is established
    app.listen(port, () => {
        console.log(`listening on port ${port}`)
      })
})
.catch((err)=>{
    console.log(err)
})
const port = 5000

// Mongoose sandbox
// In the actual thing, probably have to use POST
app.get("/add-order",(req,res)=>{

    // Testing out the mongoose model
    const order = new Order({
        ordersummary:[
            {"test1": 21233,"sellerid": "lol1"},
            {"test2": 12,"sellerid":"lol2"}
        ],
        totalprice: 123,
        buyerid: "buyerid1",
        sellerid: "sellerid1"
    })

    // Save to the mongodb
    // save is an inbuilt func of moongoose
    order.save()
    .then((result)=>{
        console.log("successful")
        res.send(result)
    })
    .catch((error)=>{
        console.log(error)
    })
})

// Get all the orders 
app.get("/get-orders",(req,res)=>{
    Order.find()
    .then((result)=>{
        // We can send a res.json back to the front-end side
        res.send(result)
    })
    .catch((error)=>{
        console.log(error)
    })
})





// ==== ROUTES =====

app.get('/', (req, res) => {
    res.send('Hello World!')
  })
  

// Get all orders for a particular user
// Use of GET method

app.get('/order', (req, res) => {
    res.send('Hello World!')
  })
