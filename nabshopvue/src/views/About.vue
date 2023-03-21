<template>
  <div class="home">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <h1 class="mt-5 mb-5">About</h1>
    <ShopFooter/>
  </div>
</template>

<script>
import ShopFooter from '@/components/ShopFooter.vue'

export default {
  name: 'About',
  components: {
    ShopFooter,
  } 
}
</script>
 <style scoped>
 .put-left {
  align-items: right;
 }
 </style>