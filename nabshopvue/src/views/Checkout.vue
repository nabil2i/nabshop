<template>
  <div class="home">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <h1 class="mt-5 mb-5">Checkout</h1>
    <section class="h-100 h-custom">
      <div class="container cart-container h-100 py-5">
        <div class="row d-flex justify-content-center align-items-center h-100">

          <div class="col"> <!-- Main div-->
            <h3 class="fw-normal mb-5 text-black">Order summary</h3>
            <!-- Cart list -->
            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col" class="h5"></th>
                    <th scope="col">Format</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Price</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <CartItemCheckout
                    v-for="item in cart.items"
                    v-bind:key="item.bookedition.id"
                    v-bind:initialItem="item"
                    v-on:removeFromCart="removeFromCart"/>
                </tbody>
              </table>
              <div class="d-flex justify-content-between" style="font-weight: 500;">
                        <p class="mb-2">Subtotal</p>
                        <p class="mb-2"><span>$</span>{{ cartTotalPrice.toFixed(2) }}</p>
                </div> 
            </div>
            <!-- End Cart list -->
            <hr>
            
            <h3 class="fw-normal mb-5 text-black">Address</h3>
            <!-- Payment details -->
            <div class="form"> 

              <div class="row"> <!-- Shipping address -->
                <div class="col-lg-6">
                  <div class="form-floating mb-4">
                    <input type="text" id="fullname" class="form-control" v-model="fullname"/>
                    <label class="form-label" for="fullname">Full name</label>
                  </div>

                  <div class="form-floating mb-4">
                    <input type="text" id="email" class="form-control" v-model="email"/>
                    <label class="form-label" for="email">Email</label>
                  </div>

                  <div class="form-floating mb-4">
                    <input type="text" id="phone" class="form-control" v-model="phone"/>
                    <label class="form-label" for="phone">Phone</label>
                  </div>
                </div>
              
                <div class="col-lg-6">
                  <div class="form-floating mb-4">
                    <input type="text" id="shippingaddress" class="form-control" v-model="shippingaddress" />
                    <label class="form-label" for="shippingaddress">Shipping Address</label>
                  </div>

                  <div class="form-floating mb-4">
                    <input type="text" id="street" class="form-control"  v-model="street" />
                    <label class="form-label" for="street">Street</label>
                  </div>


                  <div class="form-floating mb-4">
                    <input type="text" id="zipcode" class="form-control" v-model="zipcode" />
                    <label class="form-label" for="zipcode">Zip code</label>
                  </div>
                </div>
              </div> <!-- End Shipping address -->

              <div class="toast align-items-center text-white bg-primary border-0"
                v-if="errors.length"
                role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                  <div class="toast-body" v-for="error in errors" v-bind:key="error">
                    {{ error }}
                  </div>

                  <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
              </div>

                  <!-- Checkout -->
              <div class="card shadow-2-strong mb-5 mb-lg-0" style="border-radius: 16px;">
                <div class="card-body p-4">

                  <div class="row"> <!-- Row of 3 col -->
                    <div class="col-md-6 col-lg-4 col-xl-3 mb-4 mb-md-0">
                      <div class="form">
                        <div class="d-flex flex-row">
                          <div class="d-flex align-items-center pe-2">
                            <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel3v"
                              value="" aria-label="..." checked/>
                          </div>
                          <div class="rounded border w-100 p-3">
                            <p class="d-flex align-items-center mb-0">
                              <i class="fab fa-cc-stripe fa-2x fa-lg text-dark pe-2"></i>Stripe
                            </p>
                          </div>
                        </div>
                      </div>
                    </div> <!-- End of col 1 -->
                    <div class="col-md-6 col-lg-4 col-xl-6">
                      <div class="row">
                      <div id="stripe-card" col-12 col-xl-6> </div>
                        <!-- <div class="col-12 col-xl-6">
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
                        </div> -->
                      </div>
                    </div> <!-- End of col 2: col 2 is divided into 2 cols-->
                    <div class="col-lg-4 col-xl-3">
                      <div class="d-flex justify-content-between" style="font-weight: 500;">
                        <p class="mb-2">Total</p>
                        <p class="mb-2">${{ cartTotalPrice.toFixed(2) }}</p>
                      </div>

                      <!-- <div class="d-flex justify-content-between" style="font-weight: 500;">
                        <p class="mb-0">Shipping</p>
                        <p class="mb-0">$0</p>
                      </div> -->

                      <hr class="my-4">

                      <!-- <div class="d-flex justify-content-between mb-4" style="font-weight: 500;">
                        <p class="mb-2">Total (tax included)</p>
                        <p class="mb-2">$26.48</p>
                      </div> -->

                      <button @click="submitForm" type="button" class="btn btn-primary btn-block btn-lg">
                        Pay
                      </button>

                    </div> <!-- End of col 3 -->
                  </div>

              </div>
            </div> <!-- Checkout -->

              <!-- <button @click="submitForm" class="btn btn-success btn-block btn-nabshop mb-4">Save</button> -->
            </div>
            <!-- End of payment form -->
          </div> <!-- End of main div -->

        </div>
      </div>
    </section>

    <ShopFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'
