<template>
    <div class="container" >
        <div class="row">
            <div class="col-sm-6" style="margin:auto"> 
                <img src="@/assets/marketing1.png" class="img-fluid">

            </div>
            <div class="col-sm-6" style="margin:auto">
                <main class="form-signin">
                    <form>
                        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

                        <div class="form-floating">
                        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                        <label for="floatingInput">Email address</label>
                        </div>
                        <div class="form-floating">
                        <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                        <label for="floatingPassword">Password</label>
                        </div>

                        <div class="checkbox mb-3">
                        <label>
                            <input type="checkbox" value="remember-me"> Remember me
                        </label>
                        </div>
                        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
                        <p class="mt-5 mb-3 text-muted">&copy; Henesys MarketPlace 2022</p>

                        <button id="authorize_button" style="display: none;">Authorize</button>

                        <div class="oauth-btns">
                            or signin with
                            <button expand="block" @click="googleAuth">Google</button>
                        </div>
                    </form>
                </main>
            </div>
        </div>
    </div>
</template>

<script>

    export default ({
        name: "login",
        data() {
            return{
                email:null,
                password: null,
                googleUserProfile: undefined,
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
                    }).then(() => {
                    if (gapi.auth2.getAuthInstance().isSignedIn.get()) {
                        this.googleUserProfile = gapi.auth2.getAuthInstance().currentUser.get();
                        this.loginApiCall(this.googleUserProfile);
                        console.log("logged in...");
                    } else {
                        gapi.auth2.getAuthInstance().signIn().then(() => {
                        this.googleUserProfile = gapi.auth2.getAuthInstance().currentUser.get();
                        this.loginApiCall(this.googleUserProfile);
                        console.log("NOT logged in...");
                        }).catch(err => {
                        alert(`Google auth error: ${err}`);
                        });
                    }
                    })
                    .catch((err) => {
                    alert("Helllo" + err);
                    console.log(err);
                    })
                });
            },
            loginApiCall(data) {
            // API call to handle googleUserProfile data
            // then redirect to home/profile page
            console.log("googleUserProfile", data);
            this.$router.push("/HomeView");
            }
        },
    })
</script>

<style>
    .oauth-btns {
        margin: 40px;
        text-align: center;
    }
</style>