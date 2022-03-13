const mongoose = require("mongoose");
const Schema = mongoose.Schema; // Constructor function
// We need to FIRST create SCHEMA, THEN MODEL
// === Creation of Schema ===

// This is like the template for each listing
const offerSchema = new Schema({
        // Put an object here so we can have more properties like required and stuff
    

        price: {
            type: Number,
            required: true
        },

        itemname: {
            type: String,
            required: true
        },

        itemid:{
            type: String,
            required: true
        },
        buyerid:{
            type: Number,
            required: true
        },

        sellerid: {
            type: Number,
            required: true
        },

        offerstatus:{
            type: String,
            default: "Pending"
        }


    
    }, {timestamps:true})

// === Creation of Model ===
// This would refer to an instance of the blog 
const Offer = mongoose.model('Offer',offerSchema);
// First argument here refers to the collection in the database collection
// Second argument here refers to the structure. Schema is specified here to display the structure

// We will call the shop as a class
module.exports = Offer;