

// test为测试用例，接收2个参数，第一个为测试的名称
// 第二个参数是个函数，在函数内可以写一些测试逻辑

// expect为期望，期望sum(1,2)的返回值和3相等，整体称作为断言

// toBe为匹配器，匹配expect的值是否和匹配器中的值相等，相等于===
// toBe不能用于测试浮点数，可以使用toBeCloseTo
// toBe不能用于引用类型的检查, toEqual(value)匹配值，只匹配内容不匹配引用
// toBeNull(): 匹配null 等于toBe(null)
// toBeUndefined(): 匹配null 等于toBe(undefined)
// toBeNaN()：匹配NaN
// toBeTruthy()：匹配结果为true的值, 在js中false, 0, '', null, undefined, NaN都会被自动转换成false
// toBeFalsy()：匹配结果为false的值
// toBeDefined()：匹配已定义的值
// not：对后续的匹配取反
// toMatchObject(object)：匹配对象/数组是否属于子集 (是否有一部分相交)
// toContain(item)：匹配数组/Set/字符串中是否包含item
// toHaveBeenCalled()/.toBeCalled()：检查函数是否被执行
// toHaveBeenCalledWith(arg1, arg2, ...)/.toBeCalledWith(arg1, arg2, ...)：检查调用函数传入值是否匹配


// import {sum} from '.';

// test('adds 1 + 2 to equal 3', () => {
//   expect(sum(1, 2)).toBe(3);
// });

// import { featchData1 } from './index'

// test('测试 featchData1', () => {
//   featchData1((data) => {
//     //测试data中是否包含code: 200
//     expect(data).toMatchObject({
//       code: 200
//     })
//   })
// })

// const spectron = require('spectron')
// const { testWithSpectron } = require('vue-cli-plugin-electron-builder')
// jest.setTimeout(50000)

// console.log("------ssss")

// test('a window is created', async () => {
//   // Only v2.0+ require you to pass spectron as an arg
//   const { stdout, url, stopServe, app } = await testWithSpectron(spectron)
//   // stdout is the log of electron:serve
//   console.log(`electron:serve returned: ${stdout}`)
//   // url is the url for the dev server created with electron:serve
//   console.log(`the dev server url is: ${url}`)
//   // app is a spectron instance. It is attached to the dev server, launched, and waited for to load.
//   expect(await app.client.getWindowCount()).toBe(1)
//   // Before your tests end, make sure to stop the dev server and spectron
//   await stopServe()
// })

/**
 * @jest-environment node
 */
// import spectron from 'spectron'
// import { testWithSpectron } from 'vue-cli-plugin-electron-builder'
// jest.setTimeout(50000)

// test('Window Loads Properly', async () => {
//   // Wait for dev server to start
//   const { app, stopServe } = await testWithSpectron(spectron)
//   const win = app.browserWindow
//   const client = app.client
//   console.log("zzzzzzzzzzzzzzz", win)
//   console.log("fffff", client)
//   console.log("rrr", stopServe)
//   // Window was created
//   // expect(await client.getWindowCount()).toBe(1)
//   setTimeout(async () => expect(await client.getWindowCount()).toBe(1), 5000)
//   // It is not minimized
//   expect(await win.isMinimized()).toBe(false)
//   // Window is visible
//   expect(await win.isVisible()).toBe(true)
//   // Size is correct
//   const { width, height } = await win.getBounds()
//   expect(width).toBeGreaterThan(0)
//   expect(height).toBeGreaterThan(0)
//   // App is loaded properly
//   expect(
//     /Welcome to Your Vue\.js (\+ TypeScript )?App/.test(
//       await (await app.client.$('#app')).getHTML()
//     )
//   ).toBe(true)

//   await stopServe()
// })

import { mount } from '@vue/test-utils'
import Navbar from '../../src/components/Navbar.vue'

window.require = require;

const wrapper = mount(Navbar)
// const vm = wrapper.vm
// console.log('vm', vm)
console.log(wrapper)
