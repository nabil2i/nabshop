<template>
<div class="col-lg-6 mt-3 d-flex justify-content-center">
  <router-link :to="edition.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
    <div>{{ edition.booktype }}</div>$<span>{{ edition.unit_price }}</span>
  </router-link>
</div>
  
</template>

<script>

export default {
  name: 'BookBox',
  props: {
    edition: Object
  },
  components: {

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
