<template>
  <div class="container g-pt-20">
     <div class="form-group">
      <label for="name">Select Data File</label>
      <input type="text" v-model="PathForm.train_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_train_data_path()">Select Data File</button>
    </div>
    
    <div class="form-group">
      <label for="location">Select Id File</label>
      <input type="text" v-model="PathForm.train_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_train_id_path()">Select ID File</button>
    </div>

    <div class="form-group">
      <label for="location">Select Target File</label>
      <input type="text" v-model="PathForm.train_target_path" class="form-control" id="location" placeholder="">
      <button @click="get_train_target_path()">Select Target File</button>
    </div>

    <button type="submit" @click="onSubmit()" class="btn btn-primary">Start Finding Assistors</button>
  </div>
</template>

<script>
import store from '../../store'
import db from '../../db'

const fs = window.require('fs');
const {dialog} = window.require('electron').remote
const ex = window.require("child_process");
const path = window.require('path');
const os = window.require('os');
// const store = require('../../store').defaultv
// const $ = require('jquery')

export default {
  name: 'Find_Assistor',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      task_id: "",
      PathForm: {
        train_data_path: "",
        train_id_path: "",
        train_target_path: "",
      },
      root: '',
      exe_position: '',
    }
  },
  methods: {
    get_train_id () {
      console.log("$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
      this.$axios.get('/create_new_train_task/')
        .then((response) => {
          this.task_id = response.data.task_id
          console.log("task_id))))))))))))))00", this.task_id)
        })
        .catch((error) => {
          console.log(error)

        })
    },
    changeroot() {
      if (os.type() == "Linux"){
        this.root = path.resolve("./exp")
        this.exe_position = path.resolve("./dist/run/run")
      }else if (os.type() == "Darwin") {
        this.root = path.resolve("./exp")
        this.exe_position = path.resolve("./dist/run/run.dmg")
      }else if (os.type() == "Windows_NT") {
        this.root = path.resolve("./exp")
        this.exe_position = path.resolve("./dist/run/run.exe")
      }
    },
    get_train_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_data_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  

      }
    },
    get_train_id_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_id_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_id_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
          console.log('Please Select A Train ID File')
        }  

      }
    },
    get_train_target_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_train_Target_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.PathForm.train_target_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
          console.log('Please Select A Train Target File')
        }  

      }
    },

    onSubmit (e) {
      let vm = this;
      if (this.task_id == ""){
        dialog.showErrorBox('Please Type in the Paths Again', 'We apologize for the latency')
      }else{
        
        let both_path_validation = true
        // if (vm.PathForm.train_data_path == ""){
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
        // }
        try {
          fs.statSync(vm.PathForm.train_data_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
          both_path_validation = false
        }

        try {
          fs.statSync(vm.PathForm.train_id_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train ID File')
          console.log('Please Select A Train ID File')
          both_path_validation = false
        }

        try {
          fs.statSync(vm.PathForm.train_target_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Train Target File')
          console.log('Please Select A Train Target File')
          both_path_validation = false
        }
        
        if(both_path_validation == true){
          // db.serialize(function() {
          //   let update_sentence = 'UPDATE "User_Chosen_Path"'
          //             +' SET "train_data_path" = "' + vm.PathForm.train_data_path + '",'
          //             +'"train_id_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"train_target_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"WHERE "user_id" = ' + vm.sharedState.user_id
          //   console.log(update_sentence)           
          //   db.run(update_sentence)

          // });
          console.log("true")
          console.log(vm.PathForm.train_data_path,vm.PathForm.train_id_path,vm.PathForm.train_target_path)
          let insert_sentence = `INSERT INTO "User_Chosen_Path"("user_id", "test_indicator", "task_id", "train_data_path", "train_id_path", "train_target_path") VALUES 
              (`+vm.sharedState.user_id+ `,"train","` + vm.task_id + `", "`+vm.PathForm.train_data_path+ `", "` +vm.PathForm.train_id_path+`", "`+vm.PathForm.train_target_path+`")`
          console.log("insert_sentence", insert_sentence)
          db.run(insert_sentence, function(err){
            if (err){
              console.log(err);
            }

            let match_id_address = vm.PathForm.train_id_path
            let hash_id_file_address = null;
            try{   
              // + './dist/run/run make_hash --id_path '
              // let aa = vm.exe_position + ' make_hash --id_path '  + match_id_address + ' --root ' + vm.root 
              //                         + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --mode train'
              // console.log("make_hash**********", aa, '%%', vm.exe_position, '%%%', __dirname, '###', __dirname + '/../')
              hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path '  + match_id_address + ' --root ' + vm.root 
                                      + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --mode train', {encoding: 'utf8'})  
              console.log("hash_id_file_address", hash_id_file_address)
            }catch(err){
              console.log(err)
            }

            
          // let hash_id_file_data = fs.readFileSync(hash_id_file_address, {encoding:'utf8', flag:'r'});
          //     console.log(hash_id_file_data)
            let hash_id_file_data = null
            try{
              hash_id_file_data = fs.readFileSync(hash_id_file_address, {encoding:'utf8', flag:'r'});
              console.log("hash_id_file_data", hash_id_file_data)
            } catch (err) {
              console.log(err)
            }
            

            const find_assistor_data = {
              assistor_id_list: [2],
              id_file: hash_id_file_data,
              task_id: vm.task_id
            }

            vm.$axios.post('/find_assistor/', find_assistor_data)
            .then((response) => {
              let user_id = vm.sharedState.user_id

              const Log_address = vm.root + '/' + user_id + '/task/' + vm.task_id + '/' + 'train/' + 'log.txt'
              // handle success
              console.log("1.1 Sponsor calls for help", response)
              vm.$toasted.success(`1.1 Sponsor calls for help`, { icon: 'fingerprint' })

              console.log("1.2 Sponsor sends id file")
              vm.$toasted.success(`1.2 Sponsor sends id file`, { icon: 'fingerprint' })

              // Create 'Local_Data/id/task_id/' folder
              // const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/'
              // fs.mkdirSync(new_address, { recursive: true})

              try {
                fs.appendFileSync(Log_address, "\n You are SPONSOR\n")
                fs.appendFileSync(Log_address, "Task ID: " + vm.task_id + "\n")
                fs.appendFileSync(Log_address, "---------------------- Train Stage Starts\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Find assistor\n")
                fs.appendFileSync(Log_address, "1.1 Sponsor calls for help\n")
                fs.appendFileSync(Log_address, "1.2 Sponsor sends id file\n")
              } catch (err) {
                console.log(err)
              }

              
              // console.log("1.3 Sponsor creates " + new_address)
              // this.$toasted.success("1.3 Sponsor creates " + new_address, { icon: 'fingerprint' })

              try {
                // fs.appendFileSync(Log_address, "1.3 Sponsor creates " + new_address + "\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Find assistor Done\n")
              } catch (err) {
                console.log(err)
              }

              vm.task_id = ""
              vm.$router.push('/')

            })
            .catch((error) => {
              // handle error
              console.log(error)
              // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })

          })          
          
        }

      }
            
    },

  },
  created () {
    this.get_train_id();
    this.changeroot();
  }
}
</script>