<template>
<div>
    <h3>Welcome to the payments page</h3>

    <div>
        <button class="btn btn-primary" @click="pay">Pay</button>
    </div>
</div>
  
</template>

<script>
export default {
    name: "Payments",

    data(){
        return {
            url: "http://localhost:3000/create-checkout-session",
            paymentdata: {
                
            }
        }
    },

    methods:{
        async pay(){


            // Creating a post request using fetch api
            const options = {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                }
                // body: JSON.stringify({ //Convert into JSON object
                //   items: "ball",
                //   price : 20000
                // })
            }

            try{
                console.log("hi i am being first ran at the front end side")
                const res = await fetch(this.url,options)

                console.log(res)

                console.log("got back response from back-end")

                const result = await res.json()

                if (res.ok) {
                    console.log(res)
                    console.log(result)
                    window.location.href = result.sessionurl

                } else{
                    console.log(res)
                }
            }

            catch(error) {

                console.log(error)

                console.log("there is an error")

            }

        }
    }

}
</script>

<style>

</style>