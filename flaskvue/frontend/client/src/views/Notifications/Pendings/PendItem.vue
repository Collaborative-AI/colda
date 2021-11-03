<template>
  <div class="container">
    <div>Task Name: {{ task_name }}</div>
    <div>Task Id:{{ task_id }}</div>
    <div>Task Description: {{ task_description }}</div>

    <div class="form-group">
      <label for="name">Select File Path</label>
      <input type="text" v-model="manual_file_path" class="form-control" id="name" placeholder="">
      <button @click="get_manual_file_path()" class="btn btn-success">Select File</button>
    </div>
    
    <div class="form-group">
      <label for="name">Input id column</label>
      <input type="text" v-model="manual_id_column" class="form-control" id="name" placeholder="">
    </div>
    
    <div class="form-group">
      <label for="name">Input data column</label>
      <input type="text" v-model="manual_data_column" class="form-control" id="name" placeholder="">
    </div>
    <br>
    
    <button @click="Accept()" class="btn btn-success">Accept</button>
    &nbsp;&nbsp;&nbsp;
    <button @click="Reject()" class="btn btn-success">Reject</button>
  
  </div>
</template>

<script>
import store from '../../../store.js'
import db from '../../../db'
// import penditem from "../Penditem.vue"
const fs = window.require('fs');
const ex = window.require("child_process");
const node_path = window.require('path');
const os = window.require('os');
const {dialog} = window.require('electron').remote

export default {
  name: 'PendItem',  // Name of the component
  // props: ['log'],
  props: [],
  
  data () {
    return {
      sharedState: store.state,
      exe_position: '',
      manual_file_path: '',
      manual_id_column: '',
      manual_data_column: '',
      task_id: '',
      test_id: '',
      test_description: '',
      test_indicator: '',
    }
  },

  methods: {

    get_manual_file_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_manual_file_path", result)
      if (result === undefined){
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
      }else{
        try {
          let path = result[0]
          fs.statSync(path);
          this.manual_file_path = path
        } catch (err) {
          dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  
      }
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

    handle_train_log_address(task_id) {
      const Log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      console.log("train_node_path_log", Log_address)
      if(!fs.existsSync(Log_address)){
        console.log("creating log.txt");
        fs.openSync(file, "w");
        console.log("log.txt created");
      }
      return Log_address
    },

    train_unread_request(){
      let vm = this;

      const delete_pending = {
        task_id: vm.task_id,
        test_id: vm.test_id,
        test_indicator: vm.test_indicator
      }

      this.$axios.post('/delete_pending/', delete_pending)
        .then((response) => {
          // handle success
          console.log("delete_pending response", response.data)

        })
        .catch((error) => {
          // handle error
          console.log(error)

        })
        
      let hash_id_file_address = null;
      let Log_address = null;
      try{
        hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + vm.manual_file_path 
                                + ' --id_idx ' + vm.manual_id_column, {encoding: 'utf8'})

        let indicator = vm.handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
        Log_address = vm.handle_train_log_address(task_id)
        if (indicator == false){
          console.log("hash_id_file_address wrong")
          fs.appendFileSync(Log_address, "hash_id_file_address wrong")
          return 
        }
      }catch(err){
          console.log(err)
      }

      try {
        fs.appendFileSync(Log_address, "\n You are Assistor\n")
        fs.appendFileSync(Log_address, "Task ID: " + task_id + "\n")
        fs.appendFileSync(Log_address, "----------------------2. Unread Request\n")
        fs.appendFileSync(Log_address, "2.1 Update the request notification\n")
      } catch (err) {
        console.log(err)
      }
      let hash_id_file_data = fs.readFileSync(hash_id_file_address[2], {encoding:'utf8', flag:'r'});
      
      const match_assistor_id_data = {
        task_id: task_id,
        file: hash_id_file_data,
      }
      
      vm.$axios.post('/match_assistor_id/', match_assistor_id_data)
        .then((response) => {
          // handle success
          console.log("2.2 assistor uploads id file", response)
          vm.$toasted.success(`2.2 assistor uploads id file`, { icon: 'fingerprint' })

          try {
            fs.appendFileSync(Log_address, "2.2 assistor uploads id file\n")
            fs.appendFileSync(Log_address, "--------------------------2. Unread Request Done\n")
          } catch (err) {
            console.log(err)
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    },

    test_unread_request(){
      let vm = this
      console.log("2.1 Update Test request notification response", unread_test_request_notification)
      this.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })


      const delete_pending = {
        task_id: vm.task_id,
        test_id: vm.test_id,
        test_indicator: vm.test_indicator
      }

      this.$axios.post('/delete_pending/', delete_pending)
        .then((response) => {
          // handle success
          console.log("delete_pending response", response.data)

        })
        .catch((error) => {
          // handle error
          console.log(error)

        })


      let test_hash_id_file_address = null
      let Log_address = null
      try{

        test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
                                  + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id
                                  + ' --mode test' + ' --test_id ' + test_id
                                  + ' --dataset_path ' + vm.manual_file_path + ' --id_idx ' + vm.manual_id_column, {encoding: 'utf8'})

        test_hash_id_file_address = test_hash_id_file_address.split("?")
        let indicator = vm.handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
        Log_address = vm.handle_test_log_address(task_id, test_id)
        if (indicator == false){
          console.log("test_hash_id_file_address wrong")
          fs.appendFileSync(Log_address, "test_hash_id_file_address wrong")
          return 
        }

      }catch(err){
        console.log(err)
      }

      try {
        fs.appendFileSync(Log_address, "\n You are Assistor\n")
        fs.appendFileSync(Log_address, "Test ID: " + test_id + "\n")
        fs.appendFileSync(Log_address, "-----------------------Test Stage: 2.Unread Test Request\n")
        fs.appendFileSync(Log_address, "2.1 Test: Update Test request notification\n")
        fs.appendFileSync(Log_address, "2.2 Test: Hashing Done\n")
      } catch (err) {
        console.log(err)
      }

      let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});

      const match_test_assistor_id_data = {
        file: test_hash_id_file_data,
        test_id: test_id
      }

      vm.$axios.post('/match_test_assistor_id/', match_test_assistor_id_data)
        .then((response) => {
          // handle success
          console.log("2.2 Test: assistor uploads id file", response)
          vm.$toasted.success(`2.2 Test: assistor uploads id file`, { icon: 'fingerprint' })
          try {
            fs.appendFileSync(Log_address, "2.2 Test: assistor uploads id file\n")
            fs.appendFileSync(Log_address, "--------------------------2. Unread Test Request Done\n")
          } catch (err) {
            console.log(err)
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })




    },


    Accept(){
      let vm = this
      this.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

      let task_id = this.task_id
      
      if (vm.test_indicator == 'train'){
        vm.train_unread_request()
      }else{
        vm.test_unread_request()
      }

 




    },

    
    

    Reject() {
      console.log('delete')
      let vm = this;
      

      this.$router.push({ name: 'Plist' })
    },
    

  },// end method(){}


  created () {
    this.task_id = this.$route.query.task_id
    this.test_id = this.$route.query.test_id
    this.test_description = this.$route.query.test_description
    this.test_indicator = this.$route.query.test_indicator

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },//end created

}
// exports.default = Home
</script>