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
Object.defineProperty(window, 'matchMedia', {
    writable: true,
    value: jest.fn().mockImplementation(query => ({
      matches: false,
      media: query,
      onchange: null,
      addListener: jest.fn(), // deprecated
      removeListener: jest.fn(), // deprecated
      addEventListener: jest.fn(),
      removeEventListener: jest.fn(),
      dispatchEvent: jest.fn(),
    })),
  });

  

import { mount } from '@vue/test-utils';
// import Counter from './counter'
import Navbar from '../../src/components/Navbar.vue'

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

describe('Navbar', () => {
    // 现在挂载组件，你便得到了这个包裹器
    const wrapper = mount(Navbar)
  
    // 也便于检查已存在的元素
    it('log', () => {
        expect(wrapper.find('li').exists()).toBe(true)
      })

    it('function', () => {
        expect(wrapper.vm.plus(1, 2)).toBe(3);
      })

    // const car = {type:"Fiat", model:"500", color:"white"};

    const test_example = {
        check_dict: { "e7bc07bc-568b-4917-b774-9961729da1c2": "1"}
    }

    it('function', () => {
        expect(wrapper.vm.unread_request(test_example)).toBe(100);
      })


    



  })