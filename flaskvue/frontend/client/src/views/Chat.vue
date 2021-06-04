<template>
  <div class="container">
    <h2>
      All chats:
    </h2>
    <br>
    {{ chat_messages }}
    <br>
    <br>

    <input placeholder="Type in Message" v-model="msg">
    <button @click="onMsgSubmit()">Submit Message</button>
    <br>
    <br>
  
    <input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="update"/>
    <br>
    <br>
    <button @click="left()">Leave ChatRoom</button>
    {{ "server response: " + server_response }}
  </div>
</template>

<script>

import {request} from '@/network/request';

export default {
  data() {
    return {
      messages: [],
      msg: '',
      chat_messages: [],
      server_response: [],
    };
  },

  mounted() {
    // this.$socket.connect();

    request({
      url: '/index',
    }).then((res) => {
      this.server_response.push(res);
      console.log(res);
    }).catch((err) => {
      this.server_response.push('error');
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
      this.$socket.emit('connect',  );
    },
    // # 监听后端传来数据（自定义提示）
    response(res) {
      console.log('response');
      console.log('aa', res);
      this.server_response.push(res.msg);
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
      this.$socket.emit('text', this.msg);
      this.msg = '';
    },
    left() {
      this.$socket.emit('leave_chat', );
    },
    update(e) {
      let file = e.target.files[0];
      this.$socket.emit('upload_file', file);
        // let param = new FormData(); //创建form对象
        // param.append('file',file);//通过append向form对象添加数据
        // console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
        // this.$axios.post('http://127.0.0.1:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //请求头要为表单
        //   .then(response=>{
        //     console.log(response.data);
        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //   })
    }
  },

};
</script>
