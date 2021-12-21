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
      <input type="text" v-model="default_train_file_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_train_file_path()" class="btn btn-success">Select File</button>
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
      <input type="text" v-model="default_train_id_column" class="form-control" id="name" placeholder="">
    </div>
    <div class="form-group">
      <label for="name">Input data column</label>
      <input type="text" v-model="default_train_data_column" class="form-control" id="name" placeholder="">
    </div>

    <!-- <div class="form-group">
      <label for="location">Default Train/Test ID Path</label>
      <input type="text" v-model="profileForm.default_train_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_default_train_id_path()">Select Train ID File</button>
    </div> -->

    <!-- <div class="form-group">
      <label for="name">Default Test Data Path</label>
      <input type="text" v-model="profileForm.default_test_data_path" class="form-control" id="name" placeholder="">
      <button @click="get_default_test_data_path()">Select Test Data File</button>
    </div>
    <div class="form-group">
      <label for="location">Default Test ID Path</label>
      <input type="text" v-model="profileForm.default_test_id_path" class="form-control" id="location" placeholder="">
      <button @click="get_default_test_id_path()">Select Test ID File</button>
    </div> -->
    <!-- <input type="radio" id="not_receive" value="not_receive" v-model="picked" v-on:change="not_receive()">
          <label for="not_receive">Active</label>
          <br>
          <input type="radio" id="receive" value="receive" v-model="picked" v-on:change="receive()">
          <label for="receive">Passive</label>
          <br> -->
    <!-- <input type="radio" id="not_receive" value="not_receive" v-model="picked">
    <label for="not_receive">Not respond</label> -->
    <br>
    <input type="radio" id="Auto" value="Auto" v-model="sharedState.mode">
    <label for="Auto">Auto</label>
    <br>
    <input type="radio" id="Manual" value="Manual" v-model="sharedState.mode">
    <label for="Manual">Manual</label>
    <br>


    <button type="submit" @click="onSubmit()" class="btn btn-success">Update</button>
    <!-- </form> -->

  </div>
</template>

<script>

const fs = window.fs;
const dialog = window.dialog

// const store = require('../../store').default
// const db = require('../../db').default
import store from '../../store'
import db from '../../db'

