<template>
  <div class="home container signup">
    <Signupform/>
  </div> 
</template>

<script>
// @ is an alias to /src
import Signupform from "@/components/Signupform.vue";

export default {
  name: 'Signup',
  components: {
    Signupform
  }
}
</script>
