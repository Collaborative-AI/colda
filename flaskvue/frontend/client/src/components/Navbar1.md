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

          <li class="nav-item g-mr-20">
            <button @click="find_assistor">Call For Help</button>
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
// import store from '../store'
// import axios from 'axios'
// import $ from 'jquery'
// import db from '../db'

const store = require('../store').default
// 在 JQuery 中使用 axios 的话需要重新导入，不能使用 main.js 中定义的 Vue 全局属性 this.$axios
const axios = require('axios').default
const $ = require('jquery')
const db = require('../db').default

// use Node API
const fs = window.require('fs');
const join = window.require('path').join;
const xlsx2json = window.require("node-xlsx");
const sqlite3 = window.require('sqlite3').verbose();;
const ex = window.require("child_process");
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
      root: '../../../package/exp',
      picked: "not_receive",
    }
  },
  methods: {

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
// exports.default = Navbar
</script>