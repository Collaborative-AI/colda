<template>
<div>
  <!-- 历史私信列表 -->
  <div class="card border-0 g-mb-15">
    <!-- Panel Header -->
    <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
      <!-- <h3 class="h6 mb-0">
        <i class="icon-bubbles g-pos-rel g-top-1 g-mr-5"></i> 与 <router-link v-bind:to="{ path: `/user/${user.id}` }" class="g-text-underline--none--hover">{{ user.name || user.username }}</router-link> 的对话 <small v-if="messages">(共 {{ messages._meta.total_items }} 条, {{ messages._meta.total_pages }} 页)</small>
      </h3> -->
      <div class="dropdown g-mb-10 g-mb-0--md">
        <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-options-vertical g-pos-rel g-top-1"></i>
        </span>
        <div class="dropdown-menu dropdown-menu-right rounded-0 g-mt-10">
          
          <router-link v-bind:to="{ name: 'MessagesIndex' }" class="dropdown-item g-px-10">
            <i class="icon-plus g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 返回私信列表
          </router-link>

          <div class="dropdown-divider"></div>

          <router-link v-bind:to="{ path: $route.fullPath, query: { page: 1, per_page: 1 }}" class="dropdown-item g-px-10">
            <i class="icon-plus g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 1 条
          </router-link>
          <router-link v-bind:to="{ path: $route.fullPath, query: { page: 1, per_page: 5 }}" class="dropdown-item g-px-10">
            <i class="icon-layers g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 5 条
          </router-link>
          <router-link v-bind:to="{ path: $route.fullPath, query: { page: 1, per_page: 10 }}" class="dropdown-item g-px-10">
            <i class="icon-wallet g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 10 条
          </router-link>          
          <router-link v-bind:to="{ path: $route.fullPath, query: { page: 1, per_page: 20 }}" class="dropdown-item g-px-10">
            <i class="icon-fire g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 20 条
          </router-link>
          
        </div>
      </div>
    </div>
    <!-- End Panel Header -->

    <!-- Panel Body -->
    <div class="card-block g-pa-0" >
      <!-- Chat. Message Area. Messages. -->
      <div class="g-brd-around g-brd-gray-light-v4 g-pa-20">
        <div v-for="(message, index) in messages" v-bind:key="index">
          <!-- Chat. Message Area. Message (From). -->
          <section class="g-mb-30">
            <div class="media g-mb-12">
              <!-- Chat. Message Area. Message. Avatar. -->
              <!-- <router-link v-bind:to="{ path: `/user/${message.sender.id}` }" class="d-flex align-self-end g-mr-12">
                <span v-if="message.is_new" class="d-inline-block g-pos-rel">
                  <span class="u-badge-v2--xs u-badge--top-left g-bg-red g-mt-7 g-ml-7"></span>
                  <img class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username">
                  <img class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" src="../../../assets/logo.png" v-bind:alt="message.sender.name || message.sender.username">
                </span>
                <img v-else class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username">
                <img v-else class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" src="../../../assets/logo.png" v-bind:alt="message.sender.name || message.sender.username">
              </router-link> -->
              <!-- End Chat. Message Area. Message. Avatar. -->

              <!-- Chat. Message Area. Message. Body. -->
              <div class="media-body">
                <div class="d-inline-block g-width-300 g-width-auto--sm g-bg-gray-light-v8 g-font-size-12 g-font-size-default--lg g-color-gray-dark-v6 g-rounded-10 g-pa-10-15">
                  <p class="mb-0">
                    {{ message }}
                    <!-- vue-markdown 开始解析markdown，它是子组件，通过 props 给它传值即可
                    v-highlight 是自定义指令，用 highlight.js 语法高亮 -->
                    <!-- <vue-markdown
                      :source="message.body"
                      class="markdown-body"
                      v-highlight>
                    </vue-markdown> -->
                  </p>
                </div>
              </div>
              <!-- End Chat. Message Area. Message. Body. -->
            </div>

            <!-- Chat. Message Area. Message Time -->
            <!-- <em class="d-flex align-self-center align-items-center g-font-style-normal g-color-gray-light-v1 g-ml-50">
              <i class="hs-admin-time icon-clock g-mr-5"></i>
              <small>{{ $moment(message.timestamp).format('YYYY年MM月DD日 HH:mm:ss') }}</small>
              <i v-if="!message.is_new" class="icon-check g-font-size-10 g-color-lightblue-v3 g-ml-12"></i>
            </em> -->
            <!-- End Chat. Message Area. Message Time -->
          </section>
          <!-- End Chat. Message Area. Message (From). -->

          <!-- Chat. Message Area. Message (To). -->
          <!-- <section v-else class="g-mb-30"> -->
            <!-- <div class="media g-mb-12"> -->
              <!-- Chat. Message Area. Message. Body. -->
              <!-- <div class="ml-auto"> -->
                <!-- <div class="d-inline-block g-width-300 g-width-auto--sm g-bg-lightblue-v6 g-font-size-12 g-font-size-default--lg g-color-gray-dark-v6 g-rounded-10 g-pa-10-15"> -->
                  <!-- <p class="mb-0"> -->
                    <!-- {{ message.body }} -->
                    <!-- vue-markdown 开始解析markdown，它是子组件，通过 props 给它传值即可
                    v-highlight 是自定义指令，用 highlight.js 语法高亮 -->
                    <!-- <vue-markdown
                      :source="message.body"
                      class="markdown-body"
                      v-highlight>
                    </vue-markdown> -->
                  <!-- </p> -->
                <!-- </div> -->
              <!-- </div> -->
              <!-- End Chat. Message Area. Message. Body. -->

              <!-- Chat. Message Area. Message. Avatar. -->
              <!-- <router-link v-bind:to="{ path: `/user/${message.sender.id}` }" class="d-flex align-self-end g-ml-12"> -->
                <!-- <span v-if="message.is_new" class="d-inline-block g-pos-rel"> -->
                  <!-- <span class="u-badge-v2--xs u-badge--top-left g-bg-red g-mt-7 g-ml-7"></span> -->
                  <!-- <img class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username"> -->
                  <!-- <img class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" src="../../../assets/logo.png" v-bind:alt="message.sender.name || message.sender.username"> -->
                <!-- </span> -->
                <!-- <img v-else class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username"> -->
                <!-- <img v-else class="rounded-circle g-width-36 g-height-36 g-brd-around g-brd-gray-light-v4 g-pa-2" src="../../../assets/logo.png" v-bind:alt="message.sender.name || message.sender.username"> -->
              <!-- </router-link> -->
              <!-- End Chat. Message Area. Message. Avatar. -->
            <!-- </div> -->

            <!-- Chat. Message Area. Message Time -->
            <!-- <em class="d-flex align-self-center align-items-center justify-content-end g-font-style-normal g-color-gray-light-v1"> -->
              <!-- <i class="hs-admin-time icon-clock g-mr-5"></i> -->
              <!-- <small>{{ $moment(message.timestamp).format('YYYY年MM月DD日 HH:mm:ss') }}</small> -->
              <!-- <i v-if="!message.is_new" class="icon-check g-font-size-10 g-color-lightblue-v3 g-ml-12"></i> -->
            <!-- </em> -->
            <!-- End Chat. Message Area. Message Time -->
          <!-- </section> -->
          <!-- End Chat. Message Area. Message (To). -->
        </div>
        
      </div>
      <!-- End Chat. Message Area. Messages. -->
    </div>
    <!-- End Panel Body -->
  </div>

  <!-- Pagination #04 -->
  <!-- <div v-if="messages">
    <pagination
      v-bind:cur-page="messages._meta.page"
      v-bind:per-page="messages._meta.per_page"
      v-bind:total-pages="messages._meta.total_pages">
    </pagination>
  </div> -->
  <!-- End Pagination #04 -->

  <!-- Reply Message Form -->
  <!-- <form v-if="showOnce" id="replyMessageForm" @submit.prevent="onSubmitReply" @reset.prevent="onResetReply" class="g-mb-40"> -->
    <!-- <div class="form-group"> -->
      <!-- <input type="text" v-model="typein_message" placeholder="Type in message"> -->
      <!-- <textarea v-model="replyMessageForm.body" class="form-control" id="replyMessageFormBody" rows="5" placeholder=" 悄悄话..."></textarea>
      <small class="form-control-feedback" v-show="replyMessageForm.bodyError">{{ replyMessageForm.bodyError }}</small> -->
    <!-- </div> -->
    <!-- <button type="reset" class="btn btn-secondary">Cancel</button> -->
    <!-- <button type="submit" class="btn btn-primary">Submit</button> -->
  <!-- </form> -->
  <div >
    <button v-show="isSponsor" @click="find_test_assistor( $route.query.from )">Call for Test</button>
  </div>
  <!-- <div >
    <button @click="get_test_history_id( $route.query.from )">Load Test Log</button>
  </div> -->
  
  <!-- End Reply Message Form -->
