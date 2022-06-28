
// const os = window.os ? window.os : require('os');
// const node_path = window.node_path ? window.node_path : require('path');
// const paht = require('path');

import { os, node_path } from './import_package.js'
// import db from './db'

export default {
    debug: true,
    state: {
      is_authenticated: window.localStorage.getItem('Apollo-token') ? true : false,
      // 用户登录后，就算刷新页面也能再次计算出 user_id
      user_id: window.localStorage.getItem('Apollo-token') ? JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id : 0,
      authority: window.localStorage.getItem('Apollo-token') ? JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).authority : 'user',

      // user_id: 0,
      // authority: 'user',

      msg: [],
      pending_num: 0,
      // development
      // // linux
      // root: "./exp",
      // exe_position: './dist/run/run',
      
      // windows
      // root: __dirname + "/../../../../../../exp",
      // exe_position: __dirname + "/../../../../../../dist/run/run.exe",
      

      // production
      // linux
      // root: __dirname + "../../exp",
      // exe_position: __dirname + '../../dist/run/run',
      // root = path.resolve("./exp"),
      // exe_position = path.resolve("./dist/run/run"),
      // // windows
      // root: __dirname + "/../exp",
      // exe_position: __dirname + '/../dist/run/run.exe',
      mode: "manual",
      // pending:[],
      // 用户登录后，就算刷新页面也能再次计算出 user_name
    //   user_name: window.localStorage.getItem('Apollo-token') ? JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_name : '',
      // 用户登录后，就算刷新页面也能再次计算出 user_avatar
      // 后端传 URL 必须先用 base64 编码，所以这里还要多进行一次 atob 解码 base64 字符串
    //   user_avatar: window.localStorage.getItem('Apollo-token') ? atob(JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_avatar) : ''
    },
    loginAction () {
      if (this.debug) { console.log('loginAction triggered') }
      this.state.is_authenticated = true
      const payload = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1]))
      this.state.user_id = payload.user_id
    //   this.state.user_name = payload.user_name
    //   this.state.user_avatar = atob(payload.user_avatar)
    },
    logoutAction () {
      if (this.debug) console.log('logoutAction triggered')
      window.localStorage.removeItem('Apollo-token')
      this.state.is_authenticated = false
      this.state.user_id = 0
    //   this.state.user_name = ''
    //   this.state.user_avatar = ''
    },
    changeroot() {
      
      let root = ""
      let exe_position = ""
      const isDevelopment = process.env.NODE_ENV !== 'production';
      if (os.type() == "Linux"){
        if (isDevelopment == true){
          root = node_path.resolve("./exp")
          exe_position = node_path.resolve("./dist/run/run")
        }else{
          // this.root = node_path.join(__dirname, '../exp')
          root = node_path.join(__dirname, '../../../apollo_exp')
          exe_position = node_path.join(__dirname, '../dist/run/run')
        }
    
      }else if (os.type() == "Darwin") {
        if (isDevelopment == true){
          root = node_path.resolve("./exp")
          exe_position = node_path.resolve("./dist/run/run")
        }else{
          root = node_path.join(__dirname, '../../../apollo_exp')
          exe_position = node_path.join(__dirname, '../dist/run/run')
        }

      }else if (os.type() == "Windows_NT") {
        if (isDevelopment == true){
          root = node_path.resolve("./exp")
          exe_position = node_path.resolve("./dist/run/run.exe")
        }else{
          root = node_path.join(__dirname, '../../../apollo_exp')
          exe_position = node_path.join(__dirname, '../dist/run/run.exe')
        }
      }

      return {root, exe_position}
    },

    // retrieve_setting_mode(user_id) {

    //   let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + user_id;
    //   db.get(select_sentence, function(err, row){
    //     if (err){
    //       console.log(err);
    //     }

    //     console.log("retrieve_setting_mode_row", row)

    //     if (row == null){
    //       this.mode = "manual";
    //     }
    //     else{
    //       this.mode = row.mode;
    //     }  
    //   })
    // },

    
  }

  // exports.default = store