<template>
  <div class="home">
    <Store/>
    <Shopfooter/>
  </div>

</template>

<script>
// @ is an alias to /src
import Store from '@/components/Store.vue'
import Shopfooter from '@/components/Shopfooter.vue'

export default {
  name: 'Catalogue',
  components: {
    Store,
    Shopfooter
  }
}
</script>
