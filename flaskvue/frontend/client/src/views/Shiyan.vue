<template>
  <div>
    <input type="file" name="csvfile" ref="csvData" />
    <input type="button" @click="csv()" value="JS转换"/>

    <button @click="create()">create file</button>

    <button @click="tiqu()">tiqu</button>

    <button @click="test_async()">test async</button>

    <div v-for="task_id in task_id_list" :key="task_id.id">
      {{ task_id }}
      <input type="file" name="csvfile" ref="csvData" />
      <input type="button" @click="csv()" value="JS转换"/>
    </div>

  </div>
</template>


<script>
//const { require } = window
const fs = window.require('fs');
const xlsx2json = window.require("node-xlsx");
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
      task_id_list: [],
      length: 0,
      success: 0
    };
  },

  mounted() {
    // this.$socket.connect();
    
  },

  methods: {
    test(cur_list) {
      this.length = cur_list.length
      this.success = 0
      for (let i = 0; i < cur_list.length; i++){
        this.task_id_list = cur_list;
      }

      let a = 0
      while(this.length != this.success){
        a += 1
      }
    },
    test_async() {
      this.test(["a","b"]),
      this.test(["c"])
    },


    // test2(content) {
    //   console.log("test2",content)
    // },
    // test(indicator) {
    //   if(indicator){

    //     function sleep (time) {
    //       return new Promise((resolve) => setTimeout(resolve, time));
    //     }

    //     // 用法
    //     sleep(500).then(() => {
    //         for (let i = 0; i < 20000000; i++){
    //           if(i%100000 == 0){
    //             console.log("aaaaaaaaaaaaaaaaaaaaaaa", i)
    //           }
    //         }
    //         console.log("diyici");
    //         this.test2();
    //     })

    //     console.log("++++++++++++++++++++++++++++")
    //     // for (let i = 0; i < 20000000; i++){
    //     //   if(i%100000 == 0){
    //     //     console.log(i)
    //     //   }
    //     // }
    //     // console.log("diyici");
    //   }else{
        // function sleep (time) {
        //   return new Promise((resolve) => setTimeout(resolve, time));
        // }

        // // 用法
        // sleep(500).then(() => {
        //     for (let i = 0; i < 20000000; i++){
        //       if(i%100000 == 0){
        //         console.log("bbbbbbbbb", i)
        //       }
        //     }
        //     console.log("dierci");
        //     this.test2();
        // })
    //     // for (let i = 0; i < 8; i++){
        
        
    //     // }
    //     // console.log("dierci");
    //   }


    //   console.log("--------------------------")

    //     if(indicator){
    //       this.test2("11111111111111111111111")
    //     }else{
    //       this.test2("2222222222222222222222")
    //     }
    // },

    
    tiqu() {
      let list = xlsx2json.parse("/home/qile/Documents/Apollo/test.csv" );     
      console.log(list);
      console.log(list[0].data)
      console.log(typeof(list[0].data))
      console.log(JSON.stringify(list[0].data))

      // const payload = {
        
      //   // body: this.replyMessageForm.body
      //   file: JSON.stringify(list[0].data),
      // }

      // this.$axios.post('/ceshi/', payload)
      //   .then((response) => {
      //     // handle success
      //     // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
      //     // this.onResetReply()
      //     // this.getUserHistoryMessages(this.sharedState.user_id)
      //     console.log(response)
      //   })
      //   .catch((error) => {
      //     // handle error
      //     // console.log(error)
      //     // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      //   })
    },



    create() {
      //const fs = require('fs')

      
      console.log("aaaaa");
      // $(function() {
      //   fs.mkdirSync('Rabbit');
      // })
      fs.readFile('/home/qile/Documents/Apollo/test.csv', 'utf8' , (err, data) => {
        if (err) {
          console.error(err)
          return
        }
        console.log(typeof(data))
        console.log(data.length)
        let a = data.split("\n");
        console.log(a)
        console.log("type", typeof(a))
        console.log(data)

        const payload = {
        
        // body: this.replyMessageForm.body
          file: JSON.stringify(a),
        }

          // console.log("stringify",JSON.stringify(res))
          // console.log("parse",JSON.parse(JSON.stringify(res)))

            // , {headers:{'Content-Type':'application/x-www-form-urlencoded' }}
        this.$axios.post('/ceshi/', payload)
          .then((response) => {

          console.log(response)
        })
        .catch((error) => {
        })
      })
      // fs.mkdirSync(`Rabbit`);
      // import { mkdir } from 'fs';

      // 创建 /tmp/a/apple，不管 `/tmp` 和 /tmp/a 是否存在。
      // const address = 'tem/' + 'c/'
      // const new_address = address + 'bbb/'
      // fs.mkdir(new_address, { recursive: true }, (err) => {
      //   if (err) throw err;
      //   console.log("wancheng")
      //   // let prefix = 6
      //   // const filename = prefix + 'file2.txt'
      //   // fs.open(new_address + filename, 'w', function (err, file) {
      //   //   if (err) throw err;
      //   //   console.log('Saved!');
      //   // });
      //   let arr =  new Array(10);   //表格有10行
      //   for(let i = 0;i < arr.length; i++){
      //     arr[i] = new Array(10);    //每行有10列
      //   }
      //   arr[0][1] = 3
      //   arr[0][2] = 4
      //   arr = JSON.parse(JSON.stringify(arr))
      //   let csv = arr.join('\n')
      //   // const arr = ['zz','xx','www']
      //   console.log(arr)
      //   fs.writeFile(new_address + 'shiyan.csv', csv, function (err) {
      //     if (err) throw err;
      //     console.log('Saved!');
      //   });

        
      // });
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
      console.log("csvdata", this.$refs.csvData)
      console.log("csvdata,file", this.$refs.csvData.files)
      console.log("csv",this.$refs.csvData.files[0])
      console.log("typeofcsv",typeof(this.$refs.csvData.files[0]))
      // '/home/qile/Documents/Apollo/test.csv'
      csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
            this.success += 1
            console.log('我的数据', res)
            const payload = {
        
        // body: this.replyMessageForm.body
             file: JSON.stringify(res),
            }

      // console.log("stringify",JSON.stringify(res))
      // console.log("parse",JSON.parse(JSON.stringify(res)))

      //       // , {headers:{'Content-Type':'application/x-www-form-urlencoded' }}
      // this.$axios.post('/ceshi/', payload)
      //   .then((response) => {
      //     // handle success
      //     // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
      //     // this.onResetReply()
      //     // this.getUserHistoryMessages(this.sharedState.user_id)
      //     console.log(response)
      //   })
      //   .catch((error) => {
      //     // handle error
      //     // console.log(error)
      //     // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      //   })
      })      
    }
    // isRequired(value) {
    //   return value ? true : 'This field is required';
    // },
    
  },

};
</script>
