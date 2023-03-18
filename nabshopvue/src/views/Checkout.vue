<template>
  <div class="home">
    <h1>Checkout</h1>

    <ShopFooter/>
  </div>
 
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'

export default {
  name: 'Checkout',
  components: {
    ShopFooter
  }
}
</script>
