<template>
<div>
6565656
  <div class="col"
     v-for="book in books"
     v-bind:key="book.id"
    >    
    <div class="card">
      <img :src="book.image[0].get_image" class="card-img-top" alt="">
      <div class="card-body">
        <div><h5 class="card-title"><strong>{{ book.title }}</strong></h5></div>
        <div class="card-text">{{ book.author }}</div>
        <!-- 2 column grid layout -->
        <div class="row mt-3">
          <div class="col-md-6 d-flex justify-content-center mb-2">
            <!-- Buy paperback -->
            <router-link href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>{{ book.bookeditions[0].unit_price }}</span>
            </router-link> 
          </div>

          <div class="col-md-6 d-flex justify-content-center">
            <!-- Buy Ebook -->
            <a href="#" class="btn btn-success btn-nabshop mb-2" type="submit"><div>Buy Ebook</div>$<span>{{ book.bookeditions[1].unit_price }}</span></a> 
          </div>
        </div>
        View details
      </div>
    </div> 
  </div>
</div>
  
</template>

<script>
import axios from 'axios'
import Shopfooter from '@/components/Shopfooter.vue'


export default {
  name: 'BookBox',
  components: {
    Shopfooter,

  },
  data() {
    return {
      books: []
    };
  },
  mounted() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      axios
        .get('/store/books/')
        .then(response => {
          this.books = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.btn-nabshop {
  width:150px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>
