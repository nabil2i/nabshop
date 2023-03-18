<template>
  <div class="home">
    <Nabshop
      v-bind:user_data="user_data"/>
  </div>
 
  </template>

<script>
// @ is an alias to /src
import Nabshop from '@/components/Nabshop.vue'
import ShopFooter from '@/components/ShopFooter.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    Nabshop,
    ShopFooter,
 
  },
  data() {
    return {
      user_data: {},
    }
  },
  mounted() {
    document.title = 'Home - NabShop'
    this.getUserData()
  },
  methods: {
    getUserData() {
      axios
        .get('/auth/users/me/')
        .then(response => {
          //console.log(response.data)
          this.user_data = response.data
        })
    }
  }
}
</script>
