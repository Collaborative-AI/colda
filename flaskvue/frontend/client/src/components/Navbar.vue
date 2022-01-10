<template>
  <div class="container-fluid">
    <div class="row min-vh-100 flex-column flex-md-row">
        <aside class="col-12 col-md-2 p-0 bg-dark flex-shrink-1" style="overflow:auto">
            <nav class="navbar navbar-expand navbar-dark bg-dark flex-md-column flex-row align-items-start py-2">
                <div class="collapse navbar-collapse ">
                    <ul class="flex-md-column flex-row navbar-nav w-100 justify-content-between">

                        <router-link to="/" class="g-text-underline--none--hover">
                          <img src="../assets/a-logo2.png" width="30" height="30" class="d-inline-block align-top" alt="">
                            
                        </router-link>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link  v-bind:to="{ path: '/find_assistor' }" class="nav-link" @click.native="refreshView">Request</router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link  v-bind:to="{ path: '/plist' }" class="nav-link" @click.native="refreshView">Pending<span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link  v-bind:to="{ path: '/notifications' }" class="nav-link" @click.native="refreshView">History<span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link  v-bind:to="{ name: 'SettingProfile' }" class="nav-link" @click.native="refreshView">Setting</router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                            <a v-on:click="handlerLogout" class="nav-link" href="#">Logout</a>
                        </li>

                        <li v-else class="nav-item">
                          <router-link to="/login" class="nav-link">Login</router-link>
                        </li>
                      
                        <li v-if="sharedState.is_authenticated && checkAuthority(['admin','user'])"  class="nav-item">
                          <router-link  to="/shiyan" class="nav-link">Ceshi</router-link>
                        </li>       
                        <!-- <button @click="test_axios()">123</button>              -->
                        <!-- <li class="nav-item">
                            <a class="nav-link pl-0 text-nowrap" href="#"><i class="fa fa-bullseye fa-fw"></i> <span class="font-weight-bold">Brand</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link pl-0" href="#"><i class="fa fa-book fa-fw"></i> <span class="d-none d-md-inline">Link</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link pl-0" href="#"><i class="fa fa-cog fa-fw"></i> <span class="d-none d-md-inline">Link</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link pl-0" href="#"><i class="fa fa-heart codeply fa-fw"></i> <span class="d-none d-md-inline">Codeply</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link pl-0" href="#"><i class="fa fa-star codeply fa-fw"></i> <span class="d-none d-md-inline">Link</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link pl-0" href="#"><i class="fa fa-star fa-fw"></i> <span class="d-none d-md-inline">Link</span></a>
                        </li> -->
                    </ul>
                </div>
            </nav>
        </aside>
        <main class="col-12 col-md-10 bg-faded py-3 flex-grow-1" >
            <!-- <h2>Example</h2>
            <p>
                This is a Bootstrap 4 example layout that includes a Sidebar menu. On larger screen widths, the Sidebar is on the 
                left side and consumes the entire page height. It's vertically positioned down the screen. On smaller screen widths (like mobile phones and tablets), the Sidebar
                moves to the top of the page, and becomes horizontally positioned across the page like a Navbar. Only icons are shown
                on mobile to limit use of screen real estate.
            </p> 
            <p>
                This Sidebar works using only Bootstrap CSS classes and doesn't require JavaScript. It utilizes the responsive Navbar classes
                to auto-magically switch the Sidebar orientation.
            </p>  -->
            <router-view v-if="showView"/>
        </main>
    </div>
</div>
</template>

<script>
import store from '../store.js'
import axios from 'axios'
import $ from 'jquery'
import db from '../db'
// // console.log('dbzzzz', db)
import authority from '../authority'
import { execute_unittest_list, generate_unittest_parameters, generate_message_string, Log, check_if_notification_is_null } from '../utils.js'

// import axios from '../http'


// // use Node API
// If we run npm run electron:serve, window.ex would have the object
// else we are running unittest, we will require directly
import { ex,fs,os,node_path,dialog, log } from '../import.js'

// const ex = window.ex ? window.ex : require('child_process');
// const fs = window.fs ? window.fs : require('fs');
// const os = window.os ? window.os : require('os');
// const node_path = window.node_path ? window.node_path : require('path');
// const dialog = window.dialog ? window.dialog : require('electron');


