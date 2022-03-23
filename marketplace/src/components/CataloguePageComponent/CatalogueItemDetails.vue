<template>
    <div class="confirmation">

        <div v-if="itemResult != '' " class="container">


        <div class="row p-5">
            <div class="col">
                This is the item that you wanted here are its details
            </div>
        </div>

        <div class="row">
            <div class="col">
                ** picture here **
            </div>
        </div>

         <div class="row">
            <div class="col">
                <b>Item name: {{itemResult.temName}}</b>
                Price: {{priceResult}}
                ID: {{itemResult.ItemID}}
            </div>
        </div>

        <div class="row">
            <div>
                <h6>Description</h6>
                <p>{{itemResult.ItemDesc}} Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis eligendi, rem alias neque maiores aliquam nihil dignissimos velit in! Facilis nulla eum praesentium saepe necessitatibus quo explicabo eaque corrupti dignissimos.</p>
            </div>
        </div>
        </div>


    
    </div>
</template>

<script>
export default {
    name: 'CatalogueItemDetails',
    props: ["id"],
    data() {

        return{
            itemResult: ""
        }

    },

    async mounted() {
        // Get the particular details from item database
        // Not really sure whether there is a better way to do this

        // Url of particular item
        const itemDetailsUrl = `http://localhost:5000/item/${this.id}`


        try{
        
        var databaseitems = await fetch(itemDetailsUrl)
        const databaseitemsJson = await databaseitems.json()

        if (databaseitems.status === 200){
        // Get all the databases 
        this.itemResult = databaseitemsJson.data;
        // this.unfilteredResult = databaseitemsJson.data.item;
        console.log(this.itemResult)

        }
        else{
        console.log("Database not connected")
        }
        }

        catch(error) {
        console.log(error)
        }





    },
    

}
</script>

<style scoped>

</style>