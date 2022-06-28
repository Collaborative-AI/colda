import axios from 'axios'

const request = axios.create({
    baseURL: 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com',
    // baseURL: 'http://127.0.0.1:5000',
    timeout: 5000
})

request.interceptors.request.use(config => {
    const token = window.localStorage.getItem('Apollo-token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    console.log('config is', config)
    return config
  }, error => {
    // Do something with request error
    return Promise.reject(error)
  })

request.interceptors.response.use(response => {
console.log('axios response is', response)
return response
}, error => {
console.log('Error_https', error)
// if ('response' in error && error.response != undefined){
//   console.log('status' in error.response)
//   if ('status' in error.response){
//     switch  (error.response.status) {
//       case 401:
//         // 清除 Token 及 已认证 等状态
//         store.logoutAction()
//         // 跳转到登录页
//         if (router.currentRoute.path !== '/login') {
//           Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
//           router.replace({
//             path: '/login',
//             query: { redirect: router.currentRoute.path },
//           })
//         }
//         break
    
//       case 404:
//         Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
//         router.back()
//         break
//     }
//   }
// }

return Promise.reject(error)
})

export {request}

// function request(config, success, failure) {
//     const instance = axios.create({
//         baseURL: 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com',
//         timeout: 5000
//     })
//     instance(config)
//         .then(res => {
//             // console.log('result is', res);
//             success(res)
//         })
//         .catch(err => {
//             // console.log('err is', err);
//             failure(err)
//         })
// }

// export {request}