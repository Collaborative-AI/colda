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
    <button @click="delete_all_logs()">delete_all_logs</button>
    <button @click="delete_test_rows()">delete_test_rows</button>
    <button @click="try_db()">try_db</button>
    <button @click="python()">python</button>

    <button @click="duqu()">duqu</button>
    <div v-for="task_id in task_id_list" :key="task_id.id">
      {{ task_id }}
      <input type="file" name="csvfile" ref="csvData" />
      <input type="button" @click="csv()" value="JS转换"/>
    </div>
    
    <input type="file" id="ipt" @change="getpath()">
    <button @click="getpath()">get path</button>
    <button @click="sqlite()">sqlite</button>

    <div id="example-4">
      <input type="radio" id="one" value="One" v-model="picked" v-on:change="change()">
      <label for="one">Dont Response to Request</label>
      <br>
      <input type="radio" id="two" value="Two" v-model="picked" v-on:change="change2()">
      <label for="two">Response</label>
      <br>
      <span>Picked: {{ picked }}</span>
    </div>

     <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label for="name">Default Data Path</label>
        <input type="text" v-model="profileForm.default_data_path" class="form-control" id="name" placeholder="">
      </div>
      <div class="form-group">
        <label for="location">Default Id Path</label>
        <input type="text" v-model="profileForm.default_id_path" class="form-control" id="location" placeholder="">
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>

    <!-- <div>
      <el-form ref="form" :model="form" label-width="120px" style="width: 50%">
      <el-form-item label="保存至文件夹">
        <input type="file" id="file" hidden @change="fileChange" webkitdirectory>
        <el-input placeholder="请输入内容" v-model="form.imgSavePath" class="input-with-select">
          <el-button slot="append" icon="el-icon-folder" type="success" @click="btnChange"></el-button>
        </el-input>
      </el-form-item>
    </el-form>
    </div> -->
    <button id="selectFile" @click="get_default_file_path()">选择文件</button>
    {{ xinxi }}

    <button @click="test_path()">测试路径</button>
  </div>
</template>


<script>
//const { require } = window

// node electron
const fs = window.require('fs');

// const xlsx2json = window.require("node-xlsx");
const join = window.require('path').join;
const address = 'tem/' + 'b/'
const os = window.require('os');
// const ex = require("child_process").execFileSync;
const ex = window.require("child_process");
// import dialog from 'electron';
// const dialog = window.nodeRequire('electron');
// const dialog1 = require('electron');
// import dialog from 'electron';
const sqlite3 = window.require('sqlite3').verbose();
const node_path = window.require('path');

// import $ from 'jquery'

// const remote = window.require('electron').remote 
// const dialog = remote.dialog;

const {dialog} = window.require('electron').remote

