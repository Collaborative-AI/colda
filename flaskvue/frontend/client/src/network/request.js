import axios from 'axios';
// import { resolve } from 'core-js/fn/promise';

export default function request(config) {
  // create axios instance
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 20000,
  });

  // request interceptor
  instance.interceptors.request.use((curconfig) => {
    console.log('request interceptor', curconfig);
    // 1. add information
    // 2. 显示请求图标
    // 3. 某些网络请求（登录 token），必须携带一些特殊信息
    return curconfig;
  }, (err) => {
    console.log(err);
  });

  // response interceptor
  instance.interceptors.response.use((res) => {
    console.log('response interceptor', res);
    return res.data;
  }, (err) => {
    console.log(err);
  });

  // send network request, return Promise
  return instance(config);
}

// return new Promise((resolve, reject) => {

// .then(res => {
//   resolve(res);
// })
// .catch(err => {
//   reject(err)
// })
// })
