<template>
<div class="home mt-0">
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
                  <CartItem2
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
            <router-link to="/store" type="button" class="btn btn-primary btn-block btn-lg">
              <div class="d-flex justify-content-between">
                <span>Go shopping</span>
              </div>
            </router-link>
          </div>
          
          <!-- checkout -->
          <!-- <div class="card shadow-2-strong mb-5 mb-lg-0" style="border-radius: 16px;">
          <div class="card-body p-4">

            <div class="row">
              <div class="col-md-6 col-lg-4 col-xl-3 mb-4 mb-md-0">
                <form>
                  <div class="d-flex flex-row pb-3">
                    <div class="d-flex align-items-center pe-2">
                      <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel1v"
                        value="" aria-label="..." checked />
                    </div>
                    <div class="rounded border w-100 p-3">
                      <p class="d-flex align-items-center mb-0">
                        <i class="fab fa-cc-mastercard fa-2x text-dark pe-2"></i>Credit
                        Card
                      </p>
                    </div>
                  </div>
                  <div class="d-flex flex-row pb-3">
                    <div class="d-flex align-items-center pe-2">
                      <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel2v"
                        value="" aria-label="..." />
                    </div>
                    <div class="rounded border w-100 p-3">
                      <p class="d-flex align-items-center mb-0">
                        <i class="fab fa-cc-visa fa-2x fa-lg text-dark pe-2"></i>Debit Card
                      </p>
                    </div>
                  </div>
                  <div class="d-flex flex-row">
                    <div class="d-flex align-items-center pe-2">
                      <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel3v"
                        value="" aria-label="..." />
                    </div>
                    <div class="rounded border w-100 p-3">
                      <p class="d-flex align-items-center mb-0">
                        <i class="fab fa-cc-paypal fa-2x fa-lg text-dark pe-2"></i>PayPal
                      </p>
                    </div>
                  </div>
                </form>
              </div>
              <div class="col-md-6 col-lg-4 col-xl-6">
                <div class="row">
                  <div class="col-12 col-xl-6">
                    <div class="form-outline mb-4 mb-xl-5">
                      <input type="text" id="typeName" class="form-control form-control-lg" siez="17"
                        placeholder="John Smith" />
                      <label class="form-label" for="typeName">Name on card</label>
                    </div>

                    <div class="form-outline mb-4 mb-xl-5">
                      <input type="text" id="typeExp" class="form-control form-control-lg" placeholder="MM/YY"
                        size="7"  minlength="7" maxlength="7" />
                      <label class="form-label" for="typeExp">Expiration</label>
                    </div>
                  </div>
                  <div class="col-12 col-xl-6">
                    <div class="form-outline mb-4 mb-xl-5">
                      <input type="text" id="typeText" class="form-control form-control-lg" siez="17"
                        placeholder="1111 2222 3333 4444" minlength="19" maxlength="19" />
                      <label class="form-label" for="typeText">Card Number</label>
                    </div>

                    <div class="form-outline mb-4 mb-xl-5">
                      <input type="password" id="typeText" class="form-control form-control-lg"
                        placeholder="&#9679;&#9679;&#9679;" size="1" minlength="3" maxlength="3" />
                      <label class="form-label" for="typeText">Cvv</label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-xl-3">
                <div class="d-flex justify-content-between" style="font-weight: 500;">
                  <p class="mb-2">Subtotal</p>
                  <p class="mb-2">{{ cartTotalPrice.toFixed(2) }}</p>
                </div>

                <div class="d-flex justify-content-between" style="font-weight: 500;">
                  <p class="mb-0">Shipping</p>
                  <p class="mb-0">$2.99</p>
                </div>

                <hr class="my-4">

                <div class="d-flex justify-content-between mb-4" style="font-weight: 500;">
                  <p class="mb-2">Total (tax included)</p>
                  <p class="mb-2">$26.48</p>
                </div>

                <router-link to="/checkout" type="button" class="btn btn-primary btn-block btn-lg">
                  <div class="d-flex justify-content-between">
                    <span>Checkout</span>
                    <span>{{ cartTotalPrice.toFixed(2) }}</span>
                  </div>
                </router-link>

              </div>
            </div>

          </div>
        </div> -->

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
import CartItem2 from '@/components/CartItem2.vue'

export default {
  name: 'Cart2',
  components: {
    ShopFooter,
    CartItem2
  },
  data() {
    return {
      cart_id: this.$store.state.cart_id,
      cart: []
    }
  },
  mounted() {
     // this.cart = this.$store.state.cart
     this.getCart()
     console.log(this.cart.items)
  },
  computed: {
    cartTotalLength() {
      this.getCart()
      return this.cart.items_count
    },
    cartTotalPrice() {
      this.getCart()
      return this.cart.total_price
    },
  },
  methods: {
    async removeFromCart(item) {
      
    },
    async getCart() {
      if (this.cart_id == '') {
        console.log('No card_id')
      } else {
          await axios
            .get(`/store/carts/${this.cart_id}/`)
            .then(response => {
             console.log(response.data)
             this.cart = response.data 
            })
            .catch(error => {
              console.log(error)
            })
      }

      
    }
  }
}
</script>

<style scoped>
.cart-container {
  width: 900px
}
</style>