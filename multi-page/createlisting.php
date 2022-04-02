<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- Vue Application -->
    <script src="https://unpkg.com/vue@3"></script>
    <!--  Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous" />
</head>

<body>
    <div id="app">
        <!-- Navbar goes here -->
        <nav class="navbar navbar-light bg-light static-top">
            <div class="container">
                <a class="navbar-brand" href="#!">Start Bootstrap</a>
                <a class="btn btn-primary" href="#signup">Sign Up</a>
            </div>
        </nav>

        <!-- Header -->

        <header class="masthead bg-success p-5">
            <div class="container position-relative">
                <div class="row justify-content-center">
                    <div class="col-xl-6">
                        <div class="text-center text-white">
                            <!-- Page heading-->
                            <h1 class="mb-5">List your items here.</h1>
                            <div class="mb-3">
                                <div class="form-check">
                                    <label for="description" class="form-label">Item Name</label>
                                    <input  v-model="itemname" type="text" class="form-control" id="description">
                                </div>


                                <div class="mb-3">

                                    <p>Select your category</p>
                                    <div class="form-check" v-for="category in categories">
                                        <input v-model="selectedCategory" class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1" checked>
                                        <label class="form-check-label" for="exampleRadios1">
                                            {{ category }}
                                        </label>
                                    </div>
                                </div>

                                <div class="form-check">
                                    <label for="description" class="form-label">Description</label>
                                    <input v-model="description" type="text" class="form-control" id="description">
                                </div>

                                <div class="form-check">
                                    <label for="description" class="form-label">Pick Up Location</label>
                                    <input v-model="pickupLocation" type="text" class="form-control" id="description">
                                </div>

                                <div class="form-check">
                                    <label for="description" class="form-label">Select your date time</label>
                                    <input v-model="datetime" type="datetime-local">
                                </div>
                                

                            </div>

                            
                            <button @click="makeoffer()">Create listing</button>

                        </div>
                    </div>
                </div>
            </div>
    </div>
    </header>

    </div>
</body>

<script>
    const app = Vue.createApp({
        data() {
            return {
                categories: ["Fruits", "Vegetable", "Meat", "Dairy", "Wheat"],
                itemname: "",
                description: "",
                selectedCategory: "",
                datetime: "",
                pickupLocation: ""
                
                


            };
        },

        methods:{
            async makeoffer(){
                payload = {
                    item_name: this.itemname,
                    description: this.description,
                    category: this.selectedCategory,
                    datetime: this.datetime,
                    location: this.pickupLocation


                }


                
                // Date time format 
                // "2022-03-17T13:05"
                console.log(payload);
                // Usage of fetch API
                // Options for fetch API
                url = "www.google.com/forcreatelistingcomplex"
                options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                }

                const result = await fetch(url, options );

                const data = await result.json();

                try{
                    if (result.ok){
                        console.log(data);
                        alert("Listing created successfully");
                    }
                    else{
                        console.log(data);
                        alert("Listing creation failed");
                    }

                }
                catch{

                }
                
            }


        },

        computed:{

        }


    });

    app.mount("#app");
</script>

</html>