<template>
    <div>
        {{}}
    </div>

</template>



<script>
  export default {
  name: "Order",

  data() {
            return{
              isSignedIn: false,
            }
  },

  computed: {

  },
  created()  {
    this.isSignedIn = this.$routes.params.data
  },
};
</script>

<style>

</style>