<template>
  <div class="container g-pt-20">
     <div class="form-group">
      <label for="name">Select Data File</label>
      <input type="text" v-model="PathForm.test_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_test_data_path()">Select File</button>
    </div>

    <div class="form-group">
      <label for="name">Input ID colomn </label>
      <input type="text" v-model="test_id_colomn" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input data colomn (eg. 3-6)</label>
      <input type="text" v-model="test_data_colomn" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
      <label for="name">Input target colomn</label>
      <input type="text" v-model="test_target_colomn" class="form-control" id="name" placeholder="">
    </div>
    
    <!-- <div class="form-group">
      <label for="location">Select Id File</label>
      <input type="text" v-model="PathForm.test_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_test_id_path()">Select ID File</button>
    </div>

    <div class="form-group">
      <label for="location">Select Target File</label>
      <input type="text" v-model="PathForm.test_target_path" class="form-control" id="location" placeholder="">
      <button @click="get_test_target_path()">Select Target File</button>
    </div> -->

    <button type="submit" @click="onSubmit()" class="btn btn-primary">Start Finding Assistors</button>
  </div>
</template>

<script>
import store from '../../store'
import db from '../../db'

const fs = window.require('fs');
const {dialog} = window.require('electron').remote
const ex = window.require("child_process");
const os = window.require('os');
const node_path = window.require('path');
// const store = require('../../store').defaultv
// const $ = require('jquery')