import CartItemCheckout from '@/components/CartItemCheckout.vue'
import axios from 'axios'

export default {
  name: 'Checkout',
  components: {
    ShopFooter,
    CartItemCheckout
  },
  data() {
    return {
      cart: {
        items: []
      },
      stripe: {},
      card: {},
      fullname:  '',
      phone: '',
      email: '',
      shippingaddress: '',
      street: '',
      zipcode: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Checkout - Nabshop'
    this.cart = this.$store.state.cart

    if (this.cartTotalLength > 0) {
      this.stripe = Stripe(process.env.VUE_APP_STRIPE_TOKEN)
      const elements = this.stripe.elements();
      this.card = elements.create('card', { hidePostalCode: true})
      this.card.mount('#stripe-card')
    }
  },
  methods: {
    getItemTotal() {
      return item.quantity * item.bookedition.unit_price
    },
    submitForm() {
      this.errors = []

      if (this.fullname === '') {
        this.errors.push('Please provide a full name.')
      }

      if (this.email === '') {
        this.errors.push('Please provide an email.')
      }

      if (this.phone === '') {
        this.errors.push('Please provide a phone number.')
      }

      if (this.shippingaddress === '') {
        this.errors.push('Please provide a shipping address.')
      }

      if (this.street === '') {
        this.errors.push('Please provide an address.')
      }

      if (this.zipcode === '') {
        this.errors.push('Please provide a zipcode.')
      }

      if (!this.errors.length) {
        // console.log("Success")
        this.$store.commit ('setIsLoading', true)
        this.stripe.createToken(this.card).then(result => {
          if (result.error) {
            this.$store.commit('setIsLoading', false)
            this.errors.push('Something went wrong with stripe.')
            console.log(result.error.message)
          } else {
            this.stripeTokenHandler(result.token)
          }
        })
      }

     
    },
    async stripeTokenHandler(token) {
      const items = []

      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i]
        const obj = {
          // bookedition: item.bookedition,
          bookedition: item.bookedition.id,
          quantity: item.quantity,
          //unit_price: item.bookedition.unit_price,
          price: item.bookedition.unit_price * item.quantity
        }
        items.push(obj)
      }

      const data = {
        'fullname': this.fullname,
        'phone': this.phone,
        'email': this.email,
        'shippingaddress': this.shippingaddress,
        'street': this.street,
        'zipcode': this.zipcode,
        'items': items,
        'stripe_token': token.id
      }
      console.log("The data we will send", data)
      await axios
        .post('/store/checkout/', data)
        .then(response => {
          console.log(response.data)
          this.$store.commit('removeCart')
          this.$router.push('/cart/success')
        })
        .catch(error => {
          this.errors.push('Something went wrong.')
          console.log(error)
        })
        this.$store.commit('setIsLoading', false)
    }
  },
  computed: {
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.bookedition.unit_price * curVal.quantity
      }, 0)
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
    
  }
}
</script>
<style scoped>
.cart-container {
  width: 900px
}
</style>