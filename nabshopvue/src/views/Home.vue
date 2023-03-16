<template>
  <div class="home">
    <Nabshop/>
  </div>
 
  </template>

<script>
// @ is an alias to /src
import Nabshop from '@/components/Nabshop.vue'
import Shopfooter from '@/components/Shopfooter.vue'

export default {
  name: 'home',
  components: {
    Nabshop,
    Shopfooter
 
  }
}
</script>
