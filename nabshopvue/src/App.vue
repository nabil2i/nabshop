<template>
  <div class="home">
    <Navbar></Navbar>
    <!-- <div class="progress">
      <div class="progress-bar progress-bar-striped progress-bar-animated"
        v-bind:class="{'loading': $store.state.isLoading}"
      role="progressbar" aria-label="Animated striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100" style="width: 75%"></div>
    </div> -->
  <router-view/>

  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue';
 

  export default {
    components: {
        Navbar,
      },
      
  }
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
