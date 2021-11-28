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
import { createLocalVue, mount } from '@vue/test-utils'
import vue from 'vue'
// import Counter from './counter'
import Navbar from '../../src/components/Navbar.vue'
import db from '../../src/db';
import axios from 'axios'
// jest.mock("axios")

window.require = require;

// const Navbar = require('../../components/Navbar.vue');

// 现在挂载组件，你便得到了这个包裹器
// const wrapper = mount(Counter)
// const wrapper =  mount(Navbar)

// 你可以通过 `wrapper.vm` 访问实际的 Vue 实例
// const vm = wrapper.vm

// 在控制台将其记录下来即可深度审阅包裹器
// 我们对 Vue Test Utils 的探索也由此开始
// console.log(wrapper)
// jest.mock("axios", () => ({
//     get: () => Promise.resolve({ data: [{ val: 1 }] })
//   }));

// describe('Navbar', () => {
//       // 现在挂载组件，你便得到了这个包裹器
//       // const wrapper = mount(Navbar)
//       beforeEach(()=>{
//         const localVue = createLocalVue()
//         localVue.use(vue)
//         const wrapper = mount(Navbar, {
//           mocks: {
//              $toasted: {
//                  success: () => {},
//              }
//           },
//           stubs: ['router-link','router-view']
//         });
//       console.log('wrapper',wrapper)
//       })
      
      
//       // 也便于检查已存在的元素
//       it('check exist element', () => {
//           expect(wrapper.find('li').exists()).toBe(true)
//         })
  
//       it('component function', () => {
//           expect(wrapper.vm.plus(1, 2)).toBe(3);
//         })
//         // ch
//       const users = [{ id: 1, name: "testa" }, { id: 2, name: "testb" }];
//       const test_example = {
//           check_dict: { "e7bc07bc-568b-4917-b774-9961729da1c2": "1"}
//       }
  
      
//       it('function async', () => {
//           axios.get = jest.fn().mockReturnValue(users);
//           // let mockFn = jest.fn().mockReturnValue('default');
//           axios.post = jest.fn().mockReturnValue(users);
//           db.get = jest.fn().mockReturnValue(users);
  
//           wrapper.vm.sharedState.user_id = 2
          
  
//           const result = axios.get('/match_assistor_id/')
//           expect(result).toEqual(users);
//           const result1 = db.get()
//           expect(result1).toEqual(users);
//           const result2 = axios.post('/match_assistor_id/')
//           expect(result2).toEqual(users);
//           expect(wrapper.vm.unread_request(test_example)).toBe('done');
//         })

  
//     })






describe('Navbar', () => {
    // 现在挂载组件，你便得到了这个包裹器
    // const wrapper = mount(Navbar)


    jest.mock("axios", () => ({
      get: () => Promise.resolve({ data: [{ val: 1 }] })
  })); 

  it('your test name', () => {
    const wrapper = mount('your component name', {
      mocks: {
        $toasted: {
            success: () => {},
        },
        $axios : axios
     },
    })
    expect(wrapper.vm.test_axios(callback)).toBe(3);

});



    jest.mock("axios", () => ({
      get: () => Promise.resolve({ data: [{ val: 1 }] })
    })); 
    
    
    const wrapper = mount(Navbar, {
        mocks: {
           $toasted: {
               success: () => {},
           },
           $axios : axios
        },
        stubs: ['router-link','router-view']
      });
    console.log('wrapper',wrapper)
    // 也便于检查已存在的元素
    it('check exist element', () => {
        expect(wrapper.find('li').exists()).toBe(true)
      })

    it('component function', () => {
        expect(wrapper.vm.plus(1, 2)).toBe(3);
      })

      it('component function', () => {
        expect(wrapper.vm.test_axios()).toBe(3);
      })
      // ch
    const users = [{ id: 1, name: "testa" }, { id: 2, name: "testb" }];
    const test_example = {
        check_dict: { "e7bc07bc-568b-4917-b774-9961729da1c2": "1"}
    }

    
    it('function async', () => {
        axios.get = jest.fn().mockReturnValue(users);
        // let mockFn = jest.fn().mockReturnValue('default');
        axios.post = jest.fn().mockReturnValue(users);
        db.get = jest.fn().mockReturnValue(users);

        wrapper.vm.sharedState.user_id = 2
        

        // wrapper.vm.$nextTick(() => {
        //     expect(wrapper.vm.test_response).toEqual(users);
        //   });
        // const result = wrapper.vm.unread_request(test_example);
        // expect(wrapper.vm.test_response.length).toBe(1);
        const result = axios.get('/match_assistor_id/')
        expect(result).toEqual(users);
        const result1 = db.get()
        expect(result1).toEqual(users);
        const result2 = axios.post('/match_assistor_id/')
        expect(result2).toEqual(users);
        expect(wrapper.vm.unread_request(test_example)).toBe('done');
      })


  })

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