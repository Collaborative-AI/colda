<template>
  <div class="container">
    {{ msg }}
  </div>
</template>

<script>

// import request from '../network/request';
import {request} from '@/network/request';
export default {
  name: 'Ping',
  data() {
    return {
      msg: 'aaaaaaaaaaaaaaaaaaaa',
    };
  },
  
  created() {
    request({
      url: 'https://domain/chatroom/index'
    }).then(res =>{ 
      this.msg = res
      console.log(res);
    }).catch(err => {
      this.msg = "error"
      console.log(err);
    })
  },
  
  sockets: {
    connect: function() {
      console.log('socket connected')
    },
    // Monitor the data coming from the sound (custom prompt)
    response: function(res) {
      this.$message.success(res.msg)
    },
    // Monitor data from the backend (custom message)
    chat_message: function(msg) {
      this.messages.push(msg)
    },
  },
    methods: {
      onMsgSubmit(msg){  
        this.$socket.emit('user_input', msg)
      }
    },
}


</script>