import 'bootstrap'
import jQuery from 'jquery'
import 'popper.js'
import { createApp } from 'vue'
import App from './App.vue'
import './assets/app.scss'
import router from './router'
import store from './store'
import axios from 'axios'
//import VueBootstrapToasts from "vue-bootstrap-toasts";
window.$ = window.jQuery = jQuery

axios.defaults.baseURL = 'http://localhost:8000';

const app = createApp(App)

app.use(store, axios)

app.use(router)
app.mount('#app')
