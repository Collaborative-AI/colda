<template>
  <div>
    <input type="file" name="csvfile" ref="csvData" />
    <input type="button" @click="csv()" value="JS转换"/>
  </div>
</template>


<script>

// Encapsulated network request
// import {request} from '@/network/request';
// import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';

import csv2arr from '@/assets/csv-arr'

export default {
  name: "Shiyan",
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
    
  },

  methods: {
    submit(e) {
      let file = e.target.files[0];
      const payload = {
        
        // body: this.replyMessageForm.body
        file: file
      }
      this.$axios.post('/ceshi/', payload, {headers:{'Content-Type':'application/x-www-form-urlencoded' }})
        .then((response) => {
          // handle success
          // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
          // this.onResetReply()
          // this.getUserHistoryMessages(this.sharedState.user_id)
          console.log(response)
        })
        .catch((error) => {
          // handle error
          console.log(error)
          this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    },

    csv() {
      csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
            console.log('我的数据', res)
            const payload = {
        
        // body: this.replyMessageForm.body
             file: JSON.stringify(res),
            }

      console.log("stringify",JSON.stringify(res))
      console.log("parse",JSON.parse(JSON.stringify(res)))

            // , {headers:{'Content-Type':'application/x-www-form-urlencoded' }}
      this.$axios.post('/ceshi/', payload)
        .then((response) => {
          // handle success
          // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
          // this.onResetReply()
          // this.getUserHistoryMessages(this.sharedState.user_id)
          console.log(response)
        })
        .catch((error) => {
          // handle error
          // console.log(error)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
      })      
    }
    // isRequired(value) {
    //   return value ? true : 'This field is required';
    // },
    
  },

};
</script>
