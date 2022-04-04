<?php

?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Items Details</title>
  <!-- External CSS for navbar -->
  <link rel="stylesheet" href="style.css">
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
<style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        body {
            background-color: lightgreen;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif
        }

        .container {
            margin: 50px auto
        }

        .body {
            position: relative;
            width: 720px;
            height: 440px;
            margin: 20px auto;
            border: 1px solid #dddd;
            border-radius: 18px;
            overflow: hidden;
            box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
            

        }

        .box-1 img {
            width: 100%;
            height: 100%;
            object-fit: cover
        }

        .box-2 {
            padding: 10px
        }

        .box-1,
        .box-2 {
            width: 50%
        }

        .h-1 {
            font-size: 24px;
            font-weight: 700
        }

        .text-muted {
            font-size: 14px
        }

        .container .box {
            width: 100px;
            height: 100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 2px solid transparent;
            text-decoration: none;
            color: #615f5fdd
        }

        .box:active,
        .box:visited {
            border: 2px solid #124821
        }

        .box:hover {
            border: 2px solid #124821
        }

        .btn.btn-primary {
            background-color: transparent;
            color: #124821;
            border: 0px;
            padding: 0;
            font-size: 14px
        }

        .btn.btn-primary .fas.fa-chevron-right {
            font-size: 12px
        }

        .footer .p-color {
            color: #124821
        }

        .footer.text-muted {
            font-size: 10px
        }

        .fas.fa-times {
            position: absolute;
            top: 20px;
            right: 20px;
            height: 20px;
            width: 20px;
            background-color: #f3cff379;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center
        }

        .fas.fa-times:hover {
            color: #ff0000
        }

        @media (max-width:767px) {
            body {
                padding: 10px
            }

            .body {
                width: 100%;
                height: 100%
                
            }

            .box-1 {
                width: 100%
            }

            .box-2 {
                width: 100%;
                height: 440px
            }
        }
</style>
<body>
  <div id="app">
  <navbar></navbar>

  <!-- Testing New UI -->
  <div class="container" >
            <div class="body d-md-flex align-items-center justify-content-between" style="background-color:white;">
                <div class="box-1 mt-md-0 mt-5" > 
                  <img v-if="results['category'] == 'Meat'"src="./asset/Meat.jpg" style="width: 481; height:721 "class="" alt="">
                  <img v-else-if="results['category'] == 'Fruits'"src="./asset/Fruits.jpg" style="width: 481; height:721 "class="" alt=""> 
                  <img v-else-if="results['category'] == 'Vegetable'"src="./asset/Vegetable.jpg" style="width: 481; height:721 "class="" alt=""> 
                  <img v-else-if="results['category'] == 'Dairy'"src="./asset/Dairy.jpg" style="width: 481; height:721 "class="" alt=""> 
                  <img v-else-if="results['category'] == 'Wheat'"src="./asset/Wheat.jpg" style="width: 481; height:721 "class="" alt="">
                  <img v-else src="./asset/Marketplace.PNG" style="width: 481; height:721 "class="" alt=""> 


                </div>
                <div class=" box-2 d-flex flex-column h-100">
                    <div class="mt-5">
                      
                        <p class="mb-1 h-1">{{results.item_name}}</p>
                        <p class="mb-5">{{results.description}}</p>
                        <p class="mb-1 fs-6">Category: {{results.category}}</p>
                        <p class="mb-1 fs-6">Pick-up location: {{results.location}}</p>
                        <p class="mb-1 fs-6">Date Time: {{results.date_time}}</p>

                        <div class="d-flex flex-column mt-5">
                           Enter Your Offer Price: 

                            <div class="input-group">
                              <span class="input-group-text">$</span>
                              <input type="number" class="form-control" v-model="price" required>
                            </div>
                            
                            <button @click="makeOffer()" type="button" class="btn btn-success mt-3">Place Offer</button>
                            
                          </div>
                        </div>
                        
                      </div>
                    </div>
                  </div>

  <!-- End of Testing -->

</body>

</html>
<script src="./narbar.js"></script>

<script>
  const app = Vue.createApp({
    data() {
      return {
        results: [],
        price: 0,
        buyerid: localStorage.id //Taken from yuxiang side

      };
    },



    async mounted() {
      this.checkLogin()

      const queryString = window.location.search;

      if (queryString){

        var itemid = queryString.split("=")[1];
        try {
          var getItemUrl = `http://localhost:5001/items/${itemid}`
          var databaseitems = await fetch(getItemUrl)
          const databaseitemsJson = await databaseitems.json()
  
          if (databaseitems.status === 200) {
            console.log(databaseitemsJson)
            // Get all the databases 
            this.results = databaseitemsJson.Success;
            console.log(this.results)
  
          } else {
            console.log("Database not connected")
          }
        } catch (error) {
          console.log(error)
        }
      }

      else{
        // window.location.href="cataloguenew.php"
      }
      // Fetching from NEW items microservice, for a particular item.
    },

    methods: {
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

      // Invoke the complex microservice here to make an offer
      async makeOffer() {
        console.log("help")
        requiredObjects = {"item_id": this.results._id, "price": this.price, "buyer_id": this.buyerid}
        console.log(requiredObjects)

        // Make a fetch first to check if the item is available

        option = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requiredObjects)
        }

        url = "http://localhost:5200/make_offer"

        const result = await fetch(url, option)

        const response = await result.json()


        try {
          if (result.ok) {
            console.log(response)
            if (response.code == 201){
              alert("Your offer has been made successfully, you will be redirected to the catalog page shortly...")

              window.location.href = "myoffers.html";
            }
            else{
              alert("Your offer has not been made successfully, please try again later...")
            }
          } 
        }

        catch(err){

          console.log(err)
        
        }





      },

      // redirect(){
      //   let tID = setTimeout(function () {
      //       window.location.href = "cataloguenew.php";
      //       window.clearTimeout(tID);		// clear time out.
      //   }, 1000)
      // }

    },

    computed: {

    }
  })

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