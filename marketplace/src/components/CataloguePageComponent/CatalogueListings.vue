<template>
    <section id="listings">
        <!-- <div class="container">
            <h1>Listings</h1>
            <div class="row">
                <div class="col-md-12">
                    <div class="row">
                        <div class="col-md-4" v-for="listing in listings">
                            <div class="card">
                                <div class="card-image">
                                    <img :src="listing.image" alt="">
                                    <span class="card-title">{{listing.name}}</span>
                                </div>
                                <div class="card-content">
                                    <p>{{listing.description}}</p>
                                </div>
                                <div class="card-action">
                                    <a href="#">{{listing.price}}</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div> -->
        <div class="container">
            <div class="row">
                <div class="col">
                    <h1 >All listings</h1>
                    <h3 v-if="posts.length > 0 ">
                        Results: {{posts.length}}
                    </h3>
                    <h3 v-else-if="posts.length == 0">
                        No results found
                    </h3>

                    {{posts}}

                </div>
            </div>

            <div class="row" >
                <div v-for="post in posts" :key="post" class="col-sm-3 p-2">
                    <!-- Search for items with item status that is open -->
                    <div class="card" v-if="post.ItemStatus == 'Open'">
                        <img :src="image" class="card-img-top" alt="testing1">
                        <div class="card-body">
                            <h5 class="card-title">{{post.ItemName}}</h5>
                            <h6 class="card-title">{{post.Price}}</h6>
                            <p class="card-text">{{post.ItemDesc}}</p>
                            <a :href="`catalogue/item/${post.ItemID}`" class="btn btn-primary">View item details</a>
                            <!-- Pass the itemID into the href -->
                            
                        </div>
                    </div>

                    <!-- <div class="card">
                        <div class="card-image">
                            <img :src="image" alt="">
                            <span class="card-title">{{post.ItemName}}</span>
                        </div>
                        <div class="card-content">
                            <p>{{post.Price}}</p>
                            <p></p>
                        </div>
                        <div class="card-action">
                            <p>{{post.ItemDesc}}</p>
                        </div>
                    </div> -->

                </div>

            </div>


            <!-- <div class="row" v-else-if="results.length == 0">

                <h1>There is no results to be found here</h1>

            </div> -->
        </div>
    </section>
  
</template>

<script>
export default {
    name: "CatalogueListings",
    props:["posts"],

    data(){
        return{
            results: this.posts,// This would be for all the relevant listings
            image: "@/assets/test11.png"

            
        }
    },


    computed: {
        resultLength() {
            return this.results.length;
        },

        databaseStatus() {

            if (this.resultLength > 0 ){
                return true
            }
            else {
                return false
            }
        }
    }

}
</script>

<style scoped>

</style>