<template>
  <div class="container">
    <button @click="askforhelp()">Ask for Help</button>
  </div>
</template>

<script>

// Encapsulated network request
import {request} from '@/network/request';
import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';

export default {
  name: "Login",
  // components: {
  //   Field,
  //   Form,
  // },
  data() {
    return {
      name: "",
      messages: [],
    };
  },

  mounted() {
    // this.$socket.connect();
    request({
      url: '/askhelp',
    }).then((res) => {
      this.messages.push(res);
      console.log(res);
    }).catch((err) => {
      this.chat = 'error';
      console.log(err);
    });
  },

  methods: {
    // isRequired(value) {
    //   return value ? true : 'This field is required';
    // },
    askforhelp() {

      request_withdata({
        url: '/askhelp',
        
      }).then((res) => {
        this.messages.push(res);
        console.log(res);
      }).catch((err) => {
        this.chat = 'error';
        console.log(err);
      });

      this.$router.push('/askhelp');

    },
  },

};
</script>
