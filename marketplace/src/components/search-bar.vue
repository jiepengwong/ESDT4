<template>
  <div class="search-holder">
        <div class='search-holder-banner'>
            <div class="header-container">
                <h1 class='hero-header'>Search for you favourite items</h1>
            </div>

            <div class="search-bar">
                <div class="form-holder">
                    <div class="search">
                        <input @change='handleChange' v-model='SearchText' class='form-control' type="text">
                    </div>
                    <img class='icon' src='' width='' alt="">
                </div>

            </div>
            

        </div>


  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {

    computed:{

    },
    data(){
        return{
            searchText: ''

        }

    }, 
    methods: {
        handleChange(){
            this.$emit('search', this.searchText);
        }

    }
}
</script>

<style scoped>
.search-holder{
    margin-top: 60px; 

}

.search-holder-banner{
    margin-top: 60px; 
    margin: 0 auto;
    width: 80px;
    padding: 15px;
    text-align: center;
}

.hero-header{
    margin: 0 0 25px;
}

.form-control{
    display: block;
    width: 100%;
    padding: 1px 12px;
}

</style>