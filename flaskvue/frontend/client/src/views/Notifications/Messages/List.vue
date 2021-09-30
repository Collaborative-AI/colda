<template>
  <div>
    <!-- 用户收到的私信列表 -->
    <div class="card border-0 g-mb-15">
      <!-- Panel Header -->
      <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
        <h3 class="h6 mb-0">
          <i class="icon-bubbles g-pos-rel g-top-1 g-mr-5"></i> Participated Tasks <small v-if="messages">(Total: {{ messages._meta.total_items }} tasks, {{ messages._meta.total_pages }} pages)</small>
        </h3>
        <div class="dropdown g-mb-10 g-mb-0--md">
          <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="icon-options-vertical g-pos-rel g-top-1"></i>
          </span>
          <div class="dropdown-menu dropdown-menu-right rounded-0 g-mt-10">
            
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 1 }}" class="dropdown-item g-px-10">
              <i class="icon-plus g-font-size-12 g-color-gray-dark-v5 g-mr-5">good</i> 每页 1 条
            </router-link>
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 5 }}" class="dropdown-item g-px-10">
              <i class="icon-layers g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 5 条
            </router-link>
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 10 }}" class="dropdown-item g-px-10">
              <i class="icon-wallet g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 10 条
            </router-link>
            
            <div class="dropdown-divider"></div>
            
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 20 }}" class="dropdown-item g-px-10">
              <i class="icon-fire g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 20 条
            </router-link>
            
          </div>
        </div>
      </div>
      <!-- End Panel Header -->
      <!-- <p> {{messages}}</p> -->

      <!-- Panel Body -->
      <div class="d-flex justify-content-start g-brd-around g-brd-gray-light-v4 g-brd-left-1 g-pa-20 g-mb-10"
        v-for="(message, index) in messages.items" v-bind:key="index">
        <div class="g-mt-2">
          <!-- <router-link v-bind:to="{ path: `/user/${message.sender.id}` }">
            <span v-if="message.is_new" class="d-inline-block g-pos-rel">
              <span class="u-badge-v2--xs u-badge--top-left g-bg-red g-mt-7 g-ml-7"></span>
              
              <img class="g-brd-around g-brd-gray-light-v4 g-pa-2 g-width-50 g-height-50 rounded-circle" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username">
              
            </span>
            
            <img v-else class="g-brd-around g-brd-gray-light-v4 g-pa-2 g-width-50 g-height-50 rounded-circle" v-bind:src="message.sender._links.avatar" v-bind:alt="message.sender.name || message.sender.username">
          </router-link> -->
        </div>
          <div class="align-self-center g-px-10">
          <!-- <p class="m-0">Task Name</p> -->
          <!-- <p class="m-0">{{ message.task_name }}</p> -->
          <p class="m-0">Task Name: {{ message.task_name }}</p>
          <p class="m-0">Task ID:  {{ message.task_id }} </p>

          
          <!-- <h5 class="h5 g-color-gray-dark-v1 mb-0"> -->
            <!-- <router-link v-bind:to="{ path: `/user/${message.sender.id}` }" class="g-text-underline--none--hover">
              <span class="g-mr-5">{{ message.sender.name || message.sender.username }}</span>
            </router-link> -->
            <!-- <small class="g-font-size-12 g-color-aqua">Task Name: <small v-if="message.task_id" class="g-font-size-12 g-color-deeporange"> {{ message.task_name }} </small></small> -->
            <!-- <small class="g-font-size-12 g-color-aqua">Task Name: <small v-if="message.task_id" class="g-font-size-12 g-color-deeporange"> {{ message.task_name }} </small></small> -->
            <!-- <p>Task Name: {{ message.task_name }}</p> -->
            <!-- <small class="g-font-size-12 g-color-aqua">Task ID: <small v-if="message.task_id" class="g-font-size-12 g-color-deeporange"> {{ message.task_id }} </small></small> -->
          <!-- </h5> -->
          
          <p>{{ $moment(message.match_id_timestamp).format('YYYY年MM月DD日 HH:mm:ss') }}</p>
          <!-- <p class="m-0">{{ message }}</p> -->
          <!-- <p class="m-0">{{ message.task_name }}</p> -->
          <!-- <p>Task Name: {{ message.task_name }}</p> -->

          
          <!-- <p class="m-0">{{ message }}</p> -->
        </div>
        <div class="align-self-center ml-auto">
          <router-link v-bind:to="{ name: 'MessagesHistory', query: { from: message.task_id } }">
            <button class="btn btn-block u-btn-outline-primary g-rounded-20 g-px-10">Details</button>
          </router-link>
        </div>
      </div>
      <!-- End Panel Body -->


      

    </div>
  
    <!-- Pagination #04 -->
    <div v-if="messages">
      <pagination
        v-bind:cur-page="messages._meta.page"
        v-bind:per-page="messages._meta.per_page"
        v-bind:total-pages="messages._meta.total_pages">
      </pagination>
    </div>
    <!-- End Pagination #04 -->
  </div>
