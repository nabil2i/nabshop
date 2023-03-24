<template>
  <div class="hero">
        <div class="container h-100">
          <div class="row h-100 justify-content-center align-items-center">
            <div class="col-md-5">
              <div class="hero-content">
                <h1 class="hero-title">
                  NabShop
                </h1>
                <p>
                  Hello! I'm Nabil. Welcome to my bookshop, the NabShop! Your place to discover and buy my books.
                </p>
                <div class="hero-btn mt-5 d-flex">
                    <router-link to="/books" class="btn custom-btn btn-info mr-4">Explore the bookstore</router-link>
                    <!-- <button class="btn custom-btn btn-outline-secondary ms-4">Products</button> -->
                </div>
              </div>
            </div>
            <div class="col-md-7">
                <div class="graphic">
                    <img src="/images/svg/landing.svg" alt="">
                </div>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Nabshop',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .hero{
    padding-top: 7rem;
    width: 100%;
    height: 500px;
    text-align: left;
  }
</style>
