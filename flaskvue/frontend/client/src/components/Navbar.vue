<template>
<section>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light" style="margin-bottom: 20px;">
      <div class="navbar-brand">
      <router-link to="/" class="g-text-underline--none--hover">
        <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
          Apollo 
      </router-link>
      </div>

      <!-- <div class="content">
        <Home :log="log"></Home>
      </div> -->

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/ping" class="nav-link">Ping</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/shiyan" class="nav-link">Ceshi</router-link>
          </li>

        </ul>
        
        <form v-if="sharedState.is_authenticated" class="form-inline navbar-left mr-auto">
          <input class="form-control mr-sm-2" type="search" placeholder="Search">
          <!-- 暂时先禁止提交，后续实现搜索再改回 type="submit" -->
          <button class="btn btn-outline-success my-2 my-sm-0" type="button">Search</button>
        </form>

        

        <ul v-if="sharedState.is_authenticated" class="nav navbar-nav navbar-right">
          <input type="radio" id="not_receive" value="not_receive" v-model="picked" v-on:change="not_receive()">
          <label for="not_receive">Dont Response to Request</label>
          <br>
          <input type="radio" id="receive" value="receive" v-model="picked" v-on:change="receive()">
          <label for="receive">Response</label>
          <br>
          <span>Picked: {{ picked }}</span>

          <!-- <li class="nav-item g-mr-20">
            <button @click="find_assistor">Call For Help</button>
            <router-link v-bind:to="{ name: 'Shiyan' }" class="nav-link">Call For Help</router-link>
          </li> -->
          
           <li class="nav-item g-mr-20">
            <router-link v-bind:to="{ path: '/find_assistor' }" class="nav-link"><i class="icon-education-033 u-line-icon-pro g-color-red g-font-size-16 g-pos-rel g-top-2 g-mr-3"></i> Call For Help </router-link>
          </li>

          <!-- <li class="nav-item g-mr-20">
            <router-link v-bind:to="{ name: 'MessagesHistoryResource', query: { from: 5 } }" class="nav-link">Send to B</router-link>
          </li> -->
          <!-- <div v-if="sponsor_request_show">
            <input type="file" name="csvfile" ref="csvData" />
            <input type="button" @click="sponsor_csv()" value="JS转换"/>
          </div> -->

          <div v-if="unread_request_show">
            <input type="file" name="csvfile" ref="csvData" />
            <input type="button" @click="assistor_csv()" value="JS转换"/>
          </div>

          <li class="nav-item g-mr-20">
            <router-link v-bind:to="{ path: '/notifications' }" class="nav-link"><i class="icon-education-033 u-line-icon-pro g-color-red g-font-size-16 g-pos-rel g-top-2 g-mr-3"></i> Notifications <span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <img v-bind:src="sharedState.user_avatar" class="g-brd-around g-brd-gray-light-v3 g-pa-2 rounded-circle rounded mCS_img_loaded"> {{ sharedState.user_name }}
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <!-- <router-link v-bind:to="{ path: `/user/${sharedState.user_id}` }" class="dropdown-item"><i class="icon-star g-pos-rel g-top-1 g-mr-5"></i> Your profile</router-link> -->
              <!-- <router-link v-bind:to="{ name: 'PostsResource' }" class="dropdown-item"><i class="icon-share g-pos-rel g-top-1 g-mr-5"></i> Your resource</router-link> -->
              <router-link v-bind:to="{ name: 'SettingProfile' }" class="dropdown-item"><i class="icon-settings g-pos-rel g-top-1 g-mr-5"></i> Settings</router-link>
              <div class="dropdown-divider"></div>
              <a v-on:click="handlerLogout" class="dropdown-item" href="#"><i class="icon-logout g-pos-rel g-top-1 g-mr-5"></i> Sign out</a>
            </div>
          </li>
        </ul>
        <ul v-else class="nav navbar-nav navbar-right">          
          <li class="nav-item">
            <router-link to="/login" class="nav-link"><i class="icon-login g-pos-rel g-top-1 g-mr-5"></i> Sign in</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</section>
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

