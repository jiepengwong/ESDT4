<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Insert</title>
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
<body onload="checkLogin()">
<!-- END OF HEADER ############################################################################################################## -->

    <div id="app">
        <!-- NAVIGATION BAR ----------------------------------------------------------------------------------------------------- -->
        <navbar></navbar>
        <!-- END OF NAVIGATION BAR ---------------------------------------------------------------------------------------------- -->
        <div class="container">
            <div class="row">
                <img src="./asset/HenesysHome.png" class="img-fluid " style="height:25%;width:25%;  display: block;margin-left: auto;margin-right: auto;">
            </div>
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6">
                        <h1 class="h3 mb-3 fw-normal">Before we start, we need your mobile number</h1>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">+65</span>
                            <input type="text" class="form-control" placeholder="Enter your number here!" aria-label="Username" aria-describedby="basic-addon1" v-model="number">
                        </div>

                        <button v-if:disabled ="check_number" class="w-100 btn btn-lg btn-primary" @click="updateMobile" >Update</button>
                        <span v-if='!number_status' style='color:red; font-size:small'>This is not a valid number!</span>
                        <span v-if='number_status' style='color:green; font-size:small'>This is a valid number!</span>

                        <p class="mt-5 mb-3 text-muted">&copy; Henesys Grocery MarketPlace</p>
                </div>
                <div class="col-3"></div>
            </div>  
        </div>


    </div>
</body>
<script src="./narbar.js"></script>
<script>

    function checkLogin() {
        // If the login variable is initalised, then we will redirect them to 
        if (localStorage.getItem("id")){
            // redirect them to login page
            // window.location.replace("./catalogue.php");
        }
        else {
            window.location.replace("./index.html");
        }
    }

    const app = Vue.createApp({
        data() {
            return {
                links: [
                    {"link":"catalogue.php", "name": "google"},
                    ],
                isSignedIn: localStorage.getItem("id"),
                jsondata: localStorage.login,
                number: "",
                id: localStorage.id,
                number_status: false,
            }
        },
        computed : {
        
        },
        
        methods: {
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
        updateMobile() {
            var change_mobile_url = "http://127.0.0.1:5000/profile/mobile/" + this.id;
            console.log(change_mobile_url)
            var jsondata_obj = JSON.parse(this.jsondata)
            console.log(jsondata_obj)

            jsondata_obj['mobile'] = String(this.number);
            console.log(jsondata_obj)

            jsondata_obj = JSON.stringify(jsondata_obj)

            fetch(change_mobile_url,{
                    method: "PUT",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: jsondata_obj
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    window.location.replace("./cataloguenew.php");
                })
                .catch(error=> {
                    console.log(error)
                    console.log("Number failed to update")
                })
            }
            
        },
        computed: {
            check_number() {
                if (String(this.number.length) != 8 ){
                    this.number_status = false
                }
                else {
                    this.number_status = true
                }   
            }
        },
            },
        
        )
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
    const vm = app.mount('#app');
    
</script>

</html>