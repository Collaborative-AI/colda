import Vue from 'vue';
// import VueSocketIO from 'vue-socket.io';
// import SocketIO from 'socket.io-client'
import App from './App.vue';
import router from './router';
import axios from './http'
import 'bootstrap/dist/css/bootstrap.css';
import store from './store';
import VueToasted  from 'vue-toasted'

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

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
