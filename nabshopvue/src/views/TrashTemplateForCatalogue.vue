<template>
    <div class="home">
    <div class="container mt-5">
      <h1 class="mt-5 mb-5"> Bookstore</h1>
      <div class="row row-cols-1 row-cols-md-3 g-5" >
        <div class="col"
  v-for="book in books"
  :key="book.id"
  >  
  <div class="card">
    <img :src="book?.images?.[0]?.image" class="card-img-top" alt="">
    <div class="card-body">
      <div><h5 class="card-title"><strong>{{ book?.title }}</strong></h5></div>
      <div class="card-text">{{ book?.author }}</div>
      
      <div class="row mt-3">
        <div class="col-md-6 d-flex justify-content-center">
         
         
          <router-link :to="book.bookeditions?.[1]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
            <div>Buy paperback</div>$<span>{{ book.bookeditions?.[1]?.unit_price }}</span>
          </router-link>
        </div>

        <div class="col-md-6 d-flex justify-content-center">
          <router-link :to="book.bookeditions?.[0]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
            <div>Buy Ebook</div>$<span>{{ book.bookeditions?.[0]?.unit_price }}</span>
          </router-link>
        </div>
      </div>
      
      View details
    </div>
  </div> 
</div>

       

      </div>
    </div>
    <ShopFooter/>
  </div>





  
</template>

<script>
// @ is an alias to /src
import Store from '@/components/Store.vue'
import ShopFooter from '@/components/ShopFooter.vue'
import axios from 'axios'

export default {
  name: 'Catalogue',
  components: {
    Store,
    ShopFooter,
  },
  data() {
    return {
      books: []
    }
  },

  mounted() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      axios
        .get('/store/books/')
        .then((response) => {
          //console.log(response.data.results)
          this.books = response.data.results
          //console.log(this.books)
          
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.btn-nabshop {
  width:150px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>