<template>
  <div class="bookdetail">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <div class="container mt-5">
      <Toasts
        :show-progress="true"
        :rtl="false"
        :max-messages="5"
        :time-out="3000"
        :closeable="true"
      ></Toasts>
      <div class="row">
      
        <div class="col-md-3">
          <img :src="bookedition?.book?.images?.[0].image" class="card-img-top" alt="">
        </div>

        <div class="col-md-6">
          <h5 class=""><strong>{{bookedition?.book?.title}}</strong></h5>
          <div class="">{{bookedition?.book?.author}}</div>
          <hr>
          <div class="justify-content-start"> {{bookedition?.book?.description}}</div>
        </div>
      
        <div class="col-md-3 mt-3">
          <div><h5 class=""><strong>Details</strong></h5></div>
          <div class=""> <strong>Genre: </strong>{{bookedition?.book?.genre}}</div>
          <div class="justify-content-start"><strong>Publication date: </strong> {{bookedition.publicationdate}}</div>
          <div class="justify-content-start"><strong>Format: </strong>{{bookedition.bookformat}}</div>
          <div class="justify-content-start"><strong>Booktype: </strong>{{bookedition.booktype}}</div>
          <div class="justify-content-start"><strong>ISBN: </strong> {{bookedition.isbn}}</div>
          <div class="justify-content-start"><strong>Pages: </strong> {{bookedition.pages}}</div>
          <div class="justify-content-start"><strong>Unit price: </strong> $<span>{{bookedition.unit_price}}</span></div>

          <div class="input-group w-auto mt-3">
            <input
              type="number"
              class="form-control"
              min="1"
              aria-label="Quantity"
              aria-describedby="button-addon1"
              v-model="quantity"
            />
            <button
              class="btn btn-success" type="button"
              id="button-addon1" data-mdb-ripple-color="dark"
              @click="addToCart">
                Add to cart
            </button>
          </div>
          <div class="mt-5">
            <router-link to="/books" type="button" class="btn btn-primary btn-block btn-lg">
              <div class="d-flex justify-content-between">
                <span>Add other books</span>
              </div>
            </router-link>
          </div>

          <!-- <div>
            <a href="#" class="btn btn-success btn-nabshop mt-3" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a>
          </div>  -->
        </div>

      </div>
    </div>
    <ShopFooter/>
  </div>
</template>

<script>
import ShopFooter from '@/components/ShopFooter.vue'
import axios from 'axios'

  export default {
    name: 'BookDetail',
    components: {
      ShopFooter,
    },
    data() {
      return {
        bookedition: {},
        quantity: 1
      }
    },
    mounted() {
      this.getBookEdition()
    },
    methods: {
      async getBookEdition() {
        this.$store.commit('setIsLoading', true)
        const book_id = this.$route.params.book_id
        const bookedition_id = this.$route.params.bookedition_id
        // const api_url = `/store/bookeditions/${bookedition_id}/`
        const api_url = `/store/books/${book_id}/bookeditions/${bookedition_id}/`
        console.log(api_url)
        
        await axios
          .get(api_url)
          .then((response) => {
            //console.log(response.data)
            this.bookedition = response.data
            //console.log(this.bookedition)
            document.title = this.bookedition.book.title + ' | NabShop'
            
          })
          .catch((error) => {
            console.log(error)
          })
        this.$store.commit('setIsLoading', false) 
      },
      addToCart() {
        if (isNaN(this.quantity) || this.quantity < 1) {
          this.quantity = 1
        }
        const item = {
          bookedition: this.bookedition,
          quantity: this.quantity
        }

        this.$store.commit('addToCart', item)
        //this.$toast.success('You have added item(s) to the cart');
      }
    }
  }
</script>
 <style scoped>
 .put-left {
  align-items: right;
 }
 </style>