<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Listing</title>
    <!-- External CSS for navbar -->
    <link rel="stylesheet" href="style.css">
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
    <link rel="stylesheet" href="./createlisting.css">
    <link rel="icon" href="./asset/HenesysSmallLogo.png">


</head>

<style>
    body {background-color: rgb(239, 239, 239);}
</style>
<body>
    <div id="app">
        <!-- Navbar goes here -->
        <navbar></navbar>
        <!-- Header -->
        <section class="timeline_area section_padding_130 mt-5 mb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12 col-sm-8 col-lg-6">
                        <!-- Section Heading-->
                        <div class="section_heading text-center">
                            
                            <h3>Create your listing.</h3>
                            <div class="line"></div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12">
                        <!-- Timeline Area-->
                        <div class="apland-timeline-area">
                            <!-- Single Timeline Content-->
                            <div class="single-timeline-area">
                                <div class="timeline-date wow fadeInLeft" data-wow-delay="0.1s" style="visibility: visible; animation-delay: 0.1s; animation-name: fadeInLeft;">
                                    <p>Item Information</p>
                                </div>
                                <div class="row">
                                    <div class="col-12 ">
                                        <div class="single-timeline-content wow fadeInLeft" data-wow-delay="0.3s" style="visibility: visible; animation-delay: 0.3s; animation-name: fadeInLeft;">
                                            <div class="timeline-icon"><i class="fa fa-address-card" aria-hidden="true"></i></div>
                                            <div class="timeline-text">
                                                <div class="">
                                                    <label for="description" class="form-label d-flex">Item Name</label>
                                                    <input  v-model="itemname" type="text" class="form-control" id="description">
                                                </div>
                                                <div class="">
                                                    <label for="description" class="form-label">Description</label>
                                                    <input v-model="description" type="text" class="form-control" id="description">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    

                                </div>
                            </div>
                            <!-- Single Timeline Content-->
                            <div class="single-timeline-area">
                                <div class="timeline-date wow fadeInLeft" data-wow-delay="0.1s" style="visibility: visible; animation-delay: 0.1s; animation-name: fadeInLeft;">
                                    <p>Item Category</p>
                                </div>
                                <div class="row">
                                    <div class="col-12">
                                        <div class="single-timeline-content  wow fadeInLeft" data-wow-delay="0.3s" style="visibility: visible; animation-delay: 0.3s; animation-name: fadeInLeft;">
                                            <div class="timeline-icon"><i class="fa fa-briefcase" aria-hidden="true"></i></div>
                                            <div class="mb-3">

                                                <p>Select your category</p>
                                                <div class="form-check" v-for="category in categories">
                                                    <input v-model="selectedCategory" class="form-check-input" type="radio" name="exampleRadios" :id="category" :value="category" checked>
                                                    <label class="form-check-label" :for="category">
                                                        {{ category }}
                                                    </label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                </div>
                            </div>
                            <!-- Single Timeline Content-->
                            <div class="single-timeline-area">
                                <div class="timeline-date wow fadeInLeft" data-wow-delay="0.1s" style="visibility: visible; animation-delay: 0.1s; animation-name: fadeInLeft;">
                                    <p>Pick Up</p>
                                </div>
                                <div class="row">
                                    <div class="col-12">
                                        <div class="single-timeline-content  wow fadeInLeft" data-wow-delay="0.3s" style="visibility: visible; animation-delay: 0.3s; animation-name: fadeInLeft;">
                                            <div class="timeline-icon"><i class="fa fa-id-card" aria-hidden="true"></i></div>
                                            <div class="timeline-text">
                                                <div class="form-check">
                                                    <label for="description" class="form-label">Pick Up Location</label>
                                                    <input v-model="pickupLocation" type="text" class="form-control" id="description">
                                                </div>
                                                <hr>
                                                <div class="form-check">
                                                    <label for="description" class="form-label">Select your date time: </label>
                                                    <div>
                                                        <input v-model="datetime" type="datetime-local">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <button type="button" class="btn btn-success" @click="makeoffer()">Create Listing</button>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Testing New page -->
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
                pickupLocation: "",
                localStorageData: localStorage.id
                
                
            };
        },

        methods:{
            checkLogin() {
                // If the login variable is initalised, then we will redirect them to 
                    if (localStorage.getItem("id")){
                        // redirect them to login page
                        // window.location.replace("/ESD_PROJECT/ESDT4/multi-page/catalogue.php");
                        var jsondata = JSON.parse(localStorage.login)
                        var mobile = jsondata['mobile']
                        console.log(mobile)
                        if (mobile == "" || mobile == "0" || mobile == 0) {
                            window.location.replace("./Insertmobile.php");
                        }
                    }
                    else {
                        window.location.replace("./");
                    }
                }, 

            async makeoffer(){
                // Items to send to the create_offer complex
                payload = {
                    seller_id: this.localStorageData,
                    item_details:{
                        item_name: this.itemname,
                        description: this.description,
                        category: this.selectedCategory,
                        date_time: this.datetime,
                        location: this.pickupLocation,
                    }
                    
                }
                // Date time format 
                // "2022-03-17T13:05"
                console.log(payload);
                // Usage of fetch API
                // Options for fetch API
                url = "http://localhost:5100/create_listing"
                options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                }
                const result = await fetch(url, options);

                const data = await result.json();

                try{
                    if (result.ok){
                        console.log(data);
                        alert("Item Listing created successfully");
                        window.location.href="cataloguenew.php";
                    }
                    else{
                        console.log(data);
                        alert("Listing creation failed");
                    }

                }
                catch(error){

                    console.log(error)

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