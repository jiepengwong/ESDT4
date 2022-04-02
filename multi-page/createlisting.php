<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Offers</title>
    <!--bootstrap css-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!--axios-->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <!--Vue-->
    <script src="https://unpkg.com/vue@next"></script>
    <!-- Google Auth0 -->
    <script async defer src="https://apis.google.com/js/api.js"
        onload="this.onload=function(){};handleClientLoad()"
        onreadystatechange="if (this.readyState === 'complete') this.onload()">
    </script>
    <meta name="google-signin-client_id" content="616186403576-ofsdqf0tp3r19t60rmflus3l3h9p25vo.apps.googleusercontent.com">
</head>

<body>
    <div id="app">
        <!-- Navbar goes here -->
        <navbar></navbar>
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

<script src="./narbar.js"></script>
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
            checkLogin() {
                // If the login variable is initalised, then we will redirect them to 
                    if (localStorage.getItem("id")){
                        // redirect them to login page
                        // window.location.replace("/ESD_PROJECT/ESDT4/multi-page/catalogue.php");
                    }
                    else {
                        window.location.replace("/ESD_PROJECT/ESDT4/multi-page/index.html");
                    }
                }, 

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

        mounted() {
            this.checkLogin();
        }


    });

app.component("navbar",{
        template: template1,
        data() {
            return{
                links: links1,
                isSignedIn: localStorage.getItem("id"),
            }

        },

        methods:{
            
            signOut() {
                let gapi = window.gapi;
                let clientId ="616186403576-ofsdqf0tp3r19t60rmflus3l3h9p25vo.apps.googleusercontent.com";
                let apiKey ="AIzaSyC0WtHoYqLnGKgaqLWX6RGkiL0X2C7dll8";
                let secretClientId = "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";
                let discoveryDocs =["https://www.googleapis.com/discovery/v1/apis/oauth2/v2/rest"];
                let scope ="https://www.googleapis.com/auth/userinfo.profile";

                gapi.load("client:auth2", () => {
                    gapi.client.init({
                        apiKey,
                        clientId,
                        discoveryDocs,
                        scope,
                        secretClientId,})

                        .then(() => {
                            var GoogleAuthObj = gapi.auth2.getAuthInstance();
                            this.GoogleAuth = GoogleAuthObj.signOut();
                            this.isSignedIn = false;
                        })
                })
                
                localStorage.removeItem("login")
                localStorage.removeItem("id")
                alert("You have been logged out!")
                location.reload()
    },
        }
    })


    app.mount("#app");
</script>

</html>