<template>
  <div class="catalogue">
    <h1>This is a catalogue</h1>

    <table>
      <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
      </tr>

      <tr v-for="item in items" :key="item">
        <td>{{ item.name }}</td>
        <td>{{ item.price }}</td>
        <td>
          <select v-model="item.quantity">
            <option v-for="i in quantity" :key="i">{{ i }}</option>
          </select>
        </td>
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

      sumPrice(){
        let sum = 0;
        for(let i = 0; i < this.items.length; i++){
          sum += this.items[i].price * this.items[i].quantity;
        }
        return sum;
      },
      
      summarise(){

      }
    
    }
  }
</script>

<style scoped></style>
