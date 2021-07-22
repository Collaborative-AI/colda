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
          <li class="nav-item g-mr-20">
            <button @click="find_recipient">Call For Help</button>
            <!-- <router-link v-bind:to="{ name: 'Shiyan' }" class="nav-link">Call For Help</router-link> -->
          </li>
          <li class="nav-item g-mr-20">
            <router-link v-bind:to="{ name: 'MessagesHistoryResource', query: { from: 5 } }" class="nav-link">Send to B</router-link>
          </li>
          <!-- <div v-if="sponsor_request_show">
            <input type="file" name="csvfile" ref="csvData" />
            <input type="button" @click="sponsor_csv()" value="JS转换"/>
          </div> -->

          <div v-if="unread_request_show">
            <input type="file" name="csvfile" ref="csvData" />
            <input type="button" @click="recipient_csv()" value="JS转换"/>
          </div>

          <li class="nav-item g-mr-20">
            <router-link v-bind:to="{ path: '/notifications' }" class="nav-link"><i class="icon-education-033 u-line-icon-pro g-color-red g-font-size-16 g-pos-rel g-top-2 g-mr-3"></i> Notifications <span id="new_notifications_count" style="visibility: hidden;" class="u-label g-font-size-11 g-bg-aqua g-rounded-20 g-px-10">0</span></router-link>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <img v-bind:src="sharedState.user_avatar" class="g-brd-around g-brd-gray-light-v3 g-pa-2 rounded-circle rounded mCS_img_loaded"> {{ sharedState.user_name }}
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <router-link v-bind:to="{ path: `/user/${sharedState.user_id}` }" class="dropdown-item"><i class="icon-star g-pos-rel g-top-1 g-mr-5"></i> Your profile</router-link>
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
// 在 JQuery 中使用 axios 的话需要重新导入，不能使用 main.js 中定义的 Vue 全局属性 this.$axios
import axios from 'axios'
import $ from 'jquery'
// use Node API
const fs = window.require('fs');
const xlsx2json = window.require("node-xlsx");

