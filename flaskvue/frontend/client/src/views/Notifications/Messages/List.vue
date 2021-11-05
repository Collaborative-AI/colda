<template>

  <div class="container justify-content-center align-self-center ">

<div class="container">
    <div class="row">
       
        <div class="col-lg-9 right">
         
            <div class="box shadow-sm rounded bg-white mb-3">
                <div class="box-title border-bottom p-3">
                    <h6 class="m-0">Paticipated Tasks <small v-if="messages">(Total: {{ messages._meta.total_items }} tasks, {{ messages._meta.total_pages }} pages)</small></h6>
                </div>
                <div class="box-body p-0" v-for="(message, index) in messages.items" v-bind:key="index">
                    
                    <div class="p-3 d-flex align-items-center border-bottom osahan-post-header">
                        <!-- <div class="dropdown-list-image mr-3"><img class="rounded-circle" src="https://bootdey.com/img/Content/avatar/avatar3.png" alt="" /></div> -->
                        <div class="font-weight-bold mr-3">
                            <div v-if="message.test_indicator == 'test' " class="text-truncate">Test Name: {{ message.test_name }}</div>
                            <div v-if="message.test_indicator == 'train' " class="text-truncate">Task Name: {{ message.task_name }}</div>
                            <div class="small">Task ID:  {{ message.task_id }}</div>
                            <div v-if="message.test_indicator == 'train' " class="small">Task Description:  {{ message.task_description }}</div>
                            <div v-if="message.test_indicator == 'test' " class="small">Test ID:  {{ message.test_id }}</div>
                            
                            <div v-if="message.test_indicator == 'test' " class="small">Test Description:  {{ message.test_description }}</div>


                            <div class="small">{{ $moment(message.match_id_timestamp).format('YYYY年MM月DD日 HH:mm:ss') }}</div>

                            
                        </div>
                        <span class="ml-auto mb-auto">
                            <!-- <div class="btn-group">
                                <button type="button" class="btn btn-light btn-sm rounded" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i class="mdi mdi-dots-vertical"></i>
                                </button>
                                <div class="dropdown-menu dropdown-menu-right">
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-delete"></i> Delete</button>
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-close"></i> Turn Off</button>
                                </div>
                            </div> -->
                            <br />
                            <div class="text-right text-muted pt-1">
                              <router-link v-bind:to="{ name: 'MessagesHistory', query: { from: message.task_id } }">
                                <button class="btn btn-block u-btn-outline-primary g-rounded-20 ">Details</button>
                              </router-link>
                            </div>
                        </span>
                    </div>
                 
               
                   
                    
                    
                    
                </div>
            </div>
        </div>
    </div>
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
          // for (let i=0; i<vm.messages.items.length; i++) {
          //   console.log("get_user_history_message", vm.messages.items[i]);
            
            // let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=' + `task_id`;
            // let select_sentence = 'SELECT * FROM User_Chosen_Path WHERE task_id=?';
            // db.get(select_sentence, [vm.messages.items[i].task_id], function(err, row){
            //   if (err){ 
            //     console.log("get_name_from_frontend_db", err);
            //   }
            //   else{
            //     // console.log(row.task_name)
            //     // vm.messages.items[i]['task_name']=row.task_name
            //     console.log("name_db", row)
            //     if (row){
            //       vm.$set(vm.messages.items[i],'task_name',row.task_name)
            //     }
            //     console.log("vm.messages.items[i]", vm.messages.items[i])
            //     // console.log(row.task_name)
            //     // console.log(typeof(row))
            //   }
        
        
        
            // })//end db.get
            // // console.log(vm.messages)
            
          // }//end for
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
