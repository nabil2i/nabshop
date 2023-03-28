<template>
  <div class="home">
    <h1 class="mt-5 mb-5"> My Orders</h1>
  
          <OrderSummary
            v-for="order in orders"
            v-bind:key="order.id"
            v-bind:order="order"/>
    
    <ShopFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'
import OrderSummary from '@/components/OrderSummary.vue'
import axios from 'axios'

export default {
  name: 'Orders',
  components: {
    ShopFooter,
    OrderSummary
  },
  data() {
    return {
      orders: []
    }
  },

  mounted() {
    this.getOrders()
  },
  methods: {
    getOrders() {
      axios
        .get('/store/orders/')
        .then((response) => {
          //console.log(response.data.results)
          this.orders = response.data
          //console.log(this.books)
          
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
