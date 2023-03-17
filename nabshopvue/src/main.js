import 'bootstrap'
import jQuery from 'jquery'
import 'popper.js'
import { createApp } from 'vue'
import App from './App.vue'
import './assets/app.scss'
import router from './router'
import store from './store'
import axios from 'axios'
window.$ = window.jQuery = jQuery

axios.defaults.baseURL = 'http://127.0.0.1:8000';

const app = createApp(App)

app.use(store, axios)

app.use(router)
app.mount('#app')
