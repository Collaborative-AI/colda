<template>
  <div>
    <input type="file" name="csvfile" ref="csvData" />
    <input type="button" @click="csv()" value="JS转换"/>

    <button @click="create()">create file</button>

    <button @click="tiqu()">tiqu</button>

    <button @click="test_async()">test async</button>
    <button @click="sync()">Sync</button>
    <button @click="interval()">test interval</button>
    <button @click="set()">test set</button>
    <button @click="diaoyong()">test python shell</button>
    <button @click="delete_all_rows()">delete_all_rows</button>
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
// const ex = require("child_process").execFileSync;
const ex = window.require("child_process");

// const { require } = window
// const fs = require('fs')
// const path = require('path');
// Encapsulated network request
// import {request} from '@/network/request';
// import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';
import axios from 'axios'
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
    diaoyong() {
      // $.ajax({
      //   type: "POST",
      //   url: "~/pythoncode.py",
      //   data: { param: text}
      // }).done(function( o ) {
      //   // do something
      // });
      // const pyshell =  window.require('python-shell');

      // const filepath = "Python_Code/"
      // const filename = "hello.py"

      // pyshell.run(filepath+filename,  function  (err, results)  {
      // if  (err)  throw err;
      // console.log('hello.py finished.');
      // console.log('results', results);
      // });

      // var exec = require('child_process').exec;
      // var arg1 = 'hello';
      // var arg2 = 'world';
      // var filename = 'hello.py'
      // exec('python'+' '+filename+' '+arg1+' '+arg2,function(err,stdout,stderr){
      //     if(err)
      //     {
      //         console.log('stderr',err);
      //     }
      //     if(stdout)
      //     {
      //         console.log('stdout',stdout);
      //     }

      // });

      // /home/qile/Documents/Apollo/flaskvue/frontend/client/
      try{
        let stdout = ex.execSync('python Python_Code/hello.py ' + 1 + ' ' + 2, {encoding: 'utf8'})
        console.log('比较结果：', stdout);
      }catch{
        console.log("wrong")
      }

      const a = [];
      a.push("11")
      console.log(a)

      let b = [];
      b.push("2")
      console.log(b)

      


    },

    set() {
      console.log("1")
      let arr =  new Array(5);   
        // for(let i = 0;i < arr.length; i++){
        //   arr[i] = new Array(5);    
        // }
        arr[0] = 1
        arr[1] = 5
        arr[2] = 1
        arr[3] = 1
        arr[4] = 2
      console.log("2", arr.length)
      let mySet = new Set()
      for (let i = 0; i < arr.length; i++){
        console.log("arr[i]", arr[i])
        mySet.add(arr[i])
      }
      console.log("3",mySet.size)
      let myArr = Array.from(mySet)
      console.log("4", myArr.length)
      for (let i = 0; i < myArr.length; i++){
        console.log("myArr[i]", myArr[i])
      }
      console.log("5")
    },
    interval() {
      let count = 1;
      let getTime = window.performance;
      let startTime = getTime.now();
      console.log("starttune",startTime)

      function sleep(time) {
        let startTime = window.performance.now();
        while (window.performance.now() - startTime < time) {}
      }

      function ce() {
        console.log(`第${count}次开始 ${getTime.now() - startTime}`); // 显示开始时间
        // setTimeout(() => {
        //   // let startTime = window.performance.now();
        //   console.log(`任务队列函数${count}${startTime}`)
        // }, 700)
        // {params}
          // axios.get('/ceshi/')
          //   .then((response) => {
          //   // handle success
          //     console.log("11111111111")
          //     sleep(700)
          //     console.log("222222222")

          //     // axios.get('/ceshi/')
          //     //   .then((response) => {
          //     //   // handle success
          //     //   console.log("33333")
          //     //   sleep(500)
          //     //   console.log("4444")
          //     //   })
          //     //   .catch((error) => {
          //     //   })
          // })
          // .catch((error) => {
          // })
          // function doubleAfter2seconds(num) {
          //     return new Promise((resolve, reject) => {
          //         setTimeout(() => {
          //             resolve(2 * num)
          //         }, 500);
          //     } )
          // }

          // async function testResult() {
          //   let result1 = await doubleAfter2seconds(30);
          //   let result2 = await doubleAfter2seconds(40);
          //   console.log(result1);
          //   console.log(result2)
          // }

          // testResult();
        sleep(500); // 程序滞留500ms
        console.log(`第${count}次结束 ${getTime.now() - startTime}`); // 显示结束时间
        count += 1;
        console.log("--------------------")
        setTimeout(function(){ce()}, 300);
      }

      ce()

    },
    sync() {
      const Match_folder = 'Local_Data/' + '5' + '/' + '66666' + '/' + 'Match/'

      fs.mkdirSync(Match_folder, { recursive: true})
      fs.mkdirSync(Match_folder, { recursive: true})

      const filename = 'Sent_Initial_Situation.csv';
          
      // temporary data
      let arr =  new Array(5);   
      for(let i = 0;i < arr.length; i++){
        arr[i] = new Array(5);    
      }
      arr[0][1] = "Sponsor Situation File"
      arr[0][2] = 2
      arr = arr.join('\n');

      let res = fs.writeFileSync(Match_folder + filename, arr);
      console.log(res);

      let data = fs.readFileSync(Match_folder + filename, 'utf-8');
      console.log(data.toString());

    },

    delete_all_rows() {
      axios.get('/delete_all_rows/')
        .then((response) => {
        // handle success
        console.log("delete_all_rows", response)
        // console.log(response)
      })
      .catch((error) => {
      })

    },
    
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

    test3() {

      // fs.readFile(Round0_folder + filename, 'utf8' , (err, data) => {
      // })
      // .catch((error) => {
      //  })


          // this.$axios.post('/send_output/', payload)
          //   .then((response) => {
          //   // handle success
          //   console.log("Recipient output finished!!!")
          //   console.log(response)
          // })
          // .catch((error) => {
          // })

          // 测试代码
    //     console.log('main1');

    //     // 该函数仅在 Node.js 环境下可以使用
    //     process.nextTick(function() {
    //         console.log('process.nextTick1');
    //         process.nextTick(function() {
    //             console.log('process.nextTick3');
    //         });
    //     });

    //     setTimeout(function() {
    //         console.log('setTimeout');
    //         process.nextTick(function() {
    //             console.log('process.nextTick2');
    //         });
    //     }, 0);

    //     new Promise(function(resolve, reject) {
    //         console.log('promise');
    //         resolve();
    //     }).then(function() {
    //         console.log('promise then');
    //         Promise.resolve().then(function() {
    //   console.log("Promise resolved again");
    //   Promise.resolve().then(function() {
    //   console.log("Promise resolved again again");
    // });
    // });

          const params= {
                // situation: data_array,
                // initial_rounds: "true",
                // task_id: task_id
                id: 5
              }

          // axios.get('/ceshi/5/?id=5')
          // axios.get('/ceshi/', {params:{id:5}})
          axios.get('/ceshi/', {params})
            .then((response) => {
            // handle success
            console.log("Recipient output finished!!!")
            console.log(response)
          })
          .catch((error) => {
          })




        // });

        console.log('main2');


    },
    test_async() {
      // this.test(true),
      // this.test2(true)
      this.test3(true)
    },
    test4 (){
      for (let i = 0; i < 20000000; i++){
                if(i%100000 == 0){
                  console.log("aaaaaaaaaaaaaaaaaaaaaaa", i)
                }
              }
              let z = 555555;
              setTimeout(function() {
            console.log('setTimeout');
            console.log(z);
            // process.nextTick(function() {
            //     console.log('process.nextTick2');
            // });
        }, 0);
        
    },
    
    test(indicator) {
        if(indicator){

          // function sleep (time) {
          //   return new Promise((resolve) => setTimeout(resolve, time));
          // }

          // // 用法
          // sleep(500).then(() => {
          //     for (let i = 0; i < 20000000; i++){
          //       if(i%100000 == 0){
          //         console.log("aaaaaaaaaaaaaaaaaaaaaaa", i)
          //       }
          //     }
          //     console.log("diyici");
          //     // this.test2();
          // })
        let z = 6666;
          Promise.resolve().then(function() {
          console.log(z);
           console.log("Promise resolved again again");
           Promise.resolve().then(function() {
          console.log(z);
           console.log("Promise resolved again again");
          });
          });
          this.test4();
        console.log("zuihou")
        }
    },

    
    test2(indicator) {
      if(indicator){

        function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }

        // 用法
        sleep(450).then(() => {
            for (let i = 0; i < 20000000; i++){
              if(i%100000 == 0){
                console.log("bbbbbbbbb", i)
              }
            }
            console.log("diyici");
            // this.test2();
        })
      }
    },
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
