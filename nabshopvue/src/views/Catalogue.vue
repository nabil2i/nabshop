<template>
  <div class="home">
    <div class="container mt-5">
      <h1 class="mt-5 mb-5"> Bookstore</h1>
      <div class="row row-cols-1 row-cols-md-3 g-5">
      <BookBox/>
      <BookBox/>
      <BookBox/>
      <BookBox/>
      </div>
    </div>
    <Shopfooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import Store from '@/components/Store.vue'
import Shopfooter from '@/components/Shopfooter.vue'
import BookBox from '@/components/BookBox.vue'

export default {
  name: 'Catalogue',
  components: {
    Store,
    Shopfooter,
    BookBox
  }
}
</script>
