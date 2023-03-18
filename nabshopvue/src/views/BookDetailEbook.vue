<template>
  <div class="bookdetail">
    <div class="container mt-5">
      <div class="row">
      
        <div class="col-md-3">
          <img :src="bookedition?.book?.images?.[0].image" class="card-img-top" alt="">
        </div>

        <div class="col-md-6">
          <h5 class=""><strong>{{bookedition?.book?.title}}</strong></h5>
          <div class="">{{bookedition?.book?.author}}</div>
          <hr>
          <div class="justify-content-left"> {{bookedition?.book?.description}}</div>
        </div>
      
        <div class="col-md-3 justify-content-left">
          <div><h5 class=""><strong>Details</strong></h5></div>
          <div class=""> <strong> Genre: </strong>eztzetzt</div>
          <div class=" justify-content-left"><strong>Publication date: </strong> {{bookedition.publicationdate}}</div>
          <div class=" justify-content-left"><strong>Format: </strong>{{bookedition.format}}</div>
          <div class=" justify-content-left"><strong>Booktype: </strong>{{bookedition.booktype}}</div>
          <div class=" justify-content-left"><strong>ISBN: </strong> {{bookedition.isbn}}</div>
          <div class=" justify-content-left"><strong>Pages: </strong> {{bookedition.pages}}</div>
          <!-- <div class=" justify-content-left"><strong>Paperback price: </strong> $<span>1.99</span></div> -->
          <div class=" justify-content-left"><strong>Ebook price: </strong> $<span>{{bookedition.unit_price}}</span></div>

          <div class="input-group w-auto mt-3">
            <input
              type="number"
              class="form-control"
              min="1"
              aria-label="Quantity"
              aria-describedby="button-addon1"
              v-model="quantity"
            />
            <button class="btn btn-success" type="button" id="button-addon1" data-mdb-ripple-color="dark">
                Add to cart
            </button>
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
    name: 'BookDetailEbook',
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
      getBookEdition() {
        const bookedition_id = this.$route.params.bookedition_id
        const api_url = `/store/bookeditions/${bookedition_id}/`
        console.log(api_url)
        
        axios
          .get(api_url)
          .then((response) => {
            console.log(response.data)
            this.bookedition = response.data
            console.log(this.bookedition)
            
          })
          .catch((error) => {
            console.log(error)
          })
        
      }
    }
  }
</script>
 <style scoped>
 .put-left {
  align-items: right;
 }
 </style>