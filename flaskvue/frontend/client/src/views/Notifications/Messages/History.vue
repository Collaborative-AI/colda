<template>
<div>
  <!-- 历史私信列表 -->
  <div class="card border-0 g-mb-15 my-5">
    
    <!-- End Panel Header -->
    <div class="form-group">
      <router-link v-bind:to="{ name: 'FindTestAssistorHelper', query: { from: task_id } }">
        <button v-show="isSponsor" class="btn btn-success float-right">Call For Test</button>
      </router-link>
      
                
    </div>



    <!-- Panel Body -->
    <div class="card-block g-pa-0" >
      <!-- Chat. Message Area. Messages. -->
      <div class="g-brd-around g-brd-gray-light-v4 g-pa-20">
        <div v-for="(message, index) in messages" v-bind:key="index">
          <!-- Chat. Message Area. Message (From). -->
          <section class="g-mb-30">
            <div class="media g-mb-12">
              
              <div class="media-body">
                <div class="d-inline-block g-width-300 g-width-auto--sm g-bg-gray-light-v8 g-font-size-12 g-font-size-default--lg g-color-gray-dark-v6 g-rounded-10 g-pa-10-15">
                  <p class="mb-0">
                    {{ message }}
                  </p>
                </div>
              </div>
              <!-- End Chat. Message Area. Message. Body. -->
            </div>

          </section>

        </div>
        
      </div>
      <button @click="getLog($route.query.from)" class="btn btn-success float-right">Refresh</button>
      <!-- End Chat. Message Area. Messages. -->
    </div>
    <!-- End Panel Body -->
  </div>

</div>
</template>

<script>
const fs = window.require('fs');
const ex = window.require("child_process");
const path = window.require('path');
const os = window.require('os');
const node_path = window.require('path');

import store from '../../../store'
// 导入 vue-markdown 组件解析 markdown 原文为　HTML
// import VueMarkdown from 'vue-markdown'
import Pagination from '../../../components/Pagination'

// const store = require('../../../store').default
// // const VueMarkdown = require('vue-markdown').default
// const Pagination = require('../../../components/Pagination.vue').default


export default {
  name: 'History',  //this is the name of the component
  components: {
    // VueMarkdown,
    Pagination
  },
  data () {
    return {
      sharedState: store.state,
      user: '',
      messages: [],
      typein_message: '',
      showOnce: true,
      replyMessageForm: {
        body: '',
        errors: 0,  // 发送私信时，表单验证是否有错误
        bodyError: null
      },
      // Log_content_array: null,
      isSponsor: false,
      root: '',
      task_id: '',
    }
  },
  methods: {
    stop_train_task() {
      const payload = {
        task_id: this.task_id,
      }

      this.$axios.post('/stop_train_task/', payload)
        .then((response) => {

          console.log(response.data)

        })
        .catch((error) => {
          // handle error
          console.log(error)
        })


    },
    
    getLog(task_id) {
      const train_log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      let Log_content = fs.readFileSync(train_log_address, {encoding:'utf8', flag:'r'});
      Log_content = Log_content.split("\n")
      this.messages = [];
      for (let i = 0; i < Log_content.length; i++){
        this.messages.push(Log_content[i])
      }

    
      // const test_log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + response.data.test_id + '/log.txt'
    },
    // get_test_history_id(task_id) {



    // },
    checkSponsor(task_id) {
      const payload = {
        task_id: task_id,
      }

      this.$axios.post('/check_sponsor/', payload)
        .then((response) => {
          // console.log("response@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", response)
          if (response.data.result == "sponsor"){
            this.isSponsor = true
            // console.log("#############1", this.isSponsor)
          }else{
            this.isSponsor = false
            // console.log("#############2", this.isSponsor)
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })

        this.$axios.post('/get_test_history_id/', payload)
        .then((response) => {

          let test_id_list = response.data.test_id_list;
          for (let i = 0; i < test_id_list.length; i++){
            const test_log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id_list[i] + '/log.txt'
            let test_log_content = fs.readFileSync(test_log_address, {encoding:'utf8', flag:'r'});
            test_log_content = test_log_content.split("\n")
            for (let i = 0; i < test_log_content.length; i++){
              this.messages.push(test_log_content[i])
            }
            
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })
    },


    // getUser (id) {
    //   const path = `/users/${id}`
    //   this.$axios.get(path)
    //     .then((response) => {
    //       // handle success
    //       this.user = response.data
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.error(error)
    //     })
    // },
    // getUserHistoryMessages (id) {
    //   let page = 1
    //   let per_page = 10
    //   if (typeof this.$route.query.page != 'undefined') {
    //     page = this.$route.query.page
    //   }

    //   if (typeof this.$route.query.per_page != 'undefined') {
    //     per_page = this.$route.query.per_page
    //   }
      
    //   const path = `/users/${id}/history-messages/?from=${this.$route.query.from}&page=${page}&per_page=${per_page}`
    //   this.$axios.get(path)
    //     .then((response) => {
    //       // handle success
    //       this.messages = response.data
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.error(error)
    //     })
    // },
    // onSubmitReply () {
      // this.replyMessageForm.errors = 0  // 重置

      // if (!this.replyMessageForm.body) {
      //   this.replyMessageForm.errors++
      //   this.replyMessageForm.bodyError = 'Body is required.'
      //   // 给 bootstrap-markdown 编辑器内容添加警示样式，而不是添加到 #post_body 上
      //   $('#replyMessageForm .md-editor').closest('.form-group').addClass('u-has-error-v1')  // Bootstrap 4
      // } else {
      //   this.replyMessageForm.bodyError = null
      //   $('#replyMessageForm .md-editor').closest('.form-group').removeClass('u-has-error-v1')
      // }

      // if (this.replyMessageForm.errors > 0) {
      //   // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
      //   return false
      // }

    //   const payload = {
    //     assistor_id: this.user.id,
    //     // body: this.replyMessageForm.body
    //     body: this.typein_message
    //   }
    //   this.$axios.post('/messages/', payload)
    //     .then((response) => {
    //       // handle success
    //       this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
    //       this.onResetReply()
    //       this.getUserHistoryMessages(this.sharedState.user_id)
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.log(error.response.data)
    //       this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
    //     })
    // },
    // onResetReply () {
    //   // this.replyMessageForm.body = ''
    //   // this.replyMessageForm.bodyError = null
    //   // $('#replyMessageForm .md-editor').closest('.form-group').removeClass('u-has-error-v1')
    //   this.showOnce = false
    //   this.typein_message = ''
    // },
  },
  created () {
    this.task_id = this.$route.query.from;
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
    this.getLog(this.$route.query.from)
    this.checkSponsor(this.$route.query.from)
    
    // 初始化 bootstrap-markdown 插件
    // $(document).ready(function() {
    //   $("#replyMessageFormBody").markdown({
    //     autofocus:false,
    //     savable:false,
    //     iconlibrary: 'fa',  // 使用Font Awesome图标
    //     language: 'zh'
    //   })
    // })
  },
  // 当路由变化后(比如变更查询参数 page 和 per_page)重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    this.getLog(this.$route.query.from)
    this.checkSponsor(this.$route.query.from)
  }
}
</script>

<style>
  .card-block {
    overflow: auto;
}
</style>