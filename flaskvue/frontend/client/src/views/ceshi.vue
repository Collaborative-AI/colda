<template>
  <div class="container">
    <input v-model="msg">
      <br>
      <br>
      {{ "messages: " + messages }}
      <br>
      <br>
      {{ "chat: " + chat_messages }}
      <br>
      <br>
      {{ "index_return: " + chat }}
    <button @click="onMsgSubmit(msg)">Button</button>
  </div>
</template>

<script>

import request from '@/network/request';

export default {
  data() {
    return {
      messages: [],
      msg: '',
      chat_messages: [],
      chat: null,
    };
  },

  mounted() {
    this.$socket.connect();
    request({
      url: '/index',
    }).then((res) => {
      this.chat = res;
      console.log(res);
    }).catch((err) => {
      this.chat = 'error';
      console.log(err);
    });

    // const url = 'http://127.0.0.1:5000/index'
    //     axios({
    //         method: 'get',
    //         url: url,
    //         data: {
    //             msg: 'hello'
    //         }
    //     }).then(res => {
    //         console.log(res)
    //     })
  },

  sockets: {
    connect() {
      console.log('socket connected');
    },
    // # 监听后端传来数据（自定义提示）
    response(res) {
      console.log('response');
      console.log('aa', res);
      this.messages.push(res.msg);
    },
    // this.$socket.on('connect', () => {
    //   console.log("emit received from server");
    // });
    // # 监听后端传来数据（自定义消息）
    chat_message(msg) {
      this.chat_messages.push(msg.msg);
    },
  },
  methods: {
    onMsgSubmit() {
      // console.log(this.msg)
      // # 用户点击，提交用户输入
      this.$socket.emit('join', this.msg);
      // this.$socket.emit('user_input', msg)
    },
  },

};
</script>
