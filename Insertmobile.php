<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Insert</title>
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
        body {
            background-color: lightgreen
        }
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

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
            box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px
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
            border: 2px solid #ee82ee
        }

        .box:hover {
            border: 2px solid #ee82ee
        }

        .btn.btn-primary {
            background-color: transparent;
            color: #ee82ee;
            border: 0px;
            padding: 0;
            font-size: 14px
        }

        .btn.btn-primary .fas.fa-chevron-right {
            font-size: 12px
        }

        .footer .p-color {
            color: #ee82ee
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
<!-- END OF HEADER ############################################################################################################## -->

    <div id="app">
        <!-- NAVIGATION BAR ----------------------------------------------------------------------------------------------------- -->
        <navbar></navbar>
        <!-- END OF NAVIGATION BAR ---------------------------------------------------------------------------------------------- -->
        <div class="container d-flex justify-content-center mt-5 mb-5">
            <div class="card p-3 py-4">
                <div class="text-center"> <img src="./asset/henesysHome.png" width="80" class="rounded-circle">
                    <h3 class="mt-2">Update your mobile number.</h3> <span class="mt-1 clearfix">for notification</span>

                    <hr class="line"> <small class="mt-4">Our platform is powered by Twilio.</small>
                    <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">+65</span>
                            <input maxlength="8" type="text" class="form-control" placeholder="Enter your number here!" aria-label="Username" aria-describedby="basic-addon1" v-model="number">
                    </div>
                    <button v-if ="isDisabled" class="w-100 btn btn-lg btn-success" @click="updateMobile" >Update</button>
                    <button v-else disabled class="w-100 btn btn-lg btn-success" @click="updateMobile" >Update</button>

                    

                    <span v-if='isDisabled' style='color:green; font-size:small'>{{error}}</span>
                    <span v-else style='color:red; font-size:small'>{{error}}</span>

                    <p class="mt-5 mb-3 text-muted">&copy; Henesys Grocery MarketPlace</p>

                </div>
            </div>
        </div>

        


    </div>
</body>
<script src="./narbar.js"></script>
<script>

    const app = Vue.createApp({
        async mounted() {
            this.checkLogin()

            try{
                var getItemUrl = "http://localhost:5000/profile/" + localStorage.id
                console.log(getItemUrl)
                
                var databaseitems = await fetch(getItemUrl)
                const profile_json = await databaseitems.json()

                if (databaseitems.status === 200){
                    console.log(profile_json)
                    // Get all the databases 
                    localStorage.login = JSON.stringify(profile_json.data)
                }
                else{
                    console.log("Database not connected")
                }
            }

            catch(error) {
                console.log(error)
            }
        },
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
                error: ""

            }
        },
        
        methods: {
            checkLogin() {
                // If the login variable is initalised, then we will redirect them to 
                if (localStorage.getItem("id")){
                    // redirect them to login page
                    // window.location.replace("/ESD_PROJECT/ESDT4/multi-page/catalogue.php");
                }
                else {
                    window.location.replace("./");
                }
            },

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
        async updateMobile() {
            var change_mobile_url = "http://127.0.0.1:5000/profile/mobile/" + this.id;
            console.log(this.number)
            jsondata_obj = JSON.stringify({"mobile":this.number})
            

            const result = await fetch(change_mobile_url,{
                    method: "PUT",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: jsondata_obj
                })

            const resultJson =  await result.json()
            try {
                if (result.ok){
                    console.log(resultJson)
                    alert("Profile number has been updated! ")
                    window.location.replace("./myprofile.html");
                }
            }
            catch(error) {
                alert("There is a problem while updating the profile number")
            }
                // .then(response => response.json())
                // .then(data => {
                //     console.log(data)
                //     alert("Mobile Number has been updated!")
                //     window.location.replace("./myprofile.html")
                // })
                // .catch(error=> {
                //     console.log(error)
                //     alert("There is something wrong...")
                //     console.log("Number failed to update")
                // })
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
            },
            isDisabled() {
                if (this.number.length == 8 && !(/[a-zA-Z]/.test(this.number))) {
                    this.error = "This is a valid mobile number."
                    return true
                }
                else{
                    this.error = "Must be valid 8-digit number"
                    return false
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