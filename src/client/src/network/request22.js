// import axios from 'axios';
// import Qs from 'qs'
// // import { resolve } from 'core-js/fn/promise';

// export function request(config) {
//   // create axios instances
//   const instance = axios.create({
//     baseURL: 'http://127.0.0.1:5000',
//     timeout: 20000,
//   });

//   // request interceptor
//   instance.interceptors.request.use((curconfig) => {
//     console.log('request interceptor', curconfig);
//     // 1. add information
//     // 2. 显示请求图标
//     // 3. 某些网络请求（登录 token），必须携带一些特殊信息
//     return curconfig;
//   }, (err) => {
//     console.log(err);
//   });

//   // response interceptor
//   instance.interceptors.response.use((res) => {
//     console.log('response interceptor', res);
//     return res.data;
//   }, (err) => {
//     console.log(err);
//   });

//   // send network request, return Promise
//   return instance(config);
// }

// export function request_withPayLoad(config) {
//     // create axios instances
//     const instance = axios.create({
//       baseURL: 'http://127.0.0.1:5000',
//       timeout: 20000,
//       method: 'POST',
//       data: param,
//       headers: {
//         'Content-Type': 'application/json;charset=UTF-8'
//       },
//     //   useRequestBody:true
//     });
  
//     // request interceptor
//     instance.interceptors.request.use((curconfig) => {
//       console.log('request interceptor', curconfig);
//       // 1. add information
//       // 2. 显示请求图标
//       // 3. 某些网络请求（登录 token），必须携带一些特殊信息
//       return curconfig;
//     }, (err) => {
//       console.log(err);
//     });
  
//     // response interceptor
//     instance.interceptors.response.use((res) => {
//       console.log('response interceptor', res);
//       return res.data;
//     }, (err) => {
//       console.log(err);
//     });
  
//     // send network request, return Promise
//     return instance(config);
//   }


// export function request_withdata(config) {
//   // create axios instance
//   console.log(config)
//   // console.log(pass_data)

//   const instance = axios.create({
    
//     baseURL: 'http://127.0.0.1:5000',
//     timeout: 19999,
//     method: 'POST',
//     headers: {
//       'Content-Type' : 'application/json'
//     },
//     transformRequest: [function(data) {
//       console.log("laiguo")
//       data = JSON.stringify(data)
//       return data
//     }],
//   });
  

//   // request interceptor
//   instance.interceptors.request.use((curconfig) => {

//     // curconfig.data = JSON.stringify(config['pass_data']);
//     console.log('request interceptor', curconfig);
//     // 1. add information
//     // 2. 显示请求图标
//     // 3. 某些网络请求（登录 token），必须携带一些特殊信息
//     return curconfig;
//   }, (err) => {
//     console.log(err);
//   });

//   // response interceptor
//   instance.interceptors.response.use((res) => {
//     console.log('response interceptor', res);
//     return res.data;
//   }, (err) => {
//     console.log(err);
//   });

//   // send network request, return Promise
//   return instance(config);
// }


