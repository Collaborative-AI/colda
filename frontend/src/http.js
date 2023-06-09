
// const Vue = require('vue').default
// const router = require('./router').default
// const store = require('./store').default
// const axios = require('axios').default

import Vue from 'vue';
// import router from './router';
import { router } from './router'
import store from './store';
import axios from 'axios'

// 基础配置
axios.defaults.timeout = 50000  // 超时时间
// axios.defaults.baseURL = 'http://127.0.0.1:5000'
// axios.defaults.baseURL = 'http://3.145.140.55'
// axios.defaults.baseURL = 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com/' 
// #new web address

//lq xin ceshi
// axios.defaults.baseURL = 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com'

axios.defaults.baseURL = 'https://synspot-backend.herokuapp.com/'




// axios.defaults.transformRequest = [ function(data) {
//                                       console.log("laiguo")
//                                       data = JSON.stringify(data)
//                                       console.log("data", data)
//                                       return data
//                                     } ],
// Add a request interceptor
axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  const token = window.localStorage.getItem('Apollo-token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  
  // console.log("a", JSON.stringify(["match_id", "xa", "ya"]))
  
  // data = JSON.stringify(config.data.file) 
  // console.log("data",data)
    

    // console.log("file", Qs.stringify(config.data.file, {arrayFormat: 'repeat'}))
    // return Qs.stringify(config.data.file, {arrayFormat: 'repeat'})
    
  
  console.log("config shi", config)
  return config
}, function (error) {
  // Do something with request error
  console.log('cuo is', str(error), typeof(error), error_name);

  return Promise.reject(error)
})

// Add a response interceptor
axios.interceptors.response.use(function (response) {
  // Do something with response data
  // console.log("axios response", response)
  console.log("config shi2", response)
  return response
}, function (error) {
  console.log('cuo is', error, error.__name__);
  // Do something with response error
  console.log('Error_https', error)
  if ('response' in error && error.response != undefined){
    console.log('status' in error.response)
    if ('status' in error.response){
      switch  (error.response.status) {
        case 401:
          // 清除 Token 及 已认证 等状态
          store.logoutAction()
          // 跳转到登录页
          if (router.currentRoute.path !== '/login') {
            Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
            router.replace({
              path: '/login',
              query: { redirect: router.currentRoute.path },
            })
          }
          break
    
        case 404:
          Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
          router.back()
          break
      }
    }
  }
  
  
  return Promise.reject(error)
})

export default axios
// exports.default = axios