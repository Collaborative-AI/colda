
// import { mount } from '@vue/test-utils';
import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
// import vue from 'vue'
// import Counter from './counter'
import Navbar from '../../src/components/Navbar.vue'
import Login from '../../src/views/Auth/Login.vue'
// console.log('555555', Navbar)
// import db from '../../src/db';
// import describe from 
import total_object from './unread_request_inte.spec copy'
jest.setTimeout(10000);
import axios from '../../src/http'
// import {a} from './unread_request_inte.spec copy'

// https://vue-test-utils.vuejs.org/zh/api/options.html#localvue
// https://www.cnblogs.com/SamWeb/p/11454923.html
describe('zz', () =>{
  console.log('66')
  total_object.aa
})

describe('Navbar', () => {

  // 现在挂载组件，你便得到了这个包裹器    
  // const Navbar_wrapper = mount(Navbar, {
  //   // global:{
  //   mocks: {
  //     //  $toasted: {
  //     //      success: () => {},
  //     //  },
  //     $axios: axios,
  //     username: "lihailihai"

  //       // $db: db,
  //   },
  //   stubs: ['router-link','router-view']
  // });
  
  // 将原本vue page的data注掉
  // window.local有就会轮训
  const Login_wrapper = mount(Login, {
    mocks: {
      $toasted: {
        success: () => 6,
      },
      // $router: {
      //   push: () => 6,
      // },
      // $route: {
      //   query:{
      //     redirect: 'aa'
      //   },
      // },
      verifivation_res: true,
      $axios: axios,
      loginForm: {
        username: 'testa',
        password: 'Aa1234567!'
      }
    },
    stubs: ['router-link','router-view']
  });

  // beforeEach(() => {
  // });

  test('Login',(done)=>{
    let param_1 = (data) => {
      try{
        // expect(data).toEqual(
        //   'best,NIHAO'
        // )
        // c = data
        // console.log("Login", c)
        done()
        console.log('window', window.localStorage.getItem('Apollo-token'))
      }catch (error){
        done(error)
      }
    }

    Login_wrapper.vm.onSubmit(param_1)
  })

  // test('function async', (done) => {
    
  //   let c = 1
  //   let param1 = (data) => {
  //     try{
  //       expect(data).toEqual(
  //         'good,NIHAO'
  //       )
  //       c = data
  //       console.log("11111", c)
  //     }catch (error){
  //       done(error)
  //     }
  //   }
  //   let param2 = (data) => {
  //     try{
  //       expect(data).toEqual(
  //         5
  //       )
  //       c = data
  //       console.log("2222", c)
  //     }catch (error){
  //       done(error)
  //     }
  //   }

  //   let param3 = (data) => {
  //     try{
  //       expect(data).toEqual(
  //         'best,NIHAO'
  //       )
  //       c = data
  //       console.log("333", c)
  //       done()
  //       console.log('55555')
  //     }catch (error){
  //       done(error)
  //     }
  //   }

    
  //   Navbar_wrapper.vm.test_axios(param1, param2, param3)
  //   console.log("444", c)

  // })
})
