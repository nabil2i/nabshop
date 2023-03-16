<template>
  <div class="home mt-5">
    <h1 class="mt-5 mb-5">Account</h1>

    <Shopfooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import Shopfooter from '@/components/Shopfooter.vue'

export default {
  name: 'Profile',
  components: {
    Shopfooter
  }
}
</script>