</template>

<script>
import store from '../../../store'
import Pagination from '../../../components/Pagination'
import db from '../../../db'

// const store = require('../../../store').default
// const Pagination = require('../../../components/Pagination.vue').default
export default {
  name: 'List',  // this is the name of the component
  components: {
    Pagination
  },
  data () {
    return {
      sharedState: store.state,
      messages: "",
      
    }
  },

//   computed: {
//   taskName () {
//     return this.messages.items.map((message) => {
//       // do your work on this element here 
//       let vm = this;
      
//       let myPromise = new Promise(function(resolve, reject) {
//         let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=?';
//       db.get(select_sentence, [message.task_id], function(err, row){
//         if (err){ 
//           console.log(err);
//         }
//         else{
//           // vm.task_name=row.task_name
//           // vm.task_name.push(row.task_name)
//           // console.log(row.task_name)
//           vm.task_name=row.task_name
//           // return this.task_name
//           console.log(vm.task_name)
//           // return row.task_name
//         }
//         // console.log(vm.task_name)
//       })
//       console.log(vm.task_name)
//       resolve(vm.task_name)
//       })
//       // let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=' + `task_id`;
      
//       // console.log(task_name)
//       // return this.task_name[0]
//       // console.log(vm.ta)
//       // return vm.ta
//       myPromise.then(
//         function(value){
//           console.log(value)
//           return value}
//       )

//     })

//   }
// },

  

  methods: {
    // getUserMessagesSenders (id) {
    //   let page = 1
    //   let per_page = 5
    //   if (typeof this.$route.query.page != 'undefined') {
    //     page = this.$route.query.page
    //   }

    //   if (typeof this.$route.query.per_page != 'undefined') {
    //     per_page = this.$route.query.per_page
    //   }
      
    //   const path = `/users/${id}/messages-senders/?page=${page}&per_page=${per_page}`
    //   this.$axios.get(path)
    //     .then((response) => {
    //       // handle success
    //       this.messages = response.data
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.error(error)
    //     })
    // }
    getUserHistory (id) {
      let vm=this
      let page = 1
      let per_page = 5
      if (typeof this.$route.query.page != 'undefined') {
        page = this.$route.query.page
      }

      if (typeof this.$route.query.per_page != 'undefined') {
        per_page = this.$route.query.per_page
      }
     
      const path = `/get_user_history/?page=${page}&per_page=${per_page}`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          vm.messages = response.data
          console.log("vm.messages", vm.messages)
          // console.log(this.messages.items)
          // console.log(typeof(this.messages))
          // console.log(this.messages.items[0].task_id)
          // console.log(this.messages.items[0])
          for (let i=0; i<vm.messages.items.length; i++) {
            console.log("get_user_history_message", vm.messages.items[i]);
            
            // let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=' + `task_id`;
            let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=?';
            db.get(select_sentence, [vm.messages.items[i].task_id], function(err, row){
              if (err){ 
                console.log("get_name_from_frontend_db", err);
              }
              else{
                // console.log(row.task_name)
                // vm.messages.items[i]['task_name']=row.task_name
                console.log("name_db", row)
                if (row){
                  vm.$set(vm.messages.items[i],'task_name',row.task_name)
                }
                console.log("vm.messages.items[i]", vm.messages.items[i])
                // console.log(row.task_name)
                // console.log(typeof(row))
              }
        
        
        
            })//end db.get
            // console.log(vm.messages)
            
          }//end for
          // console.log(vm.messages)
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },

    // taskName: function(task_id) {
    //   // console.log(task_id)
    //   let vm = this;
    //   // let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=' + `task_id`;
    //   let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=?';
    //   db.get(select_sentence, [task_id], function(err, row){
    //     if (err){ 
    //       console.log(err);
    //     }
    //     else{
    //       vm.task_name=row.task_name
    //       // console.log(vm.task_name)
    //       // return row.task_name
    //     }
    //     // console.log(vm.task_name)
        
        
    //   })
      
    //   return vm.task_name
    //   // return row.task_name
    // }
  },
  // beforeCreate () {
  //   // this.getUserMessagesSenders(this.sharedState.user_id)
  //   this.getUserHistory(this.sharedState.user_id)
  // },
  created () {
    // this.getUserMessagesSenders(this.sharedState.user_id)
    this.getUserHistory(this.sharedState.user_id)
  },

  // beforeMount () {
  //   // this.getUserMessagesSenders(this.sharedState.user_id)
  //   this.getUserHistory(this.sharedState.user_id)
  // },
  // 当路由变化后(比如变更查询参数 page 和 per_page)重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    // this.getUserMessagesSenders(this.sharedState.user_id)
    this.getUserHistory(this.sharedState.user_id)
  }
}
</script>
