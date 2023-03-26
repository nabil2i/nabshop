<template>
  <div class="loginform container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
      <div class="mt-4"><img src="../assets/nabshop-light.png" width="150" alt="" class=""></div>
        <h1 class="mt-4">Delete your account</h1>
    </div>
      <div class="container">To delete your account, type your password in the box below and confirm </div>
    <form @submit.prevent="submitForm" >
      <div class="form-floating mb-4">
        <input type="password" id="password" class="form-control" v-model="password"/>

      </div>

      <!-- Submit button -->
      <button type="submit" class="btn btn-danger btn-block btn-nabshop mb-4">Delete</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DeleteAccount',
  data() {
    return {
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Delete account - NabShop'

  },
  methods: {
    async submitForm() {
      if (this.password === '') {
        this.errors.push('Password missing')
      }

      if (this.errors.length == 0) {
        const formData = {
          "current_password": this.password
        }
        console.log("password", formData)
        axios
          .delete('/auth/users/me/', formData )
          .then(response => {
            console.log(response)
            this.$router.push('/')
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
