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

export default {
  name: 'Navbar',  //this is the name of the component
  data () {
    return {
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

          console.log("Sponsor sends id file")
          this.$toasted.success(`Sponsor sends id file`, { icon: 'fingerprint' })

          // Create 'Local_Data/id/task_id/' folder
          const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/'
          fs.mkdirSync(new_address, { recursive: true})

          console.log("Sponsor creates " + new_address)
          this.$toasted.success("Sponsor creates " + new_address, { icon: 'fingerprint' })
          
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

    unread_request(sender_random_id_list, task_id_list) {
      
      const update_request_notification = {
          sender_random_id_list: sender_random_id_list,
          task_id_list: task_id_list,
      }

      this.$axios.post('/update_request_notification/', update_request_notification)
        .then((response) => {
          // handle success            
          console.log("Update request notification response", response)
          this.$toasted.success("Update the request notification", { icon: 'fingerprint' })

          for (let i = 0; i < sender_random_id_list.length; i++){
            // check if the current client is sponsor or not of the specific task
            // handle success
            const recipient_data_folder = 'Recipient_Data/'
            fs.mkdirSync(recipient_data_folder, { recursive: true})

            const filename = 'shiyan.csv'
            const data = fs.readFileSync(recipient_data_folder + filename,
              {encoding:'utf8', flag:'r'});
      
            let data_array = data.split("\n")

            const payload = {
              task_id: task_id_list[i],
              file: data_array
            }
            
            this.$axios.post('/match_recipient_id/', payload)
              .then((response) => {
                // handle success
                console.log("Recipient uploads id file", response)
                this.$toasted.success(`Recipient uploads id file`, { icon: 'fingerprint' })
              })
              .catch((error) => {
                // handle error
                console.log(error)
                // console.log(error.response.data)
                // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
              })
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })


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

    unread_match_id(sender_random_id_list, task_id_list) {
      
      const update_match_id_notification = {
          sender_random_id_list: sender_random_id_list,
          task_id_list: task_id_list,
      }

      this.$axios.post('/update_match_id_notification/', update_match_id_notification)
        .then((response) => {
          // handle success            
          console.log("Update match id notification response", response)
          this.$toasted.success("Update the match id notification", { icon: 'fingerprint' })

          for (let i = 0; i < sender_random_id_list.length; i++){
            // check if the current client is sponsor or not of the specific task
            // handle success
            console.log("check sponsor: match id notification", response.data.check_sponsor[task_id_list[i]])
            if (response.data.check_sponsor[task_id_list[i]] == 1){
              console.log("unread_match_id_sponsor")
              this.unread_match_id_sponsor(sender_random_id_list[i], task_id_list[i])
            }  
            else{
              console.log("unread_match_id_recipient")
              this.unread_match_id_recipient(sender_random_id_list[i], task_id_list[i])
            }
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    },

    unread_match_id_sponsor(sender_random_id, task_id) {
      
      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      let vm = this;

      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("Sponsor creates " + Match_folder)
      this.$toasted.success("Sponsor creates " + Match_folder, { icon: 'fingerprint' })
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
          console.log("Sponsor gets matched id file")
          vm.$toasted.success("Sponsor gets matched id file", { icon: 'fingerprint' })

          for(let i = 0;i < response.data.match_id_file.length; i++){
            const cur_recipient = response.data.recipient_random_id_pair[i];
            const filename = vm.sharedState.user_id + '_to_' + cur_recipient + '.csv';

            let cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');

            // Store match_id file with different recipient
            fs.writeFileSync(Match_folder + filename, cur_match_id_file)
            
            console.log('Sponsor Saved Matched id File!');
            vm.$toasted.success('Sponsor Saved Matched id File!', { icon: 'fingerprint' })
          }

          // calculate initial situation
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(15000); // 程序滞留15000ms

          // store initial situation
          // Create 'Local_Data/id/task_id/0' folder
          const Round0_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/0/'
          fs.mkdirSync(Round0_folder, { recursive: true})

          console.log("Sponsor creates" + Round0_folder)
          vm.$toasted.success("Sponsor creates" + Round0_folder, { icon: 'fingerprint' })

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
          
          console.log('Sponsor Saved ' + filename);
          vm.$toasted.success('Sponsor Saved ' + filename, { icon: 'fingerprint' })
          
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
            console.log("sponsor sends the situation", response)
            vm.$toasted.success("sponsor sends the situation", { icon: 'fingerprint' })
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

    unread_match_id_recipient(sender_random_id, task_id) {

      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      fs.mkdirSync(Match_folder, { recursive: true})
      
      console.log("Recipient creates " + Match_folder)
      this.$toasted.success("Recipient creates " + Match_folder, { icon: 'fingerprint' })
      
      // Obtain Match_id file
      const payload = {
        task_id: task_id
      }
      const path = `/users/${this.sharedState.user_id}/match_id_file/`
      // async
      this.$axios.post(path, payload)
        .then((response) => {

          console.log("Recipient gets matched id file", response)
          this.$toasted.success("Recipient gets matched id file", { icon: 'fingerprint' })
          const cur_sponsor = response.data.sponsor_random_id;
          const filename = this.sharedState.user_id + '_to_' + cur_sponsor + '.csv';

          let cur_match_id_file = JSON.parse(response.data.match_id_file[0]);
          cur_match_id_file = cur_match_id_file.join('\n');

          // Store match_id file
          fs.writeFileSync(Match_folder + filename, cur_match_id_file)
         
          console.log("Recipient saves matched id file")
          this.$toasted.success("Recipient saves matched id file", { icon: 'fingerprint' })

        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 

    },

    unread_situation(sender_random_id_list, task_id_list) {

      const update_situation_notification = {
          sender_random_id_list: sender_random_id_list,
          task_id_list: task_id_list,
      }

      this.$axios.post('/update_situation_notification/', update_situation_notification)
        .then((response) => {
          // handle success            
          console.log("Update the situation notification", response)
          this.$toasted.success("Update the situation notification", { icon: 'fingerprint' })
          for (let i = 0; i < sender_random_id_list.length; i++){

              // check if the current client is sponsor or not of the specific task
              // handle success
              if (response.data.check_sponsor[task_id_list[i]] == 1){
                this.unread_situation_sponsor(response.data.rounds[task_id_list[i]],
                  sender_random_id_list[i], task_id_list[i])
              }  
              else{
                this.unread_situation_recipient(response.data.rounds[task_id_list[i]],
                  sender_random_id_list[i], task_id_list[i])
              }
          }
        })
        .catch((error) => {
          // handle error
          console.log(error);
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
    },

    unread_situation_sponsor(rounds, sender_random_id, task_id) {
      console.log("cur round is:", rounds, task_id);
      
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
      console.log("Sponsor saved " + filename + " at " + Round_folder);
      vm.$toasted.success("Sponsor saved " + filename + " at " + Round_folder, { icon: 'fingerprint' })

    },

    unread_situation_recipient(rounds, sender_random_id, task_id) {
      
      let vm = this;

      // Create 'Local_Data/id/task_id/rounds' folder
      // store the situation from sponsor
      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + rounds + '/'
      fs.mkdirSync(Round_folder, { recursive: true})
      
      console.log("Recipient creates " + Round_folder)
      this.$toasted.success("Recipient creates " + Round_folder, { icon: 'fingerprint' })

      const payload = {
        task_id: task_id,
        rounds: rounds
      }
      
      const path = `/users/${vm.sharedState.user_id}/situation_file/`
      vm.$axios.post(path, payload)
        .then((response) => {
          // call back
          // store the situation file

          console.log("Recipient gets situation file")
          vm.$toasted.success("Recipient gets situation file", { icon: 'fingerprint' })

          const cur_sender = response.data.sender_random_id;
          const filename = cur_sender + '_to_' + vm.sharedState.user_id + '.csv';

          let cur_situation_file = JSON.parse(response.data.situation);
          cur_situation_file = cur_situation_file.join('\n');

          // Store match_id file with different recipient
          fs.writeFileSync(Round_folder + filename, cur_situation_file)
          console.log('Recipient Saved Situation File!');
          vm.$toasted.success('Recipient Saved Situation File!', { icon: 'fingerprint' })

          // train the model
          function sleep(time) {
            let startTime = window.performance.now();
            while (window.performance.now() - startTime < time) {}
          }
          sleep(15000); // 程序滞留15000ms
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

          console.log("Recipient saved " + filename1 + " at " + Round_folder);
          vm.$toasted.success("Recipient saved " + filename1 + " at " + Round_folder, { icon: 'fingerprint' })

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
            console.log("Recipient sends output", response)
            vm.$toasted.success("Recipient sends output", { icon: 'fingerprint' })
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
    
    unread_output(sender_random_id_list, task_id_list) {


      let task_id_set = new Set()
      for (let i = 0; i < task_id_list.length; i++){
        console.log("arr[i]", task_id_list[i])
        task_id_set.add(task_id_list[i])
      }

      let distinct_task_id_list = Array.from(task_id_set)

      // Update Notification
      const update_output_notification = {
        task_id_list: task_id_list
      }

      this.$axios.post('/update_output_notification/', update_output_notification)
        .then((response) => {
          // devide the task_id_list by task id
          console.log("Update the output notification", response)
          this.$toasted.success("Update the output notification", { icon: 'fingerprint' })
          // for (const [task_id, cur_task_sender_random_ids] of Object.entries(divide_dict)) {
          //   console.log("output task_id", response.data[task_id])
          //   this.unread_output_singleTask(response.data[task_id], task_id, cur_task_sender_random_ids)
          // }
          for (let i = 0; i < distinct_task_id_list.length; i++){
            console.log("output task_id", response.data[distinct_task_id_list[i]], distinct_task_id_list[i])
            this.unread_output_singleTask(response.data[distinct_task_id_list[i]], distinct_task_id_list[i])
          }
          
      })
      .catch((error) => {
        console.log(error)
      })  

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
          console.log("Sponsor gets output model")
          vm.$toasted.success("Sponsor gets output model", { icon: 'fingerprint' })
          // iterate the match_id_file
          for(let i = 0;i < response.data.output.length; i++){

            const cur_recipient = response.data.sender_random_ids_list[i];
            const filename = cur_recipient + '_to_' + this.sharedState.user_id + '.csv';

            let cur_output = JSON.parse(response.data.output[i]);
            cur_output = cur_output.join('\n');

            // Store the output
            fs.writeFileSync(Round_folder + filename, cur_output)
            console.log('Sponsor saves Output model');
            vm.$toasted.success('Sponsor saves Output model', { icon: 'fingerprint' })

            // terminate
            if ((rounds+1) >= this.max_round){
              continue;
            }
             // Create Folder: current_path/Local Data/task_id/roundn+1
            const new_Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + (rounds+1) + '/'
            fs.mkdirSync(new_Round_folder, { recursive: true})

              console.log("Sponsor creates " + new_Round_folder)
              vm.$toasted.success("Sponsor creates " + new_Round_folder, { icon: 'fingerprint' })
              // Update situation

              function sleep(time) {
                let startTime = window.performance.now();
                while (window.performance.now() - startTime < time) {}
              }
              sleep(15000); // 程序滞留15000ms

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
              
              console.log("Sponsor saved update situation " + filename1 + " at " + new_Round_folder);
              vm.$toasted.success("Sponsor saved update situation " + filename1 + " at " + new_Round_folder, { icon: 'fingerprint' })


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
                console.log("Sponsor updates situation done", response)
                vm.$toasted.success("Sponsor updates situation done", { icon: 'fingerprint' })
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
  },

  mounted () {
    // 轮询 /api/users/<int:id>/notifications/ 请求用户的新通知
    window.unread_request = this.unread_request;
    window.unread_match_id = this.unread_match_id;
    window.unread_situation = this.unread_situation;
    window.unread_output = this.unread_output;

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

      function polling() {
        console.log(`第${count}次开始 ${getTime.now() - startTime}`); // 显示开始时间
        if (window.localStorage.getItem('Apollo-token')) {
          // 如果用户已登录，才开始请求 API
          const payload = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1]))
          const user_id = payload.user_id
          // const path = `/users/${user_id}/notifications/?since=${since}`
          const path = `/users/${user_id}/notifications/`
          // console.log("since shua xin",since)
          axios.get(path)
            .then((response) => {
              // handle success
              console.log("--------------------------------------------------------- new polling")
              let promise_list = [];
              for(let i = 0; i < response.data.length; i++) {
                sender_random_id_list = response.data[i].sender_random_id_list;
                task_id_list = response.data[i].task_id_list;
                
                if (response.data[i].payload != 0){
                  switch (response.data[i].name) {
                  
                  case 'unread request':
                    unread_request_count = response.data[i].payload
                    console.log("unread_request_count", unread_request_count)

                    // const update_request_notification = {
                    //   sender_random_id_list: sender_random_id_list,
                    //   task_id_list: task_id_list,
                    // }

                    // let unread_request_promise = this.$axios.post('/update_request_notification/', update_request_notification)
                    // promise_list.push(unread_request_promise);

                    // unread_request_promise.then((response) => {
                    //     // handle success            
                    //     console.log("Update request notification response", response)
                    //     this.$toasted.success("Update the request notification", { icon: 'fingerprint' })

                    //     for (let i = 0; i < sender_random_id_list.length; i++){
                    //       // check if the current client is sponsor or not of the specific task
                    //       // handle success
                    //       const recipient_data_folder = 'Recipient_Data/'
                    //       fs.mkdirSync(recipient_data_folder, { recursive: true})

                    //       const filename = 'shiyan.csv'
                    //       const data = fs.readFileSync(recipient_data_folder + filename,
                    //         {encoding:'utf8', flag:'r'});
                    
                    //       let data_array = data.split("\n")

                    //       const payload = {
                    //         task_id: task_id_list[i],
                    //         file: data_array
                    //       }
                          
                    //       this.$axios.post('/match_recipient_id/', payload)
                    //         .then((response) => {
                    //           // handle success
                    //           console.log("Recipient uploads id file", response)
                    //           this.$toasted.success(`Recipient uploads id file`, { icon: 'fingerprint' })
                    //         })
                    //         .catch((error) => {
                    //           // handle error
                    //           console.log(error)
                    //           // console.log(error.response.data)
                    //           // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                    //         })
                    //     }
                    //   })
                    //   .catch((error) => {
                    //     // handle error
                    //     console.log(error)
                    //     // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                    //   })
                    unread_request(sender_random_id_list, task_id_list)
                    break
                  
                  case 'unread match id':
                    unread_match_id_count = response.data[i].payload
                    console.log("unread_match_id_count", unread_match_id_count)

                    // const update_match_id_notification = {
                    //   sender_random_id_list: sender_random_id_list,
                    //   task_id_list: task_id_list,
                    // }

                    // let unread_match_id_promise = this.$axios.post('/update_match_id_notification/', update_match_id_notification)
                    // promise_list.push(unread_match_id_promise);

                    // unread_match_id_promise.then((response) => {
                    //   // handle success            
                    //   console.log("Update match id notification response", response)
                    //   this.$toasted.success("Update the match id notification", { icon: 'fingerprint' })

                    //   for (let i = 0; i < sender_random_id_list.length; i++){
                    //     // check if the current client is sponsor or not of the specific task
                    //     // handle success
                    //     console.log("check sponsor: match id notification", response.data.check_sponsor[task_id_list[i]])
                    //     if (response.data.check_sponsor[task_id_list[i]] == 1){
                    //       console.log("unread_match_id_sponsor")
                    //       this.unread_match_id_sponsor(sender_random_id_list[i], task_id_list[i])
                    //     }  
                    //     else{
                    //       console.log("unread_match_id_recipient")
                    //       this.unread_match_id_recipient(sender_random_id_list[i], task_id_list[i])
                    //     }
                    //   }
                    // })
                    // .catch((error) => {
                    //   // handle error
                    //   console.log(error)
                    //   // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                    // })


                    unread_match_id(sender_random_id_list, task_id_list)
                    break
                  
                  case 'unread situation':
                    unread_situation_count = response.data[i].payload
                    console.log("unread_situation_count", unread_situation_count)

                    // const update_situation_notification = {
                    //   sender_random_id_list: sender_random_id_list,
                    //   task_id_list: task_id_list,
                    // }

                    // let unread_situation_promise = this.$axios.post('/update_situation_notification/', update_situation_notification)
                    // promise_list.push(unread_situation_promise);

                    // unread_situation_promise.then((response) => {
                    //     // handle success            
                    //     console.log("Update the situation notification", response)
                    //     this.$toasted.success("Update the situation notification", { icon: 'fingerprint' })
                    //     for (let i = 0; i < sender_random_id_list.length; i++){

                    //         // check if the current client is sponsor or not of the specific task
                    //         // handle success
                    //         if (response.data.check_sponsor[task_id_list[i]] == 1){
                    //           this.unread_situation_sponsor(response.data.rounds[task_id_list[i]],
                    //             sender_random_id_list[i], task_id_list[i])
                    //         }  
                    //         else{
                    //           this.unread_situation_recipient(response.data.rounds[task_id_list[i]],
                    //             sender_random_id_list[i], task_id_list[i])
                    //         }
                    //     }
                    //   })
                    //   .catch((error) => {
                    //     // handle error
                    //     console.log(error);
                    //     // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                    //   })


                    unread_situation(sender_random_id_list, task_id_list)
                    break
                  
                  case 'unread output':
                    unread_output_count = response.data[i].payload
                    console.log("unread_output_count", unread_output_count)

                    // let task_id_set = new Set()
                    // for (let i = 0; i < task_id_list.length; i++){
                    //   console.log("arr[i]", task_id_list[i])
                    //   task_id_set.add(task_id_list[i])
                    // }

                    // let distinct_task_id_list = Array.from(task_id_set)

                    // // Update Notification
                    // const update_output_notification = {
                    //   task_id_list: task_id_list
                    // }

                    // let unread_output_promise = this.$axios.post('/update_output_notification/', update_output_notification)
                    // promise_list.push(unread_output_promise);

                    // unread_output_promise.then((response) => {
                    //     // devide the task_id_list by task id
                    //     console.log("Update the output notification", response)
                    //     this.$toasted.success("Update the output notification", { icon: 'fingerprint' })
                    //     // for (const [task_id, cur_task_sender_random_ids] of Object.entries(divide_dict)) {
                    //     //   console.log("output task_id", response.data[task_id])
                    //     //   this.unread_output_singleTask(response.data[task_id], task_id, cur_task_sender_random_ids)
                    //     // }
                    //     for (let i = 0; i < distinct_task_id_list.length; i++){
                    //       console.log("output task_id", response.data[distinct_task_id_list[i]], distinct_task_id_list[i])
                    //       this.unread_output_singleTask(response.data[distinct_task_id_list[i]], distinct_task_id_list[i])
                    //     }
                    // })
                    // .catch((error) => {
                    //   console.log(error)
                    // }) 






                    unread_output(sender_random_id_list, task_id_list)
                    break

                  case 'unread_messages_count':
                    unread_messages_count = response.data[i].payload
                    break
                  }
                }
                // since = response.data[i].timestamp
                // console.log("since",since)

              }
              

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
                }, 15000)

              
            })
            .catch((error) => {
              // handle error
              console.log(error)
            })
        }else{
          setTimeout(function(){
            polling()
          }, 15000);
        }
        console.log(`第${count}次结束 ${getTime.now() - startTime}`); // 显示开始时间
        count += 1
      }

      // setTimeout(function(){
      //   polling()
      // }, 3000);
      polling();

    })
  }
}
</script>