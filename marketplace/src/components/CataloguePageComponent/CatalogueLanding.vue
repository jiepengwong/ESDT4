<template>
<!-- This would be the filter -->
    <section id="homepage">
        <div class="container">

            <div class="row">
                <div class="col">
                    <div class="row">
                        <div class="col-12">
                            <h1>Welcome to the marketplace</h1>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <p>Search for items here</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <input type="name" @keypress.enter="handleEventCatalogueSearch(term, 'search')" class="form-control mr-sm-1" placeholder="Search now" aria-label="Search" v-model="term">
                        </div>

                        <div class="col-12 p-2">
                            <button v-if="term.length == 0" class="btn btn-primary my-2 my-sm-0" @click="handleEventCatalogueSearch(term, 'search')" disabled>Search Now</button>
                            <button v-else class="btn btn-primary my-2 my-sm-0" @click="handleEventCatalogueSearch(term,'search')">Search Now</button>
                        </div>
                    </div>
                    <div class="row p-2">
                        <div v-for="category in categorys" :key="category" class="col">
                            <p @click="()=>handleEventCatalogueSearch(category, 'catname')">{{category}}</p>

                        </div>
                    </div>
                </div>
            </div>

            




        </div>


    </section>
  
</template>

<script>
export default {
    name: "CatalogueLanding",
    props: ["search"],

    data() {
        return {
            categorys: ["All","Sports", "Fashion", "Electronics", "Home", "Services", "Other"],
            term: ""
        }
    },   

    methods: {
        // Use emits method to send data to parent component
        handleEventCatalogueSearch(term,str){
            console.log("I am emitted from child component");
            console.log(term,str)

            this.$emit("search", term, str)


          
        },
    }

}
</script>

<style scoped>

#homepage{
    background-color: #f5f5f5;
    padding-top: 50px;
    padding-bottom: 50px;
}

</style>