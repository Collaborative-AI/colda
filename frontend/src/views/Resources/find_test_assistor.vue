<template>
  <div class="container g-pt-20">

    <div class="form-group">
      <label for="name">Input Test Name</label>
      <input type="text" v-model="test_name" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input Test Description</label>
      <input type="text" v-model="test_description" class="form-control" id="name" placeholder="">
    </div>

     <div class="form-group">
      <label for="name">Select Data File</label>
      <input type="text" v-model="test_file_path" class="form-control" id="name" placeholder="">
      <button @click="get_test_data_path()" class="btn btn-success">Select File</button>
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
    <div class="form-group">
      <label for="name">Input ID column (eg. 1)</label>
      <input type="text" v-model="test_id_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input data column (eg. 2-8)</label>
      <input type="text" v-model="test_data_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input target column (eg. 9)</label>
      <input type="text" v-model="test_target_column" class="form-control" id="name" placeholder="">
    </div>
    
    <!-- <div class="form-group">
      <label for="location">Select Id File</label>
      <input type="text" v-model="PathForm.test_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_test_id_path()">Select ID File</button>
    </div>

    <div class="form-group">
      <label for="location">Select Target File</label>
      <input type="text" v-model="PathForm.test_target_path" class="form-control" id="location" placeholder="">
      <button @click="get_test_target_path()">Select Target File</button>
    </div> -->

    <button type="submit" @click="onSubmit()" class="btn btn-success">Initiate a test</button>
  </div>
</template>

<script>
import store from '../../store'
import db from '../../db'
import {  handle_file_path, check_interaction, handle_assistor_username_list, handle_input_column_string, handle_Algorithm_return_value, execute_unittest_list, generate_unittest_parameters, generate_message_string, Log, change_db_param_to_string, add_prefix } from '../../utils.js'

import { ex,fs,os,node_path,dialog } from '../../import_package.js'

// const fs = window.fs ? window.fs : require('fs');
// const ex = window.ex ? window.ex : require('child_process');
// const node_path = window.node_path ? window.node_path : require('path');
// const os = window.os ? window.os : require('os');
// const dialog = window.dialog ? window.dialog : require('electron');
// const store = require('../../store').defaultv
// const $ = require('jquery')

