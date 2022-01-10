<template>
  <div >
    <!-- <h1>Setting</h1> -->
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
      <label for="name">Default Train File Path</label>
      <input type="text" v-model="default_file_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_file_path()" class="btn btn-success">Select File</button>
    </div>
    <div style="overflow:auto">
    <table class="table" v-if="select_data">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col" v-for="(ptitle, idx) in ptitles" :key="ptitle.index">{{idx+1}}.{{ptitle}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(pdata,idx) in pdatas" :key="pdata.index">
          <th scope="row">{{idx+1}}</th>
          <td v-for="pd in pdata" :key="pd.index">{{pd}}</td>
        </tr>
        
      </tbody>
    </table>
    </div>
    <div class="form-group">
      <label for="name">Input id column</label>
      <input type="text" v-model="default_id_column" class="form-control" id="name" placeholder="">
    </div>
    <div class="form-group">
      <label for="name">Input data column</label>
      <input type="text" v-model="default_data_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
    <label for="name">Select Model Name</label>
    &nbsp;
    <select v-model="default_model_name" class="form-control">
      <option v-for="item in model_name_list"  :key="item.index" :value="item">{{item}}</option>
    </select>
    </div>

    <br>
    <input type="radio" id="auto" value="auto" v-model="sharedState.mode">
    <label for="auto">Auto</label>
    <br>
    <input type="radio" id="manual" value="manual" v-model="sharedState.mode">
    <label for="manual">Manual</label>
    <br>


    <button type="submit" @click="onSubmit()" class="btn btn-success">Update</button>
    <!-- </form> -->

  </div>
</template>

<script>
import { ex,fs,os,node_path,dialog } from '../../import_package.js'
// const fs = window.fs ? window.fs : require('fs');
// const dialog = window.dialog ? window.dialog : require('electron');

// const store = require('../../store').default
// const db = require('../../db').default
import store from '../../store'
import db from '../../db'
import { execute_unittest_list, generate_unittest_parameters, change_db_param_to_string } from '../../utils.js'

