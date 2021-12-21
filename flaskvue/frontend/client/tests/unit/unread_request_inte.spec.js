// import { shallowMount } from '@vue/test-utils'
// // import Hello from './Hello.vue'
// import Navbar from '../../src/components/Navbar.vue'

// test('Hello', () => {
//   // 渲染这个组件
//   const wrapper = shallowMount(Hello)

//   // `username` 在除去头尾空格之后不应该少于 7 个字符
//   wrapper.setData({ username: ' '.repeat(5) })

//   // 确认错误信息被渲染了
//   expect(wrapper.find('.error').exists()).toBe(true)

//   // 将名字更新至足够长
//   wrapper.setData({ username: 'Lanchekerisjdislabcdkle' })

//   // 断言错误信息不再显示了
//   expect(wrapper.find('.error').exists()).toBe(true)
// })

// test('Navbar', () => {
//     // 渲染这个组件
//     const wrapper = shallowMount(Navbar)
  
//     // `username` 在除去头尾空格之后不应该少于 7 个字符
//     wrapper.setData({ username: ' '.repeat(5) })
  
//     // 确认错误信息被渲染了
//     expect(wrapper.find('.error').exists()).toBe(true)
  
//     // 将名字更新至足够长
//     wrapper.setData({ username: 'Lanchekerisjdislabcdkle' })
  
//     // 断言错误信息不再显示了
//     expect(wrapper.find('.error').exists()).toBe(true)
//   })

// 从测试实用工具集中导入 `mount()` 方法
// 同时导入你要测试的组件
// window.require = jest.fn(); 

// Object.defineProperty(window, 'matchMedia', {
//     writable: true,
//     value: jest.fn().mockImplementation(query => ({
//       matches: false,
//       media: query,
//       onchange: null,
//       addListener: jest.fn(), // deprecated
//       removeListener: jest.fn(), // deprecated
//       addEventListener: jest.fn(),
//       removeEventListener: jest.fn(),
//       dispatchEvent: jest.fn(),
//     })),
//   });

  

// import { mount } from '@vue/test-utils';
import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
// import vue from 'vue'
// import Counter from './counter'
import Navbar from '../../src/components/Navbar.vue'
console.log('555555', Navbar)
import db from '../../src/db';

// jest.mock("axios")
// console.log("4444", axios)
// import axios from '../../src/http'

// jest.mock('axios');

// let db = 'a'

// jest.mock('db')
// jest.mock("db", () => ({
//   get: () => Promise.resolve({ data: [{ val: 666 }] })
//   })); 

  // jest.mock("axios", () => ({
  //   get: () => Promise.resolve({ data: [{ val: 666 }] })
  //   })); 

// let a = Navbar.methods.test_axios
// console.log("a", a(), a[0], typeof a)

// let a = Navbar.methods.test_axios
// console.log("a", a(), a[0], typeof a)
// let Navbar_mock = jest.mock('../../src/components/Navbar.vue');
// console.log('Navbar_mock', Navbar_mock)
// let a_mock = jest.mock(a)
// console.log("a_mock", a_mock)

// console.log("a", a(), a[0], typeof a)


// console.log('jest', jest)

jest.setTimeout(30000);
import {sum} from './index'
import axios from '../../src/http'

test('Window Loads Properly', () => {
    expect(sum(1, 2)).toBe(3);
}) 

describe('Navbar', () => {
    // 现在挂载组件，你便得到了这个包裹器
    // const wrapper = mount(Navbar)

    // const axios = {
    //   get: () => Promise.resolve({ data: [{ val: 1 }] })
    // };

    const db = {
      prepare: () => { return {get: () => 6} },
      get: () => 6
    };
    
    const wrapper = mount(Navbar, {
      // global:{
        mocks: {
          //  $toasted: {
          //      success: () => {},
          //  },
          $axios: axios,
          // $db: db,
      },
      stubs: ['router-link','router-view']
  });
    // https://vue-test-utils.vuejs.org/zh/api/options.html#localvue
    

    // console.log('wrapper！！！',wrapper, wrapper.vm)
    // console.log('vm', wrapper.vm)
    // 也便于检查已存在的元素
    // test('check exist element', () => {
    //     expect(wrapper.find('li').exists()).toBe(true)
    //   })

      test('function async', (done) => {

        wrapper.vm.test_axios((data) => {
          expect(data).toEqual(
            'good,NIHAO'
          )
          done()
        // expect(wrapper.vm.test_axios()).toBe('done');

        // expect(wrapper.vm.unread_request(test_example)).toBe('done');
      })

      // wrapper.vm.test_axios()


    })



  })




    
//     // test('component function', () => {
//     //     expect(wrapper.vm.plus(1, 2)).toBe(3);
//     //   })

//     //   // ch
//     const users = [{ id: 1, name: "testa" }, { id: 2, name: "testb" }];
//     const test_example = {
//         check_dict: { "e7bc07bc-568b-4917-b774-9961729da1c2": "1"}
//     }

    
//     test('function async', () => {
//         axios.get = jest.fn().mockReturnValue(users);
//     //     // let mockFn = jest.fn().mockReturnValue('default');
//     //     axios.post = jest.fn().mockReturnValue(users);
//         db.get = jest.fn().mockReturnValue(users);
//         console.log('$$$$$', db)
//         // db.get = jest.fn().mockReturnValue(users);
//         // console.log('%%%%', db)
        
//         wrapper.vm.sharedState.user_id = 2
//         // wrapper.vm.test_axios()
//         console.log("sssss", axios.get)

//         // wrapper.vm.$nextTick(() => {
//         //     expect(wrapper.vm.test_response).toEqual(users);
//         //   });
//         // const result = wrapper.vm.unread_request(test_example);
//         // expect(wrapper.vm.test_response.length).toBe(1);
//         // const result = axios.get('/match_assistor_id/')
//         // expect(result).toEqual(users);
//         // const result1 = db.get()
//         // expect(result1).toEqual(users);
//         // const result2 = axios.post('/match_assistor_id/')
//         // expect(result2).toEqual(users);
//         // expect(wrapper.vm.test_axios()).toBe('done');
//         // expect(wrapper.vm.unread_request(test_example)).toBe('done');
//       })


//   })

//   describe('MyComponent', () => {
//     it('When foo is set to -something-, set bar to true', () => {
//       const myItems = [
//         { id: 200, bar: false },
//         { id: 300, bar: false }
//       ]
//       const localVue = createLocalVue()
//       const wrapper = shallowMount(MyComponent, {
//         localVue,
//         propsData: {
//           myItems
//         }
//       })
  
//       wrapper.vm.foo = 'something'
//       wrapper.vm.doSomeWork()
  
//       expect(myItems[0].bar).toBe(true)
//     })
//   })
  
//   describe("Posts.vue", () => {
//     it("mocking the axios call to get posts should work", () => {
//       var wrapper = mount(Navbar);
//       expect(wrapper.vm.posts.length).toBe(1);
//     });
//   });