export default {
  name: 'Find_Test_Assistor',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      task_id: "",
      task_name: "",
      test_id: "",
      test_name: "",
      test_description: "",
      test_file_path: "",
      test_id_column: "",
      test_data_column: "",
      test_target_column: "",
      ptitles:"",
      pdatas:"",
      select_data:false,
      PathForm: {
        test_data_path: "",
        test_id_path: "",
        test_target_path: "",
      },
      root: '',
      task_mode: '',
      model_name: '',
      metric_name: '',
      exe_position: '',
    }
  },
  methods: {
    get_test_id (unittest_callbacks) {
      
      this.$axios.get(add_prefix(`/create_new_test_task/`, `/main_flow`))
        .then((response) => {
          this.test_id = response.data.test_id
          let unittest_parameters = generate_unittest_parameters(this.test_id)
          execute_unittest_list(unittest_callbacks, 0, "find_test_assistor_unittest", unittest_parameters)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    
    get_test_data_path() {
      let vm=this
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_test_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
      }else{

        try {
          let path = result[0]

          if (handle_file_path(path) == false){
            dialog.showErrorBox('Data Path not Correct, Please do not contain space', 'Sorry')
            return
          }

          fs.statSync(path);
          this.test_file_path = path
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
            for (let i in vm.pdatas) { 
              vm.pdatas[i] = vm.pdatas[i].split(",")
            } 
            vm.ptitles=vm.pdatas[0]
            vm.pdatas=vm.pdatas.slice(1,4)
            vm.select_data=true
            console.log('preview',vm.pdatas[0])
          })

        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
        }  

      }
    },

    onSubmit (unittest_callbacks) {
      let vm = this;

      let handle_data_column_res = handle_input_column_string(vm.test_data_column, 'data', vm.ptitles.length)
      let handle_id_column_res = handle_input_column_string(vm.test_id_column, 'id', vm.ptitles.length)
      let handle_target_column_res = handle_input_column_string(vm.test_target_column, 'target', vm.ptitles.length)

      let interaction_indicator = check_interaction(vm.test_id_column, vm.test_data_column, vm.test_target_column)
      let both_path_validation = false
      if ( handle_data_column_res == false) {
        dialog.showErrorBox('Please Type in test_data_column in corrent form', 'Thank you very much')
      } else if ( handle_id_column_res == false) {
        dialog.showErrorBox('Please Type in test_id_column in corrent form', 'Thank you very much')
      } else if ( handle_target_column_res == false) {
        dialog.showErrorBox('Please Type in test_target_column in corrent form', 'Thank you very much')
      } else if ( interaction_indicator == false){
        dialog.showErrorBox('Please follow the form: id, data, target (no interaction)', 'Thank you very much')
      } else if (this.task_id == '' || this.task_name == '' || this.root == '' || this. exe_position == ''){
        dialog.showErrorBox('Please re-enter the page', 'We apologize for the latency')
      } else if (this.test_id == ''){
        dialog.showErrorBox('Please Type in the Paths Again', 'We apologize for the latency')
        vm.get_test_id()
      } else if (handle_file_path(vm.test_file_path) == false){
        dialog.showErrorBox('Data Path not Correct, Please do not contain space', 'Sorry')
      } else {
        both_path_validation = true
        try {
          fs.statSync(vm.test_file_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
          both_path_validation = false
        }
        
        if(both_path_validation == true){
          // db.serialize(function() {
          //   let update_sentence = 'UPDATE "User_Sponsor_Table"'
          //             +' SET "test_data_path" = "' + vm.PathForm.test_data_path + '",'
          //             +'"test_id_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"test_target_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"WHERE "user_id" = ' + vm.sharedState.user_id
          //   console.log(update_sentence)           
          //   db.run(update_sentence)

          // });
          console.log("true")
          console.log(vm.test_file_path,vm.test_id_column,vm.test_target_column)

          let select_sentence = `SELECT * FROM User_Sponsor_Table WHERE user_id = ?` +
                                 ` AND test_indicator = ? AND task_id = ?`
          let param = [vm.sharedState.user_id, 'train', vm.task_id]
          console.log('select_sentence', select_sentence)

          db.get(select_sentence, change_db_param_to_string(param), (err, row) => {
            if (err) {
              console.log('err info',err);;
            }
            
            console.log("s1 row",row)
            vm.task_mode = row.task_mode
            vm.model_name = row.model_name
            vm.metric_name = row.metric_name

            // let row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?').get(vm.sharedState.user_id, 'train', vm.task_id);

            // console.log("s1 row",row)
            // vm.task_mode = row.task_mode
            // vm.model_name = row.model_name
            // vm.metric_name = row.metric_name

            let sentence = `INSERT INTO "User_Sponsor_Table"("user_id", "test_indicator", "task_id", "task_name",`+ `
                            "test_id", "test_file_path", "test_id_column","test_data_column","test_target_column",`+ 
                            `"task_mode", "model_name", "metric_name") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
            let param = [vm.sharedState.user_id, 'test', vm.task_id, vm.task_name,
                      vm.test_id, vm.test_file_path, vm.test_id_column, vm.test_data_column, 
                      vm.test_target_column, vm.task_mode, vm.model_name, vm.metric_name]


            // let insert_sentence = `INSERT INTO "User_Sponsor_Table"("user_id", "test_indicator", "task_id", "task_name", "test_id", "test_file_path", "test_id_column","test_data_column","test_target_column", "task_mode", "model_name", "metric_name") VALUES 
            //     (`+`"`+vm.sharedState.user_id+`", "test","` + vm.task_id + `", "` +vm.task_name + `", "` +vm.test_id + `", "` +vm.test_file_path+ `", "` +vm.test_id_column+`", "`+vm.test_data_column+`", "`+vm.test_target_column+`", "`+vm.task_mode`", "`+vm.model_name`", "`+vm.metric_name`")`
            // console.log(insert_sentence)
            vm.$db.run(sentence, change_db_param_to_string(param), function(err){
              if (err){
                console.log(err);
              }

              let unittest_parameters = generate_unittest_parameters(vm.task_mode, vm.model_name, vm.metric_name)
              execute_unittest_list(unittest_callbacks, 0, "find_test_assistor_unittest", unittest_parameters)


              // const stmt = vm.$db.prepare('INSERT INTO User_Sponsor_Table VALUES' +
              // ' ( @task_name, @task_description, @user_id, @test_indicator, @task_id, @test_id, @train_file_path,' +
              // ' @test_id_column, @test_data_column, @test_target_column, @test_file_path, @test_id_column,' +
              // ' @test_data_column, @test_target_column, @task_mode, @model_name, @metric_name)');
                
              // stmt.run({
              //   task_name: vm.task_name, 
              //   task_description: '', 
              //   user_id: vm.sharedState.user_id, 
              //   test_indicator: "test", 
              //   task_id: vm.task_id,
              //   test_id: vm.test_id,
              //   train_file_path: '', 
              //   test_id_column: '', 
              //   test_data_column: '', 
              //   test_target_column: '', 
              //   test_file_path: vm.test_file_path,
              //   test_id_column: vm.test_id_column,
              //   test_data_column: vm.test_data_column,
              //   test_target_column: vm.test_target_column,
              //   task_mode: vm.task_mode, 
              //   model_name: vm.model_name,
              //   metric_name: vm.metric_name
              // });

              // Check DB
              unittest_parameters = generate_unittest_parameters()
              execute_unittest_list(unittest_callbacks, 1, "find_test_assistor_unittest", unittest_parameters)

              let match_id_address = vm.test_id_column
              let test_hash_id_file_address = null;
              try{
                test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
                                        + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id
                                        + ' --mode test' + ' --test_id ' + vm.test_id
                                        + ' --dataset_path ' + vm.test_file_path + ' --id_idx ' + vm.test_id_column, {encoding: 'utf8'})

                // test_hash_id_file_address = test_hash_id_file_address.replace(/\n/g, '')
                console.log(test_hash_id_file_address)
                test_hash_id_file_address = test_hash_id_file_address.split("?")
                console.log("test_hash_id_file_address", test_hash_id_file_address)
                if (test_hash_id_file_address[0] == "300" && test_hash_id_file_address[1] == "make_hash" && test_hash_id_file_address[2] == "not valid mode"){
                  vm.$toasted.success(`not valid mode, please select again`, { icon: 'fingerprint' })
                  return
                }
                if (test_hash_id_file_address[0] != "200" || test_hash_id_file_address[1] != "make_hash"){
                  vm.$toasted.success(`find assistor went wrong, please try again`, { icon: 'fingerprint' })
                  console.log("make hash wrong")
                  return 
                }
              }catch(err){
                console.log(err)
              }

              let test_hash_id_file_data = null
              try{
                test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});
                test_hash_id_file_data = test_hash_id_file_data.split(/[\r\n]+/)
              } catch(err){
                console.log(err)
              }

              const payload = {
                identifier_content:test_hash_id_file_data,
                train_id: vm.task_id,
                test_id: vm.test_id, 
                task_mode: vm.task_mode,
                model_name: vm.model_name,
                metric_name: vm.metric_name,
                test_name: vm.test_name,
                test_description: vm.test_description,
              }
              
              vm.$axios.post(add_prefix(`/find_test_assistor/${vm.sharedState.user_id}`, `/main_flow`), payload)
                .then((response) => {
                  
                  let unittest_parameters = generate_unittest_parameters(response.data)
                  execute_unittest_list(unittest_callbacks, 2, "find_test_assistor_unittest", unittest_parameters)

                  const Log_address = node_path.join(vm.root.toString(), vm.sharedState.user_id.toString(), "task", vm.task_id.toString(), "test", vm.test_id.toString(), "log.txt")
                  console.log("node_path_log", Log_address)
                  if(!fs.existsSync(Log_address)){
                    console.log("creating log.txt");
                    fs.openSync(Log_address, "w");
                    console.log("log.txt created");
                  }

                  // handle success
                  vm.$toasted.success(`Testing task: ` + vm.test_id + ` Starts`, { icon: 'fingerprint' })
                
                  //Log(generate_message_string("\nYou are SPONSOR\n"), 'info')
                  //Log(generate_message_string("Test ID: " + vm.test_id + "\n"), 'info')
                  //Log(generate_message_string("Testing Stage Starts\n"), 'info')
                  //Log(generate_message_string("1.0 Test: Find Test Assistor\n"), 'info')
                  //Log(generate_message_string("1.1 Test: Sponsor calls for help\n"), 'info')
                  //Log(generate_message_string("1.2 Test: Sponsor sends id file\n"), 'info')
                  //Log(generate_message_string("1.3 Test: Find Test Assistor Done\n"), 'info')

                  // vm.$toasted.success(`Testing: Find Assistor Done`, { icon: 'fingerprint' })

                  try {
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: You are SPONSOR\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: Test ID: " + vm.test_id + "\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: Test Stage Starts\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 1. Test: Find Test assistor\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 1.1 Test: Sponsor calls for test\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 1.2 Test: Sponsor sends id file\n")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 1. Test: Find Test assistor Done\n")
                  } catch (err) {
                    console.log(err)
                  }

                  let make_test_local = null;
                  try{   
                    make_test_local = ex.execSync(vm.exe_position + ' make_test_local --root  ' + vm.root
                                            + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --test_id ' + vm.test_id
                                            + ' --dataset_path ' + vm.test_file_path + ' --data_idx ' + vm.test_data_column 
                                            + ' --target_idx ' + vm.test_target_column + ' --task_mode ' + vm.task_mode
                                            + ' --model_name ' + vm.model_name + ' --metric_name ' + vm.metric_name, {encoding: 'utf8'})


                    make_test_local = make_test_local.split("?")
                    
                    let indicator = handle_Algorithm_return_value("make_test_local", make_test_local, "200", "make_test_local")

                    if (indicator == false){
                      console.log("make_test_local_done wrong")
                      fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: error" + ", Content: make_test_local_done wrong")
                      return 
                    }

                    console.log("make_test_local", make_test_local)
                    }catch(err){
                    console.log(err)
                    } 

                    // this.sponsor_request_show = true
                    vm.test_id = ""
                    vm.select_file=false
                    vm.$router.push('/notifications')
                  }) // axios find_test_assistor
                  .catch((error) => {
                    // handle error
                    console.log(error)
                    // console.log(error.response.data)
                    // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                  }) // axios find_test_assistor

            }) // db insert into User_Sponsor_Table
          }) // db get record of task_id in User_Sponsor_Table
        } // if(both_path_validation == true){
      } // else    
    }, // onSubmit

  },

  created () {
    console.log('find_test_assistor_created')

    // When unittesting, this.$route == undefined
    if (this.$route != undefined){
      this.task_id = this.$route.query.from;
      this.task_name = this.$route.query.from_task_name
      this.get_test_id();
    }

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position

  }
}
</script>