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
          <div v-if="sponsor_request_show">
            <input type="file" name="csvfile" ref="csvData" />
            <input type="button" @click="sponsor_csv()" value="JS转换"/>
          </div>

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
      sponsor_request_show: false,
      unread_request_show: false,
      task_id: '',
      recipient_num: 0,
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
      
      // PROMISE
      this.$axios.get('/find_recipient/')
        .then((response) => {
          // handle success
          this.$toasted.success(`Successed call for help`, { icon: 'fingerprint' })
          this.task_id = response.data.task_id

          // Create 'Local_Data/id/task_id/' folder
          const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/'
          fs.mkdir(new_address, { recursive: true }, (err) => {
            if (err) throw err;
          });

          // Upload the matching ID file
          this.sponsor_request_show = true

        })
        .catch((error) => {
          // handle error
          console.log(error.response.data)
          this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    },

    sponsor_csv() {
      csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
        this.sponsor_request_show = false

        console.log('sponsor数据', res)
        const payload = {
          task_id: this.task_id,
          file: JSON.stringify(res),
        }

      this.$axios.post('/match_sponsor_id/', payload)
        .then((response) => {
        // handle success
        console.log("sponsor_id", response)
        this.$toasted.success(`Successed send the csv file.`, { icon: 'fingerprint' })
      })
      .catch((error) => {
      // handle error
        console.log(error)
      // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      })
    })      
    },

    unread_request(sender_random_id_list, task_id_list) {
      this.unread_request_show = true
      this.task_id = task_id_list[0]
    },

    unread_request() {
      
      csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
      this.unread_request_show  = false

      console.log('recipient数据', res)
      const payload = {
        task_id: this.task_id,
        file: JSON.stringify(res),
      }

      this.$axios.post('/match_recipient_id/', payload)
        .then((response) => {
        // handle success
        console.log("recipient_id", response)
        this.$toasted.success(`Successed send the csv file.`, { icon: 'fingerprint' })
        })
        .catch((error) => {
        // handle error
        // console.log(error)
        // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })
      }) 
           
    },

    unread_match_id(sender_random_id_list, task_id_list) {
      
      const update_match_id_notification = {
          sender_random_id_list: JSON.stringify(sender_random_id_list),
          task_id_list: JSON.stringify(task_id_list),
      }

      this.$axios.post('/update_match_id_notification/', update_match_id_notification)
        .then((response) => {
          // handle success            
          console.log(response)
          for (let i = 0; i < sender_random_id_list.length; i++){

              // check if the current client is sponsor or not of the specific task
              // handle success
              if (response.data.check_sponsor[task_id_list[i]] == true){
                this.unread_match_id_sponsor(sender_random_id_list[i], task_id_list[i])
              }  
              else{
                this.unread_match_id_recipient(sender_random_id_list[i], task_id_list[i])
              }
                
              console.log(response)
          }
      })
      .catch((error) => {
      // handle error
      // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      })

    },

    unread_match_id_sponsor(sender_random_id, task_id) {
      
      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'

      // async
      fs.mkdir(Match_folder, { recursive: true }, (err) => {

        // call back
        if (err) throw err;

        // Obtain Match_id file
        // async
        const path = `/users/${this.sharedState.user_id}/match_id_file/?task_id=${task_id}`
        this.$axios.get(path)
          .then((response) => {
            
            let cur_finished_file = 0;
            // call back
            // iterate the match_id_file
            for(let i = 0;i < response.data.match_id_file.length; i++){

              const cur_recipient = response.data.recipient_random_id_pair[i];
              const filename = this.sharedState.user_id + '_to_' + cur_recipient + '.csv';

              const cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
              cur_match_id_file = cur_match_id_file.join('\n');

              // Store match_id file with different recipient
              // async
              fs.writeFile(Match_folder + filename, cur_match_id_file, function (err) {
                if (err) throw err;
                console.log('Saved!');
              });
            }
            
          })
          .catch((error) => {
            // handle error
            console.error(error)
          }) 
      });
      
      // calculate initial situation

      // simulate
      function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
      }

      // 用法
      sleep(3000).then(() => {
        // store initial situation
        // Create 'Local_Data/id/task_id/Match/round0' folder
        const Round0_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/' + 'round0/'
        // async
        fs.mkdir(Round0_folder, { recursive: true }, (err) => {

          // call back
          if (err) throw err;

          const filename = 'Sent_Initial_Situation.csv';
          
          // temporary data
          let arr =  new Array(5);   
          for(let i = 0;i < arr.length; i++){
            arr[i] = new Array(5);    
          }
          arr[0][1] = 1
          arr[0][2] = 2
          arr = arr.join('\n');

          // Store match_id file
          // async
          fs.writeFile(Round0_folder + filename, arr, function (err) {

            // call back
            if (err) throw err;
            console.log('Saved!');
            
            // async
            fs.readFile(Round0_folder + filename, 'utf8' , (err, data) => {

              if (err) {
                console.error(err)
                return
              }

              // call back
              data_array = data.split("\n");
              console.log(data)
              const payload = {
                situation: data_array,
                initial_rounds: "true",
                task_id: task_id
              }

              // send initial situation
              // async
              this.$axios.post('/send_situation/', payload)
                .then((response) => {
                // handle success
                console.log("sponsor match_id finished!!!")
                console.log(response)
              })
              .catch((error) => {
              })

            })

          });
        });    

      })

      

    
    },

    unread_match_id_recipient(sender_random_id, task_id) {

      // Create 'Local_Data/id/task_id/Match/' folder
      const Match_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/'
      fs.mkdir(Match_folder, { recursive: true }, (err) => {
        // call back
        if (err) throw err;

        // Obtain Match_id file
        const path = `/users/${this.sharedState.user_id}/match_id_file/?task_id=${task_id}`
        // async
        this.$axios.get(path)
          .then((response) => {

            const cur_sponsor = response.data.sponsor_random_id;
            const filename = cur_sponsor + '_to_' + this.sharedState.user_id + '.csv';

            const cur_match_id_file = JSON.parse(response.data.match_id_file[i]);
            cur_match_id_file = cur_match_id_file.join('\n');

            // Store match_id file
            // async
            fs.writeFile(Match_folder + filename, cur_match_id_file, function (err) {
              if (err) throw err;
              console.log('Saved!');
            });
            
          })
          .catch((error) => {
            // handle error
            console.error(error)
          }) 

      });
      

    },

    unread_situation(sender_random_id_list, task_id_list) {
      
      const update_situation_notification = {
          sender_random_id_list: sender_random_id_list,
          task_id_list: task_id_list,
      }

      this.$axios.post('/update_situation_notification/', update_situation_notification)
        .then((response) => {
          // handle success            
          console.log(response)
          for (let i = 0; i < sender_random_id_list.length; i++){

              // check if the current client is sponsor or not of the specific task
              // handle success
              if (response.data.check_sponsor[task_id_list[i]] == true){
                this.unread_situation_sponsor(response.data.rounds[task_id_list[i]],
                  sender_random_id_list[i], task_id_list[i])
              }  
              else{
                this.unread_situation_recipient(response.data.rounds[task_id_list[i]],
                  sender_random_id_list[i], task_id_list[i])
              }
                
              console.log(response)
          }
        })
        .catch((error) => {
        // handle error
        // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    },

    unread_situation_sponsor(rounds, sender_random_id, task_id) {
      // train the model
      // 1. python shiyan.py --argument1 argument2
      // 2. 内嵌python

      // get output

      // store output
      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/' + rounds + '/'
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
      fs.writeFile(Round_folder + filename, arr, function (err) {
        if (err) throw err;
        console.log('Sponsor situation Saved!');
      });
    },

    unread_situation_recipient(rounds, sender_random_id, task_id) {
      // train the model

      // get output

      // store output
      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/' + rounds + '/'
      const filename = 'Recipient_Trained_Local_Model.csv';
        
      // temporary data
      let arr =  new Array(5);   
      for(let i = 0;i < arr.length; i++){
        arr[i] = new Array(5);    
      }
      arr[0][1] = "recipient_trained_local_model"
      arr[0][2] = 5
      arr = arr.join('\n');

      // Store match_id file
      fs.writeFile(Round_folder + filename, arr, function (err) {
        if (err) throw err;
        console.log('Recipient situation Saved!');

        fs.readFile(Round_folder + filename, 'utf8' , (err, data) => {

          if (err) {
            console.error(err)
            return
          }

          // call back
          console.log(data)
          data_array = data.split("\n");
          const payload = {
            task_id: task_id,
            rounds: rounds,
            output: data_array,
          }

          // send output
          // async
          this.$axios.post('/send_output/', payload)
            .then((response) => {
            // handle success
            console.log("Recipient output finished!!!")
            console.log(response)
          })
          .catch((error) => {
          })

        })
      });

    },
    
    unread_output(sender_random_id_list, task_id_list) {

      let divide_dict = {}
      for(let i = 0;task_id_list.length; i++){
        divide_dict[task_id_list[i]] = divide_dict.get(task_id_list[i],[]).append(sender_random_id_list[i])
      }

      // Update Notification
      const update_output_notification = {
        task_id_list: task_id_list
      }

      this.$axios.post('/update_output_notification/', update_output_notification)
        .then((response) => {
          // devide the task_id_list by task id
          
          for (const [task_id, cur_task_sender_random_ids] of Object.entries(divide_dict)) {
            this.unread_output_singleTask(response.data.task_id, task_id, cur_task_sender_random_ids)
          }
      })
      .catch((error) => {
      })  

    },

    unread_output_singleTask(rounds, task_id, cur_task_sender_random_ids){

      const Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/' + rounds + '/'
      // Obtain output from recipients
      const url = `/users/${this.sharedState.user_id}/output/?task_id=${task_id}&rounds=${rounds}`

      this.$axios.get(url)
        .then((response) => {
          
          let cur_finished_file = 0;

          // iterate the match_id_file
          for(let i = 0;i < response.data.output.length; i++){

            const cur_recipient = response.data.recipient_random_id_pair[i];
            const filename = cur_recipient + '_to_' + this.sharedState.user_id + '.csv';

            const cur_output = JSON.parse(response.data.output[i]);
            cur_output = cur_output.join('\n');

            // Store the output
            // async
            fs.writeFile(Round_folder + filename, cur_output, function (err) {
              if (err) throw err;

              console.log('Output model from recipient Saved!!!');
            });
          }
          
        })
        .catch((error) => {
          // handle error
          console.error(error)
        }) 

      function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
      }

      // 用法
      sleep(3000).then(() => {
        // Create Folder: current_path/Local Data/task_id/roundn+1
        const new_Round_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/' + 'Match/' + rounds+1 + '/'
        fs.mkdir(new_Round_folder, { recursive: true }, (err) => {
          if (err) throw err;

          // Update initial situation
          const filename = 'Update_Initial_Situation.csv';
            
          let arr =  new Array(5);   
          for(let i = 0;i < arr.length; i++){
            arr[i] = new Array(5);    
          }
          arr[0][1] = "Update_Initial_Situation"
          arr[0][2] = 5
          arr = arr.join('\n');

          // Store match_id file
          fs.writeFile(new_Round_folder + filename, arr, function (err) {
            if (err) throw err;
            console.log('Recipient situation Saved!');

            fs.readFile(new_Round_folder + filename, 'utf8' , (err, data) => {

              if (err) {
                console.error(err)
                return
              }

              // call back
              data_array = data.split("\n");
              console.log(data)
              const payload = {
                situation: data_array,
                initial_rounds: "false",
                task_id: task_id
              }

              // send updated situation
              // async
              this.$axios.post('/send_situation/', payload)
                .then((response) => {
                // handle success
                console.log("Output update situation!!")
                console.log(response)
              })
              .catch((error) => {
              })
            })
          });  
        });

      })

    },

  },
  mounted () {
    // 轮询 /api/users/<int:id>/notifications/ 请求用户的新通知
    $(function() {
      let since = 0
      let total_notifications_count = 0  // 总通知计数
      let unread_request_count = 0  // 收到的新评论通知计数
      let unread_match_id_count = 0  // 收到的新私信通知计数
      let unread_situation_count = 0  // 新粉丝通知计数
      let unread_output_count = 0  // 新的喜欢或赞的通知计数
      let unread_messages_count = 0

      setInterval(function() {
        if (window.localStorage.getItem('Apollo-token')) {
          // 如果用户已登录，才开始请求 API
          const payload = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1]))
          const user_id = payload.user_id
          const path = `/users/${user_id}/notifications/?since=${since}`
          console.log("since shua xin",since)
          axios.get(path)
            .then((response) => {
              // handle success
              for(var i = 0; i < response.data.length; i++) {
                switch (response.data[i].name) {
                  case 'unread request':
                    unread_request_count = response.data[i].payload
                    break
                  
                  case 'unread match id':
                    unread_match_id_count = response.data[i].payload
                    break
                  
                  case 'unread situation':
                    unread_situation_count = response.data[i].payload
                    break
                  
                  case 'unread output':
                    unread_output_count = response.data[i].payload
                    break

                  case 'unread_messages_count':
                    unread_messages_count = response.data[i].payload
                    break
                }
                since = response.data[i].timestamp
                console.log("since",since)

                sender_random_id_list = response.data[i].sender_random_id_list
                task_id_list = response.data[i].task_id_list

                if (unread_request_count != 0){
                  unread_request_count = 0
                  this.unread_request(sender_random_id_list, task_id_list)
                  
                  if (this.unread_request_show == false){
                    this.unread_request_show = true
                  }
                }

                if (unread_match_id_count != 0){
                  unread_match_id_count = 0
                  this.unread_match_id(sender_random_id_list, task_id_list)
                  
                }

                if (unread_situation_count != 0){
                  unread_situation_count = 0
                  this.unread_situation(sender_random_id_list, task_id_list)
                  
                }

                if (unread_output_count != 0){
                  unread_output_count = 0
                  this.unread_output(sender_random_id_list, task_id_list)
                  
                }

              }

              total_notifications_count = unread_request_count + unread_match_id_count + unread_situation_count + unread_output_count + unread_messages_count
              // 每一次请求之后，根据 total_notifications_count 的值来显示或隐藏徽标
              $('#new_notifications_count').text(total_notifications_count)
              $('#new_notifications_count').css('visibility', total_notifications_count ? 'visible' : 'hidden');
            })
            .catch((error) => {
              // handle error
              console.error(error)
            })
        }
      }, 10000)
    })
  }
}
</script>