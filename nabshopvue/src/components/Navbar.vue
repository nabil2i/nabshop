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
              <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/store" class="nav-link active" aria-current="page">Catalogue</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/store/poetry" class="nav-link active" aria-current="page">Poetry</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/store/prose" class="nav-link" >Prose</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link active" aria-current="page">About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/contact" class="nav-link" >Contact</router-link>
            </li>
          </ul>

          <form class="flex-row d-none d-md-flex " role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <ul class="navbar-nav ms-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
            <li class="nav-item">
              <router-link to="/login" class="nav-link" aria-current="page">Login</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/sign-up" class="nav-link" aria-current="page">Sign up</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/cart" class="nav-link active" aria-current="page" >
                <span><i class='fas fa-shopping-cart' style='color:#3c8fc3'></i></span>
                <span class="badge rounded-pill badge-notification bg-danger">1</span>
              </router-link>
              
            </li>
            <li class="nav-item dropdown me-2 ms-2 me-lg-5">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Hello, John
              </a>
              <ul class="dropdown-menu" >
                <li><router-link to="/profile" class="dropdown-item" >Account</router-link></li>
                <li><router-link to="/orders" class="dropdown-item" >Orders</router-link></li>
                <li><router-link to="/addresses" class="dropdown-item" >Addresses</router-link></li>
                <li><hr class="dropdown-divider"></li>
                <li><router-link to="/" class="dropdown-item" href="#">Logout</router-link></li>
              </ul>
            </li>
          </ul>
          
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    msg: String
  },
  data() {
    return {
      showPhoneMenu: false,
    };
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
