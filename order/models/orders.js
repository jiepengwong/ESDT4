const mongoose = require("mongoose");
const Schema = mongoose.Schema; // Constructor function
// We need to FIRST create SCHEMA, THEN MODEL
// === Creation of Schema ===

// This is like the template for each listing
const orderSchema = new Schema({
        // Put an object here so we can have more properties like required and stuff
        ordersummary: [{type:Object,required:true, sellerid:{type: String, required: true}}],
        totalprice: {
            type:Number,
            required: true
        },
        buyerid: {
            type: String,
            required: true
        }
      
      
    }, {timestamps:true})

// === Creation of Model ===
// This would refer to an instance of the blog 
const Order = mongoose.model('Order',orderSchema);
// First argument here refers to the collection in the database collection
// Second argument here refers to the structure. Schema is specified here to display the structure

// We will call the shop as a class
module.exports = Order;