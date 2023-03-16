<template>
  <div class="home login container">
    
    <!-- <h1>This is login page</h1> -->
    <Loginform> </Loginform>
    
  </div>
</template>

<script>
// @ is an alias to /src
import Loginform from "@/components/Loginform.vue";

export default {
  name: 'Login',
  components: {
    Loginform
  }
}
</script>
