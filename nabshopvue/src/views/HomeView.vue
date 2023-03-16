<template>
  <div class="home container">
    Hello
    <nabshop/> 
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Nabshop from '@/components/Nabshop.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    Nabshop
  }
}
</script>
