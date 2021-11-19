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

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

import huakuai from 'huakuai-vue'
Vue.use(huakuai)
// import mdbvue from 'mdbvue'
// Vue.use(mdbvue)


import VueDashboard from 'vue-dashboard-vd'
// import 'vue-dashboard-vd/dist/vue-dashboard-vd.css'
Vue.use(VueDashboard);
import HeaderItems from './components/HeaderItems.vue'
import SidebarHeader from './components/SidebarHeader.vue'
import SidebarItems from './components/SidebarItems.vue'

Vue.component('header-items', HeaderItems)
Vue.component('sidebar-items', SidebarItems)
Vue.component('sidebar-header', SidebarHeader)

const node_path = window.require('path');

console.log(" this.exe_position",  node_path.resolve("./resources/dist/run/run.exe"))
console.log("dir",__dirname)
console.log(node_path.join(__dirname, '../dist/run/run.exe'))
import db from './db'

const fs = window.require("fs")
console.log("fs", fs)
// import path from 'path'
// var leveldown = window.require('leveldown');
// console.log("....", leveldown)
// var levelup = require('levelup');
// console.log("levelup", levelup)
// var levelup2 = window.require('levelup');
// console.log("levelup2", levelup2)

const sqlite3 = window.require('sqlite3');
console.log("sqlite3", sqlite3)

// function createDatabase(file){
//   var db = new sqlite3.Database(file);
//   if(!fs.existsSync(file)){
//     console.log("creating database file");
//     fs.openSync(file, "w");
//     db.run("CREATE TABLE users (username TEXT, password TEXT, email TEXT)", function(createResult){
//       if(createResult) throw createResult;
//     });
    
//     console.log("database initialized");
//   }

//   return db;
// }

// const sqlite3 = window.require('sqlite3').verbose();
// console.log("sqlite3", sqlite3)

// const sqlite31 = require('sqlite3');
// console.log("sqlite31", sqlite31)





// let db = new sqlite3.Database('Apollo_Client_db');


// import db from './lowdb'
// import db from './leveldb'


// import Datastore from 'nedb';
// import path from 'path';

// rendering process

// ipc

// main process 


// import { data } from 'jquery';

// const NeDB = require('nedb')
// const path = window.require('path');
// import { remote } from 'electron';
// const {remote} = require('electron')
// console.log("zzzz", remote)
// console.log("gggg", path.join(__dirname,'../../data.db'))
// console.log(NeDB)
// console.log('ijisfjoej')
// console.log(__dirname)
// console.log(path.join(__dirname,'../../data.db'))
// var db = new NeDB({
//     // filename: './user.db',

//     autoload: true,
//     filename: path.join(__dirname,'../../data.db'),
//     timestampData: true,
// })
// let db = new Datastore({
//     autoload: true,
//     timestampData: true,
//     // filename: path.join(remote.app.getPath('userData'), '../data.db'),
//     // filename: path.join(path.resolve("./exp"),'/data.db')
//     filename: path.join(__dirname,'../../data.db'),
// })





// import VueRouter from 'vue-router';
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
Vue.prototype.$db = db


new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
