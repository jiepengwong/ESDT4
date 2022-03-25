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

      <div class="col-4">
              <input type="name" class="form-control mr-sm-1" placeholder="Search" aria-label="Search" v-model="query">
      </div>

      <div class="row mx-1">
        
        <div class="col-3 mx-1">
            <button class="btn btn-outline-success" type="submit" v-on:click="search()">Search</button>
        </div>

        <div class="col-2">
          <ul class="navbar-nav">
        <li class="nav-item" v-for="link in links" :key="link">
          <a class="nav-link">
              <router-link :to="link.path">{{link.text}}</router-link>
            </a>
        </li>
      </ul>
        </div>
      </div>

      

      
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
                { path: '/SellerView', text: 'Seller View' }
                  ],

            query: ""
        }
    },
    methods: {
      // Push search query into the catalogue page
        search() {
            this.$router.push({ path: '/', query: { q: this.query } })
            console.log("help me")
        }

    },


}

</script>

<style scoped>

</style>
