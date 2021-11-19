import { shallowMount } from '@vue/test-utils'
import Hello from './Hello.vue'

test('Hello', () => {
  // 渲染这个组件
  const wrapper = shallowMount(Hello)

  // `username` 在除去头尾空格之后不应该少于 7 个字符
  wrapper.setData({ username: ' '.repeat(5) })

  // 确认错误信息被渲染了
  expect(wrapper.find('.error').exists()).toBe(true)

  // 将名字更新至足够长
  wrapper.setData({ username: 'Lanchekerisjdislabcdkle' })

  // 断言错误信息不再显示了
  expect(wrapper.find('.error').exists()).toBe(true)
})