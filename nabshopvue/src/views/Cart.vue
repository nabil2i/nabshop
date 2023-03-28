<template>
<div class="home">
    <!-- <h1 class="mt-5 mb-5">Cart</h1> -->
  <section class="h-100 h-custom">
    <div class="container cart-container h-100 py-5">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col">
           <h3 class="fw-normal mb-5 text-black">Shopping Cart</h3>

          <div v-if="cartTotalLength">
            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col" class="h5">Shopping Bag</th>
                    <th scope="col">Format</th>
                    <th scope="col">Unit Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Price</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <CartItem
                    v-for="item in cart.items"
                    v-bind:key="item.bookedition.id"
                    v-bind:initialItem="item"
                    v-on:removeFromCart="removeFromCart"/>
                </tbody>
              </table>
              
            </div>
            <div>
              <div class="h-50">
                <div class="d-flex justify-content-between" style="font-weight: 500;">
                      <p class="mb-2">Subtotal</p>
                      <p class="mb-2"><span>$</span>{{ cartTotalPrice.toFixed(2) }}</p>
                </div>
                <router-link v-if="cartTotalPrice.toFixed(2)" to="/cart/checkout" type="button" class="btn btn-primary btn-block btn-lg">
                    <div class="d-flex justify-content-between">
                      <span>Checkout </span>
                      
                    </div>
                </router-link>
              </div>
            </div>
          </div>
          <div v-else class="mt-5"> <p>You dont have any product in the cart</p> 
            <router-link to="/books" type="button" class="btn btn-primary btn-block btn-lg">
              <div class="d-flex justify-content-between">
                <span>Go shopping</span>
              </div>
            </router-link>
          </div>

        </div>
      </div>
    </div>
  </section>

  <ShopFooter/>
</div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Cart',
  components: {
    ShopFooter,
    CartItem,
    Navbar
  },
  data() {
    return {
      user_data: {},
      cart: {
        items: []
      }
    }
  },
  mounted() {
     this.cart = this.$store.state.cart
     // console.log(this.cart.items)
     this.getUserData()
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0) 
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.bookedition.unit_price * curVal.quantity
      }, 0) 
    }
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.bookedition.id !== item.bookedition.id)
    },
    getUserData() {
          axios
            .get('/auth/users/me/')
            .then(response => {
              //console.log(response.data)
              this.user_data = response.data
            })
        },
  }
}
</script>

<style scoped>
.cart-container {
  width: 900px
}
</style>