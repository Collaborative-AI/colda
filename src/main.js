import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// import "bootstrap/dist/css/bootstrap.min.css"
// import "bootstrap"

// import boxicons from "boxicons"

import "./assets/custom.scss";

const app = createApp(App)
// app.use(boxicons)
app.use(router)


app.mount("#app");



// import {request} from '../src/network/request.js'

// const instance1 = axios.create({
//     baseURL: 'http://123.207.32.32:8000',
//     timeout: 5000
// })

// instance1({
//     url: '/home/multidata'
// }).then(res => {
//     console.log(res);
// })
window.localStorage.setItem('color', 'blue')
console.log('color is', window.localStorage.getItem('color'));

// import axios from 'axios'
// const instance1= axios.create({
//     baseURL: 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com',
//     timeout: 5000
// })



// const payload = {
//     username: 'xie3',
//     email: 'xie00250@umn.edu',
//     password: 'Xie30123'
//   }

// request.post(`/user/users`, payload)
// .then((res) => {
// // Go to Login Page
// console.log('please verify email',res)    
// })

// axios 实现Basic Auth需要在config中设置 auth 这个属性即可
// request.post(`/auth/tokens`, {}, { 
// auth: {
//     'username': 'xie3',
//     'password': 'Xie30123'
// }
// }).then((response) => {
//     console.log('4321')
//     // handle success
//     if (response.data == 'not verify email yet'){
//         console.log('not verify email');
//     } else{
//         console.log('token is' ,response.data.token)
//         window.localStorage.setItem('Apollo-token', response.data.token)
//     }
    
// })
// http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com/user/confirm_email/InhpZTAwMjUwQHVtbi5lZHUi.YrdVcw.Ut7vjYy77mPG8CNWKk7YZrOkDpo
// request({
//     url: '/'
// }, res => {
//     console.log('result is', res);
// }, err => {
//     console.log('err is', err);
// })