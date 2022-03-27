<template>
  <div class="catalogue">


    {{results}}

    ====================================

    <table v-if="queryField != []">
      <tr v-for="filters in queryField" :key="filters">
        <td>{{filters}}</td>
      </tr>
    </table>
    {{login}}
    {{id}}
  </div>
</template>

<script>

  export default {
    name: "CatalogueView",

    data() {
      return {
        items:[
          {
            name: "Item 1",
            price: "10",
            quantity: "0",
            sellerid: "1"
          },
          {
            name: "Item 2",
            price: "20",
            quantity: "0",
            sellerid: "1"

          },
          {
            name: "Item 3",
            price: "30",
            quantity: "0",
            sellerid: "2"

          }
        ],
        quantity: [1,2,3,4,5,6,7,8,9,10],
        selected: 0,
        login: localStorage.login,
        id: localStorage.iwanthisid

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
