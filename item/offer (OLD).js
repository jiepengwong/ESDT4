const express = require("express");
const mongoose = require("mongoose");
const Offer = require("./models/offerSchema");
const bodyParser = require("body-parser");
const { OrderedBulkOperation } = require("mongodb");

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

// Test to wipe the database
app.get("/delete", (req,res) =>{
  Offer.deleteMany({}, function(err){
    if(err) console.log(err);
    else console.log("Offers deleted");
  });
})

app.post("/offer/buyer/createoffer",  (req, res) => {
  // From the front-end side of things
    const postreq = req.body;

  // Create a new instance at the database side
  // We dont want to create an instance where by 
  if (req.body && req.body.buyerid != req.body.sellerid)  {
    console.log(req.body);
    const newOffer = new Offer({
      price: postreq.price,
      itemname: postreq.itemname,
      itemid: postreq.itemid,
      buyerid: postreq.buyerid,
      sellerid: postreq.sellerid,
    });

    // Save the new instance to the database
    // Check if the offer is already in the database, if it is update offer instead of creating a new one
    Offer.findOne({ itemid: postreq.itemid, buyerid: postreq.buyerid })
      .then((result) => {
        if (result) {
          console.log("Offer already exists, please update offer instead");
          res.status(400).json({"Error": "Offer already exists, edit the offer instead!"});
        } else {

            // Async funnction
          newOffer.save()
          .then((result) => {
            res.status(200)

            // Edit code here in the future to get back the order id (postreq._id)
            res.json({"Success" : `Your order id is : ${result._id}`});

          })
          .catch((err) => {
            res.status(400).json({"Error": `${err}`});

            // console.log(err.msg)
                });


            // res.status(500).json("{Error: Network error}");
            } 
          })

        }

      else{
        if (postreq.buyerid == postreq.sellerid) {
        res.status(400).json({"Error": "Buyer cannot be the seller"});
      }

      else {
        res.status(400).json({"Error": "Invalid field?"});


      }
    }

  
});





// Buyer see offers with a status of "Pending"
app.get("/offer/buyer/view/:buyerid",  (req, res) => {
    const buyerid = req.params
    console.log(buyerid)
    // Async
    // Grabs the relevant orders which are status of pending
    Offer.find({buyerid: buyerid.buyerid, offerstatus: "Pending"})
    .then((result)=>{
        console.log(result)
        console.log(result)
        if (result.length > 0) {

            console.log(result)
            res.status(200).json(result)
            // Returns a json file, which is to be interpreted at the front-end side

        }
        else if (result.length == 0) {
            res.status(400).json({"Error": "This buyerid does not exist at all"})
        }


    })
    // Catch error activated, because unable to find the order, weird because catch only works for string
    // Error handling solved for now 13/3/2022
    .catch((error)=>{
        res.status(400).json({"Error": "This buyerid does not exist at all, buyerid in URL is a string"})
        console.log(error)
    })
})



// Buyer to update the offer via "Edit" button or smgth, to edit the price
app.put("/offer/buyer/edit/:offerid", (req,res) =>{
    const offerid= req.params
    const postreq = req.body
    console.log(postreq)
    // Only works for offerstatus = "Pending"
    Offer.findOneAndUpdate({offerid: offerid.offerid, offerstatus: "Pending"},  {price: postreq.price})
    .then((result)=>{
        console.log(result)
        if (result) {
            console.log(result)
            if (result.price == postreq.price){
              res.json({"Success": "Offer updated"})
            }
            else{
              res.status(400).json({"Error": "Offer not updated, did you key in correctly?"})

            }
        }
        else{
            res.json({"Error": "Offer not updated, wrong field?"})
        }
    })
    // Catch error activated, because unable to find the order
    .catch((error)=>{
        res.status(404)
        console.log(error)
    })
})


// Buyer to delete its offer listing, providing if it is still pending
app.delete("/offer/buyer/delete/:offerid", (req,res) =>{
  const offerid= req.params
  const postreq = req.body
  Offer.deleteOne({offerid: offerid.offerid, offerstatus: "Pending"})
  .then((result)=>{
    // If successful
    // Check of deletedcount is 1, if it is status 200, else 400
    console.log(result)
    if (result.deletedCount == 1){
      console.log(result)
      res.status(200).send({"Success": "Offer deleted!"})
    }
    else{
      
      res.status(400).send({"Error": "Offer not deleted, unable to delete,offerid does not exist OR status might have changed"})

    }
  
  })
  .catch((error)=>{
    // If error
    // Not really sure in what circumstances it would be different here
    res.status(400).send({"Error": "Offer not deleted, unable to delete, offerstatus might be pending already be accepted or rejected"})
  })
 
})

