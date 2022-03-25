<template>
  <div class="catalogue">


    {{results}}

    ====================================

    <table v-if="queryField != []">
      <tr v-for="filters in queryField" :key="filters">
        <td>{{filters}}</td>
      </tr>
    </table>


    <div v-else>
      No results found
    </div>
    

    <!-- <div v-if="isEmpty()">
      <h1>Catalogue</h1>
      <p>No items found</p>
    </div>

    <div v-else>
      <h1>Catalogue</h1>
      <p></p>
    </div> -->



  </div>
</template>

<script>

  export default {
    name: "CatalogueView",

    data() {
      return {
        results: [],
        filteredResult: []
        // Get the query results from the search
        // querytest: this.$route.query.q
        }
    },

    methods: {

      
      // Querying the database here
      // searchResults() {
      //   axios.get('/', {
      //     params: {
      //       q: this.query
      //     }
      //   })
      //     .then(response => {
      //       this.results = response.data;
      //     })
      //     .catch(error => {
      //       console.log(error);
      //     })
      // }
    },
    // computed: {
      // Check if the query is empty 

      
    //  async searchItemDatabase(){


    //     if (this.querytest == ""){
    //       this.results = [];
    //     }
    //     else{
    //       var getItemUrl = "http://localhost:5000/items"
      
    //       try{
          
    //       var databaseitems = await fetch(getItemUrl)
    //       const databaseitemsJson = await databaseitems.json()

    //       if (databaseitems.status === 200){
    //         // Get all the databases 
    //         this.results = databaseitemsJson;
    //         console.log(this.results)

    //       }




    //       }

    //       catch(error){
    //         console.log(error)

    //       }
    //     }
    //   }

    // },

    async created() {
      // Fetch all the data from the data base first before query

          try{
          var getItemUrl = "http://localhost:5000/item"
          
          var databaseitems = await fetch(getItemUrl)
          const databaseitemsJson = await databaseitems.json()

          if (databaseitems.status === 200){
            // Get all the databases 
            this.results = databaseitemsJson.data.item;
            console.log(this.results)

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
      queryField() {

        if (this.results && this.querytest){
          console.log("lol2")
          // console.log(this.results.filter(item => item.name.toLowerCase().includes(this.querytest.toLowerCase())))

          // this.filteredResult = this.results.filter(item => item["ItemName"].toLowerCase().includes(this.querytest.toLowerCase()))

          return this.results.filter(item => item["ItemName"].toLowerCase().includes(this.querytest.toLowerCase()))


        }

        else{
          console.log("lol")
          return "No result found"
        }
        

      },

      querytest(){
        console.log("lol")
        return this.$route.query.q
      
      


      }

      // changeQuery(){

      //   if (this.$route.query.q != this.querytest) {

      //     this.querytest = this.$route.query.q
      //     // return this.querytest

      //   }
      //   return this.querytest

      // }
      

    }
  }
</script>

<style scoped></style>
