import Vue from 'vue';
import App from './App.vue';
import router from './router';
import axios from './http'
import 'bootstrap/dist/css/bootstrap.css';
import store from './store';
import VueToasted  from 'vue-toasted'
import moment from 'moment'
// Import Bootstrap css and js files
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
// Styles required by the bootstrap-markdown editor
import './assets/bootstrap-markdown/css/bootstrap-markdown.min.css'
import './assets/bootstrap-markdown/css/custom.css'
import './assets/icon-awesome/css/font-awesome.min.css'

// // Change import to require for packaging

// console.log("11111111111111111111111111")
// const Vue = require('vue').default;
// const App = require('./App.vue').default
// console.log("22222222222222222222221")
// const router = require('./router').default;
// // console.log("main_router",router)

// // const axios = require('./http').default
// console.log("33333333333333333")
// // import 'bootstrap/dist/css/bootstrap.css';

// // const store = require('./store').default
// console.log("44444444444444444")
// // import VueToasted  from 'vue-toasted'
// // const VueToasted = require('vue-toasted').default
// console.log("5555555555555555521")
// const moment = require('moment').default
// console.log("666666666666666666666662221")
// // Import Bootstrap css and js files


// require('../node_modules/bootstrap/dist/css/bootstrap.css')
// require('../node_modules/bootstrap/dist/css/bootstrap.min.css')
// require('../node_modules/bootstrap') 
// require('./assets/bootstrap-markdown/css/bootstrap-markdown.min.css')
// require('./assets/bootstrap-markdown/css/custom.css')
// require('./assets/icon-awesome/css/font-awesome.min.css')


Vue.use(VueToasted, {
  // 主题样式 primary/outline/bubble
  theme: 'bubble',
  // 显示在页面哪个位置
  position: 'top-center',
  // 显示多久时间（毫秒）
  duration: 3000,
  // 支持哪个图标集合
  iconPack : 'material', // set your iconPack, defaults to material. material|fontawesome|custom-class
  // 可以执行哪些动作
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  },
});
Vue.config.productionTip = false;
Vue.prototype.$axios = axios
Vue.prototype.$moment = moment
Vue.prototype.$store = store

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
