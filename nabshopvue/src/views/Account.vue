<template>
  <div class="home">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <h1 class="mt-5 mb-5">Account</h1>

    <ShopFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'

export default {
  name: 'Account',
  components: {
    ShopFooter
  }
}
</script>
