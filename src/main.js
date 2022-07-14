import { BootstrapVue } from "bootstrap-vue";
// import "bootstrap-vue/dist/bootstrap-vue.css";
// import "bootstrap/dist/css/bootstrap.css";
import Vue from "vue";
import VueClipboard from "vue-clipboard2";
import LoadScript from "vue-plugin-load-script";
import PerfectScrollbar from "vue2-perfect-scrollbar";
import "vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css";
import App from "./App.vue";
import "./assets/css/custome.css";
import "./assets/css/popup.css";
import "./assets/css/style.css";
import "./assets/css/dark.css";
import router from "./router";
import "./util/errrorMessage";

Vue.use(LoadScript);
Vue.use(VueClipboard);
VueClipboard.config.autoSetContainer = true;

Vue.use(BootstrapVue);
Vue.use(PerfectScrollbar);

// Vue.use(VeeValidate);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
