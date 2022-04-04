<?php

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catalogue</title>
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
    <link rel="icon" href="./asset/HenesysSmallLogo.png">
</head>
  <body>
    <div id="app">
      <!-- Navbar goes here -->
      <navbar></navbar>
      <!-- Header -->

      <section id="landing" class="p-5">
        <div class="container position-relative">
          <div class="row justify-content-center">
            <div class="col-xl-6">
              <div class="text-center text-white">
                <!-- Page heading-->
                <h1 class="mb-5">Henesy Market Catalogue!</h1>

                <!-- Search bar input-->
                <div class="row">
                  <div class="col">
                    <input
                      class="form-control form-control-lg"
                      type="text"
                      placeholder="Type your desired item here"
                      v-model="search"
                  
                    />
                  </div>
                </div>


              </div>
            </div>
          </div>
        </div>

        <div class="d-flex justify-content-center cataloguefilter">
            <ul class="catalogue-li" v-for="category in categories"  :key="category" > 
              <li><button @click="filterPosts(category)" class="catalogue-li" @click="filter">{{category}}</button></li>
        </ul>
        </div>

      </section>


      <section id="listings">

        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <h2 class="mb-5 py-5">Listings</h2>
            </div>
          </div>
          <div class="row">
            <div v-for="result in filterListings" :key="result" class="col-lg-4 col-md-6 mb-4">
              <div class="card h-100">
                <a href="#"><img class="card-img-top" src="http://placehold.it/700x400" alt="" /></a>
                <div class="card-body">
                  <h4 class="card-title">
                    <a href="#">{{result.item_name}}</a>
                  </h4>
                  <p class="card-text">{{result.description}}</p>
                  <button class="btn btn-success"><a class="text-white":href="`itemDetailsNew.php?itemid=${result._id}`" >More Details</a></button>
                </div>
                <div class="card-footer">
                  <small class="text-muted">Sold by: {{result.seller_name}}
                </div>
              </div>
            </div>

        </div>


      </section>


    </div>
  </body>
</html>

<script src="./narbar.js"></script>
<script>

  const app = Vue.createApp({
    data() {
      return {
        count: 0,
        results: [],
        unfilteredResult: "",
        search: "",
        categories: ["All","Fruits","Vegetable","Meat","Dairy","Wheat"],
      };
    },

    methods:{

    },


    async mounted() {
      this.checkLogin()
      // Fetching from NEW items microservice
      try{
          var getItemUrl = "http://localhost:5001/items"
          
          var databaseitems = await fetch(getItemUrl)
          const databaseitemsJson = await databaseitems.json()

          if (databaseitems.status === 200){
            console.log(databaseitemsJson)
            // Get all the databases 
            this.results = databaseitemsJson.Success;
            this.unfilteredResult = databaseitemsJson.Success;
            console.log(this.results)

          }
          else{
            console.log("Database not connected")
          }
          }

          catch(error) {
            console.log(error)
          }




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
      filterPosts(categoryName){
        console.log("hi")
        this.resetPosts()
        if (categoryName !== "All"){

          this.results = this.results.filter((result) => {
            // console.log(result.Category)
            return result.category === categoryName;
          })
        }

      },

      resetPosts(){
        this.results = this.unfilteredResult
      }
    },

    computed:{
      filterListings() {
        return this.results.filter(item => {
          return item.item_name.toLowerCase().match(this.search.toLowerCase());
        });
      }
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

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap');


#landing{
  background-image: url("asset/marketplacebg.jpg");
  background: linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url("asset/marketplacebg.jpg");

  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  /* height: 100vh; */
}


.catalogue-li{
    list-style: none;
}

.catalogue-li li{
    display: flex;
    /* padding: 0px 20px; */
}

.catalogue-li li a{
    transition: all 0.3s ease-in-out;
}

.catalogue-li button{
  box-sizing: border-box;
  color: #1cc49d;
    background-color: #1b2f31;
    border-radius: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2em; 
    width: 7em;
    /* font-size: large; */
    /* font-weight: 600; */

} 


.catalogue-li button:hover{
    box-sizing: border-box;
    color: white;
    background-color: #1b2f31;
    border-radius: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2em; 
    width: 7em;
    /* font-size: large; */
    /* font-weight: 600; */

} 
.catalogue-li li a:hover{
    color: rgb(252, 169, 14);
    border-radius: 50px;

}

.cataloguefilter{
  margin-top: 20px;
}
</style>

<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
  crossorigin="anonymous"
></script>