</div>
</template>

<script>
const fs = window.require('fs');
const ex = window.require("child_process");

// import store from '../../../store'
// // 导入 vue-markdown 组件解析 markdown 原文为　HTML
// import VueMarkdown from 'vue-markdown'
// import Pagination from '../../../components/Pagination'

const store = require('../../../store').default
const VueMarkdown = require('vue-markdown').default
const Pagination = require('../../../components/Pagination.vue').default


export default {
  name: 'History',  //this is the name of the component
  components: {
    VueMarkdown,
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
      root: '../../../package/exp',
    }
  },
  methods: {

    getLog(task_id) {
      const train_log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
      let Log_content = fs.readFileSync(train_log_address, {encoding:'utf8', flag:'r'});
      Log_content = Log_content.split("\n")
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

    find_test_assistor(task_id) {
      // const sponsor_data_folder = 'Test_Sponsor_Data/'
      
      // fs.mkdirSync(sponsor_data_folder, { recursive: true})

      // const filename = 'shiyan.csv'
      // const data = fs.readFileSync(sponsor_data_folder + filename,
      //   {encoding:'utf8', flag:'r'});
      
      // let data_array = data.split("\n")
      
      this.$axios.get('/create_new_test_task/')
        .then((response) => {
          
          let test_id = response.data.test_id

          let match_id_address = '../../../package/data/BostonHousing/2/123/1.0/0/test/id.csv'
          let test_hash_id_file_address = null;
          try{
            test_hash_id_file_address = ex.execSync('python3 ../../../package/hash_id.py --id_path ' + match_id_address + ' --root ' + this.root 
                                    + ' --self_id ' + this.sharedState.user_id + ' --task_id ' + task_id + ' --run test' + ' --test_id ' + test_id, {encoding: 'utf8'})
            test_hash_id_file_address = test_hash_id_file_address.replace(/\n/g, '')
            console.log(test_hash_id_file_address)
          }catch(err){
            console.log(err)
          }

          let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address, {encoding:'utf8', flag:'r'});

          const payload = {
            task_id: task_id,
            test_id: test_id, 
            id_file: test_hash_id_file_data
          }
          
          this.$axios.post('/find_test_assistor/', payload)
            .then((response) => {

              const Log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + response.data.test_id + '/log.txt'
              // handle success
              console.log("1.1 Test: Sponsor calls for help", response)
              this.$toasted.success(`1.1 Test: Sponsor calls for help`, { icon: 'fingerprint' })

              console.log("1.2 Test: Sponsor sends id file")
              this.$toasted.success(`1.2 Test: Sponsor sends id file`, { icon: 'fingerprint' })

              // Create 'Local_Data/id/task_id/' folder
              // const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/' + response.data.test_id + '/'
              // fs.mkdirSync(new_address, { recursive: true})

              try {
                fs.appendFileSync(Log_address, "\n You are SPONSOR\n")
                fs.appendFileSync(Log_address, "Test ID: " + test_id + "\n")
                fs.appendFileSync(Log_address, "---------------------- Test Stage Starts\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor\n")
                fs.appendFileSync(Log_address, "1.1 Test: Sponsor calls for test\n")
                fs.appendFileSync(Log_address, "1.2 Test: Sponsor sends id file\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor Done\n")
              } catch (err) {
                console.error(err)
              }

              // // Upload the matching ID file
              // this.sponsor_request_show = true

            })
            .catch((error) => {
              // handle error
              console.log(error)
              // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })

        })
        .catch((error) => {
          console.log(error)
        })
      
    }




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