// change csv to array
import csv2arr from '@/assets/csv-arr'
import Home from '../views/Home.vue'

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
      recipient_num: 0,
      max_round: 4.
    }
  },
  methods: {
    handlerLogout (e) {
      store.logoutAction()
      this.$toasted.show('You have been logged out.', { icon: 'fingerprint' })
      this.$router.push('/login')
    },

    // sponsor find recipient
    find_recipient () {
       
      const sponsor_data_folder = 'Sponsor_Data/'
      fs.mkdirSync(sponsor_data_folder, { recursive: true})

      const filename = 'shiyan.csv'
      const data = fs.readFileSync(sponsor_data_folder + filename,
        {encoding:'utf8', flag:'r'});
      
      let data_array = data.split("\n")

      const payload = {
        recipient_id_list: [5],
        id_file: data_array
      }
      
      this.$axios.post('/find_recipient/', payload)
        .then((response) => {
          // handle success
          console.log("Sponsor calls for help", response)
          this.$toasted.success(`Sponsor calls for help`, { icon: 'fingerprint' })
          this.$store.state.msg.push(`---------------------- 1. Find Recipient`)
          this.$store.state.msg.push(`1.1 Sponsor calls for help`)

          console.log("Sponsor sends id file")
          this.$toasted.success(`Sponsor sends id file`, { icon: 'fingerprint' })
          this.$store.state.msg.push(`1.2 Sponsor sends id file`)
          

          // Create 'Local_Data/id/task_id/' folder
          const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/'
          fs.mkdirSync(new_address, { recursive: true})

          console.log("1.3 Sponsor creates " + new_address)
          this.$toasted.success("1.3 Sponsor creates " + new_address, { icon: 'fingerprint' })
          this.$store.state.msg.push("1.3 Sponsor creates " + new_address)
          this.$store.state.msg.push(`---------------------- 1. Find Recipient Done`)
          // // Upload the matching ID file
          // this.sponsor_request_show = true

        })
        .catch((error) => {
          // handle error
          console.log(error)
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    },

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
      
      console.log("Update request notification response", unread_request_notification)
      this.$toasted.success("Update the request notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("----------------------2. Unread Request")
      this.$store.state.msg.push("2.1 Update the request notification")

      let cur_unread_request_Taskid_dict = unread_request_notification["check_dict"]
      for (let task_id in cur_unread_request_Taskid_dict){
        const recipient_data_folder = 'Recipient_Data/'
        fs.mkdirSync(recipient_data_folder, { recursive: true})

        const filename = 'shiyan.csv'
        const data = fs.readFileSync(recipient_data_folder + filename,
          {encoding:'utf8', flag:'r'});
  
        let data_array = data.split("\n")

        const payload = {
          task_id: task_id,
          file: data_array
        }
        
        this.$axios.post('/match_recipient_id/', payload)
          .then((response) => {
            // handle success
            console.log("Recipient uploads id file", response)
            this.$toasted.success(`Recipient uploads id file`, { icon: 'fingerprint' })
            this.$store.state.msg.push(`2.2 Recipient uploads id file`)
            this.$store.state.msg.push("--------------------------2. Unread Request DOne")
          })
          .catch((error) => {
            // handle error
            console.log(error)
            // console.log(error.response.data)
            // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
          })
      }
    },

    // recipient_csv() {
      
    //   csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
    //   this.unread_request_show  = false

    //   console.log('recipient数据', res)
    //   const payload = {
    //     task_id: this.task_id,
    //     file: res,
    //   }

    //   this.$axios.post('/match_recipient_id/', payload)
    //     .then((response) => {
    //     // handle success
    //     console.log(`Recipient sends the csv file.`, response)
    //     this.$toasted.success(`Recipient sends the csv file.`, { icon: 'fingerprint' })
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    //   }) 
    // },

    unread_match_id(unread_match_id_notification) {
      
          
      console.log("Update match id notification response", unread_match_id_notification)
      this.$toasted.success("Update the match id notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("-------------------------- 3. Unread Match ID")
      this.$store.state.msg.push("3.1 Update the match id notification")

      let cur_unread_match_id_Taskid_dict = unread_match_id_notification["check_dict"]

      for (let task_id in cur_unread_match_id_Taskid_dict){

        let check_sponsor = cur_unread_match_id_Taskid_dict[task_id]
        console.log("check sponsor: match id notification", check_sponsor)
        if (check_sponsor == 1){
          console.log("3.2 Unread_match_id_sponsor")
          this.$store.state.msg.push("3.2 Unread_match_id_sponsor")
          this.unread_match_id_sponsor(task_id)
        }  
        else{
          console.log("3.2 Unread_match_id_recipient")
          this.$store.state.msg.push("3.2 Unread_match_id_recipient")
          this.unread_match_id_recipient(task_id)
        }
      }

    },

    unread_match_id_sponsor(task_id) {
      
      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      let vm = this;

      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("3.3 Match Folder: Sponsor creates " + Match_folder)
      this.$toasted.success("3.3 Match Folder: Sponsor creates " + Match_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("3.3 Match Folder: Sponsor creates " + Match_folder)
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
          console.log("3.4 Sponsor gets matched id file")
          vm.$toasted.success("3.4 Sponsor gets matched id file", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.4 Sponsor gets matched id file")

          for(let i = 0;i < response.data.match_id_file.length; i++){
            const cur_recipient = response.data.recipient_random_id_pair[i];
            const filename = vm.sharedState.user_id + '_to_' + cur_recipient + '.csv';

            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');

            // Store match_id file with different recipient
            fs.writeFileSync(Match_folder + filename, cur_match_id_file)
            
            console.log('3.5 Sponsor Saved Matched id File!');
            vm.$toasted.success('3.5 Sponsor Saved Matched id File!', { icon: 'fingerprint' })
            vm.$store.state.msg.push('3.5 Sponsor Saved Matched id File!')
          }

          // calculate initial situation
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(5000); // 程序滞留5000ms

          // store initial situation
          // Create 'Local_Data/id/task_id/0' folder
          const Round0_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/0/'
          fs.mkdirSync(Round0_folder, { recursive: true})

          console.log("3.6 Sponsor creates " + Round0_folder)
          vm.$toasted.success("3.6 Sponsor creates " + Round0_folder, { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.6 Sponsor creates " + Round0_folder)

          const filename = 'Sent_Initial_Situation.csv';
          
          // temporary data
          let arr =  new Array(5);   
          for(let i = 0;i < arr.length; i++){
            arr[i] = new Array(5);    
          }
          arr[0][1] = "Sponsor Situation File"
          arr[0][2] = 2
          arr = arr.join('\n');

          // Store match_id file
          fs.writeFileSync(Round0_folder + filename, arr)
          
          console.log('3.7 Sponsor Saved ' + filename);
          vm.$toasted.success('3.7 Sponsor Saved ' + filename, { icon: 'fingerprint' })
          vm.$store.state.msg.push('3.7 Sponsor Saved ' + filename)
          
          let data_array = arr.split("\n")

          const payload1 = {
            situation: data_array,
            task_id: task_id
          }

          // send initial situation
          // async
          vm.$axios.post('/send_situation/', payload1)
            .then((response) => {
            // handle success
            console.log("3.8 sponsor sends the situation", response)
            vm.$toasted.success("3.8 sponsor sends the situation", { icon: 'fingerprint' })
            vm.$store.state.msg.push("3.8 sponsor sends the situation")
            this.$store.state.msg.push("-------------------------- 3. Unread Match ID Done")
          })
          .catch((error) => {
            console.log(error)
          })

        })
        .catch((error) => {
          console.log(error)
          // handle error
        }) 
    },

    unread_match_id_recipient(task_id) {

      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("3.3 Recipient creates " + Match_folder)
      this.$toasted.success("3.3 Recipient creates " + Match_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("3.3 Recipient creates " + Match_folder)
      
      // Obtain Match_id file
      const payload = {
        task_id: task_id
      }
      const path = `/users/${this.sharedState.user_id}/match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          console.log("3.4 Recipient gets matched id file", response)
          this.$toasted.success("3.4 Recipient gets matched id file", { icon: 'fingerprint' })
          this.$store.state.msg.push("3.4 Recipient gets matched id file")
          
          const cur_sponsor = response.data.sponsor_random_id;
          const filename = this.sharedState.user_id + '_to_' + cur_sponsor + '.csv';

          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join('\n');

          // Store match_id file
          fs.writeFileSync(Match_folder + filename, cur_match_id_file)
         
          console.log("3.5 Recipient saves matched id file")
          this.$toasted.success("3.5 Recipient saves matched id file", { icon: 'fingerprint' })
          this.$store.state.msg.push("3.5 Recipient saves matched id file")
          this.$store.state.msg.push("-------------------------- 3. Unread Match ID Done")
        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 
    },

    unread_situation(unread_situation_notification) {
      
      this.$store.state.msg.push("-------------------------- 4. Unread Situation")
      console.log("4.1 Update the situation notification", unread_situation_notification)
      this.$toasted.success("4.1 Update the situation notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("4.1 Update the situation notification")

      let cur_unread_situation_Taskid_dict = unread_situation_notification["check_dict"]
      let cur_unread_situation_Rounds_dict = unread_situation_notification["rounds_dict"]

      for (let task_id in cur_unread_situation_Taskid_dict){

        let check_sponsor = cur_unread_situation_Taskid_dict[task_id];
        let rounds = cur_unread_situation_Rounds_dict[task_id];

        // check if the current client is sponsor or not of the specific task
        if (check_sponsor == 1){
          this.unread_situation_sponsor(rounds, task_id)
        }  
        else{
          this.unread_situation_recipient(rounds, task_id)
        }
      }
    },

    unread_situation_sponsor(rounds, task_id) {
      console.log("4.2 Cur round is:", rounds, task_id);
      this.$store.state.msg.push("4.2 Cur round is: " + rounds.toString())
      let vm = this;

      // 1. local db


      // train the model
      // 1. python shiyan.py --argument1 argument2

      // const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      // command call


      // get output

      // store output
      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      const filename = 'Sponsor_Trained_Local_Model.csv';
        
      // temporary data
      let arr =  new Array(5);   
      for(let i = 0;i < arr.length; i++){
        arr[i] = new Array(5);    
      }
      arr[0][1] = "sponsor_trained_local_model"
      arr[0][2] = 5
      arr = arr.join('\n');

      // Store match_id file
      fs.writeFileSync(Round_folder + filename, arr)
      console.log("4.3 Sponsor saved " + filename + " at " + Round_folder);
      vm.$toasted.success("4.3 Sponsor saved " + filename + " at " + Round_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("4.3 Sponsor saved " + filename + " at " + Round_folder)
       this.$store.state.msg.push("-------------------------- 4. Unread Situation Done")

    },

    unread_situation_recipient(rounds, task_id) {
      
      let vm = this;

      // Create 'Local_Data/id/task_id/rounds' folder
      // store the situation from sponsor
      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      fs.mkdirSync(Round_folder, { recursive: true})
      
      console.log("4.2 Recipient creates " + Round_folder)
      this.$toasted.success("4.2 Recipient creates " + Round_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("4.2 Recipient creates " + Round_folder)

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      
      const path = `/users/${vm.sharedState.user_id}/situation_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // store the situation file

          console.log("4.3 Recipient gets situation file")
          vm.$toasted.success("4.3 Recipient gets situation file", { icon: 'fingerprint' })
          this.$store.state.msg.push("4.3 Recipient gets situation file")

          const cur_sender = response.data.sender_random_id;
          const filename = cur_sender + '_to_' + vm.sharedState.user_id + '.csv';

          let cur_situation_file = JSON.parse(response.data.situation);
          cur_situation_file = cur_situation_file.join('\n');

          // Store match_id file with different recipient
          fs.writeFileSync(Round_folder + filename, cur_situation_file)
          console.log('4.4 Recipient Saved Situation File!');
          vm.$toasted.success('4.4 Recipient Saved Situation File!', { icon: 'fingerprint' })
          this.$store.state.msg.push('4.4 Recipient Saved Situation File!')
          
          // train the model
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(5000); // 程序滞留15000ms
          // get output

          // store output

          const filename1 = 'Recipient_Trained_Local_Model.csv';
          
          // temporary data
          let arr =  new Array(5);   
          for(let i = 0;i < arr.length; i++){
            arr[i] = new Array(5);    
          }
          arr[0][1] = "recipient_trained_local_model"
          arr[0][2] = 5
          arr = arr.join('\n');

          // Store match_id file
          fs.writeFileSync(Round_folder + filename1, arr)

          console.log("4.5 Recipient saved " + filename1 + " at " + Round_folder);
          vm.$toasted.success("4.5 Recipient saved " + filename1 + " at " + Round_folder, { icon: 'fingerprint' })
          this.$store.state.msg.push("4.5 Recipient saved " + filename1 + " at " + Round_folder)

          let data_array = arr.split("\n")

          const payload1 = {
            task_id: task_id,
            output: data_array,
          }

          // send output
          // async
          vm.$axios.post('/send_output/', payload1)
            .then((response) => {
            // handle success
            console.log("4.6 Recipient sends output", response)
            vm.$toasted.success("4.6 Recipient sends output", { icon: 'fingerprint' })
            this.$store.state.msg.push("4.6 Recipient sends output")
            this.$store.state.msg.push("-------------------------- 4. Unread Situation Done")
          })
          .catch((error) => {
            console.log(error)
          })

        })
        .catch((error) => {
          console.log(error)
          // handle error
        }) 


    },
    
    unread_output(unread_output_notification) {


      // let task_id_set = new Set()
      // for (let i = 0; i < task_id_list.length; i++){
      //   console.log("arr[i]", task_id_list[i])
      //   task_id_set.add(task_id_list[i])
      // }

      // let distinct_task_id_list = Array.from(task_id_set)
      this.$store.state.msg.push("-------------------------- 5. Unread Output")
      console.log("5.1 Update the output notification", unread_output_notification)
      this.$toasted.success("5.1 Update the output notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("5.1 Update the output notification")

      let cur_unread_output_Rounds_dict = unread_output_notification["rounds_dict"]

      for (let task_id in cur_unread_output_Rounds_dict){
        let rounds = cur_unread_output_Rounds_dict[task_id];
        this.unread_output_singleTask(rounds, task_id);
      }
    },

    unread_output_singleTask(rounds, task_id){

      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      let vm = this
      // Obtain output from recipients

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      const url = `/users/${this.sharedState.user_id}/output/`

      this.$axios.post(url, payload)
        .then((response) => {
          console.log("5.2 Sponsor gets output model")
          vm.$toasted.success("5.2 Sponsor gets output model", { icon: 'fingerprint' })
          this.$store.state.msg.push("5.2 Sponsor gets output model")
          // iterate the match_id_file
          for(let i = 0;i < response.data.output.length; i++){

            const cur_recipient = response.data.sender_random_ids_list[i];
            const filename = cur_recipient + '_to_' + this.sharedState.user_id + '.csv';

            let cur_output = JSON.parse(response.data.output[i]);
            cur_output = cur_output.join('\n');

            // Store the output
            fs.writeFileSync(Round_folder + filename, cur_output)
            console.log('5.3 Sponsor saves Output model');
            vm.$toasted.success('5.3 Sponsor saves Output model', { icon: 'fingerprint' })
            this.$store.state.msg.push('5.3 Sponsor saves Output model')
            // terminate
            if ((rounds+1) >= this.max_round){
              continue;
            }
             // Create Folder: current_path/Local Data/task_id/roundn+1
            const new_Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + (rounds+1) + '/'
            fs.mkdirSync(new_Round_folder, { recursive: true})

              console.log("5.4 Sponsor creates " + new_Round_folder)
              vm.$toasted.success("5.4 Sponsor creates " + new_Round_folder, { icon: 'fingerprint' })
              this.$store.state.msg.push("5.4 Sponsor creates " + new_Round_folder)
              // Update situation

              function sleep(time) {
                let startTime = window.performance.now();
                while (window.performance.now() - startTime < time) {}
              }
              sleep(5000); // 程序滞留15000ms

              const filename1 = 'Update_Initial_Situation.csv';
                
              let arr =  new Array(5);   
              for(let i = 0;i < arr.length; i++){
                arr[i] = new Array(5);    
              }
              arr[0][1] = "Update_Initial_Situation"
              arr[0][2] = 5
              arr = arr.join('\n');

              // Store match_id file
              fs.writeFileSync(new_Round_folder + filename1, arr)
              
              console.log("5.5 Sponsor saved update situation " + filename1 + " at " + new_Round_folder);
              vm.$toasted.success("5.5 Sponsor saved update situation " + filename1 + " at " + new_Round_folder, { icon: 'fingerprint' })
              this.$store.state.msg.push("5.5 Sponsor saved update situation " + filename1 + " at " + new_Round_folder)

              let data_array = arr.split("\n");

              const payload1 = {
                situation: data_array,
                task_id: task_id
              }

              // send updated situation
              // async
              vm.$axios.post('/send_situation/', payload1)
                .then((response) => {
                // handle success
                console.log("5.6 Sponsor updates situation done", response)
                vm.$toasted.success("5.6 Sponsor updates situation done", { icon: 'fingerprint' })
                this.$store.state.msg.push("5.6 Sponsor updates situation done")
                this.$store.state.msg.push("-------------------------- 5. Unread Output Done")
              })
              .catch((error) => {
                console.log(error)
              })

          }
        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 
    },

    unread_test_request(unread_test_request_notification) {
      
      // Only Recipient calls this function
      console.log("2.1 Update Test request notification response", unread_test_request_notification)
      this.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("-----------------------Test Stage: 2.Unread Test Request")
      this.$store.state.msg.push("2.1 Update Test request notification")

      let cur_unread_test_request_Taskid_dict = unread_test_request_notification["check_dict"]
      for (let task_id in cur_unread_test_request_Taskid_dict){
        const recipient_data_folder = 'Test/Recipient_Data/'
        fs.mkdirSync(recipient_data_folder, { recursive: true})

        const filename = 'shiyan.csv'
        const data = fs.readFileSync(recipient_data_folder + filename,
          {encoding:'utf8', flag:'r'});
  
        let data_array = data.split("\n")

        const payload = {
          task_id: task_id,
          file: data_array
        }
        
        this.$axios.post('/match_test_recipient_id/', payload)
          .then((response) => {
            // handle success
            console.log("2.2 Test: Recipient uploads id file", response)
            this.$toasted.success(`2.2 Test: Recipient uploads id file`, { icon: 'fingerprint' })
            this.$store.state.msg.push(`2.2 Test: Recipient uploads id file`)
            this.$store.state.msg.push("--------------------------2. Unread Test Request Done")
          })
          .catch((error) => {
            // handle error
            console.log(error)
            // console.log(error.response.data)
            // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
          })
      }
    },



    unread_test_match_id(unread_test_match_id_notification) {
      console.log("3.1 Update Test match id notification response", unread_match_id_notification)
      this.$toasted.success("3.1 Update the Test match id notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("-----------------------Test Stage: 3.Unread Test Match ID")
      this.$store.state.msg.push("3.1 Update the Test match id notification")

      let cur_unread_test_match_id_Taskid_dict = unread_test_match_id_notification["check_dict"]

      for (let task_id in cur_unread_test_match_id_Taskid_dict){

        let check_sponsor = cur_unread_test_match_id_Taskid_dict[task_id]
        console.log("check test sponsor: match id notification", check_sponsor)
        if (check_sponsor == 1){
          console.log("3.2 Unread_test_match_id_sponsor")
          this.$store.state.msg.push("3.2 Test: Unread_test_match_id_sponsor")
          this.unread_test_match_id_sponsor(task_id)
        }  
        else{
          console.log("3.2 Unread_test_match_id_recipient")
          this.$store.state.msg.push("3.2 Test: Unread_test_match_id_recipient")
          this.unread_test_match_id_recipient(task_id)
        }
      }
    },

    unread_test_match_id_sponsor(task_id) {

      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Match/'
      let vm = this;

      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("3.3 Test: Match Folder: Sponsor creates " + Match_folder)
      this.$toasted.success("3.3 Test: Match Folder: Sponsor creates " + Match_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("3.3 Test: Match Folder: Sponsor creates " + Match_folder)
      // Obtain Match_id file
      // async
      const payload = {
        task_id: task_id
      }
      
      const path = `/users/${vm.sharedState.user_id}/test_match_id_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // iterate the match_id_file
          console.log("3.4 Test: Sponsor gets matched id file")
          vm.$toasted.success("3.4 Test: Sponsor gets matched id file", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.4 Test: Sponsor gets matched id file")

          for(let i = 0;i < response.data.match_id_file.length; i++){
            const cur_recipient = response.data.recipient_random_id_pair[i];
            const filename = vm.sharedState.user_id + '_to_' + cur_recipient + '.csv';

            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');

            // Store match_id file with different recipient
            fs.writeFileSync(Match_folder + filename, cur_match_id_file)
            
            console.log('3.5 Test: Sponsor Saved Matched id File!');
            vm.$toasted.success('3.5 Test: Sponsor Saved Matched id File!', { icon: 'fingerprint' })
            vm.$store.state.msg.push('3.5 Test: Sponsor Saved Matched id File!')
          }

          // Test T Results
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(5000); // 程序滞留5000ms

          function find_Train_Models(startPath) {
          let result=[];
          function finder(path) {
              let files=fs.readdirSync(path);
              files.forEach((val,index) => {
                  let fPath=join(path,val);
                  let stats=fs.statSync(fPath);
                  // console.log("val", val)
                  // console.log("stats", fPath, stats)
                  if(stats.isDirectory()) finder(fPath);
                  if(stats.isFile()&&val=="Sponsor_Trained_Local_Model.csv") {
                    // result.push(fPath);
                    let data = fs.readFileSync(fPath,
                      {encoding:'utf8', flag:'r'});
                    result.push(data);
                  }
              });
            }
            finder(startPath);
            return result;
          }

          let train_path = 'Local_Data/' + this.sharedState.user_id + '/' + task_id;
          let files = find_Train_Models(train_path);
          
          console.log("3.6 Test: Sponsor gets all train models")
          vm.$toasted.success("3.6 Test: Sponsor gets all train models", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.6 Test: Sponsor gets all train models")

          const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';
          fs.mkdirSync(Test_Output_folder, { recursive: true});

          for (let i = 0;i < files.length; i++){
            console.log(files[i]);
            let filename = "Test_Models" + i.toString();
            fs.writeFileSync(Test_Output_folder + filename, files[i])
          }
          
          console.log("3.7 Test: Sponsor stores all test model results")
          vm.$toasted.success("3.7 Test: Sponsor stores all test model results", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.7 Test: Sponsor stores all test model results")
          this.$store.state.msg.push("--------------------------2. Unread Test Match ID Done")

        })
        .catch((error) => {
          console.log(error)
          // handle error
        }) 
    },

    unread_test_match_id_recipient(task_id) {
      // Create 'Local_Data/id/task_id/Match/' folder
      let vm = this;
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Match/'
      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("3.3 Test: Match Folder: Sponsor creates " + Match_folder)
      this.$toasted.success("3.3 Test: Match Folder: Sponsor creates " + Match_folder, { icon: 'fingerprint' })
      this.$store.state.msg.push("3.3 Test: Match Folder: Sponsor creates " + Match_folder)
      
      // Obtain Match_id file
      const payload = {
        task_id: task_id
      }
      const path = `/users/${this.sharedState.user_id}/test_match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          console.log("3.4 Test: Recipient gets matched id file", response)
          this.$toasted.success("3.4 Test: Recipient gets matched id file", { icon: 'fingerprint' })
          this.$store.state.msg.push("3.4 Test: Recipient gets matched id file")
          
          const cur_sponsor = response.data.sponsor_random_id;
          const filename = this.sharedState.user_id + '_to_' + cur_sponsor + '.csv';

          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join('\n');

          // Store match_id file
          fs.writeFileSync(Match_folder + filename, cur_match_id_file)
         
          console.log("3.5 Test: Recipient saves matched id file")
          this.$toasted.success("3.5 Test: Recipient saves matched id file", { icon: 'fingerprint' })
          this.$store.state.msg.push("3.5 Test: Recipient saves matched id file")

          // Test T Results
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(5000); // 程序滞留5000ms

          function find_Train_Models(startPath) {
          let result=[];
          function finder(path) {
              let files=fs.readdirSync(path);
              files.forEach((val,index) => {
                  let fPath=join(path,val);
                  let stats=fs.statSync(fPath);
                  // console.log("val", val)
                  // console.log("stats", fPath, stats)
                  if(stats.isDirectory()) finder(fPath);
                  if(stats.isFile()&&val=="Recipient_Trained_Local_Model.csv") {
                    // result.push(fPath);
                    let data = fs.readFileSync(fPath,
                      {encoding:'utf8', flag:'r'});
                    result.push(data);
                  }
              });
            }
            finder(startPath);
            return result;
          }

          let train_path = 'Local_Data/' + this.sharedState.user_id + '/' + task_id;
          let files = find_Train_Models(train_path);
          
          console.log("3.6 Test: Recipient gets all train models")
          vm.$toasted.success("3.6 Test: Recipient gets all train models", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.6 Test: Recipient gets all train models")

          const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';
          fs.mkdirSync(Test_Output_folder, { recursive: true});

          for (let i = 0;i < files.length; i++){
            console.log(files[i]);
            let filename = "Test_Models" + i.toString();
            fs.writeFileSync(Test_Output_folder + filename, files[i])
          }
          
          console.log("3.7 Test: Recipient stores all test model results")
          vm.$toasted.success("3.7 Test: Recipient stores all test model results", { icon: 'fingerprint' })
          vm.$store.state.msg.push("3.7 Test: Recipient stores all test model results")
          
          const payload1 = {
            task_id: task_id,
            output: files
          }

          // send output
          // async
          vm.$axios.post('/send_test_output/', payload1)
            .then((response) => {
            // handle success
            console.log("3.9 Test: Recipient sends all test model results", response)
            vm.$toasted.success("3.9 Test: Recipient sends all test model results", { icon: 'fingerprint' })
            this.$store.state.msg.push("3.9 Test: Recipient sends all test model results")
            this.$store.state.msg.push("-------------------------- 4. Unread Match ID Done")
          })
          .catch((error) => {
            console.log(error)
          })

        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 
    },

    unread_test_output(unread_test_output_notification) {
      this.$store.state.msg.push("-------------------------- 4. Unread Test Output")
      console.log("4.1 Update Test output notification", unread_test_output_notification)
      this.$toasted.success("4.1 Update Test output notification", { icon: 'fingerprint' })
      this.$store.state.msg.push("4.1 Update Test output notification")

      let cur_unread_test_output_Taskid_dict = unread_test_output_notification["check_dict"]

      for (let task_id in cur_unread_test_output_Taskid_dict){
        this.unread_test_output_singleTask(task_id);
      }
    },

    unread_test_output_singleTask(rounds, task_id){

      const Test_Output_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Test/Output/';
      let vm = this
      // Obtain output from recipients

      const payload = {
        task_id: task_id,
      }
      const url = `/users/${this.sharedState.user_id}/test_output/`

      this.$axios.post(url, payload)
        .then((response) => {
          console.log("4.2 Test: Sponsor gets Recipients' Test output model")
          vm.$toasted.success("4.2 Test: Sponsor gets Recipients' Test output model", { icon: 'fingerprint' })
          this.$store.state.msg.push("4.2 Test: Sponsor gets Recipients' Test output model")
          // iterate the match_id_file
          for(let i = 0;i < response.data.output.length; i++){

            const cur_recipient = response.data.sender_random_ids_list[i];
            const filename = cur_recipient + '_to_' + this.sharedState.user_id + '.csv';

            let multiple_outputs_from_one_recipient = JSON.parse(response.data.output[i]);
            for (let j = 0; j < multiple_outputs_from_one_recipient.length; j++){
              let cur_output = multiple_outputs_from_one_recipient[j].join('\n');

              // Store the output
              fs.writeFileSync(Round_folder + filename, cur_output)
              console.log("4.3 Test: Sponsor saves Recipients' Output model");
              vm.$toasted.success("4.3 Test: Sponsor saves Recipients' Output model", { icon: 'fingerprint' })
              this.$store.state.msg.push("4.3 Test: Sponsor saves Recipients' Output model")
              this.$store.state.msg.push("-------------------------- 4. Unread Test Output Done")
            }
            
          }
        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 
    },


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
    // window.unread_match_id_recipient = this.unread_match_id_recipient
    // window.unread_situation_sponsor = this.unread_situation_sponsor
    // window.unread_situation_recipient = this.unread_situation_recipient
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
                console.error(error)
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
</script>