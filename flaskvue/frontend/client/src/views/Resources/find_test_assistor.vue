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
      <label for="name">Input ID column </label>
      <input type="text" v-model="test_id_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input data column (eg. 3-6)</label>
      <input type="text" v-model="test_data_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input target column</label>
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
import { execute_unittest_list, generate_unittest_parameters, generate_message_string, Log } from '../../utils.js'

import { ex,fs,os,node_path,dialog } from '../../import.js'

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
    get_test_id () {
      console.log("$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", this.task_id)
      this.$axios.get('/create_new_test_task/')
        .then((response) => {
          this.test_id = response.data.test_id
          console.log("task_id))))))))))))))00", this.task_id)
          let unittest_parameters = generate_unittest_parameters(this.test_id)
          execute_unittest_list(arguments[arguments.length-1], 0, "find_test_assistor_unittest", unittest_parameters)
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
          fs.statSync(path);
          this.test_file_path = path
          fs.readFile(path, 'utf8' , (err, data) => {
            if (err) {
              console.error(err)
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
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
        }  

      }
    },
    // get_test_id_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_test_id_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.PathForm.test_id_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
    //       console.log('Please Select A Test ID File')
    //     }  

    //   }
    // },
    // get_test_target_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_test_target_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.PathForm.test_target_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
    //       console.log('Please Select A Test Target File')
    //     }  

    //   }
    // },

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

    onSubmit (e) {
      let vm = this;
      if (this.task_id == ""){
        dialog.showErrorBox('Please Type in the Paths Again', 'We apologize for the latency')
      }else{
        
        let both_path_validation = true
        // if (vm.PathForm.test_data_path == ""){
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
        // }
        try {
          fs.statSync(vm.test_file_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
          both_path_validation = false
        }

        // try {
        //   fs.statSync(vm.test_id_path);
        // } catch (err) {
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
        //   console.log('Please Select A Test ID File')
        //   both_path_validation = false
        // }

        // try {
        //   fs.statSync(vm.PathForm.test_target_path);
        // } catch (err) {
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
        //   console.log('Please Select A Test Target File')
        //   both_path_validation = false
        // }
        
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

          let insert_sentence = `INSERT INTO "User_Sponsor_Table"("user_id", "test_indicator", "task_id", "task_name", "test_id", "test_file_path", "test_id_column","test_data_column","test_target_column") VALUES 
              (`+`"`+vm.sharedState.user_id+`", "test","` + vm.task_id + `", "` +vm.task_name + `", "` +vm.test_id + `", "` +vm.test_file_path+ `", "` +vm.test_id_column+`", "`+vm.test_data_column+`", "`+vm.test_target_column+`")`
          console.log(insert_sentence)

          var row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?').get(vm.sharedState.user_id, 'train', vm.task_id);

          console.log("s1 row",row)
          vm.task_mode = row.task_mode
          vm.model_name = row.model_name
          vm.metric_name = row.metric_name

          let unittest_parameters = generate_unittest_parameters(vm.task_mode, vm.model_name, vm.metric_name)
          execute_unittest_list(arguments[arguments.length-1], 0, "find_assistor_unittest", unittest_parameters)


          const stmt = vm.$db.prepare('INSERT INTO User_Sponsor_Table VALUES' +
          ' ( @task_name, @task_description, @user_id, @test_indicator, @task_id, @test_id, @train_file_path,' +
          ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
          ' @test_data_column, @test_target_column, @task_mode, @model_name, @metric_name)');
             
          stmt.run({
            task_name: vm.task_name, 
            task_description: '', 
            user_id: vm.sharedState.user_id, 
            test_indicator: "test", 
            task_id: vm.task_id,
            test_id: vm.test_id,
            train_file_path: '', 
            train_id_column: '', 
            train_data_column: '', 
            train_target_column: '', 
            test_file_path: vm.test_file_path,
            test_id_column: vm.test_id_column,
            test_data_column: vm.test_data_column,
            test_target_column: vm.test_target_column,
            task_mode: vm.task_mode, 
            model_name: vm.model_name,
            metric_name: vm.metric_name
          });

          // Check DB
          unittest_parameters = generate_unittest_parameters()
          execute_unittest_list(arguments[arguments.length-1], 1, "find_test_assistor_unittest", unittest_parameters)

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
          } catch(err){
            console.log(err)
          }

          const payload = {
            task_id: vm.task_id,
            task_name: vm.task_name,
            test_id: vm.test_id, 
            test_name: vm.test_name,
            task_mode: vm.task_mode,
            model_name: vm.model_name,
            metric_name: vm.metric_name,
            test_description: vm.test_description,
            id_file: test_hash_id_file_data
          }
          
          vm.$axios.post('/find_test_assistor/', payload)
            .then((response) => {
              
              let unittest_parameters = generate_unittest_parameters(response.data)
              execute_unittest_list(arguments[arguments.length-1], 2, "find_test_assistor_unittest", unittest_parameters)

              const Log_address = node_path.join(vm.root.toString(), vm.sharedState.user_id.toString(), "task", vm.task_id.toString(), "test", vm.test_id.toString(), "log.txt")
              console.log("node_path_log", Log_address)
              if(!fs.existsSync(Log_address)){
                console.log("creating log.txt");
                fs.openSync(Log_address, "w");
                console.log("log.txt created");
              }

               // handle success
              vm.$toasted.success(`Testing Starts`, { icon: 'fingerprint' })
            
              Log(generate_message_string("\nYou are SPONSOR\n"), 'warn')
              Log(generate_message_string("Test ID: " + vm.test_id + "\n"), 'warn')
              Log(generate_message_string("Testing Stage Starts\n"), 'warn')
              Log(generate_message_string("1.0 Test: Find Test Assistor\n"), 'warn')
              Log(generate_message_string("1.1 Test: Sponsor calls for help\n"), 'warn')
              Log(generate_message_string("1.2 Test: Sponsor sends id file\n"), 'warn')
              Log(generate_message_string("1.3 Test: Find Test Assistor Done\n"), 'warn')

              try {
                fs.appendFileSync(Log_address, "\n You are SPONSOR\n")
                fs.appendFileSync(Log_address, "Test ID: " + vm.test_id + "\n")
                fs.appendFileSync(Log_address, "---------------------- Test Stage Starts\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor\n")
                fs.appendFileSync(Log_address, "1.1 Test: Sponsor calls for test\n")
                fs.appendFileSync(Log_address, "1.2 Test: Sponsor sends id file\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor Done\n")
              } catch (err) {
                console.log(err)
              }

              // this.sponsor_request_show = true
              vm.test_id = ""
              vm.$router.push('/notifications')
              vm.select_file=false
            })
            .catch((error) => {
              // handle error
              console.log(error)
              // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })

          let make_test_local = null;
          try{   
            make_test_local = ex.execSync(vm.exe_position + ' make_test_local --root  ' + vm.root
                                    + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --test_id ' + vm.test_id
                                    + ' --dataset_path ' + vm.test_file_path + ' --data_idx ' + vm.test_data_column 
                                    + ' --target_idx ' + vm.test_target_column + ' --task_mode ' + vm.task_mode
                                    + ' --model_name ' + vm.model_name + ' --metric_name ' + vm.metric_name, {encoding: 'utf8'})


            make_test_local = make_test_local.split("?")
            
            let indicator = vm.handle_Algorithm_return_value("make_test_local", make_test_local, "200", "make_test_local")

            if (indicator == false){
              console.log("make_test_local_done wrong")
              fs.appendFileSync(Log_address, "make_test_local_done wrong")
              return 
            }

            console.log("make_test_local", make_test_local)

            

          }catch(err){
            console.log(err)
          }
          
        }

      }
            
    },

  },
  created () {
    console.log('ttt', this.$toasted)
    console.log('fff', this.$route)
    // console.log('565656', this.$route.query.from)
    // this.task_id = this.$route.query.from;
    // this.task_name = this.$route.query.from_task_name

    this.get_test_id();

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  }
}
</script>