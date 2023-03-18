<template>
  <div class="loginform container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
      <div class="mt-4"><img src="../assets/nabshop-light.png" width="150" alt="" class=""></div>
        <h1 class="mt-4">Login</h1>
    </div>

    <form @submit.prevent="submitForm" >
      <div class="form-floating mb-4">
        <input type="text" id="username" class="form-control" v-model="username"/>
        <label class="form-label" for="username">Username</label>
      </div>

      <div class="form-floating mb-4">
        <input type="password" id="password" class="form-control" v-model="password"/>
        <label class="form-label" for="password">Password</label>
      </div>

      <div class="row mb-4">
        <div class="col-md-6 d-flex justify-content-center">

          <div class="form-check mb-3 mb-md-0">
            <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
            <label class="form-check-label" for="loginCheck"> Remember me </label>
          </div>
        </div>

        <div class="col-md-6 d-flex justify-content-center">
          <!-- Simple link -->
          <a href="#!">Forgot password?</a>
        </div>
      </div>

      <div class="toast align-items-center text-white bg-primary border-0"
        v-if="success"
        role="alert" aria-live="assertive" aria-atomic="true">
        <div class="d-flex">
          <div class="toast-body">
            Signing you in!
          </div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
      </div>
      <!-- Submit button -->
      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Sign in</button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>Don't have an account? <a href="sign-up">Sign up</a></p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogInForm',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In - NabShop'

  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')

      const formData = {
        username: this.username,
        password: this.password
      }
      await axios
        .post('/auth/jwt/create', formData)
        .then(response => {
          console.log(response)

          const access = response.data.access
          const refresh = response.data.refresh

          this.$store.commit('setAccess', access)
          this.$store.commit('setRefresh', refresh)

          axios.defaults.headers.common['Authorization'] = 'JWT ' + access
          localStorage.setItem('access', access)
          localStorage.setItem('refresh', refresh)

          const toPath = this.$route.query.to || '/cart'
          this.$router.push(toPath)
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
            console.log(JSON.stringify(error.response.data))
          } else if (error.message) {
            this.errors.push('Something went wrong. Please try again')
            console.log(JSON.stringify(error))
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.loginform {
  width: 400px;
  height: min-content;
  border: 2px;
  border-radius: 7px;
  background: rgb(219, 217, 217);
  padding: 20px 40px;
  margin-top: 50px
}
.btn-nabshop {
  width: 100%;
}
</style>
