import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Account from '../views/Account.vue'
import Addresses from '../views/Addresses.vue'
import BookDetail from '../views/BookDetail.vue'
import Cart from '../views/Cart.vue'
import Catalogue from '../views/Catalogue.vue'
import ChangeEmail from '../views/ChangeEmail.vue'
import ChangePassword from '../views/ChangePassword.vue'
import Checkout from '../views/Checkout.vue'
import Conditions from '../views/Conditions.vue'
import Contact from '../views/Contact.vue'
import DeleteAccount from '../views/DeleteAccount.vue'
import Home from '../views/Home.vue'
import LogIn from '../views/LogIn.vue'
import Orders from '../views/Orders.vue'
import Privacy from '../views/Privacy.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import Success from '../views/Success.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUP',
    component: SignUp
  },
  {
    path: '/books',
    name: 'Catalogue',
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
  // {
  //   path: '/genre/:genre_id/',
  //   name: 'Genre',
  //   component: Genre
  // },
  {
    path: '/books/:book_id/bookeditions/:bookedition_id/',
    name: 'BookDetail',
    component: BookDetail
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
    path: '/conditions',
    name: 'Conditions',
    component: Conditions
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: Privacy
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/checkout',
    name: 'checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  // {
  //   path: '/account/delete-account',
  //   name: 'DeleteAccount',
  //   component: DeleteAccount,
  //   meta: {
  //     requireLogin: true
  //   },
  // },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {
      requireLogin: true
    },
    children: [
      {
        path: '/change-email',
        name: 'ChangeEmail',
        component: ChangeEmail,
        meta: {
          requireLogin: true
        },
      },
      {
        path: '/change-password',
        name: 'ChangePassword',
        component: ChangePassword,
        meta: {
          requireLogin: true
        },
      },
      
    ]
  },
  {
    path: '/orders',
    name: 'order',
    component: Orders,
    meta: {
      requireLogin: true
    },
  },
  {
    path: '/addresses',
    name: 'addresses',
    component: Addresses,
    meta: {
      requireLogin: true
    },
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path} });
  } else {
    next()
  }
})

export default router
