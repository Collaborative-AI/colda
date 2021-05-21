import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import VueSocketIO from 'vue-socket.io';


Vue.config.productionTip = false;

Vue.use(new VueSocketIO({
  debug: true,
  connection: 'http://127.0.0.1:5000/chatroom',
}))

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
