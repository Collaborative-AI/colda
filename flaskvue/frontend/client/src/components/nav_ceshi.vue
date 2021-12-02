<template>
  <div>
</div>
</template>

<script>
import store from '../store.js'
import axios from 'axios'
import $ from 'jquery'
import db from '../db'
console.log('dbzzzz', db)
import authority from '../authority'



// // use Node API
// If we run npm run electron:serve, window.ex would have the object
// else we are running unittest, we will require directly
const ex = window.ex ? window.ex : require('child_process');
console.log("1231", ex, window.ex)

const fs = window.fs ? window.fs : require('fs');
console.log("123", fs)

const os = window.os ? window.os : require('os');
console.log("1232", os)

const node_path = window.node_path ? window.node_path : require('path');
console.log("1233", node_path)

const dialog = window.dialog ? window.dialog : require('electron');
console.log("1234", dialog)


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
      checkAuthority: authority.checkAuthority,
      sharedState: store.state,
      unread_request_show: false,
      assistor_num: 0,
      max_round: 3,
      root: '',
      exe_position: '',
      showView: true,
      test_response: {},
      
    }
  },
  methods: {

    // which_mode(task_id){
    //   let select_pending_record = 'SELECT * FROM User_Manual_Table WHERE "task_id" = ' + '"'+ task_id + '"';
    //   // console.log("select_pending_record", select_pending_record)
    //   db.get(select_pending_record, function(err, row){
    //     if (err){ 
    //       console.log(err);
    //     }
    //   if (row == null){
    //     return 'Auto'
    //   }else{
    //     return 'Manual'
    //   } 
    //   }) //end db
      
    // },

    plus(a, b) {
    return a + b;
  },

    // test_axios_integration() {
    //   console.log("llililililili")
    //   console.log(this.$axios, this.$axios.get, this.$axios.get('/url'))
    //   this.$axios.get('/url')
    //     .then((response) => {
    //       // handle success
    //       console.log('response', response)
    //       // return response
    //   })

    //   // db.get('/url')
    //   //   .then((response) => {
    //   //     // handle success
    //   //     console.log('response2', response)
    //   //     return response
    //   // })

    //   // console.log("6666666",this.$db, this.$db.get, this.$db.get())
    //   // let select_sentence = ''
    //   // console.log( '6235235', this.$db.get(select_sentence, function(err, row){
    //   //   if (err){
    //   //     console.log(err);
    //   //   }
    //   //   console.log('response2', row)
    //   // }) )

    //   const better_sqlite3_command = this.$db.prepare('SELECT age FROM cats WHERE name = ?');
    //   console.log("45421", better_sqlite3_command)
    //   const cat = better_sqlite3_command.get('Joey');
    //   console.log("452123", cat)

    // },

    test_axios() {
      console.log("wowowowowoow")
      console.log(this.$axios, this.$axios.get, this.$axios.get('/url'))
      this.$axios.get('/url')
        .then((response) => {
          // handle success
          console.log('response', response)
          // return response
      })

      // db.get('/url')
      //   .then((response) => {
      //     // handle success
      //     console.log('response2', response)
      //     return response
      // })

      // console.log("6666666",this.$db, this.$db.get, this.$db.get())
      // let select_sentence = ''
      // console.log( '6235235', this.$db.get(select_sentence, function(err, row){
      //   if (err){
      //     console.log(err);
      //   }
      //   console.log('response2', row)
      // }) )

      const better_sqlite3_command = this.$db.prepare('SELECT age FROM cats WHERE name = ?');
      console.log("45421", better_sqlite3_command)
      const cat = better_sqlite3_command.get('Joey');
      console.log("452123", cat)

    },

    refreshView () {
      this.showView = false // 通过v-if移除router-view节点
      this.$nextTick(() => {
        this.showView = true // DOM更新后再通过v-if添加router-view节点
      })
    },
    
    handlerLogout (e) {
      store.logoutAction()
      this.$toasted.show('You have been logged out.', { icon: 'fingerprint' })
      this.$router.push('/login')
    },

    

    handle_train_log_address(task_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      console.log("train_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        console.log("log.txt created");
      }
      return Log_address
    },

    handle_test_log_address(task_id, test_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "test", test_id.toString(), "log.txt")
      console.log("test_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        console.log("creating log.txt");
        fs.openSync(Log_address, "w");
        console.log("log.txt created");
      }
      return Log_address
    },

    // Helper Function for checking algorithm return value
    handle_Algorithm_return_value(name, return_val, first_val, second_val) {
      console.log(name, return_val)
      // check if return_val obeys the correct return value
      if (first_val != null){
        if (return_val[0] != first_val){
          return false
        }
      }
      if (second_val != null){
         if (return_val[1] != second_val){
           return false
         }
      }  
      return true
    },


  },

  created () {
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },
  mounted () {

  }
 }
// exports.default = Navbar
</script>

<style scoped>

</style>