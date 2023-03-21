<template>
  <div class="home">
    <!-- <Navbar/> -->
    <Navbar/>
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
  import axios from 'axios'

  export default {
    components: {
        Navbar,
      },
      data() {
        // navbar_reload: 0
        return {
         // user_data: {},
        }
      },
      beforeCreate() {
        this.$store.commit('initializeStore')
        const access = this.$store.state.access
        if (access) {
          axios.defaults.headers.common['Authorization'] = "JWT " + access
        } else {
          axios.defaults.headers.common['Authorization'] = ''
        }
      },
      mounted() {
        setInterval(() => {
          this.getAccess()
        }, 840000);

        //this.getUserData()
      },
      methods: {
        // reload() {
        //   this.navbar_reload += 1
        // },
        // getUserData() {
        //   axios
        //     .get('/auth/users/me/')
        //     .then(response => {
        //       //console.log(response.data)
        //       this.user_data = response.data
        //     })
        // },
        getAccess() {
          const accessData = {
            refresh: this.$store.state.refresh
          }

          axios
            .post('/auth/jwt/refresh', accessData)
            .then(response => {
              const access = response.data.access
              localStorage.setItem('access', access)
              this.$store.commit('setAccess', access)
            })
            .catch(error => {
              console.log(error)
            })
        }
      }
      
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
