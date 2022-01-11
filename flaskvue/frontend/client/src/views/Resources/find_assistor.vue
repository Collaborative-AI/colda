
<template>

  <div class="container g-pt-20">
    <div class="form-group">
      <label for="name">Input Task Name</label>
      <input type="text" v-model="task_name" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input Task Description</label>
      <input type="text" v-model="task_description" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input Assistor username (eg. testa, testb)</label>
      <input type="text" v-model="assistor_username_list" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Select File</label>
      <input type="text" v-model="train_file_path" class="form-control" id="name" placeholder="">
      <button class="btn btn-success" @click="get_train_file_path()">Select File</button>
    </div>
    <div style="overflow:auto">
    <table class="table" v-if="select_data">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col" v-for="(ptitle, idx) in ptitles" :key="ptitle.index">{{idx+1}}.{{ptitle}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(pdata,idx) in pdatas" :key="pdata.index">
          <th scope="row">{{idx+1}}</th>
          <td v-for="pd in pdata" :key="pd.index">{{pd}}</td>
        </tr>
        
      </tbody>
    </table>
    </div>
    <!-- <div>{{pdatas[0]}}</div> -->

    <div class="form-group">
      <label for="name">Input ID Column</label>
      <input type="text" v-model="train_id_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input Data Column (eg. 3-6)</label>
      <input type="text" v-model="train_data_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input Target Column</label>
      <input type="text" v-model="train_target_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
    <label for="name">Select Task Mode</label>
    &nbsp;
    <select v-model='task_mode' @change='get_model_name' class="form-control">
      <option v-for="item in task_mode_list" :key="item.index" :value="item.name">{{item.name}}</option>
    </select>
    <br>
    <label for="name">Select Model Name</label>
    &nbsp;
    <select v-model="model_name" @change='get_metric_name' class="form-control">
      <option v-for="item in model_name_list" :key="item.index" :value="item.name">{{item.name}}</option>
    </select>
    <!-- &nbsp; -->
    <br>
    <label for="name">Select Metric Name</label>
    &nbsp;
    <select v-model="metric_name" class="form-control">
      <option v-for="item in metric_name_list"  :key="item.index" :value="item.name">{{item.name}}</option>
    </select>


    </div>
    

    
    


    <button type="submit" @click="onSubmit()" class="btn btn-success">Initiate task</button>
    <!-- <button v-show="isSponsor" class="btn btn-success float-right">Call For Test</button> -->
  </div>
</template>



<script>
import { config } from 'process';
import store from '../../store.js'
import { execute_unittest_list, generate_unittest_parameters, generate_message_string, Log, sqlite3_run, change_db_param_to_string } from '../../utils.js'

import { ex,fs,os,node_path,dialog,log } from '../../import_package.js'


// const fs = window.fs ? window.fs : require('fs');
// const ex = window.ex ? window.ex : require('child_process');
// const node_path = window.node_path ? window.node_path : require('path');
// const os = window.os ? window.os : require('os');
// const dialog = window.dialog ? window.dialog : require('electron');
// const store = require('../../store').defaultv
// const $ = require('jquery')

