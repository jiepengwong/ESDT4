const mongoose = require("mongoose");
const Schema = mongoose.Schema; // Constructor function
// We need to FIRST create SCHEMA, THEN MODEL
// === Creation of Schema ===

// This is like the template for each listing
const itemSchema = new Schema({
        // Put an object here so we can have more properties like required and stuff
    

        item_name: {
            type: String,
            required: true
        },

        category: {
            type: String,
            required: true
        },

        description:{
            type: String,
            required: true
        },
        location:{
            type: String,
            required: true
        },

        date_time: {
            type: String,
            required: true
        },

        item_status:{
            type: String,
            default: "open"
        },

        price: {
            type: Number,
            default: null
        },

        seller_id: {
            type: String,
            required: true
        },

        
        seller_mobile: {
            type: Number,
            required: true
        },

        buyer_id: {
            type: String,
            default: null
        },

        buyer_mobile:{
            type: Number,
            default: null

        }




    
    }, {timestamps:true})

// === Creation of Model ===
// This would refer to an instance of the blog 
const Offer = mongoose.model('Item',itemSchema);
// First argument here refers to the collection in the database collection
// Second argument here refers to the structure. Schema is specified here to display the structure

// We will call the shop as a class
module.exports = Offer;