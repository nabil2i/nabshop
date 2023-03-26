<template>
  <div class="home">
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->
    <h1 class="mt-5 mb-5">Account</h1>
    <div class="loginform container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
      <div class="mt-4"><img src="../assets/nabshop-light.png" width="150" alt="" class=""></div>
        <h1 class="mt-4">Change name</h1>
    </div>

    <div> 
      <div class="row ">
        <div class="col-md-9">
          <div class="form-floating mb-4">
            <input type="text" id="username" class="form-control" v-model="user_data.username" readonly/>
            <label class="form-label" for="username">Username</label>
          </div>
        </div>
      </div>
      <hr>

      <div class="row ">
        <div class="col-md-9">
          <div class="form-floating mb-4">
            <input type="text" id="first_name" class="form-control" v-model="user_data.first_name" readonly/>
            <label class="form-label" for="first_name">First name</label>
          </div>
          <div class="form-floating mb-4">
            <input type="text" id="last_name" class="form-control" v-model="user_data.last_name" readonly/>
            <label class="form-label" for="last_name">Last name</label>
          </div>
        </div>
        <div class="col-md-3">
          <router-link to="" class="btn btn-success btn-block btn-nabshop mb-4">Edit</router-link>
        </div>
      </div>
      <hr>

      <div class="row ">
        <div class="col-md-9">
          <div class="form-floating mb-4">
            <input type="email" id="email" class="form-control" v-model="user_data.email" readonly/>
            <label class="form-label" for="email">Email</label>
          </div>
        </div>
        <div class="col-md-3">
          <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Edit</button>
        </div>
      </div>
      <hr>


      <div class="row ">
        <div class="col-md-9">
          <div class="form-floating mb-4">
            <input type="text" id="phone" class="form-control" v-model="customer_data.phone" readonly/>
            <label class="form-label" for="phone">Phone number</label>
          </div>
        </div>
        <div class="col-md-3">
          <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Edit</button>
        </div>
      </div>
      <hr>


      <div class="row ">
        <div class="col-md-9">
          <!-- <div class="form-floating mb-4">
            <input type="text" id="phone" class="form-control" v-model="customer_data.phone" readonly/>
            <label class="form-label" for="phone">Phone number</label>
          </div> -->
        </div>
        <div class="col-md-3">
          <router-link to="/account/delete-account" type="submit" class="btn btn-danger btn-block btn-nabshop mb-4">Delete account</router-link>
        </div>
      </div>
   
    </div>
  </div>
    <ShopFooter/>
  </div>
</template>

<script>
// @ is an alias to /src
import ShopFooter from '@/components/ShopFooter.vue'
import axios from "axios"

export default {
  name: 'Account',
  components: {
    ShopFooter
  },
  data() {
    return {
      user_data: {},
      customer_data: {},
      username: '',
      first_name: '',
      last_name: '',
      email: ''
    }
  },
  mounted() {
    this.getUserData() 
    this.getCustomerData() 
  },
  methods: {
    async getUserData() {
      await axios
        .get('/auth/users/me/')
        .then(response => {
          this.user_data = response.data
          console.log(this.user_data)
        })
    },
    async getCustomerData() {
      await axios
        .get('/store/customers/me/')
        .then(response => {
          this.customer_data = response.data
          console.log(this.customer_data)
        })
    }
  }

}
</script>
<style scoped>
.loginform {
  width: 800px;
  height: min-content;
  border: 2px;
  border-radius: 7px;
  background: rgb(219, 217, 217);
  padding: 20px 40px;
  margin-top: 50px
}

.row-item {
  border: 2px;
  border-radius: 7px;
}

</style>