export default {
  name: 'Find_Test_Assistor',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      task_id: "",
      test_id: "",
      test_file_path: "",
      test_id_colomn: "",
      test_data_colomn: "",
      test_target_colomn: "",
      PathForm: {
        test_data_path: "",
        test_id_path: "",
        test_target_path: "",
      },
      root: '',
      exe_position: '',
    }
  },
  methods: {
    get_test_id () {
      console.log("$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", this.task_id)
      this.$axios.get('/create_new_test_task/')
        .then((response) => {
          this.test_id = response.data.test_id
          console.log("task_id))))))))))))))00", this.task_id)
        })
        .catch((error) => {
          console.log(error)

        })
    },
    
    get_test_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_test_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.test_file_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
        }  

      }
    },
    // get_test_id_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_test_id_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.PathForm.test_id_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
    //       console.log('Please Select A Test ID File')
    //     }  

    //   }
    // },
    // get_test_target_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_test_target_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.PathForm.test_target_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
    //       console.log('Please Select A Test Target File')
    //     }  

    //   }
    // },

    onSubmit (e) {
      let vm = this;
      if (this.task_id == ""){
        dialog.showErrorBox('Please Type in the Paths Again', 'We apologize for the latency')
      }else{
        
        let both_path_validation = true
        // if (vm.PathForm.test_data_path == ""){
        //   dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
        // }
        try {
          fs.statSync(vm.PathForm.test_data_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
          both_path_validation = false
        }

        try {
          fs.statSync(vm.PathForm.test_id_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test ID File')
          console.log('Please Select A Test ID File')
          both_path_validation = false
        }

        try {
          fs.statSync(vm.PathForm.test_target_path);
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Test Target File')
          console.log('Please Select A Test Target File')
          both_path_validation = false
        }
        
        if(both_path_validation == true){
          // db.serialize(function() {
          //   let update_sentence = 'UPDATE "User_Chosen_Path"'
          //             +' SET "test_data_path" = "' + vm.PathForm.test_data_path + '",'
          //             +'"test_id_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"test_target_path" = "' + vm.profileForm.default_id_path + '",'
          //             +'"WHERE "user_id" = ' + vm.sharedState.user_id
          //   console.log(update_sentence)           
          //   db.run(update_sentence)

          // });
          console.log("true")
          console.log(vm.test_file_path,vm.test_id_colomn,vm.test_target_colomn)
          let insert_sentence = `INSERT INTO "User_Chosen_Path"("user_id", "test_indicator", "task_id", "test_id", "test_file_path", "test_id_colomn","test_target_colomn","test_data_colomn") VALUES 
              (`+`"`+vm.sharedState.user_id+`", "test","` + vm.task_id + `", "` +vm.test_id+ `", "` +vm.test_file_path+ `", "` +vm.test_id_colomn+`", "` +vm.test_target_colomn+`", "` +vm.test_data_colomn `")`
          console.log(insert_sentence)
          db.run(insert_sentence, function(err){
            if (err){
              console.log(err);
            }

          let match_id_address = vm.test_id_colomn
          let test_hash_id_file_address = null;
          try{
            test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path ' + match_id_address + ' --root ' + vm.root 
                                    + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --mode test' + ' --test_id ' + vm.test_id, {encoding: 'utf8'})
            test_hash_id_file_address = test_hash_id_file_address.replace(/\n/g, '')
            console.log(test_hash_id_file_address)
            test_hash_id_file_address = test_hash_id_file_address.split("?")
            console.log("test_hash_id_file_address", test_hash_id_file_address)
            if (test_hash_id_file_address[0] == "300" && test_hash_id_file_address[1] == "make_hash" && test_hash_id_file_address[2] == "not valid mode"){
              vm.$toasted.success(`not valid mode, please select again`, { icon: 'fingerprint' })
              return
            }
            if (test_hash_id_file_address[0] != "200" || test_hash_id_file_address[1] != "make_hash"){
              vm.$toasted.success(`find assistor went wrong, please try again`, { icon: 'fingerprint' })
              console.log("make hash wrong")
              return 
            }
          }catch(err){
            console.log(err)
          }

          let test_hash_id_file_data = null
          try{
            test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});
          } catch(err){
            console.log(err)
          }

          const payload = {
            task_id: vm.task_id,
            test_id: vm.test_id, 
            id_file: test_hash_id_file_data
          }
          
          vm.$axios.post('/find_test_assistor/', payload)
            .then((response) => {
             
              const Log_address = node_path.join(vm.root.toString(), vm.sharedState.user_id.toString(), "task", vm.task_id.toString(), "test", vm.test_id.toString(), "log.txt")
              console.log("node_path_log", Log_address)
              if(!fs.existsSync(Log_address)){
                console.log("creating log.txt");
                fs.openSync(file, "w");
                console.log("log.txt created");
              }
             
             
             // handle success
              console.log("1.1 Test: Sponsor calls for help", response)
              vm.$toasted.success(`1.1 Test: Sponsor calls for help`, { icon: 'fingerprint' })

              console.log("1.2 Test: Sponsor sends id file")
              vm.$toasted.success(`1.2 Test: Sponsor sends id file`, { icon: 'fingerprint' })

              // Create 'Local_Data/id/task_id/' folder
              // const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/' + response.data.test_id + '/'
              // fs.mkdirSync(new_address, { recursive: true})

              try {
                fs.appendFileSync(Log_address, "\n You are SPONSOR\n")
                fs.appendFileSync(Log_address, "Test ID: " + vm.test_id + "\n")
                fs.appendFileSync(Log_address, "---------------------- Test Stage Starts\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor\n")
                fs.appendFileSync(Log_address, "1.1 Test: Sponsor calls for test\n")
                fs.appendFileSync(Log_address, "1.2 Test: Sponsor sends id file\n")
                fs.appendFileSync(Log_address, "---------------------- 1. Test: Find Test assistor Done\n")
              } catch (err) {
                console.log(err)
              }

              // // Upload the matching ID file
              // this.sponsor_request_show = true
              vm.test_id = ""
              vm.$router.push('/notifications')
            })
            .catch((error) => {
              // handle error
              console.log(error)
              // console.log(error.response.data)
              // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })

            let make_test_local = null;
            try{   
              make_test_local = ex.execSync(vm.exe_position + ' make_test_local  --root ' + vm.root 
                                      + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + vm.task_id + ' --test_id ' + vm.test_id +' --data_path ' + vm.PathForm.test_data_path + ' --target_path ' + vm.PathForm.test_target_path, {encoding: 'utf8'})  
              console.log("make_test_local", make_test_local)
            }catch(err){
              console.log(err)
            }

          })          
          
        }

      }
            
    },

  },
  created () {
    this.task_id = this.$route.query.from;
    this.get_test_id();

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  }
}
</script>