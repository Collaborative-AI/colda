// fetch.js

import axios from 'axios';

export default {
  async fetchPostsList(callback) {
    return axios.get('https://jsonplaceholder.typicode.com/posts').then(res => {
      // console.log('res',res)
      return callback(res.data);
    })
  }
}