import Home from '../views/Home.vue'
// const Home = require('../views/Home.vue').default
export default {
  name: 'Navbar',  //this is the name of the component
  components: {
      Home
    },
  data () {
    return {
      log: ["a","b"],
      checkAuthority: authority.checkAuthority,
      sharedState: store.state,
      unread_request_show: false,
      assistor_num: 0,
      max_round: 3,
      root: '',
      exe_position: '',
      showView: true,
      test_response: {},
    }
  },
  methods: {

    refreshView () {
      this.showView = false // 通过v-if移除router-view节点
      this.$nextTick(() => {
        this.showView = true // DOM更新后再通过v-if添加router-view节点
      })
    },
    
    handlerLogout (e) {
      store.logoutAction()
      this.$toasted.show('You have been logged out.', { icon: 'fingerprint' })
      this.$router.push('/login')
    },

    handle_train_log_address(task_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      // // console.log("train_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        // // console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        // // console.log("log.txt created");
      }
      return Log_address
    },

    handle_test_log_address(task_id, test_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "test", test_id.toString(), "log.txt")
      // // console.log("test_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        // // console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        // // console.log("log.txt created");
      }
      return Log_address
    },

    // Helper Function for checking algorithm return value
    handle_Algorithm_return_value(name, return_val, first_val, second_val) {
      // // console.log(name, return_val)
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

    unread_request(unread_request_notification, unittest_callbacks) {

      // Only assistor will enter this function
      if (check_if_notification_is_null(unread_request_notification, 'unread_request_notification')){
        return
      }

      let vm = this
      // Log(generate_message_string("this.sharedState.receive_request", vm.sharedState.mode), 'info')
      // Log(generate_message_string("2.1 Update request notification response", unread_request_notification), 'info')

      let cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
      // Log(generate_message_string('cur_unread_request', unread_request_notification), 'info')

      // Unittest: check if testing task id in the cur_unread_request_Taskid_dict
      // // console.log('55555', unittest_callbacks)
      let unittest_parameters = generate_unittest_parameters(cur_unread_request_Taskid_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_request_unittest", unittest_parameters)


      var select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id= ?' 
      var param = [vm.sharedState.user_id]
      console.log('select_sentence', select_sentence)


      vm.$db.get(select_sentence, param, (err, row) => {
        if (err) {
          console.error(err);
        }
      

      // var row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id= ?').get(vm.sharedState.user_id);
      // Log(generate_message_string('55555',row), 'debug')

      if (row == null){
        vm.sharedState.mode = "manual";
      }
      else{
        vm.sharedState.mode = row.default_mode;
      } 

      // Assistor might receive multiple task request, We need to iterate them
      for (let task_id in cur_unread_request_Taskid_dict){
        // console.log('root shi', this.root)
        log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');
        console.log("5552121", node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt'))
        Log('assistor ceshi', 'info')
        // Log(generate_message_string('navbar unread request mode', vm.sharedState.mode), 'debug')

        if (vm.sharedState.mode == 'auto'){

          var select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id = ?'
          var param = [vm.sharedState.user_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }
          // var row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ?').get(vm.sharedState.user_id);
          // Log(generate_message_string('row kan', row), 'debug')
          let default_file_path = row.default_file_path
          let default_id_column = row.default_id_column
          let default_data_column = row.default_data_column
          let default_target_column = row.default_target_column
          let default_mode = row.default_mode
          let default_model_name = row.default_model_name


          var sentence = `INSERT INTO "User_Sponsor_Table"("user_id", "task_id", "test_id", "task_name", "task_description", "test_name", "test_description", "train_file_path",` +
          ` "train_id_column, "train_data_column", "train_target_column", "test_file_path", "test_id_column",` +
          ` "test_data_column", "test_target_column", "mode", "test_indicator", "model_name") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          var param = [vm.sharedState.user_id, task_id, '', '', '', '', '', default_file_path, default_id_column, default_data_column, default_target_column, 
                      default_file_path, default_id_column, default_data_column, default_target_column, default_mode, 'train', default_model_name]

          vm.$db.run(sentence, param, function(err){
            if (err){
              console.log('err info',err);
            }



          const stmt = vm.$db.prepare('INSERT INTO User_Assistor_Table VALUES' +
          ' ( @user_id, @task_id, @test_id, @task_name, @task_description, @test_name, @test_description, @train_file_path,' +
          ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
          ' @test_data_column, @test_target_column, @mode, @test_indicator, @model_name)');
             
          stmt.run({
            user_id: vm.sharedState.user_id, 
            task_id: task_id,
            test_id: '',
            task_name: '', 
            task_description: '', 
            test_name: '',
            test_description: '',
            train_file_path: default_file_path, 
            train_id_column: default_id_column, 
            train_data_column: default_data_column, 
            train_target_column: default_target_column, 
            test_file_path: default_file_path,
            test_id_column: default_id_column,
            test_data_column: default_data_column,
            test_target_column: default_target_column,
            mode: default_mode, 
            test_indicator: 'train',
            model_name: default_model_name
          });

          // check task_id and vm.sharedState.mode
          
          let unittest_parameters = generate_unittest_parameters(task_id, vm.sharedState.mode)
          execute_unittest_list(unittest_callbacks, 1, "unread_request_unittest", unittest_parameters)

          let hash_id_file_address = null;
          let Log_address = null;
          try{   
            hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                    + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + default_file_path 
                                    + ' --id_idx ' + default_id_column, {encoding: 'utf8'})

            hash_id_file_address = hash_id_file_address.split("?")
            let indicator = vm.handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
            Log_address = vm.handle_train_log_address(task_id)
            if (indicator == false){
              // // console.log("hash_id_file_address wrong")
              fs.appendFileSync(Log_address, "hash_id_file_address wrong")
              return 
            }
          }catch(err){
            // console.log(err)
          }

          unittest_parameters = generate_unittest_parameters()
          execute_unittest_list(unittest_callbacks, 2, "unread_request_unittest", unittest_parameters)

          Log(generate_message_string("\nYou are Assistor\n"), 'info')
          Log(generate_message_string("Task ID: " + task_id + "\n"), 'info')
          Log(generate_message_string("2.0 Unread Request Starts\n"), 'info')
          Log(generate_message_string("2.1 Update the request notification\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "\n You are Assistor\n")
            fs.appendFileSync(Log_address, "Task ID: " + task_id + "\n")
            fs.appendFileSync(Log_address, "----------------------2. Unread Request\n")
            fs.appendFileSync(Log_address, "2.1 Update the request notification\n")
          } catch (err) {
            // console.log(err)
          }

          // Read the data from designated position
          let hash_id_file_data = fs.readFileSync(hash_id_file_address[2], {encoding:'utf8', flag:'r'});

          const match_assistor_id_data = {
            task_id: task_id,
            file: hash_id_file_data,
          }
          
          vm.$axios.post('/match_assistor_id/', match_assistor_id_data)
            .then((response) => {
              // handle success

              // Unittest: check match_assistor_id response
              let unittest_parameters = generate_unittest_parameters(response.data)
              execute_unittest_list(unittest_callbacks, 3, "unread_request_unittest", unittest_parameters)

              Log(generate_message_string("2.2 Assistor uploads match id file\n"), 'info')
              Log(generate_message_string("2.3 Unread Request Done\n"), 'info')

              try {
                fs.appendFileSync(Log_address, "2.2 assistor uploads id file\n")
                fs.appendFileSync(Log_address, "--------------------------2. Unread Request Done\n")
              } catch (err) {
                // console.log(err)
              }
            })
            .catch((error) => {
              // handle error
              // console.log(error)
              this.$toasted.error('Task' + task_id.toString() + 'occurs error at stage 1', { icon: 'fingerprint' })
            })
          })
          })
      } else if (vm.sharedState.mode == 'manual'){
        vm.sharedState.pending_num++;
        const add_train_pending = {
            task_id: task_id,
          }
        
        vm.$axios.post('/add_train_pending/', add_train_pending)
          .then((response) => {
            // handle success
            Log(generate_message_string("add_train_pending response", response.data), 'debug')
          })
          .catch((error) => {
            // handle error
            // console.log(error)
            this.$toasted.error('Task' + task_id.toString() + 'occurs error at stage 1', { icon: 'fingerprint' })
          })
      } else{
        // // console.log("unread request: mode run")
        // dialog.showErrorBox('mode:run')
      }

    }//end for

      
      })
    },


    unread_match_id(unread_match_id_notification, unittest_callbacks) {

      let vm = this

      if (check_if_notification_is_null(unread_match_id_notification, 'unread_match_id_notification')){
        return
      }

      // console.log("3.1 Update match id notification response", unread_match_id_notification)
      // this.$toasted.success("3.1 Update the match id notification", { icon: 'fingerprint' })

      let cur_unread_match_id_Taskid_dict = unread_match_id_notification["check_dict"]

      // check if testing task id in the cur_unread_request_Taskid_dict
      let unittest_parameters = generate_unittest_parameters(cur_unread_match_id_Taskid_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_match_id_unittest", unittest_parameters)
      
      for (let task_id in cur_unread_match_id_Taskid_dict){

        log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');
        // Log('sponsor ceshi3', 'info')
        const Log_address = this.handle_train_log_address(task_id)

        Log(generate_message_string("3.0 Unread Match ID Starts\n"), 'info')
        Log(generate_message_string("3.1 Update the match id notification\n"), 'info')

        try {
          fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID\n")
          fs.appendFileSync(Log_address, "3.1 Update the match id notification\n")
        } catch (err) {
          // console.log(err)
        }

        let check_sponsor = cur_unread_match_id_Taskid_dict[task_id]

        if (check_sponsor == 1){
          Log(generate_message_string("3.2 Unread_match_id_sponsor\n"), 'info')
          try {
            fs.appendFileSync(Log_address, "3.2 Unread_match_id_sponsor\n")
          } catch (err) {
            // console.log(err)
          }
          this.unread_match_id_sponsor(task_id, unittest_callbacks)
        }  
        else{
          Log(generate_message_string("3.2 Unread_match_id_assistor\n"), 'info')
          try {
            fs.appendFileSync(Log_address, "3.2 Unread_match_id_assistor\n")
          } catch (err) {
            // console.log(err)
          }
          this.unread_match_id_assistor(task_id, unittest_callbacks)
        }
      }
      return 'done'
    },

    unread_match_id_sponsor(task_id, unittest_callbacks) {
      
      // Create 'Local_Data/id/task_id/Match/' folder
      // const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      let vm = this;

      log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_train_log_address(task_id)
      
      // Obtain Match_id file
      // async
      const payload = {
        task_id: task_id
      }
      
      const path = `/users/${vm.sharedState.user_id}/match_id_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // iterate the match_id_file

          // check users/user_id/match_id_file return value
          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 1, "unread_match_id_unittest", unittest_parameters)
          
          Log(generate_message_string("3.3 Sponsor gets matched id file\n"), 'info')
    
          try {
            fs.appendFileSync(Log_address, "3.3 Sponsor gets matched id file\n")
          } catch (err) {
            // console.log(err)
          }

          for(let i = 0;i < response.data.match_id_file.length; i++){

            const from_id = response.data.assistor_random_id_pair[i];
            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join("\n")

            // Store match_id file from different assistor
            let save_match_id_file_pos = null;
            try{
              save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})

              save_match_id_file_pos = save_match_id_file_pos.split("?")
              let indicator = vm.handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos, "200", "save_match_id")
              if (indicator == false){
                // console.log("save_match_id_file_pos wrong")
                fs.appendFileSync(Log_address, "save_match_id_file_pos wrong")
                return 
              }

            }catch(err){
              // console.log(err)
            }

            // check if we run here
            let unittest_parameters = generate_unittest_parameters()
            execute_unittest_list(unittest_callbacks, 2, "unread_match_id_unittest", unittest_parameters)

            fs.writeFileSync(save_match_id_file_pos[2], cur_match_id_file)
            // console.log('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos[2]);
            // vm.$toasted.success('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos[2], { icon: 'fingerprint' })
            Log(generate_message_string("3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"), 'info')
            try {
              fs.appendFileSync(Log_address, "3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n")
            } catch (err) {
              // console.log(err)
            }

            // match_id (from different assistor) to index 
            try{
              let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})

              make_match_idx_done = make_match_idx_done.split("?")
              let indicator = vm.handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
              if (indicator == false){
                // console.log("make_match_idx_done wrong")
                fs.appendFileSync(Log_address, "make_match_idx_done wrong")
                return 
              }

            }catch(err){
              // console.log(err)
            }

            unittest_parameters = generate_unittest_parameters()
            execute_unittest_list(unittest_callbacks, 3, "unread_match_id_unittest", unittest_parameters)

            // console.log('3.5 Sponsor matches id to index');
            // vm.$toasted.success('3.5 Sponsor matches id to index', { icon: 'fingerprint' })
            Log(generate_message_string("3.5 Sponsor matches id to index\n"), 'info')

            try {
              fs.appendFileSync(Log_address, "3.5 Sponsor matches id to index\n")
            } catch (err) {
              // console.log(err)
            }

          }

          // let select_train_target_column = 'SELECT * FROM User_Sponsor_Table WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' +' AND "task_id"="' + task_id + '"';
          // // console.log("select_train_target_column", select_train_target_column)
          var select_sentence = 'SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?'
          var param = [vm.sharedState.user_id, 'train', task_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }

          // var row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?').get(vm.sharedState.user_id, 'train', task_id);

          // // console.log("match row",row)
          let train_file_path = row.train_file_path
          // // console.log("train_file_path", train_file_path)
          let train_target_column = row.train_target_column
          // // console.log("train_target_column", train_target_column)
          let task_mode = row.task_mode
          // // console.log('task_mode1',task_mode)
          let metric_name = row.metric_name
          // // console.log('metric_name1',metric_name)
          let make_residual_multiple_paths = null;
          try{
            make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
              + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round 1 ' 
              + ' --dataset_path ' + train_file_path + ' --target_idx ' + train_target_column
              + ' --task_mode ' + task_mode + ' --metric_name ' + metric_name, {encoding: 'utf8'})

            make_residual_multiple_paths = make_residual_multiple_paths.split("?")
            let indicator = vm.handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
            if (indicator == false){
              // console.log("make_residual_multiple_paths wrong")
              fs.appendFileSync(Log_address, "make_residual_multiple_paths wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          // // console.log("param2 Sponsor makes residual finished")
          // vm.$toasted.success("3.6 Sponsor makes residual finished", { icon: 'fingerprint' })
          Log(generate_message_string("3.6 Sponsor makes residual finished\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "3.6 Sponsor makes residual finished\n")
          } catch (err) {
            // console.log(err)
          }

          // Read Files
          let all_residual_data = [];
          let assistor_random_id_list = [];
          let residual_paths = make_residual_multiple_paths.slice(2, make_residual_multiple_paths.length)
          for (let i = 0; i < residual_paths.length; i++){

            let data = null;
            try{
              // data = fs.readFileSync(make_residual_multiple_paths[i], {encoding:'utf8', flag:'r'});
              data = fs.readFileSync(residual_paths[i], {encoding:'utf8', flag:'r'});
            }catch(err){
              // console.log(err)
            }
            all_residual_data.push(data);

            // let cur_path = make_residual_multiple_paths[i]
            let cur_path = residual_paths[i]
            let path_split = cur_path.split(node_path.sep);
            let assistor_random_id = path_split[path_split.length-1].split(".")[0];
            assistor_random_id_list.push(assistor_random_id);
            
          }

          // // console.log("assistor_random_id_list", assistor_random_id_list)
          const send_situation_payload = {
              task_id: task_id,
              assistor_random_id_list: assistor_random_id_list,
              residual_list: all_residual_data,
            }
          // // console.log('send situation payload', send_situation_payload)

          // send initial situation
          // async
          vm.$axios.post('/send_situation/', send_situation_payload)
            .then((response) => {
            // handle success

            // check send_situation return value
            unittest_parameters = generate_unittest_parameters(response.data)
            execute_unittest_list(unittest_callbacks, 4, "unread_match_id_unittest", unittest_parameters)

            // // console.log("3.7 Sponsor sends all situations", response)
            // vm.$toasted.success("3.7 Sponsor sends all situations", { icon: 'fingerprint' })
            Log(generate_message_string("3.7 Sponsor sends all situations" + "\n"), 'info')
            Log(generate_message_string("-------------------------- 3. Unread Match ID Done\n"), 'info')

            try {
              fs.appendFileSync(Log_address, "3.7 Sponsor sends all situations" + "\n")
              fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID Done\n")
            } catch (err) {
              // console.log(err)
            }

          })
          .catch((error) => {
            // console.log(error)
          })
          
        })
        .catch((error) => {
          // console.log(error)
          // handle error
        }) 
        })
    },

    unread_match_id_assistor(task_id, unittest_callbacks) {

      let vm = this;

      log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_train_log_address(task_id)
      
      // Obtain Match_id file
      const payload = {
        task_id: task_id
      }
      const path = `/users/${vm.sharedState.user_id}/match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {
          
          // check users/user_id/match_id_file return value
          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 1, "unread_match_id_unittest", unittest_parameters)
          
          // // console.log("3.3 Assistor gets matched id file", response)
          // vm.$toasted.success("3.3 Assistor gets matched id file", { icon: 'fingerprint' })
          Log(generate_message_string("3.3 Assistor gets matched id file\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "3.3 Assistor gets matched id file\n")
          } catch (err) {
            console.log(err)
          }
          
          const from_id = response.data.sponsor_random_id;
          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join("\n")
          
          // Store match_id file from sponsor
          let save_match_id_file_pos = null;
          try{
            save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
            
            save_match_id_file_pos = save_match_id_file_pos.split("?")
            let indicator = vm.handle_Algorithm_return_value("save_match_id_file_pos", save_match_id_file_pos, "200", "save_match_id")
            if (indicator == false){
              // console.log("save_match_id_file_pos wrong")
              fs.appendFileSync(Log_address, "save_match_id_file_pos wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          // Store match_id file
          fs.writeFileSync(save_match_id_file_pos[2], cur_match_id_file)

          // console.log('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos[2]);
          // vm.$toasted.success('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos[2], { icon: 'fingerprint' })
          Log(generate_message_string("3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n")
          } catch (err) {
            // console.log(err)
          }

          // match id to index from sponsor
          try{
            let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
      
            make_match_idx_done = make_match_idx_done.split("?")
            let indicator = vm.handle_Algorithm_return_value("make_match_idx_done", make_match_idx_done, "200", "make_match_idx")
            if (indicator == false){
              // console.log("make_match_idx_done wrong")
              fs.appendFileSync(Log_address, "make_match_idx_done wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          // console.log('3.5 Assistor matches id to index');
          // vm.$toasted.success('3.5 Assistor matches id to index', { icon: 'fingerprint' })
          Log(generate_message_string("3.5 Assistor matches id to index\n"), 'info')
          Log(generate_message_string("-------------------------- 3. Unread Match ID Done\n"), 'info')


          try {
            fs.appendFileSync(Log_address, "3.5 Assistor matches id to index\n")
            fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID Done\n")
          } catch (err) {
            // console.log(err)
          }

          unittest_parameters = generate_unittest_parameters()
          execute_unittest_list(unittest_callbacks, 2, "unread_match_id_unittest", unittest_parameters)

          // const path = `/assistor_write_match_index_done/`

          // const assistor_write_match_index_done_data = {
          //   task_id: task_id
          // } 
          
          // vm.$axios.post(path, assistor_write_match_index_done_data)
          //   .then((response) => {
          //       // console.log('3.6 Assistor update done');
          //   })
          //   .catch((error)=>{
          //     // console.log(error)
          //   })   

        })
        .catch((error) => {
          // handle error
          // console.log(error)
        }) 
    },

    unread_situation(unread_situation_notification, unittest_callbacks) {

      let vm = this

      if (check_if_notification_is_null(unread_situation_notification, 'unread_situation_notification')){
        return
      }

      // // console.log("4.1 Update the situation notification", unread_situation_notification)
      // this.$toasted.success("4.1 Update the situation notification", { icon: 'fingerprint' })

      let cur_unread_situation_Taskid_dict = unread_situation_notification["check_dict"]
      let cur_unread_situation_Rounds_dict = unread_situation_notification["rounds_dict"]

      let unittest_parameters = generate_unittest_parameters(cur_unread_situation_Taskid_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_situation_unittest", unittest_parameters)

      for (let task_id in cur_unread_situation_Taskid_dict){

        log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

        
        const Log_address = this.handle_train_log_address(task_id)
        Log(generate_message_string("-------------------------- 4. Unread Situation\n"), 'info')
        Log(generate_message_string("4.1 Update the situation notification\n"), 'info')

        try {
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation\n")
          fs.appendFileSync(Log_address, "4.1 Update the situation notification\n")
        } catch (err) {
          // console.log(err)
        }

        let check_sponsor = cur_unread_situation_Taskid_dict[task_id];
        let rounds = cur_unread_situation_Rounds_dict[task_id];

        // check if the current client is sponsor or not of the specific task
        if (check_sponsor == 1){
          this.unread_situation_sponsor(rounds, task_id, unittest_callbacks)
        }  
        else{
          this.unread_situation_assistor(rounds, task_id, unittest_callbacks)
        }
      }
    },

    unread_situation_sponsor(rounds, task_id, unittest_callbacks) {
      let vm = this;
      // console.log("4.2 Cur round is:" + rounds + task_id);
      // vm.$toasted.success("4.2 Cur round is:" + rounds +  task_id, { icon: 'fingerprint' })
      log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

    
      const Log_address = vm.handle_train_log_address(task_id)

      Log(generate_message_string("4.2 Cur round is: " + rounds.toString() + "\n"), 'info')
      
      try {
        fs.appendFileSync(Log_address, "4.2 Cur round is: " + rounds.toString() + "\n")
      } catch (err) {
        // console.log(err)
      }

      var select_sentence = 'SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?'
      var param = [vm.sharedState.user_id, 'train', task_id]
      console.log('select_sentence', select_sentence)


      vm.$db.get(select_sentence, param, (err, row) => {
      if (err) {
        console.error(err);
      }
      
      // var row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?').get(vm.sharedState.user_id, 'train', task_id);

      let train_file_path = row.train_file_path
      // // console.log("train_file_path", train_file_path)
      let train_data_column = row.train_data_column
      // // console.log("train_data_column", train_data_column)
      // // console.log('row1', row)
      // let task_mode = row.task_mode
      let model_name = row.model_name

      let unittest_parameters = generate_unittest_parameters(train_file_path, train_data_column, model_name)
      execute_unittest_list(unittest_callbacks, 1, "unread_situation_unittest", unittest_parameters)

      try{
        
        // This calling make_train would not cause order issue since the send_situation is sent by sponsor itself
        let train_output = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root 
          + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds 
          + ' --dataset_path ' + train_file_path + ' --data_idx ' +train_data_column
          + ' --task_mode ' + 'regression' + ' --model_name ' + model_name, {encoding: 'utf8'})

  
        
        train_output = train_output.split("?")
        // // console.log('train_output1', train_output)
        let indicator = vm.handle_Algorithm_return_value("train_output", train_output, "200", "make_train")

        let unittest_parameters = generate_unittest_parameters(indicator)
        execute_unittest_list(unittest_callbacks, 2, "unread_situation_unittest", unittest_parameters)

        if (indicator == false){
          // console.log("train_output wrong")
          fs.appendFileSync(Log_address, "train_output wrong")
          return 
        }

        // console.log("4.3 Sponsor round " + rounds + " training done.");
        // vm.$toasted.success("4.3 Sponsor round " + rounds + " training done.", { icon: 'fingerprint' })
      
      }catch(err){
        // console.log(err)
      }
      Log(generate_message_string("4.3 Sponsor round " + rounds + " training done." + "\n"), 'info')
      Log(generate_message_string("-------------------------- 4. Unread Situation Done\n"), 'info')


      try {
        fs.appendFileSync(Log_address, "4.3 Sponsor round " + rounds + " training done." + "\n")
        fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation Done\n")
      } catch (err) {
        // console.log(err)
      }
      })
    },

    unread_situation_assistor_train_part(task_id, rounds, from_id, train_file_path, train_data_column, vm, Log_address, model_name, waiting_start_time, unittest_callbacks){
      

      log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      let waiting_current_time = new Date();
      // let waiting_current_time = myDate.toLocaleTimeString(); 
      let time_interval = waiting_current_time.getTime() - waiting_start_time.getTime()
      // // console.log("time_interval", time_interval)
      var leave1 = time_interval % (24*3600*1000) //计算天数后剩余的毫秒数
      var leave2 = leave1 % (3600*1000)             //计算小时数后剩余的毫秒数
      var minutes = Math.floor(leave2/(60*1000))  //间隔分钟
      
      if (minutes > 30){
        // // console.log('Waiting time interval exceeded')
        return 
      }
      let Assistor_train_output_path = null;
      // // console.log('wokan6', model_name )
      // get response from make_train.py. 
      let indicator = null;
      try{
        
        Assistor_train_output_path = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id '
          + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds + ' --from_id ' 
          + from_id + ' --dataset_path ' + train_file_path + ' --data_idx ' + train_data_column
          + ' --task_mode ' + 'regression' + ' --model_name ' + model_name ,{encoding: 'utf8'})

        Assistor_train_output_path = Assistor_train_output_path.split("?")
        indicator = vm.handle_Algorithm_return_value("Assistor_train_output_path", Assistor_train_output_path, "200", "make_train")
      }
      catch(err){
        // console.log(err)
      }

      // There some situations that the sponsor sends unread_situation faster than the assistor writes and translate the match id file.
      // We need to recall the function if the file is not prepared
      if (indicator == false){
        // console.log("recall unread_situation_assistor_train_part")
        setTimeout(function(){
          vm.unread_situation_assistor_train_part(task_id, rounds, from_id, train_file_path, train_data_column, vm, Log_address,task_mode, model_name)
        }, 7000);
      }else{
        
        // // console.log('Assistor_train_output_path', Assistor_train_output_path)
        // console.log("4.4 Assistor round " + rounds + " training done.");
        // vm.$toasted.success("4.4 Assistor round " + rounds + " training done.", { icon: 'fingerprint' })
        try {
          fs.appendFileSync(Log_address, "4.4 Assistor round " + rounds + " training done." + "\n")
        } catch (err) {
          // console.log(err)
        }

        let Assistor_train_output_data = fs.readFileSync(Assistor_train_output_path[2], {encoding:'utf8', flag:'r'});

        const Assistor_output_payload = {
          task_id: task_id,
          output: Assistor_train_output_data,
        }

        // send output
        // async
        vm.$axios.post('/send_output/', Assistor_output_payload)
          .then((response) => {
          // handle success
          // console.log("4.5 Assistor sends output")

          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 4, "unread_situation_unittest", unittest_parameters) 

          Log(generate_message_string("4.5 Assistor sends output\n"), 'info')
          Log(generate_message_string("-------------------------- 4. Unread Situation Done\n"), 'info')
          Log(generate_message_string("-------------------------- Train stage done\n"), 'info')

          // vm.$toasted.success("4.5 Assistor sends output", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.5 Assistor sends output\n")
            fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation Done\n")
            fs.appendFileSync(Log_address, "-------------------------- Train stage done\n")
          } catch (err) {
            // console.log(err)
          }
        })
        .catch((error) => {
          // console.log(error)
        })

      }
    },
    unread_situation_assistor(rounds, task_id, unittest_callbacks) {
      
      let vm = this;
      log.transports.file.resolvePath = () => node_path.join(this.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_train_log_address(task_id)

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      
      const path = `/users/${vm.sharedState.user_id}/situation_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // store the situation file

          let unittest_parameters = generate_unittest_parameters(response)
          execute_unittest_list(unittest_callbacks, 1, "unread_situation_unittest", unittest_parameters)

          // console.log("4.2 assistor gets situation file")
          // vm.$toasted.success("4.2 assistor gets situation file", { icon: 'fingerprint' })
          Log(generate_message_string("4.2 assistor gets situation file\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "4.2 assistor gets situation file\n")
          } catch (err) {
            // console.log(err)
          }

          const from_id = response.data.sender_random_id;
          let cur_situation_file = JSON.parse(response.data.situation);

          // Store residual file from sponsor
          let save_residual_file_pos = null;
          try{
            save_residual_file_pos = ex.execSync(vm.exe_position + ' save_residual --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --from_id ' + from_id + ' --round ' + rounds, {encoding: 'utf8'})
            
            save_residual_file_pos = save_residual_file_pos.split("?")
            let indicator = vm.handle_Algorithm_return_value("save_residual_file_pos", save_residual_file_pos, "200", "save_residual")

            // Unittest
            let unittest_parameters = generate_unittest_parameters(indicator)
            execute_unittest_list(unittest_callbacks, 2, "unread_situation_unittest", unittest_parameters)

            if (indicator == false){
              // console.log("save_residual_file_pos wrong")
              fs.appendFileSync(Log_address, "save_residual_file_pos wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          fs.writeFileSync(save_residual_file_pos[2], cur_situation_file)

          // console.log('4.3 Assistor Saved Residual File!');
          // vm.$toasted.success('4.3 Assistor Saved Residual File!', { icon: 'fingerprint' })
          Log(generate_message_string("4.3 Assistor Saved Residual File!\n"), 'info')

          try {
            fs.appendFileSync(Log_address, "4.3 Assistor Saved Residual File!\n")
          }catch (err) {
            // console.log(err)
          }

          // Assistor trains the data
          // // console.log("select_pending_record", select_pending_record)
          // // console.log('zz88', task_id)

          var select_sentence = 'SELECT * FROM User_Assistor_Table WHERE task_id = ? AND test_indicator = ? AND user_id = ?'
          var param = [task_id, 'train', vm.sharedState.user_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }

          // var row = vm.$db.prepare('SELECT * FROM User_Assistor_Table WHERE task_id = ? AND test_indicator = ? AND user_id = ?').get(task_id, 'train', vm.sharedState.user_id);
          
          let train_file_path = row.train_file_path
          // // console.log("train_file_path",train_file_path)
          let train_data_column = row.train_data_column
          // // console.log("train_data_column",train_data_column)
          let mode = row.mode
          // // console.log("mode",mode)
          let model_name = row.model_name 
          // // console.log("model_name",model_name)

          if (mode == "auto" || mode == 'manual'){
            
            let unittest_parameters = generate_unittest_parameters(train_file_path, train_data_column, mode, model_name)
            execute_unittest_list(unittest_callbacks, 3, "unread_situation_unittest", unittest_parameters)  

            let waiting_start_time = new Date();
            // let waiting_start_time = myDate.getMinutes();
            // var waiting_start_time = myDate.toLocaleTimeString(); 
            vm.unread_situation_assistor_train_part(task_id, rounds, from_id, train_file_path, train_data_column, vm, Log_address, model_name, waiting_start_time, unittest_callbacks)
          }else{
            // console.log('unread situation assistor 3rd case')
          }
          }) 
        }) //end axios
        .catch((error) => {
          // console.log(error)
          // handle error
        })
    },
    
    unread_output(unread_output_notification, unittest_callbacks) {

      let vm = this

      // Only sponsor will enter this function
      if (check_if_notification_is_null(unread_output_notification, 'unread_output_notification')){
        return
      }

      // Only sponsor would receive unread_output
      // // console.log("5.1 Update the output notification", unread_output_notification)
      // this.$toasted.success("5.1 Update the output notification", { icon: 'fingerprint' })

      let cur_unread_output_Rounds_dict = unread_output_notification["rounds_dict"]

      let unittest_parameters = generate_unittest_parameters(cur_unread_output_Rounds_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_output_unittest", unittest_parameters)

      for (let task_id in cur_unread_output_Rounds_dict){

        log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

        Log(generate_message_string("-------------------------- 5. Unread Output\n"), 'info')
        Log(generate_message_string("5.1 Update the output notification\n"), 'info')

        const Log_address = this.handle_train_log_address(task_id)
        try {
          fs.appendFileSync(Log_address, "-------------------------- 5. Unread Output\n")
          fs.appendFileSync(Log_address, "5.1 Update the output notification\n")
        } catch (err) {
          // console.log(err)
        }
        let rounds = cur_unread_output_Rounds_dict[task_id];
        this.unread_output_singleTask(rounds, task_id, unittest_callbacks);
      }
    },

    unread_output_singleTask(rounds, task_id, unittest_callbacks){
      
      let vm = this

      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_train_log_address(task_id)
      // const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      
      // Obtain output from assistors

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      const url = `/users/${vm.sharedState.user_id}/output/`

      this.$axios.post(url, payload)
        .then((response) => {
          // console.log("5.2 Sponsor gets output model")
          // vm.$toasted.success("5.2 Sponsor gets output model", { icon: 'fingerprint' })

          try {
            fs.appendFileSync(Log_address, "5.2 Sponsor gets output model\n")
          } catch (err) {
            // console.log(err)
          }
          // iterate the output file
          for(let i = 0;i < response.data.output.length; i++){

            const from_id = response.data.sender_random_ids_list[i];

            // // console.log("cur_output^^^^^^^^", response.data.output[i])
            let cur_output = JSON.parse(response.data.output[i]);
            // // console.log("cur_output^^^^^^^^1", cur_output)

            // Store the output from assistor
            let save_output_pos = null;
            try{
              // // console.log('train_cur_round',  rounds)
              save_output_pos = ex.execSync(vm.exe_position + ' save_output --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id + ' --round ' + rounds, {encoding: 'utf8'})

              save_output_pos = save_output_pos.split("?")
              let indicator = vm.handle_Algorithm_return_value("save_output_pos", save_output_pos, "200", "save_output")

              let unittest_parameters = generate_unittest_parameters(indicator)
              execute_unittest_list(unittest_callbacks, 1, "unread_output_unittest", unittest_parameters)


              if (indicator == false){
                // console.log("save_output_pos wrong")
                fs.appendFileSync(Log_address, "save_output_pos wrong")
                return 
              }

            }catch(err){
            // console.log(err)
          }

            fs.writeFileSync(save_output_pos[2], cur_output)           

            // console.log('5.3 Sponsor saves Output model');
            // vm.$toasted.success('5.3 Sponsor saves Output model', { icon: 'fingerprint' })
            Log(generate_message_string("5.3 Sponsor saves Output model\n"), 'info')

            try {
              fs.appendFileSync(Log_address, "5.3 Sponsor saves Output model\n")
            } catch (err) {
              // console.log(err)
            }
          }

          var select_sentence = 'SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?'
          var param = [vm.sharedState.user_id, 'train', task_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }

          // let select_train_target_path = 'SELECT * FROM User_Sponsor_Table WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' + ' AND "task_id"="' + task_id + '"';
          // var row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND task_id = ?').get(vm.sharedState.user_id, 'train', task_id);

          // // console.log('select train target path', row)
          let train_file_path = row.train_file_path
          // // console.log("train_file_path", train_file_path)
          let train_target_column = row.train_target_column
          // // console.log("train_target_column", train_target_column)
          let task_mode = row.task_mode
          let metric_name = row.metric_name

          let unittest_parameters = generate_unittest_parameters(train_file_path, train_target_column, task_mode, metric_name)
          execute_unittest_list(unittest_callbacks, 2, "unread_output_unittest", unittest_parameters)

          let waiting_start_time = new Date();
          vm.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column, vm, Log_address, task_mode, metric_name, waiting_start_time, unittest_callbacks)

          })
        })
        .catch((error) => {
          // handle error
          // console.log(error)
        }) 
    },

    unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column, vm, Log_address, task_mode, metric_name, waiting_start_time, unittest_callbacks){
      
      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      let waiting_current_time = new Date();
      // let waiting_current_time = myDate.toLocaleTimeString(); 
      let time_interval = waiting_current_time.getTime() - waiting_start_time.getTime()
      // // console.log("time_interval", time_interval)
      var leave1 = time_interval % (24*3600*1000) //计算天数后剩余的毫秒数
      var leave2 = leave1 % (3600*1000)             //计算小时数后剩余的毫秒数
      var minutes = Math.floor(leave2/(60*1000))  //间隔分钟
      
      if (minutes > 30){
        // // console.log('Waiting time interval exceeded')
        return 
      }

      // // console.log("unread_output_make_result_helper_rounds", rounds)
      let make_result_done = null;
      let indicator = null;
      try{

        make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
          + ' --task_id '+ task_id + ' --round ' + rounds + ' --dataset_path ' + train_file_path 
          + ' --target_idx ' + train_target_column + ' --task_mode ' + task_mode 
          + ' --metric_name ' + metric_name, {encoding: 'utf8'}) 


        make_result_done = make_result_done.split("?")
        indicator = vm.handle_Algorithm_return_value("make_result_done", make_result_done, "200", "make_result")

      }catch(err){
        // console.log(err)
      }

      // When assistors train faster than sponsor and send their results, make_result might not find the sponsor's train results.
      // We need to recall the function
      if(indicator == false){
        // console.log("recall unread_output_make_result_helper")
        setTimeout(function(){
          vm.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_column, vm, Log_address)
        }, 7000);

      }else{
        // // console.log("jinlaile")
        // console.log("5.4 Sponsor makes result done.")
        // vm.$toasted.success("5.4 Sponsor makes result done.", { icon: 'fingerprint' })
        Log(generate_message_string("5.4 Sponsor makes result done." + "\n"), 'info')

        try {
          fs.appendFileSync(Log_address, "5.4 Sponsor makes result done." + "\n")
        } catch (err) {
          // console.log(err)
        }
        
        // terminate
        // // console.log('max_round', rounds, vm.max_round)
        Log(generate_message_string("---------------------- Train stage done\n"), 'info')

        if (rounds >= vm.max_round){
          vm.$toasted.success("Training Done", { icon: 'fingerprint' })
          fs.appendFileSync(Log_address, "---------------------- Train stage done\n");
        }else{        

        let make_residual_multiple_paths = null;
        try{

          make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
            + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + (rounds+1)
            + ' --dataset_path ' + train_file_path + ' --target_idx ' + train_target_column
            + ' --task_mode ' + task_mode + ' --metric_name ' + metric_name, {encoding: 'utf8'})

          make_residual_multiple_paths = make_residual_multiple_paths.split("?")
          let indicator = vm.handle_Algorithm_return_value("make_residual_multiple_paths", make_residual_multiple_paths, "200", "make_residual")
          if (indicator == false){
            // console.log("make_residual_multiple_paths wrong")
            fs.appendFileSync(Log_address, "make_residual_multiple_paths wrong")
            return 
          }

          }catch(err){
          // console.log(err)
        }

        // console.log("5.5 Sponsor makes residual finished")
        // vm.$toasted.success("5.5 Sponsor makes residual finished", { icon: 'fingerprint' })
        Log(generate_message_string("5.5 Sponsor makes residual finished\n"), 'info')

        try {
          fs.appendFileSync(Log_address, "5.5 Sponsor makes residual finished\n")
        } catch (err) {
          // console.log(err)
        }

        let all_residual_data = [];
        let assistor_random_id_list = [];
        let residual_paths = make_residual_multiple_paths.slice(2, make_residual_multiple_paths.length)
        for (let i = 0; i < residual_paths.length; i++){
          let data = fs.readFileSync(residual_paths[i], {encoding:'utf8', flag:'r'});
          all_residual_data.push(data);

          let path_split = residual_paths[i].split(node_path.sep);
          let assistor_random_id = path_split[path_split.length-1].split(".")[0];
          assistor_random_id_list.push(assistor_random_id);
          
        }

        const payload1 = {
          residual_list: all_residual_data,
          task_id: task_id,
          assistor_random_id_list: assistor_random_id_list,
        }

        // send initial situation
        // async
        vm.$axios.post('/send_situation/', payload1)
          .then((response) => {
            // handle success
            // // console.log("5.6 Sponsor updates situation done", response)
            let unittest_parameters = generate_unittest_parameters(response.data)
            execute_unittest_list(unittest_callbacks, 3, "unread_output_unittest", unittest_parameters)
            // vm.$toasted.success("5.6 Sponsor updates situation done", { icon: 'fingerprint' })
            Log(generate_message_string("5.6 Sponsor updates situation done\n"), 'info')
            Log(generate_message_string("------------------------- 5. Unread Output Done\n"), 'info')

            try {
              fs.appendFileSync(Log_address, "5.6 Sponsor updates situation done\n")
              fs.appendFileSync(Log_address, "-------------------------- 5. Unread Output Done\n")
            } catch (err) {
              // console.log(err)
            }
          })
          .catch((error) => {
            // console.log(error)
          })
        }
      }
    },
    
    
    unread_test_request(unread_test_request_notification, unittest_callbacks) {

      // Only assistor will enter this function
      if (check_if_notification_is_null(unread_test_request_notification, 'unread_test_request_notification')){
        return
      }

      let vm = this;
        
      // // console.log("2.1 Update Test request notification response", unread_test_request_notification)
      // this.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })

      let cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
      let test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

      let unittest_parameters = generate_unittest_parameters(cur_unread_test_request_Testid_dict, test_id_to_task_id)
      execute_unittest_list(unittest_callbacks, 0, "unread_test_request_unittest", unittest_parameters)

      var select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id = ?'
      var param = [vm.sharedState.user_id]
      console.log('select_sentence', select_sentence)


      vm.$db.get(select_sentence, param, (err, row) => {
      if (err) {
        console.error(err);
      }
         
      // var row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ?').get(vm.sharedState.user_id);
      // // console.log("retrieve_setting_mode_row", row)

      if (row == null){
        vm.sharedState.mode = "manual";
      }
      else{
        vm.sharedState.mode = row.default_mode;
      }  

      for (let test_id in cur_unread_test_request_Testid_dict){
        let task_id = test_id_to_task_id[test_id]

        log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');
     
        // // console.log('unread test request mode', vm.sharedState.mode)
        if (vm.sharedState.mode == 'auto'){

          var select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id = ?'
          var param = [vm.sharedState.user_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }
          
          // var row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ?').get(vm.sharedState.user_id);
          // // console.log("default_row", row)
          let default_file_path = row.default_file_path
          let default_id_column = row.default_id_column
          let default_data_column = row.default_data_column
          let default_target_column = row.default_target_column
          let default_mode = row.default_mode
          let default_model_name = row.default_model_name

          let test_hash_id_file_address = null
          let Log_address = null


          var sentence = `INSERT INTO User_Assistor_Table (user_id, task_id, test_id, task_name, task_description, test_name, test_description, train_file_path,' +
          ' train_id_column, train_data_column, train_target_column, test_file_path, test_id_column,' +
          ' test_data_column, test_target_column, mode, test_indicator, model_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          var param = [vm.sharedState.user_id, task_id, test_id, '', '', '', '', '', '', '', '', default_file_path, default_id_column,
                      default_data_column, default_target_column, default_mode, 'test', default_model_name]

          vm.$db.run(sentence, param, function(err){
                      if (err){
                        console.log('err info',err);
                      }
 

          // const stmt = vm.$db.prepare('INSERT INTO User_Assistor_Table VALUES' +
          // ' ( @user_id, @task_id, @test_id, @task_name, @task_description, @test_name, @test_description, @train_file_path,' +
          // ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
          // ' @test_data_column, @test_target_column, @mode, @test_indicator, @model_name)');
             
          // stmt.run({
          //   user_id: vm.sharedState.user_id, 
          //   task_id: task_id,
          //   test_id: test_id,
          //   task_name: '', 
          //   task_description: '', 
          //   test_name: '',
          //   test_description: '',
          //   train_file_path: '', 
          //   train_id_column: '', 
          //   train_data_column: '', 
          //   train_target_column: '', 
          //   test_file_path: default_file_path,
          //   test_id_column: default_id_column,
          //   test_data_column: default_data_column,
          //   test_target_column: default_target_column,
          //   mode: default_mode, 
          //   test_indicator: 'test',
          //   model_name: default_model_name
          // });


          let unittest_parameters = generate_unittest_parameters(test_id, vm.sharedState.mode)
          execute_unittest_list(unittest_callbacks, 1, "unread_test_request_unittest", unittest_parameters)

          try{

            test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
                                      + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id
                                      + ' --mode test' + ' --test_id ' + test_id
                                      + ' --dataset_path ' + default_file_path + ' --id_idx ' + default_id_column, {encoding: 'utf8'})

            

            test_hash_id_file_address = test_hash_id_file_address.split("?")
            let indicator = vm.handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")

            
            unittest_parameters = generate_unittest_parameters(indicator)
            execute_unittest_list(unittest_callbacks, 2, "unread_test_request_unittest", unittest_parameters)


            Log_address = vm.handle_test_log_address(task_id, test_id)
            // // console.log('daozhele')
            if (indicator == false){
              // console.log("test_hash_id_file_address wrong")
              fs.appendFileSync(Log_address, "test_hash_id_file_address wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }
            Log(generate_message_string("\n You are Assistor\n"), 'info')
            Log(generate_message_string("Test ID: " + test_id + "\n"), 'info')
            Log(generate_message_string("-----------------------Test Stage: 2.Unread Test Request\n"), 'info')
            Log(generate_message_string("2.1 Test: Update Test request notification\n"), 'info')
            Log(generate_message_string("2.2 Test: Hashing Done\n"), 'info')


          try {
            fs.appendFileSync(Log_address, "\n You are Assistor\n")
            fs.appendFileSync(Log_address, "Test ID: " + test_id + "\n")
            fs.appendFileSync(Log_address, "-----------------------Test Stage: 2.Unread Test Request\n")
            fs.appendFileSync(Log_address, "2.1 Test: Update Test request notification\n")
            fs.appendFileSync(Log_address, "2.2 Test: Hashing Done\n")
          } catch (err) {
            // console.log(err)
          }

          let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});

          const match_test_assistor_id_data = {
            file: test_hash_id_file_data,
            task_id: task_id,
            test_id: test_id
          }

          vm.$axios.post('/match_test_assistor_id/', match_test_assistor_id_data)
            .then((response) => {
              // handle success
              // // console.log("2.2 Test: assistor uploads id file")

              unittest_parameters = generate_unittest_parameters(response.data)
              execute_unittest_list(unittest_callbacks, 3, "unread_test_request_unittest", unittest_parameters)

              Log(generate_message_string("2.2 Test: assistor uploads id file\n"), 'info')
              Log(generate_message_string("--------------------------2. Unread Test Request Done\n"), 'info')

              // vm.$toasted.success(`2.2 Test: assistor uploads id file`, { icon: 'fingerprint' })
              try {
                fs.appendFileSync(Log_address, "2.2 Test: assistor uploads id file\n")
                fs.appendFileSync(Log_address, "--------------------------2. Unread Test Request Done\n")
              } catch (err) {
                // console.log(err)
              }
            })
            .catch((error) => {
              // handle error
              // console.log(error)
              // // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })
          })
          })
        }else if (vm.sharedState.mode == 'manual'){
          // // console.log(task_id)
          vm.sharedState.pending_num++;
          const add_test_pending = {
              test_id: test_id,
            }
          
          vm.$axios.post('/add_test_pending/', add_test_pending)
            .then((response) => {
              // handle success
              // // console.log("add_test_pending response", response.data)
            })
            .catch((error) => {
              // handle error
              // console.log(error)
              // // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })
        }else{
          // console.log("unread request: If you want to receive, open receive")
          // dialog.showErrorBox('Please Open the Receive', "unread request: If you want to receive, open receive")
        }
      }
      })
    },

    unread_test_match_id(unread_test_match_id_notification, unittest_callbacks) {
      let vm = this
      if (check_if_notification_is_null(unread_test_match_id_notification, 'unread_test_match_id_notification')){
        return
      }

      // // console.log("3.1 Update Test match id notification response", unread_test_match_id_notification)
      // this.$toasted.success("3.1 Update the Test match id notification", { icon: 'fingerprint' })

      let cur_unread_test_match_id_Testid_dict = unread_test_match_id_notification["check_dict"]
      let test_id_to_task_id = unread_test_match_id_notification["test_id_to_task_id"]
      let max_rounds_dict = unread_test_match_id_notification["max_rounds"]
      // // console.log("max_rounds_dict", max_rounds_dict)

      let unittest_parameters = generate_unittest_parameters(cur_unread_test_match_id_Testid_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_test_match_id_unittest", unittest_parameters)

      for (let test_id in cur_unread_test_match_id_Testid_dict){
        let task_id = test_id_to_task_id[test_id]

        log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');


        const Log_address = this.handle_test_log_address(task_id, test_id)

        Log(generate_message_string("-----------------------3.Unread Test Match ID\n"), 'info')
        Log(generate_message_string("3.1 Test: Update the Test match id notification\n"), 'info')


        try {
          fs.appendFileSync(Log_address, "-----------------------3.Unread Test Match ID\n")
          fs.appendFileSync(Log_address, "3.1 Test: Update the Test match id notification\n")
        } catch (err) {
          // console.log(err)
        }

        let check_sponsor = cur_unread_test_match_id_Testid_dict[test_id]
        let cur_max_round = max_rounds_dict[test_id]
        // // console.log("test_id, max_round", test_id, cur_max_round)

        if (check_sponsor == 1){
          // console.log("3.2 Unread_test_match_id_sponsor")
          try {
            fs.appendFileSync(Log_address, "3.2 Test: Unread_test_match_id_sponsor\n")
          } catch (err) {
            // console.log(err)
          }
          this.unread_test_match_id_sponsor(task_id, test_id, cur_max_round, unittest_callbacks)
        }  
        else{
          // console.log("3.2 Unread_test_match_id_assistor")
          try {
            fs.appendFileSync(Log_address, "3.2 Test: Unread_test_match_id_assistor\n")
          } catch (err) {
            // console.log(err)
          }
          this.unread_test_match_id_assistor(task_id, test_id, cur_max_round, unittest_callbacks)
        }
      }
    },

    unread_test_match_id_sponsor(task_id, test_id, max_rounds, unittest_callbacks) {

      
      let vm = this;

      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_test_log_address(task_id, test_id)
      

      // Obtain Match_id file
      // async
      const payload = {
        task_id: task_id,
        test_id: test_id
      }
      
      const path = `/users/${vm.sharedState.user_id}/test_match_id_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // iterate the match_id_file

          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 1, "unread_test_match_id_unittest", unittest_parameters)

          // console.log("3.4 Test: Sponsor gets matched id file")
          // vm.$toasted.success("3.4 Test: Sponsor gets matched id file", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Test: Sponsor gets matched id file\n")
          } catch (err) {
            // console.log(err)
          }

          for(let i = 0;i < response.data.match_id_file.length; i++){
            
            const from_id = response.data.assistor_random_id_pair[i];
            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');
            // // console.log('sponsor_match', cur_match_id_file)
            // Store match_id file from different assistor
            let test_save_match_id_file_pos = null;
            try{
              test_save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --from_id ' + from_id  + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})
              
              test_save_match_id_file_pos = test_save_match_id_file_pos.split("?")
              let indicator = vm.handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos, "200", "save_match_id")
              if (indicator == false){
                // console.log("test_save_match_id_file_pos wrong")
                fs.appendFileSync(Log_address, "test_save_match_id_file_pos wrong")
                return 
              }

            }catch(err){
              // console.log(err)
            }

            fs.writeFileSync(test_save_match_id_file_pos[2], cur_match_id_file)

            let unittest_parameters = generate_unittest_parameters()
            execute_unittest_list(unittest_callbacks, 2, "unread_test_match_id_unittest", unittest_parameters)

            
            // console.log('3.5 Test: Sponsor Saved Matched id File!');
            // vm.$toasted.success('3.5 Test: Sponsor Saved Matched id File!', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.5 Test: Sponsor Saved Matched id File!\n")
            } catch (err) {
              // console.log(err)
            }

            try{
              let test_make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --from_id ' + from_id  + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})

              test_make_match_idx_done = test_make_match_idx_done.split("?")
              let indicator = vm.handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
              if (indicator == false){
                // console.log("test_make_match_idx_done wrong")
                fs.appendFileSync(Log_address, "test_make_match_idx_done wrong")
                return 
              }
              
            }catch(err){
              // console.log(err)
            }

            // console.log('3.6 Test: Sponsor matches id to index');
            // vm.$toasted.success('3.6 Test: Sponsor matches id to index', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.6 Test: Sponsor matches id to index\n")
            } catch (err) {
              // console.log(err)
            }

          }

          var select_sentence = 'SELECT test_file_path, test_data_column FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND test_id = ?'
          var param = [vm.sharedState.user_id, 'test', test_id]
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }

          // var row = vm.$db.prepare('SELECT test_file_path, test_data_column FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND test_id = ?').get(vm.sharedState.user_id, 'test', test_id);
          
          let test_file_path = row.test_file_path
          let test_data_column = row.test_data_column
          // // console.log("test_file_path", test_file_path, max_rounds)
          
          try{
            let test_done = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
              + ' --task_id ' + task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --dataset_path ' + test_file_path + ' --data_idx ' + test_data_column, {encoding: 'utf8'})

            test_done = test_done.split("?")
            let make_test_res = JSON.parse(test_done[2])
            let unittest_parameters = generate_unittest_parameters(make_test_res)
            execute_unittest_list(unittest_callbacks, 3, "unread_test_match_id_unittest", unittest_parameters)

            let indicator = vm.handle_Algorithm_return_value("test_done", test_done, "200", "make_test")
            if (indicator == false){
              // console.log("test_done wrong")
              fs.appendFileSync(Log_address, "test_done wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          // console.log("3.7 Test: Sponsor stores all test model results")
          // vm.$toasted.success("3.7 Test: Sponsor stores all test model results", { icon: 'fingerprint' })

          try {
            fs.appendFileSync(Log_address, "3.7 Test: Sponsor stores all test model results\n")
            fs.appendFileSync(Log_address, "--------------------------3. Unread Test Match ID Done\n")
          } catch (err) {
            // console.log(err)
          }
      
          })
        })
        .catch((error) => {
          // console.log(error)
          // handle error
        }) 

         
    },

    unread_test_match_id_assistor(task_id, test_id, max_rounds, unittest_callbacks) {

      let vm = this;

      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      const Log_address = vm.handle_test_log_address(task_id, test_id)
      
      // Obtain Match_id file
      const payload = {
        task_id: task_id,
        test_id: test_id
      }
      const path = `/users/${vm.sharedState.user_id}/test_match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 1, "unread_test_match_id_unittest", unittest_parameters)


          // console.log("3.4 Test: assistor gets matched id file", response)
          // vm.$toasted.success("3.4 Test: assistor gets matched id file", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Test: assistor gets matched id file\n")
          } catch (err) {
            // console.log(err)
          }

          const from_id = response.data.sponsor_random_id;
          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join('\n');
          // // console.log('assistor_match', cur_match_id_file)

          // Store match_id file from sponsor
          let test_save_match_id_file_pos = null;
          try{
           
            test_save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --from_id ' + from_id + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})

            test_save_match_id_file_pos = test_save_match_id_file_pos.split("?")
            let indicator = vm.handle_Algorithm_return_value("test_save_match_id_file_pos", test_save_match_id_file_pos, "200", "save_match_id")
            if (indicator == false){
              // console.log("test_save_match_id_file_pos wrong")
              fs.appendFileSync(Log_address, "test_save_match_id_file_pos wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          fs.writeFileSync(test_save_match_id_file_pos[2], cur_match_id_file)
          
          // console.log('3.5 Test: Assistor Saved Matched id File!');
          // vm.$toasted.success('3.5 Test: Assistor Saved Matched id File!', { icon: 'fingerprint' })


          unittest_parameters = generate_unittest_parameters()
          execute_unittest_list(unittest_callbacks, 2, "unread_test_match_id_unittest", unittest_parameters)

          try {
            fs.appendFileSync(Log_address, "3.5 Test: Assistor Saved Matched id File!\n")
          } catch (err) {
            // console.log(err)
          }

          try{

            let test_make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --from_id ' + from_id + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})

            test_make_match_idx_done = test_make_match_idx_done.split("?")
            let indicator = vm.handle_Algorithm_return_value("test_make_match_idx_done", test_make_match_idx_done, "200", "make_match_idx")
            if (indicator == false){
              // console.log("test_make_match_idx_done wrong")
              fs.appendFileSync(Log_address, "test_make_match_idx_done wrong")
              return 
            }

          }catch(err){
            // console.log(err)
          }

          // console.log('3.6 Test: Assistor matches id to index');
          // vm.$toasted.success('3.6 Test: Assistor matches id to index', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.6 Test: Assistor matches id to index\n")
          } catch (err) {
            // console.log(err)
          }

          var select_sentence = 'SELECT * FROM User_Assistor_Table WHERE user_id = ? AND test_id = ? AND test_indicator = ?'
          var param = [vm.sharedState.user_id, test_id, 'test']
          console.log('select_sentence', select_sentence)


          vm.$db.get(select_sentence, param, (err, row) => {
          if (err) {
            console.error(err);
          }

          // var row = vm.$db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND test_id = ? AND test_indicator = ?').get(vm.sharedState.user_id, test_id, 'test');

          let mode = row.mode
          let test_file_path = row.test_file_path
          let test_data_column = row.test_data_column
          // // console.log('zzz77', from_id)
          unittest_parameters = generate_unittest_parameters(test_file_path, test_data_column)
          execute_unittest_list(unittest_callbacks, 3, "unread_test_match_id_unittest", unittest_parameters)

          if(mode == "auto" || mode == "manual"){
            
            let test_outputs_pos = null
            try{

              test_outputs_pos = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                + ' --task_id ' + task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --from_id ' + from_id 
                + ' --dataset_path ' +  test_file_path + ' --data_idx ' + test_data_column, {encoding: 'utf8'})

              test_outputs_pos = test_outputs_pos.split("?")

              let make_test_assistor_res = JSON.parse(test_outputs_pos[2])
              console.log('wawa', make_test_assistor_res)
              let unittest_parameters = generate_unittest_parameters(make_test_assistor_res)
              execute_unittest_list(unittest_callbacks, 4, "unread_test_match_id_unittest", unittest_parameters)
              
              let indicator = vm.handle_Algorithm_return_value("test_outputs_pos", test_outputs_pos, "200", "make_test")
              if (indicator == false){
                // console.log("test_outputs_pos wrong")
                fs.appendFileSync(Log_address, "test_outputs_pos wrong")
                return 
              }
              
            }catch(err){
              // console.log(err)
            }

            // console.log("3.7 Test: assistor stores all test model results")
            // vm.$toasted.success("3.7 Test: assistor stores all test model results", { icon: 'fingerprint' })

            try {
              fs.appendFileSync(Log_address, "3.7 Test: assistor stores all test model results\n")
            } catch (err) {
              // console.log(err)
            }

            let all_test_output = [];
            let make_test_lists = test_outputs_pos.slice(3, test_outputs_pos.length)
            // // console.log("make_test_lists", make_test_lists)
            for (let i = 0; i < make_test_lists.length; i++){
              let data = fs.readFileSync(make_test_lists[i], {encoding:'utf8', flag:'r'});
              all_test_output.push(data);
            }
            // // console.log("all_test_output", all_test_output)

            const payload1 = {
              output: all_test_output,
              test_id: test_id,
              task_id: task_id,
            }

            vm.$axios.post('/send_test_output/', payload1)
              .then((response) => {
              // handle success
              let unittest_parameters = generate_unittest_parameters(response.data)
              execute_unittest_list(unittest_callbacks, 5, "unread_test_match_id_unittest", unittest_parameters)

              // console.log("3.8 Test: assistor sends all test model results")
              // vm.$toasted.success("3.8 Test: assistor sends all test model results", { icon: 'fingerprint' })
              try {
                fs.appendFileSync(Log_address, "3.8 Test: assistor sends all test model results\n")
                fs.appendFileSync(Log_address, "-------------------------- 3. Unread Test Match ID Done\n")
                fs.appendFileSync(Log_address, "-------------------------- Test stage done\n")
              } catch (err) {
                // console.log(err)
              }
            })
            .catch((error) => {
              // console.log(error)
            })
          
          }else{
            // console.log('unread_test_match_id_assistor error')
          }
          
          })
        })
        .catch((error) => {
          // handle error
          // console.log(error)
        }) 
    },

    unread_test_output(unread_test_output_notification, unittest_callbacks) {
      
      let vm = this;
      // only sponsor will enter this function
      if (check_if_notification_is_null(unread_test_output_notification, 'unread_test_output_notification')){
        return
      }

      // console.log("4.1 Update Test output notification", unread_test_output_notification)
      // this.$toasted.success("4.1 Update Test output notification", { icon: 'fingerprint' })

      let cur_unread_test_output_Testid_dict = unread_test_output_notification["check_dict"]
      let test_id_to_task_id = unread_test_output_notification["test_id_to_task_id"]

      let unittest_parameters = generate_unittest_parameters(cur_unread_test_output_Testid_dict)
      execute_unittest_list(unittest_callbacks, 0, "unread_test_output_unittest", unittest_parameters)

      for (let test_id in cur_unread_test_output_Testid_dict){
        let task_id = test_id_to_task_id[test_id]

        log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');


        const Log_address = this.handle_test_log_address(task_id, test_id)

        try {
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Test Output\n")
          fs.appendFileSync(Log_address, "4.1 Update Test output notification\n")
        } catch (err) {
          // console.log(err)
        }
        this.unread_test_output_singleTask(task_id, test_id, unittest_callbacks);
      }
    },

    unread_test_output_singleTask(task_id, test_id, unittest_callbacks){

      const Log_address = this.handle_test_log_address(task_id, test_id)

      let vm = this
      // Obtain output from assistors
      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');


      const payload = {
        task_id: task_id, 
        test_id: test_id,
      }

      const url = `/test_output/`
      this.$axios.post(url, payload)
        .then((response) => {
          // console.log("4.2 Test: Sponsor gets assistors' Test output model")
          // vm.$toasted.success("4.2 Test: Sponsor gets assistors' Test output model", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.2 Test: Sponsor gets assistors' Test output model\n")
          } catch (err) {
            // console.log(err)
          }
          // iterate the match_id_file
          // List[List[List]] structure: [[[data from one assistor],[data from one assistor]],[[data from another assistor],[data from another assistor]]]
          for(let i = 0;i < response.data.output.length; i++){

            const from_id = response.data.sender_random_ids_list[i];
            let multiple_outputs_from_one_assistor = JSON.parse(response.data.output[i]);
            // // console.log("multiple_outputs_from_one_assistor", multiple_outputs_from_one_assistor)

            for (let j = 0; j < multiple_outputs_from_one_assistor.length; j++){
              let cur_output = multiple_outputs_from_one_assistor[j];
              
              // Store test output from assistors
              let test_save_output_pos = null
              try{

                test_save_output_pos = ex.execSync(vm.exe_position + ' save_output --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                  + ' --task_id '+ task_id + ' --mode test --test_id ' + test_id + ' --from_id ' + from_id + ' --round ' + (j+1), {encoding: 'utf8'})

                // // console.log('test save output pos', test_save_output_pos)
                test_save_output_pos = test_save_output_pos.split("?")
                // // console.log('test_save_output_pos', test_save_output_pos)
                let indicator = vm.handle_Algorithm_return_value("test_save_output_pos", test_save_output_pos, "200", "save_output")

                let unittest_parameters = generate_unittest_parameters(indicator)
                execute_unittest_list(unittest_callbacks, 1, "unread_test_output_unittest", unittest_parameters)

                if (indicator == false){
                  // console.log("test_save_output_pos wrong")
                  fs.appendFileSync(Log_address, "test_save_output_pos wrong")
                  return 
                }

              }catch(err){
                // console.log(err)
              }

              // Store match_id file
              // // console.log('wokan1', cur_output)
              fs.writeFileSync(test_save_output_pos[2], cur_output)
            }

          }//end for loop
          // console.log("4.3 Test: Sponsor saves assistors' Output model");

          // vm.$toasted.success("4.3 Test: Sponsor saves assistors' Output model", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.3 Test: Sponsor saves assistors' Output model\n")
          } catch (err) {
            // console.log(err)
          }
          let waiting_start_time = new Date()
          vm.unread_test_output_make_eval_helper(task_id, test_id, vm, Log_address, response, waiting_start_time, unittest_callbacks)

        })
        .catch((error) => {
            // handle error
          // console.log(error)
        }) 

          
    },

    unread_test_output_make_eval_helper(task_id, test_id, vm, Log_address, response, waiting_start_time, unittest_callbacks){
      
      log.transports.file.resolvePath = () => node_path.join(vm.root.toString(), '/logs', vm.sharedState.user_id.toString(), task_id.toString(), 'log.txt');

      let waiting_current_time = new Date();
      // let waiting_current_time = myDate.toLocaleTimeString(); 
      let time_interval = waiting_current_time.getTime() - waiting_start_time.getTime()
      // // console.log("time_interval", time_interval)
      var leave1 = time_interval % (24*3600*1000) //计算天数后剩余的毫秒数
      var leave2 = leave1 % (3600*1000)             //计算小时数后剩余的毫秒数
      var minutes = Math.floor(leave2/(60*1000))  //间隔分钟
      
      if (minutes > 30){
        // // console.log('Waiting time interval exceeded')
        return 
      }

      let max_round = JSON.parse(response.data.output[0]).length;
      // // console.log("unread_test_output_max_round", JSON.parse(response.data.output[0]))
      // // console.log("max_round", max_round)

      var select_sentence = 'SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND test_id = ?'
      var param = [vm.sharedState.user_id, 'test', test_id]
      console.log('select_sentence', select_sentence)


      vm.$db.get(select_sentence, param, (err, row) => {
      if (err) {
        console.error(err);
      }

      // var row = vm.$db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND test_indicator = ? AND test_id = ?').get(vm.sharedState.user_id, 'test', test_id);

      let test_file_path = row.test_file_path
      let test_target_column = row.test_target_column
      let task_mode = row.task_mode
      let metric_name = row.metric_name
      // // console.log("test_target_path",test_target_path)
      let eval_done = null;
      let indicator = null;
      try{

        eval_done = ex.execSync(vm.exe_position + ' make_eval --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
          + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_round 
          + ' --dataset_path ' + test_file_path + ' --target_idx ' + test_target_column
          + ' --task_mode ' + task_mode + ' --metric_name ' + metric_name, {encoding: 'utf8'})

        eval_done = eval_done.split("?")
        // // console.log('wokan2', eval_done)
        let make_eval_res = JSON.parse(eval_done[2])
        let unittest_parameters = generate_unittest_parameters(make_eval_res)
        execute_unittest_list(unittest_callbacks, 2, "unread_test_output_unittest", unittest_parameters)

        indicator = vm.handle_Algorithm_return_value("eval_done", eval_done, "200", "make_eval")
      }catch(err){
        // console.log(err)
      }

      if (indicator == false){
        // console.log("recall unread_test_output_make_eval_helper")
        setTimeout(function(){
          vm.unread_test_output_make_eval_helper(task_id, test_id, vm, Log_address, response, waiting_start_time, unittest_callbacks)
        }, 7000);
      }else{
        

        // console.log("4.4 Test: Sponsor evaluates output models done");
        vm.$toasted.success("Testing Done", { icon: 'fingerprint' })
        try {
          fs.appendFileSync(Log_address, "4.4 Test: Sponsor evaluates output models done\n")
        } catch (err) {
          // console.log(err)
        }

        try {
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Test Output Done\n")
          fs.appendFileSync(Log_address, "-------------------------- 4. Test Stage Done\n")
        } catch (err) {
          // console.log(err)
        }

        let unittest_parameters = generate_unittest_parameters()
        execute_unittest_list(unittest_callbacks, 3, "unread_test_output_unittest", unittest_parameters)
      }
      })
    },
  },

  created () {
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
    
  },
  mounted () {
    // console.log("mounted @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
    // 轮询 /api/users/<int:id>/notifications/ 请求用户的新通知
    window.unread_request = this.unread_request;
    window.unread_match_id = this.unread_match_id;
    window.unread_situation = this.unread_situation;
    window.unread_output = this.unread_output;

    window.unread_test_request = this.unread_test_request;
    window.unread_test_match_id = this.unread_test_match_id;
    window.unread_test_output = this.unread_test_output;

    // window.unread_match_id_sponsor = this.unread_match_id_sponsor
    // window.unread_match_id_assistor = this.unread_match_id_assistor
    // window.unread_situation_sponsor = this.unread_situation_sponsor
    // window.unread_situation_assistor = this.unread_situation_assistor
    // window.unread_output_singleTask = this.unread_output_singleTask

    let count = 1;
    let getTime = window.performance;
    let startTime = getTime.now();

    // $(function() {
    //   let since = 0
    //   let total_notifications_count = 0  // 总通知计数
    //   let unread_request_count = 0  // 收到的新评论通知计数
    //   let unread_match_id_count = 0  // 收到的新私信通知计数
    //   let unread_situation_count = 0  // 新粉丝通知计数
    //   let unread_output_count = 0  // 新的喜欢或赞的通知计数
    //   let unread_messages_count = 0
    //   let sender_random_id_list = []
    //   let task_id_list = []
      
    //   let vm = this

      // function polling() {
      //   // console.log(`第${count}次开始 ${getTime.now() - startTime}`); // 显示开始时间

      //   // db.select
      //   // check result => None => change to setting page


      //   if (window.localStorage.getItem('Apollo-token')) {
      //     // 如果用户已登录，才开始请求 API
      //     const payload = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1]))
      //     const user_id = payload.user_id
      //     // const path = `/users/${user_id}/notifications/?since=${since}`
      //     const path = `/users/${user_id}/notifications/`
      //     // const path = ''
      //     // console.log("since shua xin",since)
      //     axios.get(path)
      //       .then((response) => {
      //         // handle success
              
      //         for (let res of response.data){
      //           if (res.task_id_list.length != 0){
      //             console.log("response.data", res)
      //           }
      //         }
      //       for (let item of response.data){
      //         // console.log('item', item, item.payload)
      //         if (item.payload >= 1){

      
      //           console.log("++++++++++++++++++++++++=", response.data)

      //           const all_notifications = {
      //             response_data: response.data
      //           } 

      //           axios.post('/update_all_notifications/', all_notifications)
      //           .then((response) => {
      //             // train stage
      //             let unread_request_notification = response.data["unread request"]
      //             let unread_match_id_notification = response.data["unread match id"]
      //             let unread_situation_notification = response.data["unread situation"]
      //             let unread_output_notification = response.data["unread output"]

      //             // test stage
      //             let unread_test_request_notification = response.data["unread test request"]
      //             let unread_test_match_id_notification = response.data["unread test match id"]
      //             let unread_test_output_notification = response.data["unread test output"]


      //             console.log("unread_request_notification",unread_request_notification,
      //               unread_request_notification["check_dict"])
      //             console.log("unread_match_id_notification",unread_match_id_notification,
      //               unread_match_id_notification["check_dict"])
      //             console.log("unread_situation_notification",unread_situation_notification,
      //               unread_situation_notification["check_dict"])
      //             console.log("unread_output_notification",unread_output_notification,
      //               unread_output_notification["check_dict"])

      //             console.log("unread_test_request_notification",unread_test_request_notification,
      //               unread_test_request_notification["check_dict"])
      //             console.log("unread_test_match_id_notification",unread_test_match_id_notification,
      //               unread_test_match_id_notification["check_dict"])
      //             console.log("unread_test_output_notification",unread_test_output_notification,
      //               unread_test_output_notification["check_dict"])


      //             if (unread_request_notification["check_dict"] ){
      //                 unread_request(unread_request_notification)
      //             }

      //             if (unread_match_id_notification["check_dict"]){
      //                 unread_match_id(unread_match_id_notification)
      //             }

      //             if (unread_situation_notification["check_dict"]){
      //                 unread_situation(unread_situation_notification)
      //             }

      //             if (unread_output_notification["rounds_dict"]){
      //                 unread_output(unread_output_notification)
      //             }

      //             if (unread_test_request_notification["check_dict"]){
      //                 unread_test_request(unread_test_request_notification)
      //             }

      //             if (unread_test_match_id_notification["check_dict"]){
      //                 unread_test_match_id(unread_test_match_id_notification)
      //             }

      //             if (unread_test_output_notification["check_dict"]){
      //                 unread_test_output(unread_test_output_notification)
      //             }
      //           })
      //           .catch((error) => {
      //             // handle error
      //             console.log(error)
      //           }) 
      //           break
      //         }
      //       }
            

      //       // console.log("--------------------------------------------------------- new polling")
          

      //       total_notifications_count = unread_request_count + unread_match_id_count + unread_situation_count + unread_output_count + unread_messages_count
      //       // 每一次请求之后，根据 total_notifications_count 的值来显示或隐藏徽标
      //       $('#new_notifications_count').text(total_notifications_count)
      //       $('#new_notifications_count').css('visibility', total_notifications_count ? 'visible' : 'hidden');
          
      //       // if (promise_list.length >= 1){
      //       //   Promise.all(promise_list).then((resArr) => {
                  


      //         //   });
      //         // }else{
      //         //   setTimeout(function(){
      //         //     console.log("polling again")
      //         //     polling()
      //         //   }, 15000)
      //         // }
              
      //         setTimeout(function(){
      //           // console.log("polling again")
      //           polling()
      //         }, 5000)

              
      //       })
      //       .catch((error) => {
              
      //         setTimeout(function(){
      //           // console.log("polling again")
      //           polling()
      //         }, 5000)
      //         // handle error
      //         console.log(error)
      //       })
      //   }else{
      //     setTimeout(function(){
      //       polling()
      //     }, 5000);
      //   }
      //   // console.log(`第${count}次结束 ${getTime.now() - startTime}`); // 显示开始时间
      //   count += 1
      // }

      // setTimeout(function(){
      //   polling()
      // }, 3000);
    //   setTimeout(function(){
    //       polling()
    //     }, 7000);
    //   // polling()
     
    // })
  }
 }
// exports.default = Navbar
</script>

<style scoped>
  /* .container {
    height: 750px;
  }
  .icon-div {
    width: 49%;
    display: inline-block;
  }
  .icon-div .fa {
    cursor: pointer;
  } */
  a{
    color: rgb(128, 131, 128) !important
  }
  
  .router-link-exact-active{
    color:rgb(249, 249, 250) !important;
    /* background:green; */
    /* text-decoration: underline !important; */
  }
</style>