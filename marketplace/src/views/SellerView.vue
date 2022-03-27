<template>

    <div class="container container-fluid">

    <div class="row">
        <div class="col-12 text-center">
            <br>
            <h4>Add a New Product</h4>
        </div>
    </div>

    <div class="row text-center">
        <div class="col-3"></div>
        <div class="col-6">
            <form action="">
                <div class="form-group">
                    <label for="productName">Product Name</label>
                    <input type="text" class="form-control" id="productName" placeholder="Enter Product Name" v-model='name'>
                </div>
                <br>
                <div class="form-group">
                    <label for="productDescription">Product Description</label>
                    <input type="text" class="form-control" id="productDescription" placeholder="Enter Product Description" v-model='description'>
                </div>
                <br>
                <div class="form-group">
                    <label for="productCategory">Product Category</label>
                    <input type="text" class="form-control" id="productCategory" placeholder="Enter Product Category" v-model='category'>
                </div>
                <br>
                <div class="form-group">
                    <label for="productPrice">Product Price</label>
                    <input type="text" class="form-control" id="productPrice" placeholder="Enter Product Price" v-model='price'>
                </div>
                <br>
                <div class="form-group">
                    <label for="productImage">Product Image</label>
                    <input type="text" class="form-control" id="productImage" placeholder="Enter Product ImageURL" v-model='imageURL'>
                </div>
                <br>

                <button type='button' class='btn btn-primary' @click="addProduct">Add Product</button>
            </form>
        </div>
        <div class="col-3"></div>
    </div>

    <div class="row">
        <div class="col-6">
        </div>
    </div>

    <div class="row">
        <div class="col-6">
        </div>
    </div>

    </div>
</template>

<script>

    import axios from 'axios';
    import swal from 'sweetalert';
export default {
    name: "SellerView",

    prop: ["baseURL"],

    data() {
    //   return {
    //     items:[
    //       {
    //         name: "Item 1",
    //         price: "10",
    //         quantity: "0",
    //         sellerid: "1"
    //       },
    //       {
    //         name: "Item 2",
    //         price: "20",
    //         quantity: "0",
    //         sellerid: "1"

    //       },
    //       {
    //         name: "Item 3",
    //         price: "30",
    //         quantity: "0",
    //         sellerid: "2"

    //       }
    //     ],
    //     quantity: [1,2,3,4,5,6,7,8,9,10],
    //     selected: 0

    //     }

        return{
            id: null,
            categoryID: null,
            name: null,
            description: null,
            price: null,
            imageURL: null
        }
    },

    methods: {


    addProduct(){

        const newProduct ={
            name: this.name,
            description: this.description,
            price: this.price,
            imageURL: this.imageURL,
            categoryID: this.categoryID
        }

        axios.post(this.baseURL + 'product/add', newProduct)
        .then(() => {
            // console.log(response);
            // this.name = null;
            // this.description = null;
            // this.price = null;
            // this.imageURL = null;
            // this.categoryID = null;

            this.$router.push({ name: 'SellerView' });
            swal({

                text: "Product Added",
                icon: "success",

            });
        })



    }
    
    }
  }
</script>

<style scoped>


.form-group {
  margin: auto;
}
</style>