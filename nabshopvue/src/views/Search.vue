<template>
  <div class="home">
  
    <div class="container mt-5">
      <h1 class="mt-5 mb-5"> Search</h1>
      <h2 class="text-secondary"> Search terms: "{{ query }}"</h2>
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
  name: 'Searh',
  components: {
    ShopFooter,
    BookBox
  },
  data() {
    return {
      books: [],
      query: ''
    }
  },

  mounted() {
    document.title = 'Search - NabShop'
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get('query')) {
      this.query = params.get('query')
      this.doSearch()
    }
  },
  methods: {
    async doSearch() {
      const api_url = `/store/books/?search=${this.query}` 
      await axios
        .get(api_url)
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