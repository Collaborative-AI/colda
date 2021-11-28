import fetch from './fetch_axios.js'

test('fetch data callback', async () => {
  expect.assertions(1);
  let mockFn = jest.fn();
  await fetch.fetchPostsList(mockFn);

  // 断言mockFn被调用
  expect(mockFn).toBeCalled();
})


// fetch.spec.js

// import events from './events';
// import fetch from './fetch';
// import {describe, expect, it } from '@jest/globals'
// // import  jest  from 'jest';

// // jest.mock('./fetch');
// // jest.mock('./fetch', () => {
// //     return jest.fn(() => 42);
// //   });

// const mockPlaySoundFile = jest.fn();
// jest.mock('./fetch', () => {
//   return jest.fn().mockImplementation(() => {
//     return {playSoundFile: mockPlaySoundFile};
//   });
// });

// test('mock 整个 fetch.js模块', async () => {
//   expect.assertions(2);
//   await events.getPostList();
//   expect(fetch.fetchPostsList).toHaveBeenCalled();
//   expect(fetch.fetchPostsList).toHaveBeenCalledTimes(1);
// });




// describe("ModuleA", () => {
//     beforeEach(() => {
//         jest.mock("./fetch.js")
//     })

//     it("should return the mock name", async () => {
//         expect.assertions(2);
//   await events.getPostList();
//   expect(fetch.fetchPostsList).toHaveBeenCalled();
//   expect(fetch.fetchPostsList).toHaveBeenCalledTimes(1);
//     })
// })