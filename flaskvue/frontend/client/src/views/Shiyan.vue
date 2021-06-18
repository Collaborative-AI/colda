<template>
  <div>
    <input type="file" name="csvfile" ref="csvData" />
    <input type="button" @click="csv()" value="JS转换"/>

    <button @click="create()">create file</button>

    <button @click="tiqu()">tiqu</button>

  </div>
</template>


<script>
//const { require } = window
const fs = window.require('fs');
const address = 'tem/' + 'b/'
// const { require } = window
// const fs = require('fs')
// const path = require('path');
// Encapsulated network request
// import {request} from '@/network/request';
// import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';

import csv2arr from '@/assets/csv-arr'
// import $ from 'jquery'
// import { mkdir } from 'fs';
//import fs from 'fs'
// import path from 'path'
//const fs = window.fs
// const fs = window.fs;
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

    tiqu() {
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
    },


    create() {
      //const fs = require('fs')

      
      console.log("aaaaa");
      // $(function() {
      //   fs.mkdirSync('Rabbit');
      // })
      fs.readFile('/home/qile/Documents/Apollo/test.txt', 'utf8' , (err, data) => {
        if (err) {
          console.error(err)
          return
        }
        console.log(data)
      })
      // fs.mkdirSync(`Rabbit`);
      // import { mkdir } from 'fs';

      // 创建 /tmp/a/apple，不管 `/tmp` 和 /tmp/a 是否存在。
      const address = 'tem/' + 'c/'
      const new_address = address + 'bbb/'
      fs.mkdir(new_address, { recursive: true }, (err) => {
        if (err) throw err;
        console.log("wancheng")
        // let prefix = 6
        // const filename = prefix + 'file2.txt'
        // fs.open(new_address + filename, 'w', function (err, file) {
        //   if (err) throw err;
        //   console.log('Saved!');
        // });
        let arr =  new Array(10);   //表格有10行
        for(let i = 0;i < arr.length; i++){
          arr[i] = new Array(10);    //每行有10列
        }
        arr[0][1] = 3
        arr[0][2] = 4
        arr = JSON.parse(JSON.stringify(arr))
        let csv = arr.join('\n')
        // const arr = ['zz','xx','www']
        console.log(arr)
        fs.writeFile(new_address + 'shiyan.csv', csv, function (err) {
          if (err) throw err;
          console.log('Saved!');
        });

        
      });
      // console.log("zzz");
      // fs.mkdir('/Rabbit', (err) => {
      //   if(err) throw err; // 如果出现错误就抛出错误信息

      //   console.log('文件夹创建成功');
      // })
      // mkdir('/tmp/a/apple', { recursive: true }, (err) => {
      //   if (err) throw err;
      // });
    },

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
      // console.log("csv",this.$refs.csvData.files[0])
      csv2arr.csv('/home/qile/Documents/Apollo/test.csv').then((res)=>{
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
