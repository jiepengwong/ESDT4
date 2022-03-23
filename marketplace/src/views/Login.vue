<template>
    <div>
        <div class="container-fluid h-custom">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-md-9 col-lg-6 col-xl-6 my-lg-5 py-lg-5">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp" class="img-fluid"
              alt="Sample image">
          </div>
          <div class="col-md-8 col-lg-6 col-xl-5 offset-xl-1 my-lg-5 py-lg-5">
            <form>
            <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
                <h2>Welcome to Henesys Market Place!</h2>
                
            </div>
            <hr>

            <div style="margin-top:30px"></div>
            
                <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
                    <p class="lead fw-normal mb-0 me-3 text-centre" style="">Sign in with</p>
                    <button @click="googleAuth()" type="button" class="btn btn-success btn-floating mx-1" style="">
                        Google
                    </button>
                </div>
                <button @click="signOut()" v-bind:disabled = "!isSignedIn" type="button" class="btn btn-success btn-floating mx-1" style="">
                        SignOut
                    </button>
            </form>
            
          </div>
        </div>
      </div>
    </div>
                <div> Hello {{name}} </div>
                <div>{{id}} </div>
                <div> {{email}}</div>
                <div> Am I signed in?  {{isSignedIn}} 
                </div>
                <div>{{testing}}</div>
</template>

<script>
    // import axios from "axios"
    export default ({
        name: "login",
        data() {
            return{
                id:null,
                name: null,
                email:null,
                password: null,
                googleUserProfile: undefined,
                token: undefined, 
                isSignedIn: null,
                databaseSign: null,
                registered: null,
                GoogleUser: null,
            } 
        },
    methods: {
        googleAuth() {
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
                    secretClientId,
                    })
                    .then(() => {
                        gapi.auth2.getAuthInstance().signIn().then(() => {
                        this.googleUserProfile = gapi.auth2.getAuthInstance().currentUser.get()});

                        this.googleUserProfile = gapi.auth2.getAuthInstance().currentUser.get();
                        // gapi.auth2.getAuthInstance() returns a GoogleAuth Object#########################################################
                        this.GoogleAuth = gapi.auth2.getAuthInstance();
                        

                        // There are many functions in Google OAuth. #######################################################################
                        // console.log("This is Google Auth")
                        // console.log(GoogleAuth)
                        // console.log(GoogleAuth.signOut)
                        // console.log(GoogleAuth.isSignedIn.get())
                        var GoogleUser = this.GoogleAuth.currentUser.get();

                        

                        // GoogleAuth.currentUser.get() ==> google user. ###################################################################
                        // This will give me the getId() portion, but do not use this for your backend. Instead call out. ##################
                        // console.log(GoogleUser.getId())
                        // console.log(GoogleUser.isSignedIn())
                        // console.log(GoogleUser.getGrantedScopes())

                        // Get the Token stuff via a HTTP GET, call out function OfficialToken###############################################
                        var BasicProfile = GoogleUser.getBasicProfile()
                        this.id = BasicProfile.getId();
                        this.name = BasicProfile.getName();
                        this.email = BasicProfile.getEmail();
                        this.isSignedIn = GoogleUser.isSignedIn();


                        // Retrieving all the necessary information 

                        // Connecting to Profile Microservice : 
                        if (this.isSignedIn && this.id != null) {
                            // If Authentication with Google Login is successful, proceed to register into database or check with database. 
                            // Check with the database. 
                            var database_url = "http://127.0.0.1:5000/profile/" + this.id;
                            
                            console.log(database_url);

                            fetch(database_url)
                                .then(response => response.json())
                                .then(data => {
                                    console.log(data.code)
                                    console.log(data.code == 404)
                                    if (data.code == 404) {
                                        console.log("This is condition 1")
                                        this.registered = false
                                    }
                                    else {
                                        console.log("this is condition 2")
                                        this.registered = true;
                                    }
                                })
                                .catch(error => {
                                    console.log(error)
                                })

                            // Why is registered here a null
                            console.log(this.registered)
                            
                            // If not registered, I have to pass fields into my microservice. 
                            var registered_url = "http://127.0.0.1:5000/profile/register/" + this.id
                            console.log(registered_url)
                            let jsondata = JSON.stringify({
                                    "name": this.name,
                                    "email": this.email,
                                    "ratings": null
                            })
                            console.log(jsondata)
                            console.log(typeof jsondata)
                            // Json Data ia String now
                            localStorage.login = jsondata

                            localStorage.iwanthisid = this.id


                            if (this.registered==false){
                                fetch(registered_url,{
                                    method: "POST",
                                    headers: {
                                        "Content-type": "application/json"
                                    },
                                    body: jsondata
                                })
                                .then(response => response.json())
                                .then(data => {
                                    console.log(data)
                                })
                                .catch(error=> {
                                    console.log(error)
                                })
                            }
                            

                        }
                    })
             })

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
            localStorage.login = ""
            alert("You have been logged out!")
        }


    }
    })
</script>


<style>
    .oauth-btns {
        margin: 40px;
        text-align: center;
    }

</style>