// Sellers see all the relevant offers
app.get("/offer/seller/:sellerid",  (req, res) => {
    const sellerid = req.params
    console.log(sellerid)
    // Async
    // Grabs the relevant orders which are status of pending
    // We want to find offers that are not created by the seller as well
    // Buyerid cannot be equals to the sellerid
    // Usage of mongodb queries (Stackoverflow)
    Offer.find({sellerid: sellerid.sellerid, offerstatus: "Pending"}).where("buyerid").ne(sellerid.sellerid)
    .then((result)=>{

        console.log(result)
        console.log(result)
        if (result.length > 0) {

            console.log(result)
            res.json(result)
            // Returns a json file, which is to be interpreted at the front-end side

        }
        else if (result.length == 0) {


       
          // Check for existance of sellerid in the database
          Offer.exists({sellerid: sellerid.sellerid})
          .then((result)=>{
            if (result){
              res.json({"Error": "You have no existing offers yet!"})
            }
            else{
              res.json({"Error": "There is no such sellerid in the database"})
            }
          })
          .catch((error)=>{
            res.json({"Error": `${error}`})
          })

        }
        // Note to self if things doesn't make sense
        // Sellerid and buyerid will be in the offer, hence we can say that there is no such sellerid, ALTHOUGH there exists the profile ID, so logic is fine here

        


        })

    // Catch error activated, because unable to find the offer
    // Error activated if it is not a string 
    .catch((error)=>{
        res.status(404)
        res.json({"Error": `${error.reason}`})
        console.log(error)
    })
})

// Sellers accept the offer
app.put("/offer/seller/accept/:offerid",  (req, res) => {
    const offerid = req.params;
    var itemid = "";
    var sellerid = "";
    console.log(offerid)
    // Get the orderID from the frontend, get the itemid, we need this to retrieve the relevant orders 
    Offer.find({_id: offerid.offerid})
    .then((result)=>{
        // console.log(result)
        itemid = result[0].itemid;
        sellerid = result[0].sellerid;
    })
    .catch((error)=>{
        console.log(error)
        res.json({"Error": "Unable to update failed, does the offer exist?"})

    })
    

    // Update the offer status to "Accepted", FOR THAT particular ORDERID

    Offer.findByIdAndUpdate(offerid.offerid, {offerstatus: "Accepted"})
    .then((result)=>{
        console.log(`Offer ${offerid.offerid} has been accepted by seller ${sellerid}`)

        // // Reject all other offers, by setting the status to updated+, but at the same time invoke the notification service? TBC
        // // Find the orders at which sellerid is the same  and the same itemid and offerstatus is pending
        // Offer.find({sellerid: sellerid, itemid: itemid, offerstatus: "Pending"}).where("buyerid").ne(sellerid.sellerid)
        // .then((result)=>{
        //     console.log("i AM EXECUTED HERE")
        //     console.log(result)

        //     // Update the offerstatus to rejected
        //     if (result.length > 0) {
        //         Offer.updateMany({ name: 'Jon Snow' }, {
        //           title: 'King in the North'
        //         });
        //       }
        //       else{
        //           console.log("No offers to reject")
        //       }

        // })

        // Update the other offers to offerstatus: "Rejected"
        // Search for sellerid listing itemid, since itemid is unique, with the offerstatus of Pending

        Offer.updateMany({sellerid: sellerid, itemid: itemid, offerstatus: "Pending"}, {offerstatus: "Rejected"})
        .then((result)=>{

          console.log(result)

          for (var i = 0; i < result.n; i++) {
            console.log(`Offer ${result._id} has been rejected`)
          }

          res.json({"Success":"Successfully updated all the other sellers to rejected"})

        })
        .catch((error)=>{
          console.log(error)

          res.json("{Error: Unable to update}")

        })
        
        });

        
      })
      
      // .catch((error)=>{
      //     console.log(error)
      //     res.json({"Error": "Unable to update failed, does the offer exist?"})
  
      // })











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
 // Update the offer
//  Offer.findOneAndUpdate(
//   { itemid: postreq.itemid, buyerid: postreq.buyerid },
//   { $set: { price: postreq.price } },