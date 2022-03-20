<template>
  <div class="catalogue">
    <!-- This would contain the filter component -->
    <CatalogueLanding :filterPosts="filterPosts" :search="search"/>

    <div>
    <CatalogueListings :posts="results"/>

    <!-- {{results}} -->

    </div>

    <!-- <div v-else-if="results.length == 0">
      <h3>There is no such item available sorry</h3>

    </div>     -->
    




  </div>
</template>

<script>
import CatalogueLanding from '../components/CataloguePageComponent/CatalogueLanding.vue'
import CatalogueListings from '../components/CataloguePageComponent/CatalogueListings.vue'


  export default {
    name: "CatalogueView",
    components: {
      CatalogueLanding,
      CatalogueListings
    },

    data() {
      return {
        results: [],
        unfilteredResult: []
        // Get the query results from the search
        // querytest: this.$route.query.q
        // posts: ""
        }
    },

    methods: {
      // Filter based on categories
      filterPosts(categoryName){
        console.log("hi")
        this.resetPosts()
        if (categoryName !== "All"){

          this.results = this.results.filter((result) => {
            console.log(result.Category)
            return result.Category === categoryName;
          })
        }

      },

      search(name){
        this.resetPosts()
        this.results = this.results.filter((result) =>{
          // Because the search is case insensitive, we need to make sure that the search is lowercase
          return result.ItemName.toLowerCase().includes(name.toLowerCase())
        })
        

      },

      resetPosts(){
        this.results = this.unfilteredResult
      }

      
  
    },
      async created() {
      // Fetch all the data from the data base first before query

          try{
          var getItemUrl = "http://localhost:5000/item"
          
          var databaseitems = await fetch(getItemUrl)
          const databaseitemsJson = await databaseitems.json()

          if (databaseitems.status === 200){
            // Get all the databases 
            this.results = databaseitemsJson.data.item;
            this.unfilteredResult = databaseitemsJson.data.item;
            console.log(this.results)

          }
          else{
            console.log("Database not connected")
          }
          }

          catch(error) {
            console.log(error)
          }

         





    //       }

    //       catch(error){
    //         console.log(error)

    //       }
    //     }
    //   }




    },

   

   
    computed: {

      // checkResult() {
      //   if (this.results > 0) {
      //     return this.results
      //   }
      //   else {
      //     return "No results"
      //   }
      // }
       
      
      

    }
  }
</script>

<style scoped></style>