export default {
  name: 'Profile',  //this is the name of the component
  data () {
    return {
      sharedState: store.state,
      default_file_path: "",
      default_id_column: "",
      default_data_column: "",
      default_model_name: "",
      ptitles:"",
      pdatas:"",
      select_data:false,
      model_name_list:['linear'],
    }
  },
  methods: {
    
    get_default_file_path() {
      let vm = this
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_file_path", result)
      if (result === undefined){
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          
          this.default_file_path = path

          fs.readFile(path, 'utf8' , (err, data) => {
            if (err) {
              console.log('err info',err);
              return
            }
            
            // data = data.split("\r\n")
            // for (let i of data) { data[i] = data[i].split(",") }
            // vm.pdatas=data
            // console.log('preview',vm.pdatas[0][0])
            
            vm.pdatas = data.split("\n")
            for (let i in vm.pdatas) { vm.pdatas[i] = vm.pdatas[i].split(",")} 
            vm.ptitles=vm.pdatas[0]
            vm.pdatas=vm.pdatas.slice(1,4)
            vm.select_data=true
            console.log('preview',vm.pdatas[0])
          })
        } catch (err) {
          dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
          console.log('Please Select A Train Data File')
        }  

      }
    },
    
    getUser (id) {
      let vm = this
      // console.log('bug1')

      let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id= ?'
      let param = [this.sharedState.user_id]
      console.log('select_sentence', select_sentence)

      vm.$db.get(select_sentence, change_db_param_to_string(param), (err, row) => {
      if (err) {
        console.log('err info',err);;
      }

      // let row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id= ?').get(this.sharedState.user_id);
      console.log('haha',row);
      if (row != null){
          vm.default_file_path = row.default_file_path
          vm.default_id_column = row.default_id_column
          vm.default_data_column = row.default_data_column
          vm.default_model_name = row.default_model_name
          vm.sharedState.mode = row.default_mode
          console.log('mode', vm.sharedState.mode)
        } 
      })
    },
    onSubmit (unittest_callbacks) {
      let vm = this;
      let both_path_validation = true
      console.log("vm.default_file_path", vm.default_file_path)
      try {
        fs.statSync(vm.default_file_path);
      } catch (err) {
        // dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
        console.log('Please Select A Train Data File')
        both_path_validation = false
      }

      console.log("vm.default_id_column", vm.default_id_column)
      console.log("vm.default_data_column", vm.default_data_column)

      let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id= ?'
      let param = [this.sharedState.user_id.toString()]
      let a = ''
      console.log('aaa1', a.length)
      console.log('zzz995', typeof(this.sharedState.user_id))
      console.log('select_sentence123', select_sentence, change_db_param_to_string(param))


      vm.$db.get(select_sentence, change_db_param_to_string(param), (err, row) => {
      if (err) {
        console.log('err info',err);;
      }

      // const row = vm.$db.prepare('SELECT * FROM User_Default_Table WHERE user_id= ?').get(this.sharedState.user_id);
      console.log('haha',row);
      if (row == null){
        console.log('dele0')

        let sentence = `INSERT INTO User_Default_Table (user_id , default_file_path , default_id_column, default_data_column,` + 
        `             default_target_column, default_mode, default_model_name) VALUES (?, ?, ?, ?, ?, ?, ?)`
        let param = [vm.sharedState.user_id , vm.default_file_path, vm.default_id_column, vm.default_data_column,  "",
                      vm.sharedState.mode, vm.default_model_name]

        vm.$db.run(sentence, change_db_param_to_string(param), function(err){
          if (err){
            console.log('err info',err);
          }


          // const stmt = vm.$db.prepare('INSERT INTO User_Default_Table VALUES ( @user_id , @default_file_path , @default_id_column, @default_data_column , @default_target_column, @default_mode, @default_model_name)');
          // stmt.run({
          //   user_id: vm.sharedState.user_id , 
          //   default_file_path: vm.default_file_path, 
          //   default_id_column: vm.default_id_column, 
          //   default_data_column: vm.default_data_column, 
          //   default_target_column: "",
          //   default_mode: vm.sharedState.mode,
          //   default_model_name: vm.default_model_name,
          // });
          console.log('dele1')
          console.log('dele2')
          let unittest_parameters = generate_unittest_parameters(vm.default_file_path, vm.default_id_column, vm.default_data_column)
          execute_unittest_list(unittest_callbacks, 0, "profile_unittest", unittest_parameters)
          vm.$toasted.success(`setting updated`, { icon: 'fingerprint' })

        })
      }else{
        console.log('dele4', both_path_validation)
        if(both_path_validation == true){

          let sentence = 'UPDATE User_Default_Table' 
          + ' SET default_file_path = ?,'
          + ' default_id_column = ?,'
          + ' default_data_column = ?,'
          + ' default_target_column = ?,'
          + ' default_mode = ?,'
          + ' default_model_name = ?'
          + ' WHERE user_id = ?'

          let param = [vm.default_file_path, vm.default_id_column, vm.default_data_column, '', vm.sharedState.mode, vm.default_model_name, vm.sharedState.user_id];

          db.run(sentence, change_db_param_to_string(param), function(err) {
            if (err) {
              console.log(err);
            }
            console.log(`Row(s) updated`);

            // const stmt = vm.$db.prepare('UPDATE User_Default_Table' 
            // + ' SET default_file_path = ?,'
            // + ' default_id_column = ?,'
            // + ' default_data_column = ?,'
            // + ' default_target_column = ?,'
            // + ' default_mode = ?,'
            // + ' default_model_name = ?'
            // + ' WHERE user_id = ?'); 
            // console.log('dele3')
            // stmt.run(vm.default_file_path, vm.default_id_column, vm.default_data_column, '', vm.sharedState.mode, vm.default_model_name, vm.sharedState.user_id);
            console.log('dele2')
            let unittest_parameters = generate_unittest_parameters(vm.default_file_path, vm.default_id_column, vm.default_data_column)
            execute_unittest_list(unittest_callbacks, 0, "profile_unittest", unittest_parameters)
            vm.$toasted.success(`setting updated`, { icon: 'fingerprint' })

          })
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