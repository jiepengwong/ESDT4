const express = require("express");
const mongoose = require("mongoose");
const Offer = require("./models/offerSchema");
const bodyParser = require("body-parser");

const app = express();

// Converts Json to javascript object
// app.use(express.json());

// Takes URL encoded data and parses it into a JavaScript object on express server
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

var jsonParser = bodyParser.json();

// Connection to the mongoDB
const dbURI =
  "mongodb+srv://esdt4:esdt4@nodejstutoriallearning.xssjk.mongodb.net/offerdb?retryWrites=true&w=majority";
// Use mongoose to connect to the database (ASYNC function)
mongoose
  .connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then((res) => {
    console.log("Connected to the database");
    // Listen only when connection is established
    app.listen(port, () => {
      console.log(`listening on port ${port}`);
    });
  })
  .catch((err) => {
    console.log(err);
  });
const port = 5000;

// Simple implementation for now NOT using controllers

// Buyer places an offer, keys in the relevant data from the UI side and sends it to the server
// /offer/createoffer
app.post("/offer/createoffer",  (req, res) => {
  // From the front-end side of things

  // Create a new instance at the database side

  if (req.body) {
    console.log(req.body);
    const postreq = req.body;
    const newOffer = new Offer({
      price: postreq.price,
      itemname: postreq.itemname,
      itemid: postreq.itemid,
      buyerid: postreq.buyerid,
      sellerid: postreq.sellerid,
    });

    // Save the new instance to the database
    // Async funnction
    newOffer.save()
      .then((result) => {
        res.status(200)

        // Edit code here in the future to get back the order id (postreq._id)
        res.send(`Your order id is : ${result._id}`);
      })
      .catch((err) => {
        res.status(400).json({"Error": "Offer not placed"});

        // console.log(err.msg)
      });
  } else {
    res.status(500).send("Check your network connection");
  }
});


// Buyer see offers with a status of "Pending"
app.get("/offer/:buyerid",  (req, res) => {
    const buyerid = req.params
    console.log(buyerid)
    // Async
    Offer.find({buyerid: buyerid.buyerid, offerstatus: "Pending"})
    .then((result)=>{
        console.log(result)
        console.log(result)
        if (result.length > 0) {

            console.log(result)
            res.json(result)
            // Returns a json file, which is to be interpreted at the front-end side

        }
        else{
            res.json({"Error": "You havent placed any offers yet!"})
        }


    })
    .catch((error)=>{
        res.status(404).send(error.msg)
    })
})






// // Mongoose sandbox
// // In the actual thing, probably have to use POST
// app.get("/add-order",(req,res)=>{

//     // Testing out the mongoose model
//     const order = new Order({
//         ordersummary:[
//             {"test1": 2123123012233,"sellerid": "lol1"},
//             {"test2": 12,"sellerid":"lol2"}
//         ],
//         totalprice: 123,
//         buyerid: "buyerid1",
//     })

//     // Save to the mongodb
//     // save is an inbuilt func of moongoose
//     order.save()
//     .then((result)=>{
//         console.log("successful")
//         res.send(result)
//     })
//     .catch((error)=>{
//         console.log(error)
//     })
// })

// // Get all the orders
// app.get("/get-orders",(req,res)=>{
//     Order.find()
//     .then((result)=>{
//         // We can send a res.json back to the front-end side
//         res.send(result)
//     })
//     .catch((error)=>{
//         console.log(error)
//     })
// })

// app.

// ==== ROUTES =====

// app.get('/', (req, res) => {
//     res.send('Hello World!')
//   })

// // Get all orders for a particular user
// // Use of GET method

// app.get('/order', (req, res) => {
//     res.send('Hello World!')
//   })
