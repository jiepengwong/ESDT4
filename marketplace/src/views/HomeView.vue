<template>
  <div class="home">
    <HelloWorld msg="Marketplace Homepage"/>
    <input type="text" v-model="username">
    <input type="text" v-model="username">

    Hello Testing things
    {{isSignedIn}}

  </div>
</template>


<script>
  export default ({
    name: "home",
    data() {
            return{
              isSignedIn: false,
            }
          },

    
  })
</script>