export default {
  name: 'Find_Assistor',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      task_id: "",
      task_name: "",
      task_description: "",
      train_file_path: "",
      train_id_column: "",
      train_data_column: "",
      train_target_column:"",
      assistor_username_list:"",
      task_mode: '',
      model_name: '',
      metric_name: '',
      ptitles:"",
      pdatas:"",
      select_data:false,
      root: '',
      exe_position: '',
      task_mode_list: [
        {
            name: "classification",
            sub: 
            [
              {
                  name: "linear",
                  sub: [{ name: "Accuracy_F1" }],
              },
            ],   
        },
        {
            name: "regression",
            sub: 
            [
              {
                  name: "linear",
                  sub: [{ name: "MAD_RMSE_R2" }],
              },
            ],   
        },
      ],
      model_name_list:[],
      metric_name_list:[],
    }
  },
  methods: {

     ceshi(unittest_callbacks){
      let vm = this

      
      // let insert_sentence = `INSERT INTO "User_Sponsor_Table"("task_name", "task_description", "user_id", "test_indicator", "task_id", "train_file_path", "train_id_column", "train_data_column", "train_target_column", "task_mode", "model_name", "metric_name") VALUES 
      //         (`+`"`+vm.task_name +`", "`+vm.task_description+`", "`+vm.sharedState.user_id+ `","train","`+vm.task_id+`", "`+vm.train_file_path+`", "`+vm.train_id_column+`", "`+vm.train_data_column+`", "`+vm.train_target_column+`", "`+vm.task_mode+`", "`+vm.model_name+`", "`+vm.metric_name+`")`
      let sentence = `INSERT INTO "User_Sponsor_Table"("task_name", "task_description", "user_id", "test_indicator", "task_id", "train_file_path",`+
                      ` "train_id_column", "train_data_column", "train_target_column", "task_mode", "model_name", "metric_name") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
      let param = [vm.task_name, vm.task_description, vm.sharedState.user_id, "train",
                    vm.task_id, vm.train_file_path, vm.train_id_column, vm.train_data_column, 
                    vm.train_target_column, vm.task_mode, vm.model_name, vm.metric_name]
      // sqlite3_run(sentence, change_db_param_to_string(param))
      //       .then(function(response) {
      //          console.log('shuchu response', response)
      //                       let unittest_parameters = generate_unittest_parameters(vm.train_file_path, vm.train_id_column, vm.train_data_column, vm.train_target_column)
      //         execute_unittest_list(unittest_callbacks, 0, "find_assistor_unittest", unittest_parameters)

      //         vm.$axios.get('/changshi/')
      //           .then((response) => {
      //             let res = response.data

      //             let unittest_parameters = generate_unittest_parameters(res)
      //             execute_unittest_list(unittest_callbacks, 1, "find_assistor_unittest", unittest_parameters)
      //             // console.log("task_id))))))))))))))00", this.task_id)
      //           })
      //           .catch((error) => {
      //             console.log(error)
      //           })
      //       }).catch(function(error) {
      //         // 处理 getJSON 和 前一个回调函数运行时发生的错误
      //         console.log('发生错误！', error);
      //       });

             


            // })
      vm.$db.run(sentence, change_db_param_to_string(param), function(err) {
              if (err) {
                return console.log(err.message);
              }
              // get the last insert id
              console.log(`A row has been inserted with rowid`);

              let unittest_parameters = generate_unittest_parameters(vm.train_file_path, vm.train_id_column, vm.train_data_column, vm.train_target_column)
              execute_unittest_list(unittest_callbacks, 0, "find_assistor_unittest", unittest_parameters)

              vm.$axios.get('/changshi/')
                .then((response) => {
                  let res = response.data

                  let unittest_parameters = generate_unittest_parameters(res)
                  execute_unittest_list(unittest_callbacks, 1, "find_assistor_unittest", unittest_parameters)
                  // console.log("task_id))))))))))))))00", this.task_id)
                })
                .catch((error) => {
                  console.log(error)
                })


                    });

      // console.log("insert_sentence", insert_sentence) 
      // vm.$db.run(insert_sentence, function(err){
      // if (err){
      //   console.log(err);
      // }

      // let unittest_parameters = generate_unittest_parameters(vm.train_file_path, vm.train_id_column, vm.train_data_column, vm.train_target_column)
      // execute_unittest_list(unittest_callbacks, 0, "find_assistor_unittest", unittest_parameters)

      // this.$axios.get('/changshi/')
      //   .then((response) => {
      //     let res = response.data

      //     let unittest_parameters = generate_unittest_parameters(res)
      //     execute_unittest_list(unittest_callbacks, 1, "find_assistor_unittest", unittest_parameters)
      //     // console.log("task_id))))))))))))))00", this.task_id)
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })

      // // console.log('print row', row)
      // })
    },
    get_model_name() {
      for (let i = 0; i < this.task_mode_list.length; i++) {
        let obj = this.task_mode_list[i]
        if (this.task_mode == obj.name ) {
          this.model_name_list = obj.sub
        }
      }
      this.model_name=''
      this.metric_name=''
    },
    get_metric_name() {
      for (let i = 0; i < this.model_name_list.length; i++) {
        let obj = this.model_name_list[i]
        if (this.model_name == obj.name ) {
          this.metric_name_list = obj.sub
        }
      }
    },
    get_train_id (unittest_callbacks) {
      // console.log("$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
      this.$axios.get('/create_new_train_task/')
        .then((response) => {
          this.task_id = response.data.task_id

          let unittest_parameters = generate_unittest_parameters(this.task_id)
          execute_unittest_list(unittest_callbacks, 0, "find_assistor_unittest", unittest_parameters)
          // console.log("task_id))))))))))))))00", this.task_id)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    get_train_file_path() {
      let vm=this
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_file_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.train_file_path = path
          fs.readFile(path, 'utf8' , (err, data) => {
            if (err) {
              console.log('err info',err);
              return
            }
            
            // data = data.split("\r\n")
            // for (let i of data) { data[i] = data[i].split(",") }
            // vm.pdatas=data
            // console.log('preview',vm.pdatas[0][0])
            
            vm.pdatas = data.split("\n")
            for (let i in vm.pdatas) { vm.pdatas[i] = vm.pdatas[i].split(",")} 
            vm.ptitles=vm.pdatas[0]
            vm.pdatas=vm.pdatas.slice(1,4)
            vm.select_data=true
            console.log('preview',vm.pdatas[0])
          })
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  

      }
    },
    get_train_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_data_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  

      }
    },
    get_train_id_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_id_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_id_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
          console.log('Please Select A Train ID File')
        }  

      }
    },
    get_train_target_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_Target_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_target_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
          console.log('Please Select A Train Target File')
        }  

      }
    },

    handle_Algorithm_return_value(name, return_val, first_val, second_val) {
      console.log(name, return_val)
      // check if return_val obeys the correct return value
      if (first_val != null){
        if (return_val[0] != first_val){
          return false
        }
      }
      if (second_val != null){
         if (return_val[1] != second_val){
           return false
         }
      }  
      return true
    },

   

    onSubmit (unittest_callbacks) {
      
      console.log("this.root, this.exe_position", this.root, this.exe_position)
      let vm = this;
      // log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), this.task_id.toString(), 'log.txt');
      Log('sponsor ceshi', 'info')
      console.log('sponsor ceshi1', unittest_callbacks)
      if (this.assistor_username_list == ""){
        dialog.showErrorBox('Please Type in the Assistor Username', 'Thank you very much')
      }else if (this.task_id == ""){
        dialog.showErrorBox('Please Type in the Paths Again', 'We apologize for the latency')
      }else{
        
        let both_path_validation = true
        // if (vm.PathForm.train_data_path == ""){
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
        // }
        try {
          fs.statSync(vm.train_file_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
          both_path_validation = false
        }

        // try {
        //   fs.statSync(vm.PathForm.train_id_path);
        // } catch (err) {
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
        //   console.log('Please Select A Train ID File')
        //   both_path_validation = false
        // }

        // try {
        //   fs.statSync(vm.PathForm.train_target_path);
        // } catch (err) {
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
        //   console.log('Please Select A Train Target File')
        //   both_path_validation = false
        // }
        
        if(both_path_validation == true){
        
          console.log("true")
          
          console.log(vm.train_file_path)
          
          let sentence = `INSERT INTO "User_Sponsor_Table"("task_name", "task_description", "user_id", "test_indicator", "task_id", "train_file_path",`+
                      ` "train_id_column", "train_data_column", "train_target_column", "task_mode", "model_name", "metric_name") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          let param = [vm.task_name, vm.task_description, vm.sharedState.user_id, "train",
                    vm.task_id, vm.train_file_path, vm.train_id_column, vm.train_data_column, 
                    vm.train_target_column, vm.task_mode, vm.model_name, vm.metric_name]
          

          // let insert_sentence = `INSERT INTO "User_Sponsor_Table"("task_name", "task_description", "user_id", "test_indicator", "task_id", "train_file_path", "train_id_column", "train_data_column", "train_target_column", "task_mode", "model_name", "metric_name") VALUES 
          //     (`+`"`+vm.task_name +`", "`+vm.task_description+`", "`+vm.sharedState.user_id+ `","train","`+vm.task_id+`", "`+vm.train_file_path+`", "`+vm.train_id_column+`", "`+vm.train_data_column+`", "`+vm.train_target_column+`", "`+vm.task_mode+`", "`+vm.model_name+`", "`+vm.metric_name+`")`

          // console.log("insert_sentence", insert_sentence) 
          vm.$db.run(sentence, change_db_param_to_string(param), function(err){
            if (err){
              console.log('err info',err);
            }
          // const stmt = vm.$db.prepare('INSERT INTO User_Sponsor_Table VALUES' +
          // ' ( @task_name, @task_description, @user_id, @test_indicator, @task_id, @test_id, @train_file_path,' +
          // ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
          // ' @test_data_column, @test_target_column, @task_mode, @model_name, @metric_name)');
             
          // stmt.run({
          //   task_name: vm.task_name, 
          //   task_description: vm.task_description, 
          //   user_id: vm.sharedState.user_id, 
          //   test_indicator: "train", 
          //   task_id: vm.task_id,
          //   test_id: '',
          //   train_file_path: vm.train_file_path, 
          //   train_id_column: vm.train_id_column, 
          //   train_data_column: vm.train_data_column, 
          //   train_target_column: vm.train_target_column, 
          //   test_file_path: '',
          //   test_id_column: '',
          //   test_data_column: '',
          //   test_target_column: '',
          //   task_mode: vm.task_mode, 
          //   model_name: vm.model_name,
          //   metric_name: vm.metric_name
          // });
          console.log('daozhele')
          // test if the sqlite db stores the aboving values
          let unittest_parameters = generate_unittest_parameters(vm.train_file_path, vm.train_id_column, vm.train_data_column, vm.train_target_column)
          console.log('dachu3', unittest_parameters,unittest_callbacks)
          execute_unittest_list(unittest_callbacks, 0, "find_assistor_unittest", unittest_parameters)

          // let match_id_address = vm.PathForm.train_id_path
          let hash_id_file_address = null;
          try{   
            
            // call make_hash to convert id to sha-256 id
            console.log("vm.exe_position", vm.exe_position)
            hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                    + ' --task_id ' + vm.task_id + ' --mode train' + ' --dataset_path ' + vm.train_file_path 
                                    + ' --id_idx ' + vm.train_id_column, {encoding: 'utf8'})

            console.log("hash_id_file_address", hash_id_file_address)
            hash_id_file_address = hash_id_file_address.split("?")
            console.log("hash_id_file_address_2", hash_id_file_address)
            if (hash_id_file_address[0] == "300" && hash_id_file_address[1] == "make_hash" && hash_id_file_address[2] == "not valid mode"){
              vm.$toasted.success(`not valid mode, please select again`, { icon: 'fingerprint' })
              return
            }
            if (hash_id_file_address[0] != "200" || hash_id_file_address[1] != "make_hash"){
              vm.$toasted.success(`find assistor went wrong, please try again`, { icon: 'fingerprint' })
              console.log("make hash wrong")
              return 
            }
          }catch(err){
            console.log(err)
          }

          let hash_id_file_data = null
          try{
            hash_id_file_data = fs.readFileSync(hash_id_file_address[2], {encoding:'utf8', flag:'r'});
            // console.log("hash_id_file_data", hash_id_file_data)
          } catch (err) {
            console.log(err)
          }
          
          
          let user_id = vm.sharedState.user_id
          const Log_address = node_path.join(vm.root.toString(), user_id.toString(), "task", vm.task_id.toString(), "train", "log.txt")
          
          let assistor_username_list = vm.assistor_username_list.split(",")
          console.log(assistor_username_list,"assistor_username_list")
          const find_assistor_data = {
            assistor_username_list: assistor_username_list,
            id_file: hash_id_file_data,
            task_id: vm.task_id,
            task_name: vm.task_name,
            task_mode: vm.task_mode,
            model_name: vm.model_name,
            metric_name: vm.metric_name,
            task_description: vm.task_description,
          }
          // console.log('fins_assistor_data', find_assistor_data)

          vm.$axios.post('/find_assistor', find_assistor_data)
          .then((response) => {
            // console.log('response!!', response.data)
            if (response.data == "wrong username"){
              // console.log("Username Wrong", response)
              console.log('user_name_wrong')
              vm.$toasted.success(`Username Wrong. Please start a new task"`, { icon: 'fingerprint' })
              fs.appendFileSync(Log_address, "Username Wrong. Please start a new task")
              return
            }

            let unittest_parameters = generate_unittest_parameters(response.data)
            execute_unittest_list(unittest_callbacks, 1, "find_assistor_unittest", unittest_parameters)

            console.log("node_path_log", Log_address)
            if(!fs.existsSync(Log_address)){
              console.log("creating log.txt");
              fs.openSync(Log_address, "w");
              console.log("log.txt created");
            }
            // handle success
            vm.$toasted.success(`Training Starts`, { icon: 'fingerprint' })

            Log(generate_message_string("\nYou are SPONSOR\n"), 'info')
            Log(generate_message_string("Task ID: " + vm.task_id + "\n"), 'info')
            Log(generate_message_string("Training Stage Starts\n"), 'info')
            Log(generate_message_string("1.0 Find Assistor\n"), 'info')
            Log(generate_message_string("1.1 Sponsor calls for help\n"), 'info')
            Log(generate_message_string("1.2 Sponsor sends id file\n"), 'info')
            Log(generate_message_string("1.3 Find Assistor Done\n"), 'info')

            try {
              fs.appendFileSync(Log_address, "\n You are SPONSOR\n")
              fs.appendFileSync(Log_address, "Task ID: " + vm.task_id + "\n")
              fs.appendFileSync(Log_address, "---- Train Stage Starts\n")
              fs.appendFileSync(Log_address, "---- 1. Find assistor\n")
              fs.appendFileSync(Log_address, "1.1 Sponsor calls for help\n")
              fs.appendFileSync(Log_address, "1.2 Sponsor sends id file\n")
              fs.appendFileSync(Log_address, "---- 1. Find assistor Done\n")
            } catch (err) {
              console.log(err)
            }
            let make_train_local = null;

            try{   
              make_train_local = ex.execSync(vm.exe_position + ' make_train_local --root  ' + vm.root
                                      + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id 
                                      + ' --dataset_path ' + vm.train_file_path + ' --data_idx ' + vm.train_data_column 
                                      + ' --target_idx ' + vm.train_target_column + ' --task_mode ' + vm.task_mode
                                      + ' --model_name ' + vm.model_name + ' --metric_name ' + vm.metric_name, {encoding: 'utf8'})

              make_train_local = make_train_local.split("?")              
              let indicator = vm.handle_Algorithm_return_value("make_train_local", make_train_local, "200", "make_train_local")

              if (indicator == false){
                console.log("make_train_local_done wrong")
                fs.appendFileSync(Log_address, "make_train_local_done wrong")
                return 
              }
              console.log("make_train_local", make_train_local)
            }catch(err){
              console.log(err)
            }
              unittest_parameters = generate_unittest_parameters()
              execute_unittest_list(unittest_callbacks, 2, "find_assistor_unittest", unittest_parameters)        // })          
              
                vm.task_id = ""
                // vm.$router.push('/notifications')
                vm.select_data=false

              })

          .catch((error) => {
              // handle error
              console.log(error)
              // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            }) //axios (find_assistor)

        
          }) //db.get
          
        }

      }
            
    },

  },
  created () {
    console.log('find_assistor_created')

    // When unittesting, this.$route == undefined
    if (this.$route != undefined){
      this.get_train_id();
    }

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position

  },
  

}
</script>