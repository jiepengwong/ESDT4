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
            <a class="nav-link">
                <router-link to="/login">Login</router-link>
            </a>
        </li>
      </ul>
    </div>
  </div>
</nav>


</template>

<script>

export default{
    name: "Navbar",
    data() {
        // return {
        //     image: "../assets/henesys.png"
        // }
    },
    methods: {

    },


}

</script>

<style scoped>

</style>
