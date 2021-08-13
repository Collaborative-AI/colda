<template>
  <div>
    <h1>Public profile</h1>
    <!-- <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label for="name">Real Name</label>
        <input type="text" v-model="profileForm.name" class="form-control" id="name" placeholder="">
      </div>
      <div class="form-group">
        <label for="location">Location</label>
        <input type="text" v-model="profileForm.location" class="form-control" id="location" placeholder="">
      </div>
      <div class="form-group">
        <label for="about_me">About Me</label>
        <textarea v-model="profileForm.about_me" class="form-control" id="about_me" rows="5" placeholder=""></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form> -->

    <!-- <form @submit.prevent="onSubmit"> -->
    <div class="form-group">
      <label for="name">Default Train Data Path</label>
      <input type="text" v-model="profileForm.default_train_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_train_data_path()">Select Train Data File</button>
    </div>
    <div class="form-group">
      <label for="location">Default Train ID Path</label>
      <input type="text" v-model="profileForm.default_train_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_default_train_id_path()">Select Train ID File</button>
    </div>

    <div class="form-group">
      <label for="name">Default Test Data Path</label>
      <input type="text" v-model="profileForm.default_test_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_test_data_path()">Select Test Data File</button>
    </div>
    <div class="form-group">
      <label for="location">Default Test ID Path</label>
      <input type="text" v-model="profileForm.default_test_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_default_test_id_path()">Select Test ID File</button>
    </div>

    <button type="submit" @click="onSubmit()" class="btn btn-primary">Update</button>
    <!-- </form> -->

  </div>
</template>

<script>

const {dialog} = window.require('electron').remote
const fs = window.require('fs');

// const store = require('../../store').default
// const db = require('../../db').default
import store from '../../store'
import db from '../../db'

export default {
  name: 'Profile',  //this is the name of the component
  data () {
    return {
      sharedState: store.state,
      profileForm: {
        default_train_data_path: "",
        default_train_id_path: "",
        default_test_data_path: "",
        default_test_id_path: "",
      },
    }
  },
  methods: {
    get_default_train_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_train_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_train_data_path = path
        } catch (err) {
          dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  

      }
    },
    get_default_train_id_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_train_id_path", result)
      if (result === undefined){
        dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_train_id_path = path
        } catch (err) {
          dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
          console.log('Please Select A Train ID File')
        }  

      }
    },
    get_default_test_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_test_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_test_data_path = path
        } catch (err) {
          dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
          console.log('Please Select A Test Data File')
        }  

      }
    },
    get_default_test_id_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_test_id_path", result)
      if (result === undefined){
        dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_test_id_path = path
        } catch (err) {
          dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
          console.log('Please Select A Test ID File')
        }  

      }
    },
    getUser (id) {
      let vm = this
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
        if (err){ 
          console.log(err);
        }

        console.log(row)

        if (row != null){
          vm.profileForm.default_train_data_path = row.default_train_data_path
          vm.profileForm.default_train_id_path = row.default_train_id_path
          vm.profileForm.default_test_data_path = row.default_test_data_path
          vm.profileForm.default_test_id_path = row.default_test_id_path
        }

        if (row == null){
          console.log("get false")
          vm.sharedState.set_default = false
          vm.sharedState.receive_request = false
        }else{
            if (row.default_train_data_path == "" | row.default_train_id_path == "" | 
              row.default_test_data_path == "" | row.default_test_id_path == ""){
            console.log("get false")
            vm.sharedState.set_default = false
            vm.sharedState.receive_request = false
          }
        }
      })
    },
    onSubmit (e) {
      let vm = this;
      
      let both_path_validation = true
      console.log("vm.profileForm.default_train_data_path", vm.profileForm.default_train_data_path)
      try {
        fs.statSync(vm.profileForm.default_train_data_path);
      } catch (err) {
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
        console.log('Please Select A Train Data File')
        both_path_validation = false
      }

      console.log("vm.profileForm.default_train_id_path", vm.profileForm.default_train_id_path)
      try {
        fs.statSync(vm.profileForm.default_train_id_path);
      } catch (err) {
        dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
        console.log('Please Select A Train ID File')
        both_path_validation = false
      }

      console.log("vm.profileForm.default_test_data_path", vm.profileForm.default_test_data_path)
      try {
        fs.statSync(vm.profileForm.default_test_data_path);
      } catch (err) {
        dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
        console.log('Please Select A Test Data File')
        both_path_validation = false
      }

      console.log("vm.profileForm.default_test_id_path", vm.profileForm.default_test_id_path)
      try {
        fs.statSync(vm.profileForm.default_test_id_path);
      } catch (err) {
        dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
        console.log('Please Select A Test ID File')
        both_path_validation = false
      }

      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
        if (err){ 
          console.log(err);
        }
        console.log("row", row)
        
        if (row == null){
          // db.run(`INSERT INTO "User_Default_Path"("user_id", "default_train_data_path", "default_train_id_path") VALUES (1, 'love', 'consume')`)
          let insert_new_val = `INSERT INTO "User_Default_Path"("user_id", "default_train_data_path", "default_train_id_path", "default_test_data_path", "default_test_id_path") VALUES 
            (`+vm.sharedState.user_id+`, "`+vm.profileForm.default_train_data_path+`", "`+vm.profileForm.default_train_id_path+`", "`
            +vm.profileForm.default_test_data_path+`", "`+vm.profileForm.default_test_id_path+`")`
          console.log("insert_new_val", insert_new_val)
          db.run(insert_new_val)
        }else{          
          
          if(both_path_validation == true){
            db.serialize(function() {
              let update_sentence = 'UPDATE "User_Default_Path"'
                        +'SET "default_train_data_path" = "' + vm.profileForm.default_train_data_path + '",'
                        +'"default_train_id_path" = "' + vm.profileForm.default_train_id_path + '",'
                        +'"default_test_data_path" = "' + vm.profileForm.default_test_data_path + '",'
                        +'"default_test_id_path" = "' + vm.profileForm.default_test_id_path
                        +'"WHERE "user_id" = ' + vm.sharedState.user_id
              console.log("update_sentence", update_sentence)           
              db.run(update_sentence)
            });
          }
        }    
      })

    },
    



  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
  }
}
</script>