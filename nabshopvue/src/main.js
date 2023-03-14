import 'bootstrap'
import jQuery from 'jquery'
import 'popper.js'
import { createApp } from 'vue'
import App from './App.vue'
import './assets/app.scss'
import router from './router'
import store from './store'
window.$ = window.jQuery = jQuery

createApp(App).use(store).use(router).mount('#app')
