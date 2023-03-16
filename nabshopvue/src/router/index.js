import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Catalogue from '../views/Catalogue.vue'
import Checkout from '../views/Checkout.vue'
import Contact from '../views/Contact.vue'
import Orders from '../views/Orders.vue'
import Profile from '../views/Profile.vue'
import Signup from '../views/Signup.vue'
import Cart from '../views/Cart.vue'
import Addresses from '../views/Addresses.vue'
import BookDetail from '../views/BookDetail.vue'
import ChangePassword from '../views/ChangePassword.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: ChangePassword
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: Signup
  },
  {
    path: '/store',
    name: 'store',
    component: Catalogue
  },
  {
    path: '/book-detail',
    name: 'bookdetail',
    component: BookDetail
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: Checkout
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/orders',
    name: 'order',
    component: Orders
  },
  {
    path: '/addresses',
    name: 'paddresses',
    component: Addresses
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
