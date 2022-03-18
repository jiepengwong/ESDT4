// If I didnt login, re-route to Log In vue.
<template>
  <div>
      <Navbar />

      <router-view/>

  </div>
<!-- this is where the application is gonna live -->

</template>

<script>
  // Importing NavBar 
  import Navbar from "@/components/Navbar.vue";


  export default {
  name: "App",
  components: {
    Navbar,
  },
  computed: {

  },
};
  
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
