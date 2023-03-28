<template>
  <div class="hello">
    <nav class="navbar navbar-expand-lg bg-body-tertiary bg-dark navbar-dark">
      <div class="container-fluid justify-content-between">
        <router-link to="/" class="navbar-brand ms-0 ms-lg-5"><img src="../assets/nabshop-dark.png" width="150" alt="Logo"> </router-link>
        <button
          class="navbar-toggler" type="button"
          data-bs-toggle="collapse" data-bs-target="#navbarScroll"
          aria-controls="navbarScroll" aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarScroll" :class="{'is-active': showPhoneMenu}">
          <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
            <!-- <li class="nav-item">
              <router-link to="/home" class="nav-link active" aria-current="page">Home</router-link>
            </li> -->
            <li class="nav-item">
              <router-link to="/" class="nav-link " >Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/books" class="nav-link " >Catalogue</router-link>
            </li>
            <!-- <li class="nav-item">
              <router-link to="/store/poetry" class="nav-link active" aria-current="page">Poetry</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/store/prose" class="nav-link" >Prose</router-link>
            </li> -->
            <li class="nav-item">
              <router-link to="/about" class="nav-link " >About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/contact" class="nav-link" >Contact</router-link>
            </li>
          </ul>

          <form class="flex-row d-none d-md-flex " role="search" action="/search">
          <!-- <span><i class="fas fa-search"></i></span> -->
            <input class="form-control me-2" name="query" type="search" placeholder="Search for a book" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <ul class="navbar-nav ms-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
            <template v-if="!$store.state.isAuthenticated">
            <li class="nav-item">
              <router-link to="/login" class="nav-link" aria-current="page">Login</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/sign-up" class="nav-link" aria-current="page">Sign up</router-link>
            </li>
            </template>
            
            <template v-else>
            <li class="nav-item dropdown me-2 ms-0 me-lg-0">
              <a class="nav-link dropdown-toggle" href="/profile" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Hello <span> {{ name }}</span> 
              </a>
              <ul class="dropdown-menu" >
                <li><router-link to="/account" class="dropdown-item" >Account</router-link></li>
                <li><router-link to="/orders" class="dropdown-item" >Orders</router-link></li>
                <!-- <li><router-link to="/addresses" class="dropdown-item" >Addresses</router-link></li> -->
                <li><hr class="dropdown-divider"></li>
                <li><button class="dropdown-item" @click="logout">Logout</button></li>
              </ul>
            </li>
            </template>
            
            <li class="nav-item me-5">
              <router-link to="/cart" class="nav-link active" aria-current="page" >
                <span><i class='fas fa-shopping-cart' style='color:#3c8fc3'></i></span>
                <span class="badge rounded-pill badge-notification bg-danger">{{ cartTotalLength }}</span>
              </router-link>
              
            </li>
          </ul>
          
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Navbar',
  props: {
    user_data: Object

  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  data() {
    return {
      showPhoneMenu: false,
      name: this.$store.state.name,
      cart: {
        items: []
      }
    };
  },
  methods: {
    logout() {
      axios.defaults.headers.common['Authorization'] = ''

      localStorage.removeItem("access")
      localStorage.removeItem("username")
      localStorage.removeItem("id")
      localStorage.removeItem("name")

      this.$store.commit('removeAccess')
      this.$store.commit('removeName')
      this.$store.commit('removeCart')

      this.$router.push('/')
    }
  }
}
</script>

<style scoped lang="scss">

</style>
