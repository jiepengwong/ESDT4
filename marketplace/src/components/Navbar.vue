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
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link">
              <router-link to="/catalogue">Catalogue</router-link>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" v-if="!login" >
                <router-link  to="/login">Login</router-link>
            </a>
        </li>
                <li class="nav-item">
            <a class="nav-link">
                <router-link to="/homeview">{{String(login)}}</router-link>
            </a>
        </li>
        <button @click="signOut()" type="button" class="btn btn-success btn-floating mx-1" style="">
                        SignOut
        </button>
      </ul>
    </div>
  </div>
</nav>


</template>

<script>

export default{
    name: "Navbar",
    data() {
      return {
        login: undefined,
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
            localStorage.login = null
            alert("You have been logged out!")
        }

    },
    watch: {
      computingLogin() {
        if(localStorage.login == undefined) {
          this.login = false
        }
        else if (typeof localStorage == "string") {
          this.login = true
        }
        else {
          this.login = false
        }
      }
    }



}

</script>

<style scoped>

</style>
