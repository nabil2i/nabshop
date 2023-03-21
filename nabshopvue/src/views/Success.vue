<template>
  <div class="success-page">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <h1 class="mt-5 mb-5"> You have successfully place your order </h1>
      <p> Your order is being proccessed and will be delievered shorlty!</p>
    <ShopFooter/>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Success',
  components: {
    Navbar
  },
  data() {
    return {
      user_data: {}
    }
  },
  mounted() {
    document.title = 'Success - NabShop'
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
        },
  }
}
</script>
