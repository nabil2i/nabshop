<template>
  <div class="home">
    <div class="container mt-5">
      <h1 class="mt-5 mb-5"> Bookstore</h1>
      <div class="row row-cols-1 row-cols-md-3 g-5" >

       <BookBox
        v-for="book in books"
        v-bind:key="book.id"
        v-bind:book="book"/>

      </div>
    </div>
    <ShopFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'
import BookBox from '@/components/BookBox.vue'
import axios from 'axios'

export default {
  name: 'Catalogue',
  components: {
    ShopFooter,
    BookBox
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
          this.books = response.data
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

</style>