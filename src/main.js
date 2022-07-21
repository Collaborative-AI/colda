import '@babel/polyfill'
import 'mutationobserver-shim'
import Raphael from 'raphael/raphael'
global.Raphael = Raphael
import Vue from 'vue'
import './plugins'
import App from './App.vue'
import router from './router'
import store from './store'
import './directives'

Vue.config.productionTip = false

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

import axios from 'axios'
const instance1 = axios.create({
      baseURL: 'http://123.207.32.32:8000',
      timeout: 5000
  })
  
  instance1({
      url: '/home/multidata'
  }).then(res => {
      console.log(res);
  })