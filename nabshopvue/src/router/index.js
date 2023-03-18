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
import BookDetailEbook from '../views/BookDetailEbook.vue'
import ChangePassword from '../views/ChangePassword.vue'
import Genre from '../views/Genre.vue'
import Search from '../views/Search.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: Signup
  },
  {
    path: '/store',
    name: 'store',
    component: Catalogue,
    children: [
      {
        path: 'poetry',
        name: 'poetry',
        component: Catalogue
      },
      {
        path: 'prose',
        name: 'prose',
        component: Catalogue
      },
    ]
  },
  {
    path: '/genre/:genre_id/',
    name: 'Genre',
    component: Genre
  },
  {
    path: '/:bookedition_id/',
    name: 'BookDetail',
    component: BookDetail
  },
  {
    path: '/:bookedition_id/',
    name: 'BookDetailEbook',
    component: BookDetailEbook
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
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
    name: 'addresses',
    component: Addresses
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
