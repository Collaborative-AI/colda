// const navbar = require('../../components/Navbar');

// test('adds 1 + 2 to equal 3', () => {
//     expect(navbar.sum(1, 2)).toBe(3);
//   });


// test.js

// 从测试实用工具集中导入 `mount()` 方法
// 同时导入你要测试的组件
import { mount } from '@vue/test-utils';
// import Counter from './counter'
import Navbar from '../../components/Navbar'
// const Navbar = require('../../components/Navbar.vue');

// 现在挂载组件，你便得到了这个包裹器
// const wrapper = mount(Counter)
// const wrapper =  mount(navbar)

// 你可以通过 `wrapper.vm` 访问实际的 Vue 实例
// const vm = wrapper.vm

// 在控制台将其记录下来即可深度审阅包裹器
// 我们对 Vue Test Utils 的探索也由此开始
// console.log(wrapper)

describe('Counter', () => {
    // 现在挂载组件，你便得到了这个包裹器
    const wrapper = mount(Navbar)
  
    it('renders the correct markup', () => {
      expect(wrapper.html()).toContain('<span class="count">0</span>')
    })
  
    // 也便于检查已存在的元素
    it('has a button', () => {
      expect(wrapper.contains('button')).toBe(true)
    })
  })