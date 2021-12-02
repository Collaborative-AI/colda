// events.js

import fetch from './fetch';

export default {
  async getPostList() {
    return fetch.fetchPostsList(data => {
      console.log('fetchPostsList be called!');
      // do something
    });
  }
}