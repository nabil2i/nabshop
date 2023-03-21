<template>
  <div class="home">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <Nabshop/>
  </div>
 
  </template>

<script>
// @ is an alias to /src
import Nabshop from '@/components/Nabshop.vue'
import Navbar from '@/components/Navbar.vue'
import ShopFooter from '@/components/ShopFooter.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    Nabshop,
    ShopFooter,
    Navbar,
 
  },
  data() {
    return {
      // user_data: {},
    }
  },
  mounted() {
    document.title = 'Home - NabShop'
    // this.getUserData()
  },
  methods: {
    
  }
}
</script>
