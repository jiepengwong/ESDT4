<template>
    <div class="container" >
        <div class="row">
            <div class="col-sm-6" style="margin:auto"> 
                <img src="@/assets/marketing1.png">

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
                        <button expand="block" @click="googleAuth"><ion-icon slot="start" :icon="logoGoogle" />Google</button>
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

            }
        }
    })
</script>

<style>

</style>