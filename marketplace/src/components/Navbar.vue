<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid" >
    <a class="navbar-brand">
        <!-- <img class="img-fluid" src="@/assets/henesys.png" > -->
        Henesys MarketPlace
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">



      <div class="row mx-1">

        <div class="col-2">
          <ul class="navbar-nav">
        <li class="nav-item" v-for="link in links" :key="link">
          <a class="nav-link">
              <router-link :to="link.path" >{{link.text}}</router-link>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" v-if="!login" >
                <router-link  to="/login">Login</router-link>
            </a>
        </li>

        <button v-if="computingLogin" @click="signOut()" type="button" class="btn btn-success btn-floating mx-1" style="">
                        SignOut
        </button>
        <button v-if="!computingLogin" @click="googleAuth()" type="button" class="btn btn-success btn-floating mx-1" style="">
          Login
        </button>
      </ul>
        </div>
      </div>

      {{localStorage}} {{localStorage2}}

      
    </div>
  </div>
</nav>


</template>

<script>

export default{
    name: "Navbar",
    data() {

        return {
            links: [
                { path: '/catalogue', text: 'Catalogue'},
                { path: '/login', text: 'Login' },
                { path: '/payment', text: 'Payment' },
                  ],

            query: "",
            login: undefined,
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
            show:false,
            localStorage: localStorage.id,
            localStorage2: localStorage.login,

        }
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
            localStorage.removeItem('login')
            localStorage.removeItem('id')
            console.log(localStorage.id)
            alert("You have been logged out!")
            document.location.reload()
        },
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
                            // {name: "Yu Xiang" ,....}



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
                            localStorage.login = jsondata
                            localStorage.id = this.id
                            this.show = true

                            this.localStorage= localStorage.id
                            document.location.reload()

                        }
                    })
             })

        },

    },
    computed: {
      computingLogin() {
        if(localStorage.getItem("id")) {
          return true
        }
        else {return false}
      }
    }



}

</script>

<style scoped>

</style>
