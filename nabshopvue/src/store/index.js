import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    access:'',
    refresh: '',
    isLoading: false
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
        state.access = localStorage.getItem('refresh')
        state.isAuthenticated = true
      } else {
        state.access = ''
        state.refresh = ''
        state.isAuthenticated = false
      }
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    setAccess(state, access){
      state.access = access
      state.isAuthenticated = true
    },
    removeAccess(state) {
      state.access = ''
      state.isAuthenticated = false  
    },
    setRefresh(state, refresh) {
      state.refresh = refresh
    },
    removeRefresh(state) {
      state.refresh = ''
      state.isAuthenticated = false  
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.bookedition.id === item.bookedition.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    }
  },
  actions: {
  },
  modules: {
  }
})
