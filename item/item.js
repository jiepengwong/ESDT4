const express = require("express");
const cors = require('cors');
const mongoose = require("mongoose");
const Item = require("./models/itemSchema");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());

// Converts Json to javascript object
// app.use(express.json());

// Takes URL encoded data and parses it into a JavaScript object on express server
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

var jsonParser = bodyParser.json();

// Connection to the mongoDB
const dbURI =
  "mongodb+srv://esdt4:esdt4@nodejstutoriallearning.xssjk.mongodb.net/itemdb?retryWrites=true&w=majority";
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
const port = 5001;
// =========================================================================================

// ======= [POST] =======

// Method: [POST] create item
// URL: /createitem

// What if the buyer post 2 of the exact same item?
app.post("/createitem", (req, res) => {
    // From the front-end side of things
    const itemreq = req.body;

    // Create a new item
    const newItem = new Item({
        item_name: itemreq.item_name,
        category: itemreq.category,
        description: itemreq.description,
        location: itemreq.location,
        date_time: itemreq.date_time,
        seller_name: itemreq.seller_name,
        seller_id: itemreq.seller_id,
        seller_mobile: itemreq.seller_mobile,
    });

    newItem.save()
        .then((result) => {
            // Edit code here in the future to get back the order id (postreq._id)
            res.status(200).json({"code": 200, "Success" : result});

        })
        .catch((err) => {
            res.status(404).json({"code": 404, "message": `${err}`});

            // console.log(err.msg)
        });



})

// ======= [GET] =======

// Method: [GET] all items
// URL: /items
app.get("/items", (req,res) =>{
    Item.find().where("item_status").equals("open")
    .then((result)=>{

        console.log(result)


        if (result === []){
            res.json({"code": 404,"message": result}).status(404);


        }

        else{
            res.json({"code": 200,"Success": result}).status(200);

        }

    })

    .catch((err)=>{
        res.json({"code": 404,"message":err}).status(404);

    })
    
});

// Method: [GET] particular item details
// URL: /items/:id
app.get("/items/:id",(req,res) =>{
    console.log(req.params.id);
    Item.findOne({ "_id": req.params.id}, (err, item) => {
        if (err) {
        res.json({"code": 404,"message":err}).status(404);
        }
        // Send json response of items
        res.json({"code": 200,"Success":item}).status(200);
    });


})

// Potential security issue with this.
// There has be some validation at the front-end side of things
//  Check if the session id is same as the buyerid
// E.g if yuxuan access and got hold of yuxiang page, it would be unsuccessful, as conditional checks 


// At offers page. Upon mounted, fetch this items/buyer_id and display them. Since we get oauthid this is possible
// Categorize according to (Pending, Accepted By Seller (Not Paid), Completed (Paid))

// Method: [GET] offers made by a particular buyer
// This would include  (Pending, Closed, Accepted)
// URL: /items/myoffers/:buyer_id
app.get("/items/myoffers/buyer/:buyer_id",(req,res) =>{
    console.log(req.params.buyer_id);

    // Check if buyer_id exists
    Item.exists({"buyer_id": req.params.buyer_id})
    .then((result) =>{
        console.log(result);

        if (result === null){
            res.json({"code": 404,"message": "There is no such buyer at all"}).status(404);
        }


        else{
            // Buyer exists
            Item.find({ "buyer_id": req.params.buyer_id}).where("seller_id").ne(req.params.buyer_id)
            .then((result) => {
    
                if (result === []){
                    console.log("hi")
                    console.log(result)
                    res.json({"code": 404,"message": "Buyer did not make an offer"}).status(404);
                }
                else{
                    res.json({"code": 200,"Success": result}).status(200);
    
                } 
    
            })
    
            .catch((err)=>{
                res.json({"code": 404, "message" : err}.status(404))
            })

        }

        // Conditional clause to check if buyer_id not equals to buyer_id



    })

    .catch((err) =>{
        res.json({"code": 404,"message": err}).status(404);



    })

    
        // Send json response of items


})

// UI side to include 
// We get all the items from seller_id and display them.
// Method: [GET] offers made by a particular buyer
// This would include  (Open, Pending, Accepted, Closed)
// URL: /items/myoffers/:buyer_id