// const dialog = window.require('electron')
// const { require } = window
// const fs = require('fs')
// const path = require('path');
// Encapsulated network request
// import {request} from '@/network/request';
// import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';
const axios = require('axios').default
// import axios from 'axios'
// import csv2arr from '@/assets/csv-arr'
// import db from '../db.js'
const db = require('../db.js').default
const store = require('../store').default
// import store from '../store'
// import sq3 from 'sqlite3'
// import fse from 'fs-extra';
// import path from 'path';
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
      success: 0,
      form: {
        imgSavePath: ''
      },
      sharedState: store.state,
      picked: "One",
      profileForm: {
        default_data_path: "",
        default_id_path: "",
      },
      xinxi: '',
      root: '',
      exe_position: '',
    };
  },

  mounted() {
    // this.$socket.connect();
    
  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
    this.changeroot()
  },
  methods: {
    changeroot() {
      
      const isDevelopment = process.env.NODE_ENV !== 'production';
      if (os.type() == "Linux"){
        if (isDevelopment == true){
          this.root = node_path.resolve("./exp")
          this.exe_position = node_path.resolve("./dist/run/run")
        }else{
          // this.root = node_path.join(__dirname, '../exp')
          this.root = node_path.join(__dirname, '../../../apollo_exp')
          this.exe_position = node_path.join(__dirname, '../dist/run/run')
        }
    
      }else if (os.type() == "Darwin") {
        if (isDevelopment == true){
          this.root = node_path.resolve("./exp")
          this.exe_position = node_path.resolve("./dist/run/run")
        }else{
          this.root = node_path.resolve("./resources/exp")
          this.exe_position = node_path.resolve("./resources/dist/run/run")
        }

      }else if (os.type() == "Windows_NT") {
        if (isDevelopment == true){
          this.root = node_path.resolve("./exp")
          this.exe_position = node_path.resolve("./dist/run/run.exe")
        }else{
          this.root = node_path.resolve("./resources/exp")
          this.exe_position = node_path.resolve("./resources/dist/run/run.exe")
        }
      }
    },
    test_path() {
      const isDevelopment = process.env.NODE_ENV !== 'production';
      console.log("isDevelopment", isDevelopment)
      console.log("))))))))))))))))))))))")
      console.log("dirname", __dirname)
      let dist_path = node_path.join(__dirname, '../dist')
      console.log("dirname2", dist_path)
      console.log("this.root", this.root)
      console.log("this.exe", this.exe_position)
      // let lujing ='C:/Users/Lucky/Desktop/Apolll/Application/flaskvue/frontend/client/node_modules/electron/dist/resources/electron.asar/renderer/../../../../../../exp/1/task/75925eee-9e2c-4f43-b1d5-d2d94c09512d/train/id/1.csv'
      let lujing = __dirname + "/../../../../"
      console.log(typeof(lujing), lujing)
      // lujing = lujing.split(path.sep).join('/')
      // console.log(lujing)

      // let a = fs.readFileSync(lujing, {encoding:'utf8', flag:'r'});
      // console.log(a)
      console.log("os", os.type())
      let lujing1 = node_path.resolve("./dist")
      console.log(lujing1)

      lujing = node_path.resolve("./dist/run")
      console.log("path.resolve", lujing)
     
      fs.readdir(dist_path,function(err,files){
      if(err){
        return console.error(err);
      }
      files.forEach(function(file){
        console.info(file);
      });
});
    
    },
    get_default_file_path() {
      // console.log("aaaa")
      // let result = dialog.showOpenDialogSync({
      //   // 选择文件, 隐藏文件也显示出来
      //   properties: ['openFile'],
      //   // 后缀为html, js, json, md其中之一
      //   filters: [{
      //     name: 'Text', 
      //     extensions: ['html', 'js', 'json', 'md', 'csv'] 
      //   }]
      // })
      // console.log("result", result)
      // if (result === undefined){
      //   console.log("wu")
      // }
      // console.log("1")
      console.log("1",$)
      console.log("2", ceshi)
      console.log("3", ceshi2)
      // function(filenames) {
      //   console.log("jieguo");
      //   // filenames是一个数组, 每一项为选择的文件的绝对路径
      //   let firstFile = filenames[0];
      //   console.log(firstFile);
      //   fileContentEle = document.getElementById('fileContent');

      //   if (firstFile) {
      //     fs.readFile(firstFile, 'utf8', function(err, data) {
      //       if (err) {
      //         // 如果读取错误, 弹出错误提示窗口
      //         dialog.showErrorBox('error', `read ${firstFile} error`);
      //         return;
      //       }

      //       // fileContentEle.innerText = data;
      //       this.xinxi = data
      //     });
      //   } else {
      //     fileContentEle.innerText = 'no file selected';
      //   }
      // };

    },


    getUser (id) {
      let vm = this
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
        console.log(row)

        if (row != null){
          vm.profileForm.default_data_path = row.default_data_path
          vm.profileForm.default_id_path = row.default_id_path
        }

        if (row == null){
          console.log("get false")
          vm.sharedState.set_default = false
          vm.sharedState.receive_request = false
        }else{
            if (row.default_data_path == "" | row.default_id_path == ""){
            console.log("get false")
            vm.sharedState.set_default = false
            vm.sharedState.receive_request = false
          }
        }
        
      })
    },
      getpath() {
          // let ipt = document.getElementById('ipt').files
          // console.log("1", ipt);
          // ipt = ipt[0];
          // console.log("2", ipt);

          // dialog.showOpenDialogSync(mainWindow, {
          //   properties: ['openFile', 'openDirectory']
          // })
          // console.log(dialog.showOpenDialog({
          //   properties: ['openFile', 'openDirectory', 'multiSelections']
          // }));
          // console.log(dialog)
          console.log("1",this.sharedState.set_default)
          // console.log(db)
          // console.log(window)
          // console.log("fs", fs)
          // // console.log("dialog", dialog)
          // console.log(require.resolve('electron'));
          // // console.log("window electron", console.log(dialog.showOpenDialog({ properties: [ 'openFile', 'openDirectory', 'multiSelections' ]})))
          // dialog.showOpenDialog({ 
          //   // 不能同时设置openFile openDirectory => 否则只能打开文件夹
          //   // properties: [ 'openFile', 'openDirectory', 'multiSelections' ]
          //   properties: [ 'openFile' ]
          // }).then(result => {
          //   console.log("result")
          //   console.log(result.canceled)
          //   console.log(result.filePaths)
          // }).catch(err => {
          //   console.log("error", err)
          // })
          // console.log("daole")
          // console.log("electron", require('electron'))
          // console.log((process && process.type === 'renderer'))
          // console.log(require('is-electron-renderer'))
          // console.log(window.require('is-electron-renderer'))

          // const a = require('electron')
          // console.log(a)
          // console.log("dialog1", dialog1.showOpenDialog)
          // console.log(this.$electron.remote.dialog.showOpenDialog({properties: ['openFile', 'openDirectory', 'multiSelections']}))
          
          // let stats=fs.statSync(ipt.path);
          // if (stats.isDirectory() == false){
          //   alert("please choose file");
          // }else{
          //   console.log(ipt);
          // }
          // let path = dialog.showOpenDialog({
          //   properties:['openDirectory']
          // })
          // console.log(path)
      },
      change() {
        console.log("change")
        this.sharedState.receive_request = false
      },
      change2() {
        console.log("change2")
        if (this.picked == "Two"){
          console.log("ainiaini")
        }
        let vm = this
        let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
        db.get(select_sentence, function(err, row){
          console.log(row)

          if (row == null | row.default_data_path == "" | row.default_id_path == "" ){
            console.log("get false")
            vm.sharedState.set_default = false
            vm.sharedState.receive_request = false
            vm.$toasted.success('Please Fill the Default Setting', { icon: 'fingerprint' })
            vm.picked = "One";
            console.log(this.picked)
          }
          else{
            vm.sharedState.receive_request = true
          }
          
        })
      },
      onSubmit (e) {

        let vm = this;
        let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;

        db.get(select_sentence, function(err, row){
          console.log(row)
          
          
          if (row == null){
            // db.run(`INSERT INTO "User_Default_Path"("user_id", "default_data_path", "default_id_path") VALUES (1, 'love', 'consume')`)
            let insert_new_val = `INSERT INTO "User_Default_Path"("user_id", "default_data_path", "default_id_path") VALUES 
              (`+vm.sharedState.user_id+`, "`+vm.profileForm.default_data_path+`", "`+vm.profileForm.default_id_path+`")`
            console.log(insert_new_val)
            db.run(insert_new_val)
          }else{

            if (vm.profileForm.default_data_path == "" | vm.profileForm.default_id_path == "" ){
              vm.sharedState.set_default = false
              vm.sharedState.receive_request = false
              console.log("false")
            }

            db.serialize(function() {
            let update_default_data_path = 'UPDATE "User_Default_Path"'
                      +' SET "default_data_path" = "' + vm.profileForm.default_data_path
                       + '" WHERE "user_id" = ' + vm.sharedState.user_id
            console.log(update_default_data_path)           
            db.run(update_default_data_path)

            let update_default_id_path = 'UPDATE "User_Default_Path"'
                      +' SET "default_id_path" = "' + vm.profileForm.default_id_path
                       + '" WHERE "user_id" = ' + vm.sharedState.user_id
            console.log(update_default_id_path)
            db.run(update_default_id_path)

          });

          }
          
        })
        
      },
      python(){

        // fs.mkdirSync(Round_folder, { recursive: true})
          let save_match_id_file_pos = null;
          try{
            // import ("../../../../../../Algorithm/package")
            // save_match_id_file_pos = ex.execSync('./dist/run/run make_test --root ../../../../../../Algorithm/package/exp --self_id 0 --task_id abc --test_id def --round 1 --data_path /home/qile/Documents/Apollo/package/data/BostonHousing/2/123/1.0/0/test/data.csv', {encoding: 'utf8'})
            let a = ex.execSync('./dist/run/run make_hash --id_path ./data/BostonHousing/2/123/1.0/0/all/id.csv --root ./exp --self_id 0 --mode default', {encoding: 'utf8'})
            console.log(a, typeof(a))
            

          }catch(err){
            console.log(err)
          }

          // delete "\n"

          // '../../../package'
          // ' + this.root + '
          // save_match_id_file_pos = save_match_id_file_pos.replace(/\n/g, '')
          // let save_match_id_file_pos_list = save_match_id_file_pos.split('?')
          // console.log(save_match_id_file_pos_list)

          // let all_data = []
          // for (let i = 0; i < save_match_id_file_pos_list.length; i++){

          //   let cur_file = save_match_id_file_pos_list[i];
          //   // let gain = save_match_id_file_pos_list[i];
          //   // gain = gain.split("/")
          //   // console.log(gain)
          //   // let random = gain[gain.length-1].split(".")[0]
          //   // console.log(random)

          //   let save_match_id_file_pos_data = fs.readFileSync(cur_file, {encoding:'utf8', flag:'r'});
          //   console.log("not splite", save_match_id_file_pos_data)
          //   let save_match_id_file_pos_data_array = save_match_id_file_pos_data.split("\n")
          //   console.log(save_match_id_file_pos_data_array)
          //   all_data.push(save_match_id_file_pos_data_array)
          // }
          // console.log(all_data)

          // // 读取是每行(列数多则加,号)，会变为string， 去\n
          // // splite后多行为array, 读多个文件为二维矩阵

          // // 写入时要join('\n'), 变单个array为string

          // let ceshi1 = './ceshi1.csv'
          // let ceshi2 = './ceshi2.csv'
          // let all_data1 = [];
          // let ceshi1_data = fs.readFileSync(ceshi1, {encoding:'utf8', flag:'r'})
          // console.log("ceshi1_data", ceshi1_data)
          // let ceshi2_data = fs.readFileSync(ceshi2, {encoding:'utf8', flag:'r'})
          // console.log("ceshi2_data", ceshi2_data)

          // let ceshi1_data_array = ceshi1_data.split("\n")
          // console.log("ceshi1_data_array", ceshi1_data_array)
          // let ceshi2_data_array = ceshi2_data.split("\n")
          // console.log("ceshi2_data_array", ceshi2_data_array)

          // all_data1.push(ceshi1_data)
          // all_data1.push(ceshi2_data)
          // console.log(all_data1)
          // fs.writeFileSync("./ceshi3.csv", all_data1[0])
          

          
      },

    // fs.mkdirSync(assistor_data_folder, { recursive: true})
      try_db() {
        // let db = new sqlite3.Database(':memory:');

        // db.serialize(function() {
        // db.run("CREATE TABLE lorem (info TEXT)");

        // let stmt = db.prepare("INSERT INTO lorem VALUES (?)");
        // for (var i = 0; i < 10; i++) {
        //   stmt.run("Ipsum " + i);
        // }

        // stmt.finalize();

        //   let rows = document.getElementById("database");
        //   db.each("SELECT rowid AS id, info FROM lorem", function(err, row) {
        //     let item = document.createElement("li");
        //     item.textContent = "" + row.id + ": " + row.info;
        //     rows.appendChild(item);
        //   });
        // });

        // db.close();
        // var db = new sqlite3.Database('Apollo_Client');

        // db.serialize(function() {
        //   // db.run("CREATE TABLE user (id INT, dt TEXT)");
        //   // db.run("CREATE TABLE IF NOT EXISTS user (id INT, dt TEXT)")
        //   db.run("CREATE TABLE IF NOT EXISTS User (id int primary key not null, user_id int, default_data_path text, default_id_path text)")
        //   // var stmt = db.prepare("INSERT INTO user VALUES (?,?)");
        //   // for (var i = 0; i < 10; i++) {
          
        //   // var d = new Date();
        //   // var n = d.toLocaleTimeString();
        //   // stmt.run(i, n);
        //   // }
        //   // stmt.finalize();

        //   // db.each("SELECT id, dt FROM user", function(err, row) {
        //   //     console.log("User id : "+row.id, row.dt);
        //   // });
        // });

        // db.close();
        db.run(`INSERT INTO "User_Default_Path"("user_id", "default_data_path", "default_id_path") VALUES (1, 'love', 'consume')`)
        let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + 1;
        db.get(select_sentence, function(err, row){
          console.log(row)
          if (row == null){
            console.log("no")
          }
        })
        // console.log(a)

      },
         

