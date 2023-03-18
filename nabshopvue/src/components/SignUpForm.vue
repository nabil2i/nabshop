<template>
  <div class="loginform container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
      <div class="mt-4"><img src="../assets/nabshop-light.png" width="150" alt="" class=""></div>
        <h1 class="mt-4">Sign up</h1>
    </div>

    <form @submit.prevent="submitForm">
      <div class="form-floating mb-4">
        <input type="text" id="username" class="form-control" v-model="username" />
        <label class="form-label" for="username">Username</label>
      </div>

 
      <div class="form-floating mb-4">
        <input type="email" id="email" class="form-control" v-model="email"/>
        <label class="form-label" for="email">Email</label>
      </div>


      <div class="form-floating mb-4">
        <input type="password" id="password" class="form-control" v-model="password"/>
        <label class="form-label" for="password">Password</label>
      </div>

 
      <div class="form-floating mb-4">
        <input type="password" id="password2" class="form-control" v-model="password2" />
        <label class="form-label" for="password2">Confirm Password</label>
      </div>

      <div class="" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error}}</p>
      </div>
  
      <div class="toast align-items-center text-white bg-primary border-0"
        v-if="errors.length"
        role="alert" aria-live="assertive" aria-atomic="true">
        <div class="d-flex">
          <div class="toast-body" v-for="error in errors" v-bind:key="error">
            {{ error }}
          </div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
      </div>

      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Continue</button>


      <div class="text-center">
        <p>By creating an account, you agree to NabShop's Conditions of User and Privacy policy.</p>
        <p>Already have an account? <a href="/login">Log in</a></p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpForm',

  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: [],
      
    }
  },
  methods: {
    submitForm(e) {
      console.log(this.username, this.email, this.password, this.password2, this.errors)
      this.errors = []

      if (this.username === '') {
        this.errors.push('Please, provide a username.')
      }
      if (this.email === '') {
        this.errors.push('Please, provide an email.')
      }
      if (this.password !== this.password2) {
        this.errors.push('Passwords do not match!')
      }

      if (this.errors.length == 0) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password
        }
      
      console.log("Sign up data", this.formData)

        axios
          .post('/auth/users/', formData)
          .then(response => {
         

            this.$router.push('/login')
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
