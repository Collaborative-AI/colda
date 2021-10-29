<template>
  <div class="container-fluid">
    <div class="row min-vh-100 flex-column flex-md-row">
        <aside class="col-12 col-md-2 p-0 bg-dark flex-shrink-1">
            <nav class="navbar navbar-expand navbar-dark bg-dark flex-md-column flex-row align-items-start py-2">
                <div class="collapse navbar-collapse ">
                    <ul class="flex-md-column flex-row navbar-nav w-100 justify-content-between">

                        <router-link to="/" class="g-text-underline--none--hover">
                          <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
                            
                        </router-link>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link v-bind:to="{ path: '/find_assistor' }" class="nav-link" >Request</router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link v-bind:to="{ path: '/plist' }" class="nav-link">Pend<span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link v-bind:to="{ path: '/notifications' }" class="nav-link">History<span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                          <router-link v-bind:to="{ name: 'SettingProfile' }" class="nav-link">Setting</router-link>
                        </li>
                        <li v-if="sharedState.is_authenticated" class="nav-item">
                            <a v-on:click="handlerLogout" class="nav-link" href="#">Logout</a>
                        </li>

                        <li v-else class="nav-item">
                          <router-link to="/login" class="nav-link">Login</router-link>
                        </li>
                      
                        <li class="nav-item">
                          <router-link to="/shiyan" class="nav-link">Ceshi</router-link>
                        </li>                    
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
        <main class="col bg-faded py-3 flex-grow-1">
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
            <router-view />
        </main>
    </div>
</div>
</template>

<script>
import store from '../store'
import axios from 'axios'
import $ from 'jquery'
import db from '../db'


// const store = require('../store').default
// // 在 JQuery 中使用 axios 的话需要重新导入，不能使用 main.js 中定义的 Vue 全局属性 this.$axios
// const axios = require('axios').default
// const $ = require('jquery')
// const db = require('../db').default

