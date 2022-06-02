import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

// import boxicons from "boxicons"

import "./assets/custom.scss";

const app = createApp(App)
// app.use(boxicons)
app.use(router)


app.mount("#app");