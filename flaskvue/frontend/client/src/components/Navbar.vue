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
      const payload = {
        recipient_id: 5,
      }
      this.$axios.post('/find_recipient/', payload)
        .then((response) => {
          // handle success
          this.$toasted.success(`Successed send the help`, { icon: 'fingerprint' })
          this.task_id = response.data["new_task_id"]
          // Create File

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
        this.task_id = ''

        console.log('sponsor数据', res)
        const payload = {
          // task_id = this.task_id,
          // body: this.replyMessageForm.body
          file: JSON.stringify(res),
        }


        // , {headers:{'Content-Type':'application/x-www-form-urlencoded' }}
      this.$axios.post('/match_sponsor_id/', payload)
        .then((response) => {
      // handle success
      // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
      // this.onResetReply()
      // this.getUserHistoryMessages(this.sharedState.user_id)
        console.log(response)
      })
      .catch((error) => {
      // handle error
      // console.log(error)
      // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      })
    })      
    },

    recipient_csv() {
      csv2arr.csv(this.$refs.csvData.files[0]).then((res)=>{
        this.sponsor_request_show = false
        this.task_id = ''

        console.log('recipient数据', res)
        const payload = {
          // task_id = this.task_id,
          // body: this.replyMessageForm.body
          file: JSON.stringify(res),
        }


        // , {headers:{'Content-Type':'application/x-www-form-urlencoded' }}
      this.$axios.post('/match_recipient_id/', payload)
        .then((response) => {
      // handle success
      // this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
      // this.onResetReply()
      // this.getUserHistoryMessages(this.sharedState.user_id)
        console.log(response)
      })
      .catch((error) => {
      // handle error
      // console.log(error)
      // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      })
    })      
    },

    unread_request() {
      this.unread_request_show = true
    },

    unread_match_id() {
      
      const payload = {
        task_id: this.task_id,
      }

      // check if the current client is sponsor or not of the specific task
      this.$axios.post('/check_match_id_sponsor/', payload)
        .then((response) => {
      // handle success
          if (response.data["sponsor"] == "true"){
            this.unread_match_id_sponsor()
          }  
          else{
            this.unread_match_id_recipient()
          }
            
        console.log(response)
      })
      .catch((error) => {
      // handle error
      // console.log(error)
      // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      })
    },

    unread_match_id_sponsor() {
      // create local file

      // calculate initial situation

      // send initial situation
      const payload = {
        initial_situation: null,
        initial_rounds: "true",
        task_id: this.task_id
      }

      this.$axios.post('/send_situation/', payload)
        .then((response) => {
        // handle success
        console.log(response)
      })
      .catch((error) => {
      })
    },

    unread_match_id_recipient() {
      // create local file and Store the Matched id file

    },

    unread_situation() {

      // check if the current client is sponsor or not of the specific task
      const payload = {
        task_id: this.task_id,
      }

      // check if the current client is sponsor or not of the specific task, update situation notification
      this.$axios.post('/check_situation_sponsor/', payload)
        .then((response) => {
      // handle success
          if (response.data["sponsor"] == "true"){
            this.unread_situation_sponsor()
          }  
          else{
            this.unread_situation_recipient()
          }
            
        console.log(response)
      })
      .catch((error) => {
      
      })
    },

    unread_situation_sponsor() {
      // train the model

      // get output

      // store output
    },

    unread_situation_recipient() {
      // train the model

      // get output

      // send output
      const payload = {
        output: "output",
        task_id: this.task_id
      }

      this.$axios.post('/send_output/', payload)
        .then((response) => {
        // handle success
        console.log(response)

      })
      .catch((error) => {
      })
    },
    
    unread_output() {

      // Update Notification
      const update_output_notification = {
        task_id: this.task_id
      }

      this.$axios.post('/update_output_notification/', update_output_notification)
        .then((response) => {
        // handle success
        console.log(response)
      })
      .catch((error) => {
      })

      // Create local file


      // Update initial situation


      
      // send situation
      const payload = {
        initial_situation: null,
        initial_rounds: "false",
        task_id: this.task_id
      }

      // check if the current client is sponsor or not of the specific task
      this.$axios.post('/send_situation/', payload)
        .then((response) => {
        // handle success
        console.log(response)
      })
      .catch((error) => {
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
              }

              if (unread_request_count != 0){
                this.unread_request()
              }

              if (unread_match_id_count != 0){
                this.unread_match_id()
              }

              if (unread_situation_count != 0){
                this.unread_situation()
              }

              if (unread_output_count != 0){
                this.unread_output()
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