// // use Node API
const fs = window.require('fs');
// const join = window.require('path').join;
//// const xlsx2json = window.require("node-xlsx");
const sqlite3 = window.require('sqlite3').verbose();;
const ex = window.require("child_process");
const {dialog} = window.require('electron').remote;
const os = window.require('os');
const node_path = window.require('path');
// change csv to array

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
      sharedState: store.state,
      unread_request_show: false,
      assistor_num: 0,
      max_round: 2,
      picked: "receive",
      root: '',
      exe_position: '',
      
    }
  },
  methods: {
    
    handlerLogout (e) {
      store.logoutAction()
      this.$toasted.show('You have been logged out.', { icon: 'fingerprint' })
      this.$router.push('/login')
    },

    not_receive() {
      this.sharedState.receive_request = false
      // this.sharedState.pending.a='apple'
      // console.log(this.sharedState.pending)
    },
    receive() {

      let vm = this
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
        if (err){
          console.log(err);
        }

        console.log(row)

        if (row == null | row.default_data_path == "" | row.default_id_path == "" |
            row.default_test_data_path == "" | row.default_test_id_path == ""){
          console.log("get false")
          vm.sharedState.set_default = false
          vm.sharedState.receive_request = false
          vm.$toasted.success('Please Fill the Default Setting', { icon: 'fingerprint' })
          vm.picked = "One";
        }
        else{
          vm.sharedState.receive_request = true
        }
        
      })
    },

    handle_train_log_address(task_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      console.log("train_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        console.log("log.txt created");
      }
      return Log_address

    },
    handle_test_log_address(task_id, test_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "test", test_id.toString(), "log.txt")
      console.log("test_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        console.log("log.txt created");
      }
      
      return Log_address

    },
    // sponsor find assistor
    

    // sponsor_csv() {
    //   csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
    //     this.sponsor_request_show = false

    //     console.log('sponsor数据', res)
    //     const payload = {
    //       task_id: this.task_id,
    //       file: res,
    //     }

    //   this.$axios.post('/match_sponsor_id/', payload)
    //     .then((response) => {
    //     // handle success
    //     console.log(`Sponsor sends the csv file.`, response)
    //     this.$toasted.success(`Sponsor sends the csv file.`, { icon: 'fingerprint' })
    //   })
    //   .catch((error) => {
    //   // handle error
    //     console.log(error)
    //   // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
    //   })
    // })      
    // },

    unread_request(unread_request_notification) {
      let vm = this

      console.log("this.sharedState.receive_request", this.sharedState.receive_request)
      if (this.sharedState.receive_request == 'passive' || this.sharedState.receive_request== 'active'){
        console.log("2.1 Update request notification response", unread_request_notification)
        this.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

        let cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
        for (let task_id in cur_unread_request_Taskid_dict){
          
          // const assistor_store_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/'
          // fs.mkdirSync(assistor_store_folder, { recursive: true})
          if (this.sharedState.receive_request=='passive'){

          let select_default_train_file_path = 'SELECT default_train_file_path, default_train_id_colomn FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_file_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_file_path = row.default_train_file_path
            console.log("default_train_id_path", default_train_file_path)
            let default_train_id_colomn = row.default_train_id_colomn

            let hash_id_file_address = null;
            // try{
            //   hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path ' + default_train_id_path + ' --root ' + vm.root 
            //                             + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --mode train', {encoding: 'utf8'})
            //   console.log("hash_id_file_address", hash_id_file_address)
            // }catch(err){
            //     console.log(err)
            // }
            try{   
              hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                      + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + default_train_file_path 
                                      + ' --id_idx ' + default_train_id_colomn, {encoding: 'utf8'})
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
            
            const Log_address = vm.handle_train_log_address(task_id)

            try {
              fs.appendFileSync(Log_address, "\n You are Assistor\n")
              fs.appendFileSync(Log_address, "Task ID: " + task_id + "\n")
              fs.appendFileSync(Log_address, "----------------------2. Unread Request\n")
              fs.appendFileSync(Log_address, "2.1 Update the request notification\n")
            } catch (err) {
              console.log(err)
            }
            let hash_id_file_data = fs.readFileSync(hash_id_file_address[2], {encoding:'utf8', flag:'r'});

            const match_assistor_id_data = {
              task_id: task_id,
              file: hash_id_file_data,
            }
            console.log('hash_id_file_data', hash_id_file_data)
            
            vm.$axios.post('/match_assistor_id/', match_assistor_id_data)
              .then((response) => {
                // handle success
                console.log("2.2 assistor uploads id file", response)
                vm.$toasted.success(`2.2 assistor uploads id file`, { icon: 'fingerprint' })

                try {
                  fs.appendFileSync(Log_address, "2.2 assistor uploads id file\n")
                  fs.appendFileSync(Log_address, "--------------------------2. Unread Request Done\n")
                } catch (err) {
                  console.log(err)
                }
              })
              .catch((error) => {
                // handle error
                console.log(error)
                // console.log(error.response.data)
                // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
              })

          })  
        }  //end if
        //else if active
        else {
          console.log(task_id)
          // let select_task_info = 'SELECT * FROM User_Chosen_Path WHERE task_id=' + task_id;
          // db.get(select_task_info, function(err, row){
          //   if (err){ 
          //     throw err;
          //   }
          //   vm.sharedState.pending.push({task_name: row.task_name, task_id: row.task_id})
          //   console.log(vm.sharedState.pending)
          // })  
          // let db_task_id
          // let db_task_name
          // let db_task_description
          let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=?';
            db.get(select_sentence, [task_id], function(err, row){
            if (err){ 
              console.log(err);
            }
            else{
              // vm.sharedState.pending.push({task_name: row.task_name, task_id: task_id})
              // console.log(vm.sharedState.pending)
              let db_task_id
              let db_task_name
              let db_task_description
              db_task_id=row.task_id
              db_task_name=row.task_name
              db_task_description=row.task_description
              let insert_sentence = `INSERT INTO "User_Pending_Page"("task_name", "task_description", "user_id", "task_id") VALUES 
              (`+`"`+db_task_name +`", "`+db_task_description+`", "`+vm.sharedState.user_id+ `", "` + db_task_id + `")`
          console.log("insert_sentence", insert_sentence)
          db.run(insert_sentence, function(err){
            if (err){
              console.log(err);
            }
          })
            }
        
            })//end db.get
          // vm.sharedState.pending.push({task_id: task_id})
          // console.log(vm.sharedState.pending)
          
        }//end else
        }//end for
      }
      else{
        console.log("unread request: If you want to receive, open receive")
        dialog.showErrorBox('Please Open the Receive', "unread request: If you want to receive, open receive")

      }
    },

    // assistor_csv() {
      
    //   csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
    //   this.unread_request_show  = false

    //   console.log('assistor数据', res)
    //   const payload = {
    //     task_id: this.task_id,
    //     file: res,
    //   }

    //   this.$axios.post('/match_assistor_id/', payload)
    //     .then((response) => {
    //     // handle success
    //     console.log(`assistor sends the csv file.`, response)
    //     this.$toasted.success(`assistor sends the csv file.`, { icon: 'fingerprint' })
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    //   }) 
    // },

    unread_match_id(unread_match_id_notification) {
      
          
      console.log("3.1 Update match id notification response", unread_match_id_notification)
      this.$toasted.success("3.1 Update the match id notification", { icon: 'fingerprint' })

      let cur_unread_match_id_Taskid_dict = unread_match_id_notification["check_dict"]

      for (let task_id in cur_unread_match_id_Taskid_dict){
        
        const Log_address = this.handle_train_log_address(task_id)

        try {
          fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID\n")
          fs.appendFileSync(Log_address, "3.1 Update the match id notification\n")
        } catch (err) {
          console.log(err)
        }

        let check_sponsor = cur_unread_match_id_Taskid_dict[task_id]

        if (check_sponsor == 1){
          console.log("3.2 Unread_match_id_sponsor")
          try {
            fs.appendFileSync(Log_address, "3.2 Unread_match_id_sponsor\n")
          } catch (err) {
            console.log(err)
          }
          this.unread_match_id_sponsor(task_id)
        }  
        else{
          console.log("3.2 Unread_match_id_assistor")
          try {
            fs.appendFileSync(Log_address, "3.2 Unread_match_id_assistor\n")
          } catch (err) {
            console.log(err)
          }
          this.unread_match_id_assistor(task_id)
        }
      }
    },

    unread_match_id_sponsor(task_id) {
      
      // Create 'Local_Data/id/task_id/Match/' folder
      // const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      let vm = this;
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
          console.log("3.3 Sponsor gets matched id file")
          vm.$toasted.success("3.3 Sponsor gets matched id file", { icon: 'fingerprint' })

          try {
            fs.appendFileSync(Log_address, "3.3 Sponsor gets matched id file\n")
          } catch (err) {
            console.log(err)
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
              console.log("save_match_id_file_pos", save_match_id_file_pos)
              if (save_match_id_file_pos[0] != "200" || save_match_id_file_pos[1] != "save_match_id"){
                vm.$toasted.success(`save match id wrong`, { icon: 'fingerprint' })
                console.log("save match id wrong")
                return 
              }
            }catch(err){
              console.log(err)
            }

            fs.writeFileSync(save_match_id_file_pos[2], cur_match_id_file)
            console.log('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos[2]);
            vm.$toasted.success('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos[2], { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos[2] + "\n")
            } catch (err) {
              console.log(err)
            }

            // match_id (from different assistor) to index 
            try{
              let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
              make_match_idx_done = make_match_idx_done.split("?")
              console.log("make_match_idx_done", make_match_idx_done)
              if (make_match_idx_done[0] != "200" || make_match_idx_done[1] != "make_match_idx" || make_match_idx_done[2] != "complete"){
                vm.$toasted.success(`make_match_idx wrong`, { icon: 'fingerprint' })
                console.log("make_match_idx wrong")
                return 
              }
            }catch(err){
              console.log(err)
            }

            console.log('3.5 Sponsor matches id to index');
            vm.$toasted.success('3.5 Sponsor matches id to index', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.5 Sponsor matches id to index\n")
            } catch (err) {
              console.log(err)
            }

          }


          let select_train_target_colomn = 'SELECT train_file_path, train_target_colomn FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' +' AND "task_id"="' + task_id + '"';
          db.get(select_train_target_colomn, function(err, row){
            if (err){ 
              console.log(err);
            }
            let train_file_path = row.train_file_path
            console.log("train_file_path", train_file_path)
            let train_target_colomn = row.train_target_colomn
            console.log("train_target_colomn", train_target_colomn)
            let make_residual_multiple_paths = null;
            try{
              // make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
              //   + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round 0 ' 
              //   + ' --target_path ' + train_target_path, {encoding: 'utf8'})

              make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
                + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round 0 ' 
                + ' --dataset_path ' + train_file_path + ' --target_idx ' + train_target_colomn, {encoding: 'utf8'})

              make_residual_multiple_paths = make_residual_multiple_paths.split("?")
              console.log("make_residual_multiple_paths", make_residual_multiple_paths)
              if (make_residual_multiple_paths[0] != "200" || make_residual_multiple_paths[1] != "make_residual"){
                vm.$toasted.success(`make_residual wrong`, { icon: 'fingerprint' })
                console.log("make_residual wrong")
                return 
              }
                // make_residual_multiple_paths = make_residual_multiple_paths.split('?')
              
              console.log("make_residual_multiple_paths", make_residual_multiple_paths, make_residual_multiple_paths.length)
            }catch(err){
              console.log(err)
            }

            console.log("3.6 Sponsor makes residual finished")
            vm.$toasted.success("3.6 Sponsor makes residual finished", { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.6 Sponsor makes residual finished\n")
            } catch (err) {
              console.log(err)
            }

            // Read Files
            let all_residual_data = [];
            let assistor_random_id_list = [];
            let residual_paths = make_residual_multiple_paths[2].split("?")
            for (let i = 0; i < residual_paths.length; i++){

              let data = null;
              try{
                // data = fs.readFileSync(make_residual_multiple_paths[i], {encoding:'utf8', flag:'r'});
                data = fs.readFileSync(residual_paths[i], {encoding:'utf8', flag:'r'});
              }catch(err){
                console.log(err)
              }
              all_residual_data.push(data);

              // let cur_path = make_residual_multiple_paths[i]
              let cur_path = residual_paths[i]
              let path_split = cur_path.split(node_path.sep);
              let assistor_random_id = path_split[path_split.length-1].split(".")[0];
              assistor_random_id_list.push(assistor_random_id);
              
            }

            console.log("assistor_random_id_list", assistor_random_id_list)
            const send_situation_payload = {
                task_id: task_id,
                assistor_random_id_list: assistor_random_id_list,
                residual_list: all_residual_data,
              }

            // send initial situation
            // async

            // function sleep(time) {
            //   let startTime = window.performance.now();
            //   while (window.performance.now() - startTime < time) {}
            // }
            // sleep(5000); // 程序滞留5000ms

            vm.$axios.post('/send_situation/', send_situation_payload)
              .then((response) => {
              // handle success
              console.log("3.7 Sponsor sends all situations", response)
              vm.$toasted.success("3.7 Sponsor sends all situations", { icon: 'fingerprint' })
              
              try {
                fs.appendFileSync(Log_address, "3.7 Sponsor sends all situations" + "\n")
                fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID Done\n")
              } catch (err) {
                console.log(err)
              }

            })
            .catch((error) => {
              console.log(error)
            })

          });
          

        })
        .catch((error) => {
          console.log(error)
          // handle error
        }) 
    },

    unread_match_id_assistor(task_id) {

      // Create 'Local_Data/id/task_id/Match/' folder
      
      // const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      // fs.mkdirSync(Match_folder, { recursive: true})
      let vm = this;
      const Log_address = vm.handle_train_log_address(task_id)
      

      // Obtain Match_id file
      const payload = {
        task_id: task_id
      }
      const path = `/users/${this.sharedState.user_id}/match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          console.log("3.3 Assistor gets matched id file", response)
          vm.$toasted.success("3.3 Assistor gets matched id file", { icon: 'fingerprint' })
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
            console.log(save_match_id_file_pos)
            // console.log(save_match_id_file_pos)
            save_match_id_file_pos = save_match_id_file_pos.split("?")
            console.log("save_match_id_file_pos", save_match_id_file_pos)
            if (save_match_id_file_pos[0] != "200" || save_match_id_file_pos[1] != "save_match_id"){
              vm.$toasted.success(`save match id wrong`, { icon: 'fingerprint' })
              console.log("save match id wrong")
              return 
            }
          }catch(err){
            console.log(err)
          }

          // Store match_id file
          fs.writeFileSync(save_match_id_file_pos[2], cur_match_id_file)

          console.log('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos[2]);
          vm.$toasted.success('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos[2], { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Assistor Saved Matched id File at " + save_match_id_file_pos[2] + "\n")
          } catch (err) {
            console.log(err)
          }

          // match id to index from sponsor
          try{
            let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
            make_match_idx_done = make_match_idx_done.split("?")
            console.log("make_match_idx_done", make_match_idx_done)
            if (make_match_idx_done[0] != "200" || make_match_idx_done[1] != "make_match_idx" || make_match_idx_done[2] != "complete"){
              vm.$toasted.success(`make_match_idx wrong`, { icon: 'fingerprint' })
              console.log("make_match_idx wrong")
              return 
            }
          }catch(err){
            console.log(err)
          }

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(2000); // 程序滞留2000ms

          console.log('3.5 Assistor matches id to index');
          vm.$toasted.success('3.5 Assistor matches id to index', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.5 Assistor matches id to index\n")
            fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID Done\n")
          } catch (err) {
            console.log(err)
          }

          // const path = `/assistor_write_match_index_done/`

          // const assistor_write_match_index_done_data = {
          //   task_id: task_id
          // } 
          
          // vm.$axios.post(path, assistor_write_match_index_done_data)
          //   .then((response) => {
          //       console.log('3.6 Assistor update done');
          //   })
          //   .catch((error)=>{
          //     console.log(error)
          //   })   




        })
        .catch((error) => {
          // handle error
          console.log(error)
        }) 
    },

    unread_situation(unread_situation_notification) {
      
      console.log("4.1 Update the situation notification", unread_situation_notification)
      this.$toasted.success("4.1 Update the situation notification", { icon: 'fingerprint' })

      let cur_unread_situation_Taskid_dict = unread_situation_notification["check_dict"]
      let cur_unread_situation_Rounds_dict = unread_situation_notification["rounds_dict"]

      for (let task_id in cur_unread_situation_Taskid_dict){
        
        const Log_address = this.handle_train_log_address(task_id)
        try {
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation\n")
          fs.appendFileSync(Log_address, "4.1 Update the situation notification\n")
        } catch (err) {
          console.log(err)
        }

        let check_sponsor = cur_unread_situation_Taskid_dict[task_id];
        let rounds = cur_unread_situation_Rounds_dict[task_id];

        // check if the current client is sponsor or not of the specific task
        if (check_sponsor == 1){
          this.unread_situation_sponsor(rounds, task_id)
        }  
        else{
          this.unread_situation_assistor(rounds, task_id)
        }
      }
    },

    unread_situation_sponsor(rounds, task_id) {
      let vm = this;
      console.log("4.2 Cur round is:" + rounds + task_id);
      vm.$toasted.success("4.2 Cur round is:" + rounds +  task_id, { icon: 'fingerprint' })
    
      const Log_address = vm.handle_train_log_address(task_id)
      

      try {
        fs.appendFileSync(Log_address, "4.2 Cur round is: " + rounds.toString() + "\n")
      } catch (err) {
        console.log(err)
      }
      
      let select_train_data_path = 'SELECT train_file_path, train_data_colomn FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' + ' AND "task_id"="' + task_id + '"';
      db.get(select_train_data_path, function(err, row){
        if (err){ 
          throw err;
        }
        let train_file_path = row.train_file_path
        console.log("train_file_path", train_file_path)
        let train_data_colomn = row.train_data_colomn
        console.log("train_data_colomn", train_data_colomn)
        try{
          // let train_output = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id ' 
          //   + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds + ' --data_path ' 
          //   + train_data_path, {encoding: 'utf8'})

          let train_output = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id '
            + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds + ' --dataset_path ' + train_file_path + ' --data_idx ' +train_data_colomn, {encoding: 'utf8'})
          
          train_output = train_output.split("?")
          console.log("train_output", train_output)
          if (train_output[0] != "200" || train_output[1] != "make_train"){
            vm.$toasted.success(`make_train wrong`, { icon: 'fingerprint' })
            console.log("make_train wrong")
            return 
          }
          
          console.log("4.3 Sponsor round " + rounds + " training done.");
          vm.$toasted.success("4.3 Sponsor round " + rounds + " training done.", { icon: 'fingerprint' })
        
        }catch(err){
          console.log(err)
        }

        try {
          fs.appendFileSync(Log_address, "4.3 Sponsor round " + rounds + " training done." + "\n")
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation Done\n")
        } catch (err) {
          console.log(err)
        }


        // const path = `/Sponsor_situation_training_done/`

        // const Sponsor_situation_training_done_data = {
        //   task_id: task_id
        // } 
        
        // vm.$axios.post(path, Sponsor_situation_training_done_data)
        //   .then((response) => {
        //     console.log("4.4 Sponsor update training done")
        //   })
        //   .catch((error)=>{
        //     console.log(error)
        //   })  

      });

      
    },

    unread_situation_assistor_train_part(task_id, rounds, from_id, default_train_file_path, default_train_data_colomn, vm, Log_address){

      let Assistor_train_output_path = null;

      // get response from make_train.py. 
      try{
        // Assistor_train_output_path = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id ' 
        //   + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds + ' --from_id ' 
        //   + from_id + ' --data_path ' + default_train_data_path, {encoding: 'utf8'})
        //  console.log("Assistor_train_output_path", Assistor_train_output_path)

        Assistor_train_output_path = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id '
          + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + rounds + ' --from_id ' 
          + from_id + ' --dataset_path ' + default_train_file_path + ' --data_idx ' + default_train_data_colomn,{encoding: 'utf8'})
        
        Assistor_train_output_path = Assistor_train_output_path.split("?")
        console.log("Assistor_train_output_path", Assistor_train_output_path)
        if (Assistor_train_output_path[0] != "200" || Assistor_train_output_path[1] != "make_train"){
          vm.$toasted.success(`make_train wrong`, { icon: 'fingerprint' })
          console.log("make_train wrong")
          return 
        }
      }
      catch(err){
        console.log(err)
      }
      

      console.log("4.4 Assistor round " + rounds + " training done.");
      vm.$toasted.success("4.4 Assistor round " + rounds + " training done.", { icon: 'fingerprint' })
      try {
        fs.appendFileSync(Log_address, "4.4 Assistor round " + rounds + " training done." + "\n")
      } catch (err) {
        console.log(err)
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
        console.log("4.5 Assistor sends output", response)
        vm.$toasted.success("4.5 Assistor sends output", { icon: 'fingerprint' })
        try {
          fs.appendFileSync(Log_address, "4.5 Assistor sends output\n")
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Situation Done\n")
        } catch (err) {
          console.log(err)
        }
      })
      .catch((error) => {
        console.log(error)
      })

    },
    unread_situation_assistor(rounds, task_id) {
      
      let vm = this;

      const Log_address = vm.handle_train_log_address(task_id)

      // function sleep(time) {
      //       let startTime = window.performance.now();
      //       while (window.performance.now() - startTime < time) {}
      //     }
      //     sleep(5000); // 程序滞留5000ms

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      
      const path = `/users/${vm.sharedState.user_id}/situation_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // store the situation file

          console.log("4.2 assistor gets situation file")
          vm.$toasted.success("4.2 assistor gets situation file", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.2 assistor gets situation file\n")
          } catch (err) {
            console.log(err)
          }

          const from_id = response.data.sender_random_id;
          let cur_situation_file = JSON.parse(response.data.situation);
          // cur_situation_file = cur_situation_file.join('\n');

          // Store residual file from sponsor
          let save_residual_file_pos = null;
          try{
            save_residual_file_pos = ex.execSync(vm.exe_position + ' save_residual --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --from_id ' + from_id + ' --round ' + rounds, {encoding: 'utf8'})
            console.log(save_residual_file_pos)
            save_residual_file_pos = save_residual_file_pos.split("?")
            console.log("save_residual_file_pos", save_residual_file_pos)
            if (save_residual_file_pos[0] != "200" || save_residual_file_pos[1] != "save_residual"){
              vm.$toasted.success(`save_residual wrong`, { icon: 'fingerprint' })
              console.log("save_residual wrong")
              return 
            }
          }catch(err){
            console.log(err)
          }

          fs.writeFileSync(save_residual_file_pos[2], cur_situation_file)

          console.log('4.3 Assistor Saved Residual File!');
          vm.$toasted.success('4.3 Assistor Saved Residual File!', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.3 Assistor Saved Residual File!\n")
          } catch (err) {
            console.log(err)
          }

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(5000); // 程序滞留5000ms

          // Assistor trains the data
          
          let select_default_train_data_path = 'SELECT default_train_file_path, default_train_data_colomn FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_file_path = row.default_train_file_path
            console.log("default_train_file_path",default_train_file_path)
            let default_train_data_colomn = row.default_train_data_colomn
            console.log("default_train_data_colomn",default_train_data_colomn)

            vm.unread_situation_assistor_train_part(task_id, rounds, from_id, default_train_file_path, default_train_data_colomn, vm, Log_address)

          });
          
        })
        .catch((error) => {
          console.log(error)
          // handle error
        }) 


    },
    
    unread_output(unread_output_notification) {


      console.log("5.1 Update the output notification", unread_output_notification)
      this.$toasted.success("5.1 Update the output notification", { icon: 'fingerprint' })

      let cur_unread_output_Rounds_dict = unread_output_notification["rounds_dict"]

      for (let task_id in cur_unread_output_Rounds_dict){

        const Log_address = this.handle_train_log_address(task_id)
        try {
          fs.appendFileSync(Log_address, "-------------------------- 5. Unread Output\n")
          fs.appendFileSync(Log_address, "5.1 Update the output notification\n")
        } catch (err) {
          console.log(err)
        }
        let rounds = cur_unread_output_Rounds_dict[task_id];
        this.unread_output_singleTask(rounds, task_id);
      }
    },

    unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_colomn, vm, Log_address){
      console.log("unread_output_make_result_helper_rounds", rounds)
      let make_result_done = null;
      try{
        // make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
        //   + ' --task_id '+ task_id + ' --round ' + rounds + ' --target_path ' + train_target_path, {encoding: 'utf8'})
        // console.log("make_result_done", make_result_done)
        make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
          + ' --task_id '+ task_id + ' --round ' + rounds + ' --dataset_path ' + train_file_path 
          + ' --target_idx ' + train_target_colomn, {encoding: 'utf8'})
          
        console.log("make_result_done", make_result_done)
        make_result_done = make_result_done.split("?")
        console.log("make_result_done", make_result_done)
        if (make_result_done[0] != "200" || make_result_done[1] != "make_result"){
          vm.$toasted.success(`make_result wrong`, { icon: 'fingerprint' })
          console.log("make_result wrong")
          return 
        }
      }catch(err){
        console.log(err)
      }

      let a = (make_result_done[2] == "sponsor cannot find train output file")
      console.log("a",a)
      if(make_result_done == "sponsor cannot find train output file"){
        console.log("-------meijinlai")
        make_result_done = null;
        setTimeout(function(){
          vm.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_colomn, vm, Log_address)
        }, 5000);

      }else{
        console.log("jinlaile")
        console.log("5.4 Sponsor makes result done.")
        vm.$toasted.success("5.4 Sponsor makes result done.", { icon: 'fingerprint' })
        try {
          fs.appendFileSync(Log_address, "5.4 Sponsor makes result done." + "\n")
        } catch (err) {
          console.log(err)
        }

        // terminate
        if ((rounds+1) >= vm.max_round){
          fs.appendFileSync(Log_address, "---------------------- Train Stage Ends\n");
        }else{        

        let make_residual_multiple_paths = null;
        try{
          // make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
          //   + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + (rounds+1) 
          //   + ' --target_path ' + train_target_path, {encoding: 'utf8'})
          // make_residual_multiple_paths = make_residual_multiple_paths.split('?')
          // console.log(make_residual_multiple_paths)
          make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
            + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + (rounds+1)
            + ' --dataset_path ' + train_file_path + ' --target_idx ' + train_target_colomn, {encoding: 'utf8'})
          // make_residual_multiple_paths = make_residual_multiple_paths.split('?')
          
          make_residual_multiple_paths = make_residual_multiple_paths.split("?")
          console.log(make_residual_multiple_paths)
          console.log("make_residual_multiple_paths", make_residual_multiple_paths)
          if (make_residual_multiple_paths[0] != "200" || make_residual_multiple_paths[1] != "make_residual"){
            vm.$toasted.success(`make_residual wrong`, { icon: 'fingerprint' })
            console.log("make_residual wrong")
            return 
          }
          }catch(err){
          console.log(err)
        }

        console.log("5.5 Sponsor makes residual finished")
        vm.$toasted.success("5.5 Sponsor makes residual finished", { icon: 'fingerprint' })

        try {
          fs.appendFileSync(Log_address, "5.5 Sponsor makes residual finished\n")
        } catch (err) {
          console.log(err)
        }

        let all_residual_data = [];
        let assistor_random_id_list = [];

        for (let i = 2; i < make_residual_multiple_paths.length; i++){

          let data = fs.readFileSync(make_residual_multiple_paths[i], {encoding:'utf8', flag:'r'});
          all_residual_data.push(data);

          let path_split = make_residual_multiple_paths[i].split(node_path.sep);
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
          console.log("5.6 Sponsor updates situation done", response)
            vm.$toasted.success("5.6 Sponsor updates situation done", { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "5.6 Sponsor updates situation done\n")
              fs.appendFileSync(Log_address, "-------------------------- 5. Unread Output Done\n")
            } catch (err) {
              console.log(err)
            }
          })
          .catch((error) => {
            console.log(error)
          })
        }
      }
    },

    unread_output_singleTask(rounds, task_id){
      
      let vm = this
      const Log_address = vm.handle_train_log_address(task_id)
      // const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      
      // Obtain output from assistors

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      const url = `/users/${this.sharedState.user_id}/output/`

      this.$axios.post(url, payload)
        .then((response) => {
          console.log("5.2 Sponsor gets output model")
          vm.$toasted.success("5.2 Sponsor gets output model", { icon: 'fingerprint' })

          try {
            fs.appendFileSync(Log_address, "5.2 Sponsor gets output model\n")
          } catch (err) {
            console.log(err)
          }
          // iterate the output file
          for(let i = 0;i < response.data.output.length; i++){

            const from_id = response.data.sender_random_ids_list[i];

            console.log("cur_output^^^^^^^^", response.data.output[i])
            let cur_output = JSON.parse(response.data.output[i]);
            console.log("cur_output^^^^^^^^1", cur_output)
            // cur_output = cur_output.join('\n');
            console.log("cur_output^^^^^^^^2", cur_output)

            // Store the output from assistor
            let save_output_pos = null;
            try{
              save_output_pos = ex.execSync(vm.exe_position + ' save_output --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id + ' --round ' + rounds, {encoding: 'utf8'})
              console.log(save_output_pos)
              save_output_pos = save_output_pos.split("?")
              console.log("save_output_pos", save_output_pos)
              if (save_output_pos[0] != "200" || save_output_pos[1] != "save_output"){
                vm.$toasted.success(`save_output wrong`, { icon: 'fingerprint' })
                console.log("save_output wrong")
                return 
              }
            }catch(err){
            console.log(err)
          }

            fs.writeFileSync(save_output_pos[2], cur_output)           

            console.log('5.3 Sponsor saves Output model');
            vm.$toasted.success('5.3 Sponsor saves Output model', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "5.3 Sponsor saves Output model\n")
            } catch (err) {
              console.log(err)
            }
          }

          let select_train_target_path = 'SELECT train_file_path, train_target_colomn FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' + ' AND "task_id"="' + task_id + '"';
          db.get(select_train_target_path, function(err, row){
            if (err){ 
              throw err;
            }
            let train_file_path = row.train_file_path
            console.log("train_file_path", train_file_path)
            let train_target_colomn = row.train_target_colomn
            console.log("train_target_colomn", train_target_colomn)

            vm.unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_colomn, vm, Log_address)

          });
          
        })
        .catch((error) => {
          // handle error
          console.log(error)
        }) 
    },


    unread_output_make_result_helper(task_id, rounds, train_file_path, train_target_colomn, vm, Log_address){
      console.log("unread_output_make_result_helper_rounds", rounds)
      let make_result_done = null;
      try{
        // make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
        //   + ' --task_id '+ task_id + ' --round ' + rounds + ' --target_path ' + train_target_path, {encoding: 'utf8'})
        // console.log("make_result_done", make_result_done)
        make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
          + ' --task_id '+ task_id + ' --round ' + rounds + ' --dataset_path ' + train_file_path 
          + ' --target_idx ' + train_target_colomn, {encoding: 'utf8'})
          
        console.log("make_result_done", make_result_done)
        make_result_done = make_result_done.split("?")
        console.log("make_result_done", make_result_done)
        if (make_result_done[0] != "200" || make_result_done[1] != "make_result"){
          vm.$toasted.success(`make_result wrong`, { icon: 'fingerprint' })
          console.log("make_result wrong")
          return 
        }
      }catch(err){
        console.log(err)
      }

      console.log("jinlaile")
      console.log("5.4 Sponsor makes result done.")
      vm.$toasted.success("5.4 Sponsor makes result done.", { icon: 'fingerprint' })
      try {
        fs.appendFileSync(Log_address, "5.4 Sponsor makes result done." + "\n")
      } catch (err) {
        console.log(err)
      }

      // terminate
      if ((rounds+1) >= vm.max_round){
        fs.appendFileSync(Log_address, "---------------------- Train Stage Ends\n");
      }else{        

      let make_residual_multiple_paths = null;
      try{
        // make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
        //   + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + (rounds+1) 
        //   + ' --target_path ' + train_target_path, {encoding: 'utf8'})
        // make_residual_multiple_paths = make_residual_multiple_paths.split('?')
        // console.log(make_residual_multiple_paths)
        make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root 
          + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --round ' + (rounds+1)
          + ' --dataset_path ' + train_file_path + ' --target_idx ' + train_target_colomn, {encoding: 'utf8'})
        // make_residual_multiple_paths = make_residual_multiple_paths.split('?')
        
        make_residual_multiple_paths = make_residual_multiple_paths.split("?")
        console.log(make_residual_multiple_paths)
        console.log("make_residual_multiple_paths", make_residual_multiple_paths)
        if (make_residual_multiple_paths[0] != "200" || make_residual_multiple_paths[1] != "make_residual"){
          vm.$toasted.success(`make_residual wrong`, { icon: 'fingerprint' })
          console.log("make_residual wrong")
          return 
        }
        }catch(err){
        console.log(err)
      }

      console.log("5.5 Sponsor makes residual finished")
      vm.$toasted.success("5.5 Sponsor makes residual finished", { icon: 'fingerprint' })

      try {
        fs.appendFileSync(Log_address, "5.5 Sponsor makes residual finished\n")
      } catch (err) {
        console.log(err)
      }

      let all_residual_data = [];
      let assistor_random_id_list = [];
      let residual_paths = make_residual_multiple_paths[2].split("?")
      for (let i = 0; i < residual_paths.length; i++){

        let data = fs.readFileSync(residual_paths[i], {encoding:'utf8', flag:'r'});
        all_residual_data.push(data);

        let cur_path = residual_paths[i]
        let path_split = cur_path.split(node_path.sep);
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
        console.log("5.6 Sponsor updates situation done", response)
          vm.$toasted.success("5.6 Sponsor updates situation done", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "5.6 Sponsor updates situation done\n")
            fs.appendFileSync(Log_address, "-------------------------- 5. Unread Output Done\n")
          } catch (err) {
            console.log(err)
          }
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },

    
    unread_test_request(unread_test_request_notification) {
      let vm = this;
      // Only assistor calls this function
      if (this.sharedState.receive_request == 'passive' || this.sharedState.receive_request == 'active'){
        
        console.log("2.1 Update Test request notification response", unread_test_request_notification)
        this.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })

        let cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
        let test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

        for (let test_id in cur_unread_test_request_Testid_dict){
          let task_id = test_id_to_task_id[test_id]
          
          let select_default_test_id_path = 'SELECT default_train_file_path, default_train_id_colomn FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_test_id_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_id_colomn = row.default_train_id_colomn
            let default_train_file_path = row.default_train_file_path
            console.log("default_train_id_colomn", default_train_id_colomn)
            let test_hash_id_file_address = null
            try{
              // test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
              //                           + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})

              test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
                                        + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id
                                        + ' --mode test' + ' --test_id ' + test_id
                                        + ' --dataset_path ' + default_train_file_path + ' --id_idx ' + default_train_id_colomn, {encoding: 'utf8'})
              test_hash_id_file_address = test_hash_id_file_address.split("?")
              console.log(test_hash_id_file_address)
            }catch(err){
              console.log(err)
            }

            const Log_address = vm.handle_test_log_address(task_id, test_id)

            try {
              fs.appendFileSync(Log_address, "\n You are Assistor\n")
              fs.appendFileSync(Log_address, "Test ID: " + test_id + "\n")
              fs.appendFileSync(Log_address, "-----------------------Test Stage: 2.Unread Test Request\n")
              fs.appendFileSync(Log_address, "2.1 Test: Update Test request notification\n")
              fs.appendFileSync(Log_address, "2.2 Test: Hashing Done\n")
            } catch (err) {
              console.log(err)
            }

            let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});

            const match_test_assistor_id_data = {
              file: test_hash_id_file_data,
              test_id: test_id
            }

            vm.$axios.post('/match_test_assistor_id/', match_test_assistor_id_data)
              .then((response) => {
                // handle success
                console.log("2.2 Test: assistor uploads id file", response)
                vm.$toasted.success(`2.2 Test: assistor uploads id file`, { icon: 'fingerprint' })
                try {
                  fs.appendFileSync(Log_address, "2.2 Test: assistor uploads id file\n")
                  fs.appendFileSync(Log_address, "--------------------------2. Unread Test Request Done\n")
                } catch (err) {
                  console.log(err)
                }
              })
              .catch((error) => {
                // handle error
                console.log(error)
                // console.log(error.response.data)
                // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
              })

          });
          
        }
      }else{
        console.log("unread request: If you want to receive, open receive")
        dialog.showErrorBox('Please Open the Receive', "unread request: If you want to receive, open receive")
      }
    },


    unread_test_match_id(unread_test_match_id_notification) {
      console.log("3.1 Update Test match id notification response", unread_test_match_id_notification)
      this.$toasted.success("3.1 Update the Test match id notification", { icon: 'fingerprint' })

      let cur_unread_test_match_id_Testid_dict = unread_test_match_id_notification["check_dict"]
      let test_id_to_task_id = unread_test_match_id_notification["test_id_to_task_id"]
      let max_rounds_dict = unread_test_match_id_notification["max_rounds"]

      for (let test_id in cur_unread_test_match_id_Testid_dict){
        let task_id = test_id_to_task_id[test_id]

        const Log_address = this.handle_test_log_address(task_id, test_id)

        try {
          fs.appendFileSync(Log_address, "-----------------------3.Unread Test Match ID\n")
          fs.appendFileSync(Log_address, "3.1 Test: Update the Test match id notification\n")
        } catch (err) {
          console.log(err)
        }

        let check_sponsor = cur_unread_test_match_id_Testid_dict[test_id]
        let cur_max_round = max_rounds_dict[test_id]

        if (check_sponsor == 1){
          console.log("3.2 Unread_test_match_id_sponsor")
          try {
            fs.appendFileSync(Log_address, "3.2 Test: Unread_test_match_id_sponsor\n")
          } catch (err) {
            console.log(err)
          }
          this.unread_test_match_id_sponsor(task_id, test_id, cur_max_round)
        }  
        else{
          console.log("3.2 Unread_test_match_id_assistor")
          try {
            fs.appendFileSync(Log_address, "3.2 Test: Unread_test_match_id_assistor\n")
          } catch (err) {
            console.log(err)
          }
          this.unread_test_match_id_assistor(task_id, test_id, cur_max_round)
        }
      }
    },

    unread_test_match_id_sponsor(task_id, test_id, max_rounds) {

      // Create 'Local_Data/id/task_id/Match/' folder
      // const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + test_id + '/' + 'Match/'
      let vm = this;
      const Log_address = vm.handle_test_log_address(task_id, test_id)
      

      // Obtain Match_id file
      // async
      const payload = {
        test_id: test_id
      }
      
      const path = `/users/${vm.sharedState.user_id}/test_match_id_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // iterate the match_id_file
          console.log("3.4 Test: Sponsor gets matched id file")
          vm.$toasted.success("3.4 Test: Sponsor gets matched id file", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Test: Sponsor gets matched id file\n")
          } catch (err) {
            console.log(err)
          }

          for(let i = 0;i < response.data.match_id_file.length; i++){
            
            const from_id = response.data.assistor_random_id_pair[i];
            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');

            // Store match_id file from different assistor
            let test_save_match_id_file_pos = null;
            try{
              test_save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode test' + ' --from_id ' + from_id  + ' --test_id ' + test_id, {encoding: 'utf8'})
                
              test_save_match_id_file_pos = test_save_match_id_file_pos.split("?")
              console.log(test_save_match_id_file_pos)
            }catch(err){
              console.log(err)
            }

            fs.writeFileSync(test_save_match_id_file_pos[2], cur_match_id_file)
            
            console.log('3.5 Test: Sponsor Saved Matched id File!');
            vm.$toasted.success('3.5 Test: Sponsor Saved Matched id File!', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.5 Test: Sponsor Saved Matched id File!\n")
            } catch (err) {
              console.log(err)
            }

            try{
              let test_make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode test' + ' --from_id ' + from_id  + ' --test_id ' + test_id, {encoding: 'utf8'})

                
            }catch(err){
              console.log(err)
            }

            function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(2000); // 程序滞留2000ms

            console.log('3.6 Test: Sponsor matches id to index');
            vm.$toasted.success('3.6 Test: Sponsor matches id to index', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.6 Test: Sponsor matches id to index\n")
            } catch (err) {
              console.log(err)
            }

          }

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(8000); // 程序滞留8000ms

          // function find_Train_Models(startPath) {
          // let result=[];
          // function finder(path) {
          //     let files=fs.readdirSync(path);
          //     files.forEach((val,index) => {
          //         let fPath=join(path,val);
          //         let stats=fs.statSync(fPath);
          //         // console.log("val", val)
          //         // console.log("stats", fPath, stats)
          //         if(stats.isDirectory()) finder(fPath);
          //         if(stats.isFile()&&val=="Sponsor_Trained_Local_Model.csv") {
          //           // result.push(fPath);
          //           let data = fs.readFileSync(fPath,
          //             {encoding:'utf8', flag:'r'});
          //           result.push(data);
          //         }
          //     });
          //   }
          //   finder(startPath);
          //   return result;
          // }

          // let train_path = 'Local_Data/' + this.sharedState.user_id + '/' + task_id;
          // let files = find_Train_Models(train_path);
          
          // console.log("3.6 Test: Sponsor gets all train models")
          // vm.$toasted.success("3.6 Test: Sponsor gets all train models", { icon: 'fingerprint' })
          // try {
          //   fs.appendFileSync(Log_address, "3.6 Test: Sponsor gets all train models\n")
          // } catch (err) {
          //   console.log(err)
          // }
          // const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';
          // fs.mkdirSync(Test_Output_folder, { recursive: true});

          // for (let i = 0;i < files.length; i++){
          //   console.log(files[i]);
          //   let filename = "Test_Models" + i.toString();
          //   fs.writeFileSync(Test_Output_folder + filename, files[i])
          // }
          let select_test_data_path = 'SELECT test_file_path, test_data_colomn FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="test"' + ' AND "test_id"="' + test_id + '"';
          db.get(select_test_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let test_file_path = row.test_file_path
            let test_data_colomn = row.test_data_colomn
            console.log("test_file_path", test_file_path)
            
            try{
              let test_done = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                + ' --task_id ' + task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --dataset_path ' + test_file_path + ' --data_idx ' + test_data_colomn, {encoding: 'utf8'})

            }catch(err){
              console.log(err)
            }

            console.log("3.7 Test: Sponsor stores all test model results")
            vm.$toasted.success("3.7 Test: Sponsor stores all test model results", { icon: 'fingerprint' })

            try {
              fs.appendFileSync(Log_address, "3.7 Test: Sponsor stores all test model results\n")
              fs.appendFileSync(Log_address, "--------------------------3. Unread Test Match ID Done\n")
            } catch (err) {
              console.log(err)
            }
          });
          
          })
          .catch((error) => {
            console.log(error)
            // handle error
          }) 

         
    },

    unread_test_match_id_assistor(task_id, test_id, max_rounds) {
      // Create 'Local_Data/id/task_id/Match/' folder
      let vm = this;
      // const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Match/'
      // fs.mkdirSync(Match_folder, { recursive: true})

      const Log_address = vm.handle_test_log_address(task_id, test_id)
      
      
      // Obtain Match_id file
      const payload = {
        test_id: test_id
      }
      const path = `/users/${this.sharedState.user_id}/test_match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          console.log("3.4 Test: assistor gets matched id file", response)
          vm.$toasted.success("3.4 Test: assistor gets matched id file", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Test: assistor gets matched id file\n")
          } catch (err) {
            console.log(err)
          }

          const from_id = response.data.sponsor_random_id;
          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join('\n');

          // Store match_id file from sponsor
          let test_save_match_id_file_pos = null;
          try{
            test_save_match_id_file_pos = ex.execSync(vm.exe_position + ' save_match_id --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode test' + ' --from_id ' + from_id + ' --test_id ' + test_id, {encoding: 'utf8'})
            test_save_match_id_file_pos = test_save_match_id_file_pos.split("?")
            console.log("test_save_match_id_file_pos", test_save_match_id_file_pos)
          }catch(err){
            console.log(err)
          }

          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(2000); // 程序滞留2000ms

          fs.writeFileSync(test_save_match_id_file_pos[2], cur_match_id_file)
          
          console.log('3.5 Test: Assistor Saved Matched id File!');
          vm.$toasted.success('3.5 Test: Assistor Saved Matched id File!', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.5 Test: Assistor Saved Matched id File!\n")
          } catch (err) {
            console.log(err)
          }

          try{
            let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode test' + ' --from_id ' + from_id + ' --test_id ' + test_id, {encoding: 'utf8'})
          }catch(err){
            console.log(err)
          }

          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(2000); // 程序滞留2000ms
          
          console.log('3.6 Test: Assistor matches id to index');
          vm.$toasted.success('3.6 Test: Assistor matches id to index', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.6 Test: Assistor matches id to index\n")
          } catch (err) {
            console.log(err)
          }

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(5000); // 程序滞留5000ms

          // function find_Train_Models(startPath) {
          // let result=[];
          // function finder(path) {
          //     let files=fs.readdirSync(path);
          //     files.forEach((val,index) => {
          //         let fPath=join(path,val);
          //         let stats=fs.statSync(fPath);
          //         // console.log("val", val)
          //         // console.log("stats", fPath, stats)
          //         if(stats.isDirectory()) finder(fPath);
          //         if(stats.isFile()&&val=="assistor_Trained_Local_Model.csv") {
          //           // result.push(fPath);
          //           let data = fs.readFileSync(fPath,
          //             {encoding:'utf8', flag:'r'});
          //           result.push(data);
          //         }
          //     });
          //   }
          //   finder(startPath);
          //   return result;
          // }

          // let train_path = 'Local_Data/' + this.sharedState.user_id + '/' + task_id;
          // let files = find_Train_Models(train_path);
          
          // console.log("3.6 Test: assistor gets all train models")
          // vm.$toasted.success("3.6 Test: assistor gets all train models", { icon: 'fingerprint' })
          // try {
          //   fs.appendFileSync(Log_address, "3.6 Test: assistor gets all train models\n")
          // } catch (err) {
          //   console.log(err)
          // }

          // const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';
          // fs.mkdirSync(Test_Output_folder, { recursive: true});

          // for (let i = 0;i < files.length; i++){
          //   console.log(files[i]);
          //   let filename = "Test_Models" + i.toString();
          //   fs.writeFileSync(Test_Output_folder + filename, files[i])
          // }

          // let select_test_data_path = 'SELECT test_data_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_id"="' + test_id + '"';
          // db.get(select_test_data_path, function(err, row){
          //   if (err){ 
          //     throw err;
          //   }
          //   let test_data_path = row.test_data_path
          //   console.log("test_data_path", test_data_path)
          // });

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(7000); // 程序滞留7000ms

          let select_default_test_data_path = 'SELECT default_train_file_path, default_train_data_colomn FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_test_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_file_path = row.default_train_file_path
            let default_train_data_colomn = row.default_train_data_colomn
            console.log("default_train_file_path",default_train_file_path)

            let test_outputs_pos = null
            try{
              // test_outputs_pos = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              //   + ' --task_id ' + task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --from_id ' + from_id 
              //   + ' --data_path ' + default_test_data_path, {encoding: 'utf8'})
              
              test_outputs_pos = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                + ' --task_id ' + task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --from_id ' + from_id 
                + ' --dataset_path ' +  default_train_file_path + ' --data_idx ' + default_train_data_colomn, {encoding: 'utf8'})

              test_outputs_pos = test_outputs_pos.split('?')
              console.log("test_output_pos", test_outputs_pos)
              
            }catch(err){
              console.log(err)
            }

            console.log("3.7 Test: assistor stores all test model results")
            vm.$toasted.success("3.7 Test: assistor stores all test model results", { icon: 'fingerprint' })

            try {
              fs.appendFileSync(Log_address, "3.7 Test: assistor stores all test model results\n")
            } catch (err) {
              console.log(err)
            }

            let all_test_output = [];
            // for (let i = 0; i < test_outputs_pos.length; i++){

              const data = fs.readFileSync(test_outputs_pos[2], {encoding:'utf8', flag:'r'});
              all_test_output.push(data);

            // }

            const payload1 = {
              output: all_test_output,
              test_id: test_id,
            }

            vm.$axios.post('/send_test_output/', payload1)
              .then((response) => {
              // handle success
              console.log("3.8 Test: assistor sends all test model results", response)
              vm.$toasted.success("3.8 Test: assistor sends all test model results", { icon: 'fingerprint' })
              try {
                fs.appendFileSync(Log_address, "3.8 Test: assistor sends all test model results\n")
                fs.appendFileSync(Log_address, "-------------------------- 3. Unread Test Match ID Done\n")
              } catch (err) {
                console.log(err)
              }
            })
            .catch((error) => {
              console.log(error)
            })
          });

        })
        .catch((error) => {
          // handle error
          console.log(error)
        }) 
    },

    unread_test_output(unread_test_output_notification) {

      console.log("4.1 Update Test output notification", unread_test_output_notification)
      this.$toasted.success("4.1 Update Test output notification", { icon: 'fingerprint' })

      let cur_unread_test_output_Testid_dict = unread_test_output_notification["check_dict"]
      let test_id_to_task_id = unread_test_output_notification["test_id_to_task_id"]

      for (let test_id in cur_unread_test_output_Testid_dict){
        let task_id = test_id_to_task_id[test_id]

        const Log_address = this.handle_test_log_address(task_id, test_id)

        try {
          fs.appendFileSync(Log_address, "-------------------------- 4. Unread Test Output\n")
          fs.appendFileSync(Log_address, "4.1 Update Test output notification\n")
        } catch (err) {
          console.log(err)
        }
        this.unread_test_output_singleTask(task_id, test_id);
      }
    },

    unread_test_output_singleTask(task_id, test_id){

      // const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';

      const Log_address = this.handle_test_log_address(task_id, test_id)

      let vm = this
      // Obtain output from assistors

      const payload = {
        test_id: test_id,
      }

      const url = `/test_output/`
      this.$axios.post(url, payload)
        .then((response) => {
          console.log("4.2 Test: Sponsor gets assistors' Test output model")
          vm.$toasted.success("4.2 Test: Sponsor gets assistors' Test output model", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.2 Test: Sponsor gets assistors' Test output model\n")
          } catch (err) {
            console.log(err)
          }
          // iterate the match_id_file
          for(let i = 0;i < response.data.output.length; i++){

            const from_id = response.data.sender_random_ids_list[i];
            let multiple_outputs_from_one_assistor = JSON.parse(response.data.output[i]);
            console.log("multiple_outputs_from_one_assistor", multiple_outputs_from_one_assistor)

            for (let j = 0; j < multiple_outputs_from_one_assistor.length; j++){
              
              let cur_output = multiple_outputs_from_one_assistor[j];
              
              // Store test output from assistors
              let test_save_output_pos = null
              try{
                test_save_output_pos = ex.execSync(vm.exe_position + ' save_output --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                  + ' --task_id '+ task_id + ' --mode test --test_id ' + test_id + ' --from_id ' + from_id + ' --round ' + j, {encoding: 'utf8'})
                test_save_output_pos = test_save_output_pos.split("?")
                console.log("test_save_output_pos", test_save_output_pos)
                    
              }catch(err){
                console.log(err)
              }

              // Store match_id file
              fs.writeFileSync(test_save_output_pos[2], cur_output)

            }
          }
          console.log("4.3 Test: Sponsor saves assistors' Output model");

          vm.$toasted.success("4.3 Test: Sponsor saves assistors' Output model", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.3 Test: Sponsor saves assistors' Output model\n")
          } catch (err) {
            console.log(err)
          }
          vm.unread_test_output_make_eval_helper(task_id, test_id, vm, Log_address, response)


        })
        .catch((error) => {
            // handle error
          console.log(error)
        }) 

          
    },

    unread_test_output_make_eval_helper(task_id, test_id, vm, Log_address, response){
      

      let max_round = JSON.parse(response.data.output[0]).length - 1;
      console.log("max_round", max_round)

      let select_test_target_path = 'SELECT test_file_path, test_target_colomn FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="test"' + ' AND "test_id"="' + test_id + '"';
      db.get(select_test_target_path, function(err, row){
        if (err){ 
          throw err;
        }
        let test_file_path = row.test_file_path
        let test_target_colomn= row.test_target_colomn
        // console.log("test_target_path",test_target_path)
        let eval_done = null;
        try{
          // eval_done = ex.execSync(vm.exe_position + ' make_eval --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
          //   + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_round 
          //   + ' --target_path ' + test_target_path, {encoding: 'utf8'})

          eval_done = ex.execSync(vm.exe_position + ' make_eval --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
            + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_round 
            + ' --dataset_path ' + test_file_path + ' --target_idx ' + test_target_colomn, {encoding: 'utf8'})

          
        }catch(err){
          console.log(err)
        }
        console.log("eval_done", eval_done)
        if (eval_done == "sponsor test not ready"){
          setTimeout(function(){
            vm.unread_test_output_make_eval(task_id, test_id, vm, Log_address, response)
          }, 5000);

        }else{
          console.log("4.4 Test: Sponsor evaluates output models done");
          vm.$toasted.success("4.4 Test: Sponsor evaluates output models done", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.4 Test: Sponsor evaluates output models done\n")
          } catch (err) {
            console.log(err)
          }

          try {
            fs.appendFileSync(Log_address, "-------------------------- 4. Unread Test Output Done\n")
            fs.appendFileSync(Log_address, "-------------------------- 4. Test Stage Done\n")
          } catch (err) {
            console.log(err)
          }


        }

       
      });

    },

  },

  created () {
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },
  mounted () {
    console.log("mounted @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
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

    $(function() {
      let since = 0
      let total_notifications_count = 0  // 总通知计数
      let unread_request_count = 0  // 收到的新评论通知计数
      let unread_match_id_count = 0  // 收到的新私信通知计数
      let unread_situation_count = 0  // 新粉丝通知计数
      let unread_output_count = 0  // 新的喜欢或赞的通知计数
      let unread_messages_count = 0
      let sender_random_id_list = []
      let task_id_list = []
      
      let vm = this

      function polling() {
        console.log(`第${count}次开始 ${getTime.now() - startTime}`); // 显示开始时间

        // db.select
        // check result => None => change to setting page


        if (window.localStorage.getItem('Apollo-token')) {
          // 如果用户已登录，才开始请求 API
          const payload = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1]))
          const user_id = payload.user_id
          // const path = `/users/${user_id}/notifications/?since=${since}`
          const path = `/users/${user_id}/notifications/`
          // const path = ''
          // console.log("since shua xin",since)
          axios.get(path)
            .then((response) => {
              // handle success
            console.log("response.data", response.data, response.data.length)
            for (let item of response.data){
              // console.log('item', item, item.payload)
              if (item.payload >= 1){

      
                console.log("++++++++++++++++++++++++=", response.data)

                const all_notifications = {
                  response_data: response.data
                } 

                axios.post('/update_all_notifications/', all_notifications)
                .then((response) => {
                  // train stage
                  let unread_request_notification = response.data["unread request"]
                  let unread_match_id_notification = response.data["unread match id"]
                  let unread_situation_notification = response.data["unread situation"]
                  let unread_output_notification = response.data["unread output"]

                  // test stage
                  let unread_test_request_notification = response.data["unread test request"]
                  let unread_test_match_id_notification = response.data["unread test match id"]
                  let unread_test_output_notification = response.data["unread test output"]


                  console.log("unread_request_notification",unread_request_notification,
                    unread_request_notification["check_dict"])
                  console.log("unread_match_id_notification",unread_match_id_notification,
                    unread_match_id_notification["check_dict"])
                  console.log("unread_situation_notification",unread_situation_notification,
                    unread_situation_notification["check_dict"])
                  console.log("unread_output_notification",unread_output_notification,
                    unread_output_notification["check_dict"])

                  console.log("unread_test_request_notification",unread_test_request_notification,
                    unread_test_request_notification["check_dict"])
                  console.log("unread_test_match_id_notification",unread_test_match_id_notification,
                    unread_test_match_id_notification["check_dict"])
                  console.log("unread_test_output_notification",unread_test_output_notification,
                    unread_test_output_notification["check_dict"])


                  if (unread_request_notification["check_dict"] ){
                      unread_request(unread_request_notification)
                  }

                  if (unread_match_id_notification["check_dict"]){
                      unread_match_id(unread_match_id_notification)
                  }

                  if (unread_situation_notification["check_dict"]){
                      unread_situation(unread_situation_notification)
                  }

                  if (unread_output_notification["rounds_dict"]){
                      unread_output(unread_output_notification)
                  }

                  if (unread_test_request_notification["check_dict"]){
                      unread_test_request(unread_test_request_notification)
                  }

                  if (unread_test_match_id_notification["check_dict"]){
                      unread_test_match_id(unread_test_match_id_notification)
                  }

                  if (unread_test_output_notification["check_dict"]){
                      unread_test_output(unread_test_output_notification)
                  }
                })
                .catch((error) => {
                  // handle error
                  console.log(error)
                }) 
                break
              }
            }
            

            console.log("--------------------------------------------------------- new polling")
          

            total_notifications_count = unread_request_count + unread_match_id_count + unread_situation_count + unread_output_count + unread_messages_count
            // 每一次请求之后，根据 total_notifications_count 的值来显示或隐藏徽标
            $('#new_notifications_count').text(total_notifications_count)
            $('#new_notifications_count').css('visibility', total_notifications_count ? 'visible' : 'hidden');
          
            // if (promise_list.length >= 1){
            //   Promise.all(promise_list).then((resArr) => {
                  


              //   });
              // }else{
              //   setTimeout(function(){
              //     console.log("polling again")
              //     polling()
              //   }, 15000)
              // }
              
              setTimeout(function(){
                console.log("polling again")
                polling()
              }, 5000)

              
            })
            .catch((error) => {
              
              setTimeout(function(){
                console.log("polling again")
                polling()
              }, 5000)
              // handle error
              console.log(error)
            })
        }else{
          setTimeout(function(){
            polling()
          }, 5000);
        }
        console.log(`第${count}次结束 ${getTime.now() - startTime}`); // 显示开始时间
        count += 1
      }

      // setTimeout(function(){
      //   polling()
      // }, 3000);
      setTimeout(function(){
          polling()
        }, 7000);
      // polling()
     
    })
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
    color: rgb(118, 122, 118) !important
  }
</style>