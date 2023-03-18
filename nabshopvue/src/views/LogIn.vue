<template>
  <div class="home">
    
    <!-- <h1>This is login page</h1> -->
    <LogInForm> </LogInForm>
    
  </div>
</template>

<script>
// @ is an alias to /src
import LogInForm from "@/components/LogInForm.vue";


export default {
  name: 'Login',
  components: {
    LogInForm
  }
}
</script>