// use Node API
const fs = window.require('fs');
const join = window.require('path').join;
// const xlsx2json = window.require("node-xlsx");
const sqlite3 = window.require('sqlite3').verbose();;
const ex = window.require("child_process");
const {dialog} = window.require('electron').remote;
const os = window.require('os');
const path = window.require('path');
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
      max_round: 3,
      picked: "not_receive",
      root: '',
      exe_position: '',
      
    }
  },
  methods: {
    changeroot() {
      
      const isDevelopment = process.env.NODE_ENV !== 'production';
      if (os.type() == "Linux"){
        if (isDevelopment == true){
          this.root = path.resolve("./exp")
          this.exe_position = path.resolve("./dist/run/run")
        }else{
          this.root = path.resolve("./resources/exp")
          this.exe_position = path.resolve("./resources/dist/run/run")
        }
    
      }else if (os.type() == "Darwin") {
        if (isDevelopment == true){
          this.root = path.resolve("./exp")
          this.exe_position = path.resolve("./dist/run/run.dmg")
        }else{
          this.root = path.resolve("./resources/exp")
          this.exe_position = path.resolve("./resources/dist/run/run.dmg")
        }

      }else if (os.type() == "Windows_NT") {
        if (isDevelopment == true){
          this.root = path.resolve("./exp")
          this.exe_position = path.resolve("./dist/run/run.exe")
        }else{
          this.root = path.resolve("./resources/exp")
          this.exe_position = path.resolve("./resources/dist/run/run.exe")
        }
      }
    },
    handlerLogout (e) {
      store.logoutAction()
      this.$toasted.show('You have been logged out.', { icon: 'fingerprint' })
      this.$router.push('/login')
    },

    not_receive() {
      this.sharedState.receive_request = false
    },
    receive() {

      let vm = this
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
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
      if (this.sharedState.receive_request == true){
        console.log("2.1 Update request notification response", unread_request_notification)
        this.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

        let cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
        for (let task_id in cur_unread_request_Taskid_dict){
          
          // const assistor_store_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/'
          // fs.mkdirSync(assistor_store_folder, { recursive: true})
          
          let select_default_train_id_path = 'SELECT default_train_id_path FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_id_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_id_path = row.default_train_id_path
            console.log("default_train_id_path", default_train_id_path)
            let hash_id_file_address = null;
            try{
              hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path ' + default_train_id_path + ' --root ' + vm.root 
                                        + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --mode train', {encoding: 'utf8'})
              console.log("hash_id_file_address", hash_id_file_address)
            }catch(err){
                console.log(err)
            }
            
            const Log_address = vm.root + '/' + vm.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'

            try {
              fs.appendFileSync(Log_address, "\n You are Assistor\n")
              fs.appendFileSync(Log_address, "Task ID: " + task_id + "\n")
              fs.appendFileSync(Log_address, "----------------------2. Unread Request\n")
              fs.appendFileSync(Log_address, "2.1 Update the request notification\n")
            } catch (err) {
              console.log(err)
            }
            let hash_id_file_data = fs.readFileSync(hash_id_file_address, {encoding:'utf8', flag:'r'});

            const match_assistor_id_data = {
              task_id: task_id,
              file: hash_id_file_data,
            }
            
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
          
        }
      }else{
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
        
        const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
      let vm = this;

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
              console.log(save_match_id_file_pos)
            }catch(err){
              console.log(err)
            }

            fs.writeFileSync(save_match_id_file_pos, cur_match_id_file)
            console.log('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos);
            vm.$toasted.success('3.4 Sponsor Saved Matched id File at ' + save_match_id_file_pos, { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "3.4 Sponsor Saved Matched id File at " + save_match_id_file_pos + "\n")
            } catch (err) {
              console.log(err)
            }

            // match_id (from different assistor) to index 
            try{
              let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
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

          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(8000); // 程序滞留5000ms

          // store initial situation
          // Create 'Local_Data/id/task_id/0' folder
          // const Round0_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/0/'
          // fs.mkdirSync(Round0_folder, { recursive: true})
          let select_train_target_path = 'SELECT train_target_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' +' AND "task_id"="' + task_id + '"';
          db.get(select_train_target_path, function(err, row){
            if (err){ 
              throw err;
            }
            let train_target_path = row.train_target_path
            console.log("train_target_path", train_target_path)
            let make_residual_multiple_paths = null;
            try{
              make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --round 0 ' + ' --target_path ' + train_target_path, {encoding: 'utf8'})
              make_residual_multiple_paths = make_residual_multiple_paths.split('?')
              console.log(make_residual_multiple_paths)
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

            for (let i = 0; i < make_residual_multiple_paths.length; i++){

              let data = fs.readFileSync(make_residual_multiple_paths[i], {encoding:'utf8', flag:'r'});
              all_residual_data.push(data);

              let path_split = make_residual_multiple_paths[i].split("/");
              let assistor_random_id = path_split[path_split.length-1].split(".")[0];
              assistor_random_id_list.push(assistor_random_id);
              
            }

            const send_situation_payload = {
                residual_list: all_residual_data,
                task_id: task_id,
                assistor_random_id_list: assistor_random_id_list,
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
      let vm = this;

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
          }catch(err){
            console.log(err)
          }

          // Store match_id file
          fs.writeFileSync(save_match_id_file_pos, cur_match_id_file)

          console.log('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos);
          vm.$toasted.success('3.4 Assistor Saved Matched id File at ' + save_match_id_file_pos, { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.4 Assistor Saved Matched id File at " + save_match_id_file_pos + "\n")
          } catch (err) {
            console.log(err)
          }

          // match id to index from sponsor
          try{
            let make_match_idx_done = ex.execSync(vm.exe_position + ' make_match_idx --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
              + ' --task_id '+ task_id + ' --mode train' + ' --from_id ' + from_id , {encoding: 'utf8'})
          }catch(err){
            console.log(err)
          }

          console.log('3.5 Assistor matches id to index');
          vm.$toasted.success('3.5 Assistor matches id to index', { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "3.5 Assistor matches id to index\n")
            fs.appendFileSync(Log_address, "-------------------------- 3. Unread Match ID Done\n")
          } catch (err) {
            console.log(err)
          }

          const path = `/assistor_write_match_index_done/`

          const assistor_write_match_index_done_data = {
            task_id: task_id
          } 
          
          vm.$axios.post(path, assistor_write_match_index_done_data)
            .then((response) => {
                console.log('3.6 Assistor update done');
            })
            .catch((error)=>{
              console.log(error)
            })   




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
        
        const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
      

      try {
        fs.appendFileSync(Log_address, "4.2 Cur round is: " + rounds.toString() + "\n")
      } catch (err) {
        console.log(err)
      }
      
      let select_train_data_path = 'SELECT train_data_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' + ' AND "task_id"="' + task_id + '"';
      db.get(select_train_data_path, function(err, row){
        if (err){ 
          throw err;
        }
        let train_data_path = row.train_data_path
        console.log("train_data_path", train_data_path)
        try{
          let train_output = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
            + ' --task_id '+ task_id + ' --round ' + rounds + ' --data_path ' + train_data_path, {encoding: 'utf8'})
          
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


          // function sleep(time) {
          //   let startTime = window.performance.now();
          //   while (window.performance.now() - startTime < time) {}
          // }
          // sleep(5000); // 程序滞留5000ms
        const path = `/Sponsor_situation_training_done/`

        const Sponsor_situation_training_done_data = {
          task_id: task_id
        } 
        
        vm.$axios.post(path, Sponsor_situation_training_done_data)
          .then((response) => {
            console.log("4.4 Sponsor update training done")
          })
          .catch((error)=>{
            console.log(error)
          })  

      });

      
    },

    unread_situation_assistor(rounds, task_id) {
      
      let vm = this;
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'

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
          }catch(err){
            console.log(err)
          }

          fs.writeFileSync(save_residual_file_pos, cur_situation_file)

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
          let select_default_train_data_path = 'SELECT default_train_data_path FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_data_path = row.default_train_data_path
            console.log("default_train_data_path",default_train_data_path)
            let Assistor_train_output_path = null;
            try{
              Assistor_train_output_path = ex.execSync(vm.exe_position + ' make_train --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --round ' + rounds + ' --from_id ' + from_id + ' --data_path ' + default_train_data_path, {encoding: 'utf8'})
              console.log(Assistor_train_output_path)

              console.log("4.4 Assistor round " + rounds + " training done.");
              vm.$toasted.success("4.4 Assistor round " + rounds + " training done.", { icon: 'fingerprint' })
              try {
                fs.appendFileSync(Log_address, "4.4 Assistor round " + rounds + " training done." + "\n")
              } catch (err) {
                console.log(err)
              }
              
            }catch(err){
              console.log(err)
            }

            let Assistor_train_output_data = fs.readFileSync(Assistor_train_output_path, {encoding:'utf8', flag:'r'});

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
        const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
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

    unread_output_singleTask(rounds, task_id){

      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
      // const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      let vm = this
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
            }catch(err){
            console.log(err)
          }

            fs.writeFileSync(save_output_pos, cur_output)           

            console.log('5.3 Sponsor saves Output model');
            vm.$toasted.success('5.3 Sponsor saves Output model', { icon: 'fingerprint' })
            try {
              fs.appendFileSync(Log_address, "5.3 Sponsor saves Output model\n")
            } catch (err) {
              console.log(err)
            }
          }

          let select_train_target_path = 'SELECT train_target_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="train"' + ' AND "task_id"="' + task_id + '"';
          db.get(select_train_target_path, function(err, row){
            if (err){ 
              throw err;
            }
            let train_target_path = row.train_target_path
            console.log("train_target_path", train_target_path)
            try{
              let make_result_done = ex.execSync(vm.exe_position + ' make_result --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --round ' + rounds + ' --target_path ' + train_target_path, {encoding: 'utf8'})
            }catch(err){
              console.log(err)
            }

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

              // Update situation

              // function sleep(time) {
              //   let startTime = window.performance.now();
              //   while (window.performance.now() - startTime < time) {}
              // }
              // sleep(5000); // 程序滞留5000ms

            

            let make_residual_multiple_paths = null;
            try{
              make_residual_multiple_paths = ex.execSync(vm.exe_position + ' make_residual --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --round ' + (rounds+1) + ' --target_path ' + train_target_path, {encoding: 'utf8'})
              make_residual_multiple_paths = make_residual_multiple_paths.split('?')
              console.log(make_residual_multiple_paths)
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

            for (let i = 0; i < make_residual_multiple_paths.length; i++){

              let data = fs.readFileSync(make_residual_multiple_paths[i], {encoding:'utf8', flag:'r'});
              all_residual_data.push(data);

              let path_split = make_residual_multiple_paths[i].split("/");
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

          });
          
        })
        .catch((error) => {
          // handle error
          console.log(error)
        }) 
    },

    unread_test_request(unread_test_request_notification) {
      let vm = this;
      // Only assistor calls this function
      if (this.sharedState.receive_request == true){
        
        console.log("2.1 Update Test request notification response", unread_test_request_notification)
        this.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })

        let cur_unread_test_request_Testid_dict = unread_test_request_notification["check_dict"]
        let test_id_to_task_id = unread_test_request_notification["test_id_to_task_id"]

        for (let test_id in cur_unread_test_request_Testid_dict){
          let task_id = test_id_to_task_id[test_id]
          
          let select_default_test_id_path = 'SELECT default_test_id_path FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_test_id_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_test_id_path = row.default_test_id_path
            console.log("default_test_id_path", default_test_id_path)
            let test_hash_id_file_address = null
            try{
              test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path ' + default_test_id_path + ' --root ' + vm.root 
                                        + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --mode test' + ' --test_id ' + test_id, {encoding: 'utf8'})
              console.log(test_hash_id_file_address)
            }catch(err){
              console.log(err)
            }
            const Log_address = vm.root + '/' + vm.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'

            try {
              fs.appendFileSync(Log_address, "\n You are Assistor\n")
              fs.appendFileSync(Log_address, "Test ID: " + test_id + "\n")
              fs.appendFileSync(Log_address, "-----------------------Test Stage: 2.Unread Test Request\n")
              fs.appendFileSync(Log_address, "2.1 Test: Update Test request notification\n")
              fs.appendFileSync(Log_address, "2.2 Test: Hashing Done\n")
            } catch (err) {
              console.log(err)
            }

            let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address, {encoding:'utf8', flag:'r'});

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

        const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'
      let vm = this;

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
              console.log(test_save_match_id_file_pos)
            }catch(err){
              console.log(err)
            }

            fs.writeFileSync(test_save_match_id_file_pos, cur_match_id_file)
            
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
          let select_test_data_path = 'SELECT test_data_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="test"' + ' AND "test_id"="' + test_id + '"';
          db.get(select_test_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let test_data_path = row.test_data_path
            console.log("test_data_path", test_data_path)
            
            try{
              let test_done = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --data_path ' + test_data_path, {encoding: 'utf8'})
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'
      
      
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
            console.log("test_save_match_id_file_pos", test_save_match_id_file_pos)
          }catch(err){
            console.log(err)
          }

          fs.writeFileSync(test_save_match_id_file_pos, cur_match_id_file)
          
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

          let select_default_test_data_path = 'SELECT default_test_data_path FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_test_data_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_test_data_path = row.default_test_data_path
            console.log("default_test_data_path",default_test_data_path)

            let test_outputs_pos = null
            try{
              test_outputs_pos = ex.execSync(vm.exe_position + ' make_test --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_rounds + ' --from_id ' + from_id + ' --data_path ' + default_test_data_path, {encoding: 'utf8'})
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
            for (let i = 0; i < test_outputs_pos.length; i++){

              const data = fs.readFileSync(test_outputs_pos[i], {encoding:'utf8', flag:'r'});
              all_test_output.push(data);

            }

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

        const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'
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
      const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id + '/log.txt'
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
                console.log("test_save_output_pos", test_save_output_pos)
              }catch(err){
                console.log(err)
              }

              // Store match_id file
              fs.writeFileSync(test_save_output_pos, cur_output)

            }
          }

          console.log("4.3 Test: Sponsor saves assistors' Output model");
          vm.$toasted.success("4.3 Test: Sponsor saves assistors' Output model", { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "4.3 Test: Sponsor saves assistors' Output model\n")
          } catch (err) {
            console.log(err)
          }

          let max_round = JSON.parse(response.data.output[0]).length - 1;
          console.log("max_round", max_round)

          let select_test_target_path = 'SELECT test_target_path FROM User_Chosen_Path WHERE "user_id"=' + vm.sharedState.user_id + ' AND "test_indicator"="test"' + ' AND "test_id"="' + test_id + '"';
          db.get(select_test_target_path, function(err, row){
            if (err){ 
              throw err;
            }
            let test_target_path = row.test_target_path
            console.log("test_target_path",test_target_path)
            try{
              let eval_done = ex.execSync(vm.exe_position + ' make_eval --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id 
                + ' --task_id '+ task_id + ' --test_id ' + test_id + ' --round ' + max_round + ' --target_path ' + test_target_path, {encoding: 'utf8'})
            }catch(err){
              console.log(err)
            }

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
          });
          


        })
        .catch((error) => {
            // handle error
          console.log(error)
        }) 

          
    },


  },
  created () {
    this.changeroot()
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
            if (response.data.length >= 1){
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