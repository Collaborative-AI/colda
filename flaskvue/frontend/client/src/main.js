// import Vue from 'vue';
// import App from './App.vue';
// import router from './router';
// import axios from './http'
// import 'bootstrap/dist/css/bootstrap.css';
// import store from './store';
// import VueToasted  from 'vue-toasted'
// import moment from 'moment'
// // Import Bootstrap css and js files
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap'
// // Styles required by the bootstrap-markdown editor
// import './assets/bootstrap-markdown/css/bootstrap-markdown.min.css'
// import './assets/bootstrap-markdown/css/custom.css'
// import './assets/icon-awesome/css/font-awesome.min.css'

// Change import to require for packaging
const Vue = require('vue').default
const App = require('./App.vue').default
const router = require('./router').default
const axios = require('./http').default

// import 'bootstrap/dist/css/bootstrap.css';

const store = require('./store').default

// import VueToasted  from 'vue-toasted'
const VueToasted = require('vue-toasted').default
const moment = require('moment').default
// import moment from 'moment'
// Import Bootstrap css and js files

// require('bootstrap/dist/css/bootstrap.css')
// require('bootstrap/dist/css/bootstrap.min.css')
// require('bootstrap') 
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
