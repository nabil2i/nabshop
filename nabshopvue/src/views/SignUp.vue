<template>
  <div class="home">
    <Signupform/>
  </div> 
</template>

<script>
// @ is an alias to /src
import Signupform from "@/components/SignUpForm.vue";
import axios from 'axios';

export default {
  name: 'SignUp',
  components: {
    Signupform
  },
  
}
</script>
