<template>

    <div class="sellerView">
    <h1>This is the Seller's View</h1>

    <br><br>
    <div>
        <form action=" ">
            <label for="ItemName">Name of Item: &nbsp;</label> 
                <input type="text" id="ItemName" name="ItemName"><br><br>
            <label for="Category">Item Category: &nbsp;</label>
                <input type="text" id="Category" name="Category"><br><br>
            <label for="ItemDesc">Item Description: &nbsp;</label>
                <input type="text" id="ItemDesc" name="ItemDesc"><br><br>
            <label for="Price">Price of Item: &nbsp;</label>
                <input type="text" id="Price" name="Price"><br><br>
            <label for="SellerID">Enter your ID: &nbsp;</label>
                <input type="text" id="SellerID" name="SellerID"><br><br>
            <label for="ItemStatus">Item Status: &nbsp;</label>
                <input type="text" id="ItemStatus" name="ItemStatus" value="Open" readonly><br><br>
            <input type="submit" value="Submit">
        </form>
    </div>

    </div>
</template>

<script>

//   export default {
//     name: "SellerView",

//     data() {
//       return {
//         items:[
//           {
//             name: "Item 1",
//             price: "10",
//             quantity: "0",
//             sellerid: "1"
//           },
//           {
//             name: "Item 2",
//             price: "20",
//             quantity: "0",
//             sellerid: "1"

//           },
//           {
//             name: "Item 3",
//             price: "30",
//             quantity: "0",
//             sellerid: "2"

//           }
//         ],
//         quantity: [1,2,3,4,5,6,7,8,9,10],
//         selected: 0

//         }
//     },

//     methods: {

//       sumPrice(){
//         let sum = 0;
//         for(let i = 0; i < this.items.length; i++){
//           sum += this.items[i].price * this.items[i].quantity;
//         }
//         return sum;
//       },
      
//       summarise(){

//       }
    
//     }
//   }
</script>

<style scoped></style>