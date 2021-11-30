// export function sum(a, b) {
//   return a + b;
// }

import axios from 'axios'

/**
 * 传入一个回调函数，获取数据后执行
 */
export function featchData1(fn) {
  // 实际开发应为接口路径
  axios.get('https://bird.ioliu.cn/v2/?url=https://music.163.com/store/api/searchsuggest/get')
    .then(response => {
      fn(response.data)
    })
}