export default {
  name: 'Profile',  //this is the name of the component
  data () {
    return {
      sharedState: store.state,
      default_train_file_path: "",
      default_train_id_column: "",
      default_train_data_column: "",
      ptitles:"",
      pdatas:"",
      select_data:false,
      // profileForm: {
      //   default_train_data_path: "",
      //   default_train_id_path: "",
      //   default_test_data_path: "",
      //   default_test_id_path: "",
      // },
    }
  },
  methods: {
    // not_receive() {
      // this.sharedState.receive_request = 'not_receive'
      // this.sharedState.pending.a='apple'
      // this.sharedState.pending.b='big'
    //   this.sharedState.pending.push({
    //     a: 'add',
    //     b: 'bust'
    // })
    //   this.sharedState.pending.splice(0, 1);
    //   console.log(this.sharedState.pending)
    // },
    // passive() {

    //   let vm = this
    //   let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + this.sharedState.user_id;
    //   db.get(select_sentence, function(err, row){
    //     if (err){
    //       console.log(err);
    //     }

    //     console.log(row)

    //     if (row == null | row.default_data_path == "" | row.default_id_path == "" |
    //         row.default_test_data_path == "" | row.default_test_id_path == ""){
    //       console.log("get false")
    //       vm.sharedState.set_default = false
    //       vm.sharedState.receive_request = 'not_respond'
    //       vm.$toasted.success('Please Fill the Default Setting', { icon: 'fingerprint' })
    //       vm.picked = "One";
    //     }
    //     else{
    //       vm.sharedState.receive_request = 'passive'
    //     }
        
    //   })
    // },
    // active() {

    //   let vm = this
    //   let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + this.sharedState.user_id;
    //   db.get(select_sentence, function(err, row){
    //     if (err){
    //       console.log(err);
    //     }

    //     console.log(row)

    //     if (row == null | row.default_data_path == "" | row.default_id_path == "" |
    //         row.default_test_data_path == "" | row.default_test_id_path == ""){
    //       console.log("get false")
    //       vm.sharedState.set_default = false
    //       vm.sharedState.receive_request = 'not_respond'
    //       vm.$toasted.success('Please Fill the Default Setting', { icon: 'fingerprint' })
    //       vm.picked = "One";
    //     }
    //     else{
    //       vm.sharedState.receive_request = 'active'
    //     }
        
    //   })
    // },
    get_default_train_file_path() {
      let vm = this
      let result = dialog.showOpenDialogSync({
        properties: ['openFile'],
        // sufix
        filters: [{
          name: 'Text', 
          extensions: ['html', 'js', 'json', 'md', 'csv'] 
        }]
      })
      console.log("get_default_train_file_path", result)
      if (result === undefined){
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
      }else{

        try {
          let path = result[0]
          fs.statSync(path);
          // this.profileForm.default_train_data_path = path
          // this.profileForm.default_test_data_path = path
          this.default_train_file_path = path

          fs.readFile(path, 'utf8' , (err, data) => {
            if (err) {
              console.error(err)
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
    // get_default_train_id_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_default_train_id_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.profileForm.default_train_id_path = path
    //       this.profileForm.default_test_id_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
    //       console.log('Please Select A Train ID File')
    //     }  

    //   }
    // },
    // get_default_test_data_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_default_test_data_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.profileForm.default_test_data_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
    //       console.log('Please Select A Test Data File')
    //     }  

    //   }
    // },
    // get_default_test_id_path() {
    //   let result = dialog.showOpenDialogSync({
    //     properties: ['openFile'],
    //     // sufix
    //     filters: [{
    //       name: 'Text', 
    //       extensions: ['html', 'js', 'json', 'md', 'csv'] 
    //     }]
    //   })
    //   console.log("get_default_test_id_path", result)
    //   if (result === undefined){
    //     dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
    //   }else{

    //     try {
    //       let path = result[0]
    //       fs.statSync(path);
    //       this.profileForm.default_test_id_path = path
    //     } catch (err) {
    //       dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
    //       console.log('Please Select A Test ID File')
    //     }  

    //   }
    // },
    getUser (id) {
      let vm = this

      const row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id= ?').get(this.sharedState.user_id);
      // console.log('haha',row);
      if (row != null){
          vm.default_train_file_path = row.default_train_file_path
          vm.default_train_id_column = row.default_train_id_column
          vm.default_train_data_column = row.default_train_data_column
          vm.sharedState.mode = row.mode
          console.log('mode', vm.sharedState.mode)
        }





      // let vm = this
      // let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + this.sharedState.user_id;
      // db.exec(select_sentence, function(err, row){
      //   if (err){ 
      //     console.log(err);
      //   }

      //   console.log('xianshi',row)

      //   if (row != null){
      //     vm.default_train_file_path = row.default_train_file_path
      //     vm.default_train_id_column = row.default_train_id_column
      //     vm.default_train_data_column = row.default_train_data_column
      //     vm.sharedState.mode = row.mode
      //     console.log('mode', vm.sharedState.mode)
      //   }

      // })
      // let vm = this
      // let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + this.sharedState.user_id;
      // db.exec(select_sentence, function(err, row){
      //   if (err){ 
      //     console.log(err);
      //   }

      //   console.log('xianshi',row)

      //   if (row != null){
      //     vm.default_train_file_path = row.default_train_file_path
      //     vm.default_train_id_column = row.default_train_id_column
      //     vm.default_train_data_column = row.default_train_data_column
      //     vm.sharedState.mode = row.mode
      //     console.log('mode', vm.sharedState.mode)
      //   }

      // })
    },
    onSubmit (e) {
      let vm = this;
      let both_path_validation = true
      console.log("vm.default_train_file_path", vm.default_train_file_path)
      try {
        fs.statSync(vm.default_train_file_path);
      } catch (err) {
        dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
        console.log('Please Select A Train Data File')
        both_path_validation = false
      }

      console.log("vm.default_train_id_column", vm.default_train_id_column)
      console.log("vm.default_train_data_column", vm.default_train_data_column)



//       const stmt = db.prepare('INSERT INTO User_Default_Table VALUES ( @user_id , @default_train_file_path , @default_train_id_column, @default_train_data_column , @default_train_target_column,@mode)');
//       stmt.run({
//         user_id:vm.sharedState.user_id , 
//         default_train_file_path:3 , 
//         default_train_id_column:4, 
//         default_train_data_column:5 , 
//         default_train_target_column:6,
//         mode: 'auto'
// });
      const row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id= ?').get(this.sharedState.user_id);
      console.log('haha',row);
      if (row == null){

        const stmt = db.prepare('INSERT INTO User_Default_Table VALUES ( @user_id , @default_train_file_path , @default_train_id_column, @default_train_data_column , @default_train_target_column,@mode)');
        stmt.run({
          user_id:vm.sharedState.user_id , 
          default_train_file_path:vm.default_train_file_path , 
          default_train_id_column:vm.default_train_id_column, 
          default_train_data_column:vm.default_train_data_column , 
          default_train_target_column:"",
          mode: vm.sharedState.mode
        });
      }else{
        if(both_path_validation == true){
          const stmt = db.prepare('UPDATE User_Default_Table' 
          + 'SET default_train_file_path = ? ,'
          + 'default_train_id_column = ? ,'
          + 'default_train_data_column = ? ,'
          + 'mode = ? ,'
          + 'WHERE user_id = ?'); 
          stmt.run(vm.default_train_file_path, vm.default_train_id_column, vm.default_train_data_column, vm.sharedState.mode, vm.sharedState.user_id);
        } 
      }
      vm.$toasted.success(`setting updated`, { icon: 'fingerprint' })
    },
//     onSubmit (e) {
//       let vm = this;
//       let both_path_validation = true
//       console.log("vm.default_train_file_path", vm.default_train_file_path)
//       try {
//         fs.statSync(vm.default_train_file_path);
//       } catch (err) {
//         dialog.showErrorBox('Train Data Path not Correct', 'Please Select A Train Data File')
//         console.log('Please Select A Train Data File')
//         both_path_validation = false
//       }

//       console.log("vm.default_train_id_column", vm.default_train_id_column)
//       console.log("vm.default_train_data_column", vm.default_train_data_column)



// //       const stmt = db.prepare('INSERT INTO User_Default_Table VALUES ( @user_id , @default_train_file_path , @default_train_id_column, @default_train_data_column , @default_train_target_column,@mode)');
// //       stmt.run({
        
// //         user_id:vm.sharedState.user_id , 
// //         default_train_file_path:3 , 
// //         default_train_id_column:4, 
// //         default_train_data_column:5 , 
// //         default_train_target_column:6,
// //   mode: 'auto'
// // });



//       // try {
//       //   fs.statSync(vm.profileForm.default_train_id_path);
//       // } catch (err) {
//       //   dialog.showErrorBox('Train ID Path not Correct', 'Please Select A Train ID File')
//       //   console.log('Please Select A Train ID File')
//       //   both_path_validation = false
//       // }

//       // console.log("vm.profileForm.default_test_data_path", vm.profileForm.default_test_data_path)
//       // try {
//       //   fs.statSync(vm.profileForm.default_test_data_path);
//       // } catch (err) {
//       //   dialog.showErrorBox('Test Data Path not Correct', 'Please Select A Test Data File')
//       //   console.log('Please Select A Test Data File')
//       //   both_path_validation = false
//       // }

//       // console.log("vm.profileForm.default_test_id_path", vm.profileForm.default_test_id_path)
//       // try {
//       //   fs.statSync(vm.profileForm.default_test_id_path);
//       // } catch (err) {
//       //   dialog.showErrorBox('Test ID Path not Correct', 'Please Select A Test ID File')
//       //   console.log('Please Select A Test ID File')
//       //   both_path_validation = false
//       // }





//       let select_sentence = 'SELECT * FROM User_Default_Table WHERE user_id=' + this.sharedState.user_id;
//       db.run(select_sentence, function(err, row){
//         if (err){ 
//           console.log(err);
//         }
//         console.log("row", row)
        
//         if (row == null){
//           // db.run(`INSERT INTO "User_Default_Table"("user_id", "default_train_data_path", "default_train_id_path") VALUES (1, 'love', 'consume')`)
//           let insert_new_val = `INSERT INTO "User_Default_Table" ("user_id", "default_train_file_path", "default_train_id_column", "default_train_data_column", "mode") VALUES 
//             (`+`"`+vm.sharedState.user_id+`", "`+vm.default_train_file_path+`", "`+vm.default_train_id_column+`", "`
//             +vm.default_train_data_column+`", "`+vm.sharedState.mode+`")`
//           console.log("insert_new_val", insert_new_val)
//           console.log("db", db)
//           db.run(insert_new_val, function(err){
//             if (err){
//               console.log(err)
//             }
//           })
//         }else{          
          
//           if(both_path_validation == true){
//             db.serialize(function() {
//               let update_sentence = 'UPDATE "User_Default_Table"'
//                         +'SET "default_train_file_path" = "' + vm.default_train_file_path + '",'
//                         +'"default_train_id_column" = "' + vm.default_train_id_column + '",'
//                         +'"default_train_data_column" = "' + vm.default_train_data_column + '",'   
//                         +'"mode" = "' + vm.sharedState.mode + '" '                  
//                         +'WHERE "user_id" = ' + vm.sharedState.user_id
//               console.log("update_sentence", update_sentence) 
              

//               db.run(update_sentence, function(err, rows) {
//                 if (err){
//                   console.log(err)
//                 }
//               });

//             });
//           }
//         }  
//         console.log("vm.sharedState.mode", vm.sharedState.mode)
//       })
//       vm.$toasted.success(`setting updated`, { icon: 'fingerprint' })
//     },

  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
  }
}
</script>