//       sqlite(){
//         const dbPath = path.join("/home/qile/Documents/Apollo/flaskvue/frontend/client/sqlite"
// , 'data.sqlite3');
//         fse.ensureFileSync(dbPath);

//         const sqlite3 = sq3.verbose();
//         const db = new sqlite3.Database(dbPath);
//         db.serialize(() => {
//           /**
//            * 物品表 GOODS
//            * name 品名
//            * standard_buy_unit_price 标准进价
//            * standard_sell_unit_price 标准售价
//            * total_amount 总金额
//            * total_count 总数量
//            * remark 备注
//            * create_time 创建时间
//            * update_time 修改时间
//            */
//           db.run(`CREATE TABLE GOODS(
//             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
//             name VARCHAR(255) NOT NULL,
//             standard_buy_unit_price DECIMAL(15,2) NOT NULL,
//             standard_sell_unit_price DECIMAL(15,2) NOT NULL,
//             total_amount DECIMAL(15,2) NOT NULL,
//             total_count DECIMAL(15,3) NOT NULL,
//             remark VARCHAR(255) NOT NULL,
//             create_time INTEGER NOT NULL,
//             update_time INTEGER NOT NULL
//             )`, err => {
//             console.log(err);
//           });

//           /**
//            * 进出明细表 GOODS_DETAIL_LIST
//            * goods_id 物品id
//            * count 计数（+加 -减）
//            * actual_buy_unit_price 实际进价
//            * actual_sell_unit_price 实际售价
//            * amount 实际金额
//            * remark 备注
//            * latest 是否某物品最新一条记录（不是最新操作无法删除）（1是 0不是）
//            * create_time 创建时间
//            * update_time 修改时间
//            */
//           db.run(`CREATE TABLE GOODS_DETAIL_LIST(
//             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
//             goods_id INTEGER NOT NULL, 
//             count DECIMAL(15,3) NOT NULL,
//             actual_sell_unit_price DECIMAL(15,2) NOT NULL,
//             actual_buy_unit_price DECIMAL(15,2) NOT NULL,
//             amount DECIMAL(15,2) NOT NULL,
//             remark VARCHAR(255) NOT NULL,
//             latest INTEGER NOT NULL,
//             create_time INTEGER NOT NULL,
//             update_time INTEGER NOT NULL,
//             FOREIGN KEY (goods_id) REFERENCES GOODS(id)
//             )`, err => {
//             console.log(err);
//           });
//         });
//       },


    delete_test_rows() {
      axios.get('/delete_test_rows/')
        .then((response) => {
        // handle success
        console.log("delete_test_rows", response)
        // console.log(response)
      })
      .catch((error) => {
      })

    },
    duqu(){
      // function findSync(startPath) {
      //   let result=[];
      //   function finder(path) {
      //       let files=fs.readdirSync(path);
      //       files.forEach((val,index) => {
      //           let fPath=join(path,val);
      //           let stats=fs.statSync(fPath);
      //           console.log("val", val)
      //           console.log("stats", fPath, stats)
      //           if(stats.isDirectory()) finder(fPath);
      //           if(stats.isFile()&&val=="Sponsor_Trained_Local_Model.csv") {
      //             // result.push(fPath);
      //             let data = fs.readFileSync(fPath,
      //               {encoding:'utf8', flag:'r'});
      //             result.push(data);
      //           }
      //       });

      //   }
      //   finder(startPath);
      //   return result;
      // }
      
      // let fileNames=findSync('Local_Data/4/7cb0e4af-1736-4717-a809-5772c08a1603');
      // for (let i = 0;i < fileNames.length; i++){
      //   console.log(fileNames[i]);
      // }

      // const route = "Local_Data/4/a4ddab0b-79a6-483b-a894-280f01cbd0af/Log.txt"
      // try {
      //   const data = fs.appendFileSync(route, "1.22222\n")
      //   console.log("data", data)
      //   fs.appendFileSync(route, "3.22222\n")
      //   fs.appendFileSync(route, "4.@@@@\n")
      //   //文件写入成功。

      //   const data1 = fs.readFileSync(route,
      //     {encoding:'utf8', flag:'r'});
        
      //   console.log("data", data1, data1.split("\n"))
      // } catch (err) {
      //   console.error(err)
      // }

      // try {
      //   route = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Log.txt'
      //   fs.appendFileSync(route, "1.22222\n")
      // } catch (err) {
      //   console.error(err)
      // }
      try{
        let save_match_id_file_pos = ex.execSync('python3 ../../../package/save_match_id.py --self_id ' + this.sharedState.user_id 
          + ' --task_id '+ 2 + ' --from_id ' + 1 + ' --run train', {encoding: 'utf8'})
        console.log(save_match_id_file_pos)
        console.log(save_match_id_file_pos.split("\n"))
      }catch{
        console.log("wrong")
      }

    },
    

    delete_all_logs() {
      this.$store.state.msg = [];



    },
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
        let stdout = ex.execSync('python3 ../../../algorithm/make_dataset.py --num_users 2', {encoding: 'utf8'})
        // let stdout = ex.execSync('python ../../../algorithm/hello.py', {encoding: 'utf8'})

        console.log(stdout.split("\n"))
      }catch{
        console.log("wrong")
      }

      // const a = [];
      // a.push("11")
      // console.log(a)

      // let b = [];
      // b.push("2")
      // console.log(b)

      


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
