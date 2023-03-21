import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    access:'',
    refresh: '',
    isLoading: false,
    //cart_id: '',
    name: ''
  },
  
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
        if (localStorage.getItem('refresh')) {
          state.refresh = localStorage.getItem('refresh')
        }
        // state.refresh = localStorage.getItem('refresh')
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
      // if (localStorage.getItem('cart_id')) {
      //   state.cart_id = localStorage.getItem('cart_id')
      // } else {
      //   localStorage.setItem('cart_id', '')
      //   state.cart_id = localStorage.getItem('cart_id')
      // }
      if (localStorage.getItem('name')) {
        state.cart_id = localStorage.getItem('name')
      } else {
        localStorage.setItem('name', '')
        state.cart_id = localStorage.getItem('name')
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
    setName(state, name){
      state.name = name
    },
    removeName(state) {
      state.name = ''
    },
    setRefresh(state, refresh) {
      state.refresh = refresh
    },
    removeRefresh(state) {
      state.refresh = ''
      state.isAuthenticated = false  
    },
    // setCartId(state, cart_id) {
    //   state.cart_id = cart_id
    // },
    // removeCartId(state) {
    //   state.cart_id = ''
    // },
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
    },
    removeCart(state) {
      state.cart = { items: [] }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