// WEIRD THING IS THAT SELLER ID HAS TO BE A STRING, 
app.get("/items/mylistings/seller/:seller_id",(req,res) =>{

    console.log(req.params.seller_id);

    // Check if buyer_id exists
    Item.exists({"seller_id": req.params.seller_id})
    .then((result) =>{
        console.log(result);

        if (result === null){
            res.json({"code": 404,"message": "There is no such seller at all"}).status(404);
        }

        else{

            Item.find({ "seller_id": req.params.seller_id}).where("buyer_id").ne(req.params.seller_id)
            .then((result) => {
                console.log("hi")
                console.log(result)
    
                if (result === []){
                    res.json({"code": 404,"message": "Seller has no listings"}).status(404);
                }
                else{
                    res.json({"code": 200,"Success": result}).status(200);
    
                } 
    
            })
    
            .catch((err)=>{
                console.log(err)
                res.json({"code": 404, "message": err}).status(404)
            })
        }

        // Buyer exists
        // Conditional clause to check if buyer_id not equals to buyer_id


    })

    .catch((err) =>{
        res.json({"code": 404,"message": `"${req.params.seller_id} There is no such buyer at all"`}).status(404);



    })

    // console.log(req.params.seller_id);
    // Item.find({ "seller_id": req.params.seller_id})
    // .then((item) => {
    //     console.log(item)
    //     res.json({"Success": item} ).status(200);
    // })

    // .catch((err)=>{
    //     res.json({ "Error" : err} .status(404))
    // })
})

// ======== [PUT] ========
// Method: [PUT] Update relevant item details (This can be both the buyer and the seller side)
// Can be used by a buyer or a seller
// buyer_id, mobile and price, item status (Buyer)
// Update item status (Seller) 

app.put("/items/:id",(req,res) =>{
    // On the front-end side of things, verify the data format first
    const updateDetails = req.body;  // Contains the existing parameters that needs to be changed
    console.log(updateDetails)
    // console.log(req.params.id);

    // Filter and update
    Item.find({ "_id": req.params.id})
    .then((result) =>{
        // console.log(result);
        // console.log(req.params.id)
        console.log(result)
        console.log(result[0].seller_id)
        console.log(updateDetails.buyer_id)

        if (result[0].seller_id == updateDetails.buyer_id){
            res.status(404).json({"code": 404,"message": "Not updated, buyer_id cannot be the same as seller_id. TRY again"});
        }
        else{

            Item.findByIdAndUpdate({ "_id": req.params.id}, updateDetails, {new: true})  
            
            .then((result)=>{
                // console.log(result)
        
                // Check if buyer_id == to seller_id (This is not possible)
        
                if (result["buyer_id"] == result["seller_id"]){
                    res.status(404).json({"code": 404,"message": "Not updated, buyer_id cannot be the same as seller_id. TRY again"});
                }
        
                else{
                    for (value in updateDetails){
                        console.log(value)
                        // Check if update is successful here
                        if (result[value] != updateDetails[value]){
                            console.log("Unsuccessful update")
                            return res.status(404).json({"code": 404,"message": "Not updated, check the data type of the parameters"});
                        }
                    }
        
                    return res.status(200).json({"code": 200,"Success" : result});
                }
        
        
        
            })
            .catch((err)=>{
                res.status(404).json({"code": 404,"message": 'Unable to find the item'});
            })
        }
        // res.status(200).json({"code": 200,"Success" : result});
        // Check if the item exists
     

    })
    .catch((error) =>{
        res.json({"code": 404,"message": 'Unable to find the item'}).status(404);
    })
})

// ========== [DELETE] ==========
// Method: [DELETE] Delete an item
app.delete("/items/delete/:id", (req, res) => {
    Item.findByIdAndDelete(req.params.id)
        .then((result) => {
            res.status(200).json({"code": 200,"Success" : `${result._id} Deleted successfully`});
        })
        .catch((err) => {
            res.status(404).json({"code": 404,"message": `${err}`});
        });
})

// To delete all the items
app.get("/delete", (req,res) =>{
    Item.deleteMany({}, function(err){
      if(err) console.log(err);
      else console.log("Offers deleted");
    });
})