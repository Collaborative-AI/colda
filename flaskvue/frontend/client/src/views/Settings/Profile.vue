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
      <label for="name">Default Data Path</label>
      <input type="text" v-model="profileForm.default_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_data_path()">Select Data File</button>
    </div>
    <div class="form-group">
      <label for="location">Default Id Path</label>
      <input type="text" v-model="profileForm.default_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_default_id_path()">Select ID File</button>
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
        default_data_path: "",
        default_id_path: ""
      },
    }
  },
  methods: {
    get_default_data_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_data_path", result)
      if (result === undefined){
        dialog.showErrorBox('Please Select A Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_data_path = path
        } catch (err) {
          dialog.showErrorBox('Data Path not Correct', 'Please Select A Data File')
          console.log('Please Select A Data File')
        }  

      }
    },
    get_default_id_path() {
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_id_path", result)
      if (result === undefined){
        dialog.showErrorBox('Please Select A ID File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          this.profileForm.default_id_path = path
        } catch (err) {
          dialog.showErrorBox('ID Path not Correct', 'Please Select A ID File')
          console.log('Please Select A ID File')
        }  

      }
    },
    getUser (id) {
      let vm = this
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;
      db.get(select_sentence, function(err, row){
        console.log(row)

        if (row != null){
          vm.profileForm.default_data_path = row.default_data_path
          vm.profileForm.default_id_path = row.default_id_path
        }

        if (row == null){
          console.log("get false")
          vm.sharedState.set_default = false
          vm.sharedState.receive_request = false
        }else{
            if (row.default_data_path == "" | row.default_id_path == ""){
            console.log("get false")
            vm.sharedState.set_default = false
            vm.sharedState.receive_request = false
          }
        }
      })
    },
    onSubmit (e) {
      let vm = this;
      let select_sentence = 'SELECT * FROM User_Default_Path WHERE user_id=' + this.sharedState.user_id;

      db.get(select_sentence, function(err, row){
        console.log(row)
        
        if (row == null){
          // db.run(`INSERT INTO "User_Default_Path"("user_id", "default_data_path", "default_id_path") VALUES (1, 'love', 'consume')`)
          let insert_new_val = `INSERT INTO "User_Default_Path"("user_id", "default_data_path", "default_id_path") VALUES 
            (`+vm.sharedState.user_id+`, "`+vm.profileForm.default_data_path+`", "`+vm.profileForm.default_id_path+`")`
          console.log(insert_new_val)
          db.run(insert_new_val)
        }else{

          // if (vm.profileForm.default_data_path == "" | vm.profileForm.default_id_path == "" ){
          //   vm.sharedState.set_default = false
          //   vm.sharedState.receive_request = false
          //   console.log("false")
          // }

          let both_path_validation = true
          try {
            fs.statSync(vm.profileForm.default_data_path);
          } catch (err) {
            dialog.showErrorBox('Data Path not Correct', 'Please Select A Data File')
            console.log('Please Select A Data File')
            both_path_validation = false
          }

          try {
            fs.statSync(vm.profileForm.default_id_path);
          } catch (err) {
            dialog.showErrorBox('ID Path not Correct', 'Please Select A ID File')
            console.log('Please Select A ID File')
            both_path_validation = false
          }
          
          // let check_default_data_path=fs.statSync( vm.profileForm.default_data_path);
          // console.log("check_default_data_path", check_default_data_path)
          // // if(!check_default_data_path.isFile()){
          // //   dialog.showErrorBox('Please Select A Data File')
          // // }
          
          // let check_default_id_path=fs.statSync( vm.profileForm.default_id_path);
          // console.log("check_default_id_path", check_default_id_path)
          // // if(!check_default_id_path.isFile()){
          // //   dialog.showErrorBox('Please Select A ID File')
          // // }

          if(both_path_validation == true){
            db.serialize(function() {
              let update_default_data_path = 'UPDATE "User_Default_Path"'
                        +' SET "default_data_path" = "' + vm.profileForm.default_data_path
                          + '" WHERE "user_id" = ' + vm.sharedState.user_id
              console.log(update_default_data_path)           
              db.run(update_default_data_path)

              let update_default_id_path = 'UPDATE "User_Default_Path"'
                        +' SET "default_id_path" = "' + vm.profileForm.default_id_path
                          + '" WHERE "user_id" = ' + vm.sharedState.user_id
              console.log(update_default_id_path)
              db.run(update_default_id_path)
            });
          }
          
        }    
      })



      // const path = `/users/${user_id}`
      // const payload = {
      //   name: this.profileForm.name,
      //   location: this.profileForm.location,
      //   about_me: this.profileForm.about_me
      // }
      // this.$axios.put(path, payload)
      //   .then((response) => {
      //     // handle success
      //     this.$toasted.success('Successed modify your profile.', { icon: 'fingerprint' })
      //     this.$router.push({ path: `/user/${user_id}/overview` })
      //   })
      //   .catch((error) => {
      //     // handle error
      //     console.log(error.response.data)
      //     this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
      //   })
    },
    



  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
  }
}
</script>