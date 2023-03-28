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

<style scoped lang="scss">
.btn-nabshop {
  width:120px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>
