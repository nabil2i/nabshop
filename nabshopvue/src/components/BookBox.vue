<template>
<div>
  <div class="card">
    <img :src="book?.images?.[0]?.image" class="card-img-top" alt="">
    <div class="card-body">
      <div><h5 class="card-title"><strong>{{ book?.title }}</strong></h5></div>
      <div class="card-text">{{ book?.author }}</div>
      
      <div class=" row">
        <EditionButton
          v-for="edition in book.bookeditions"
          v-bind:key="edition.id"
          v-bind:edition="edition"/>

        <!-- <div class="col-lg-6 mt-3 d-flex justify-content-center">
          
          <router-link :to="book.bookeditions?.[1]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
            <div>Paperback</div>$<span>{{ book.bookeditions?.[1]?.unit_price }}</span>
          </router-link>
        </div>

        <div class="col-lg-6 mt-3 d-flex justify-content-center">

          <router-link :to="book.bookeditions?.[0]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
            <div>Ebook</div>$<span>{{ book.bookeditions?.[0]?.unit_price }}</span>
          </router-link>
        </div> -->

      </div>
    </div>
  </div> 
</div>
  
</template>

<script>
import EditionButton from '@/components/EditionButton.vue'

export default {
  name: 'BookBox',
  props: {
    book: Object
  },
  components: {
    EditionButton
  },
  data() {
    return {
    };
  },
  mounted() {
 
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.btn-nabshop {
  width:120px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>
