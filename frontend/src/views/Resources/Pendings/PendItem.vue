<template>
  <div class="container">
    <div> You are currently viewing a {{ test_indicator }} task</div>
    <div>Task Name: {{ task_name }}</div>
    <div>Task Id:{{ task_id }}</div>
    <div>Test Id:{{ test_id }}</div>
    <div>Task Mode: {{ task_mode }}</div>
    <div>Model Name: {{ model_name }}</div>
    <div>Metric Name: {{ metric_name }}</div>
    
    <div>Task Description: {{ task_description }}</div>
    <div>Test Description: {{ test_description }}</div>

    <div class="form-group">
      <label for="name">Select File Path</label>
      <input type="text" v-model="manual_file_path" class="form-control" id="name" placeholder="">
      <button @click="get_manual_file_path()" class="btn btn-success">Select File</button>
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
      <input type="text" v-model="manual_id_column" class="form-control" id="name" placeholder="">
    </div>
    
    <div class="form-group">
      <label for="name">Input data column</label>
      <input type="text" v-model="manual_data_column" class="form-control" id="name" placeholder="">
    </div>

    <div class="form-group">
    <label for="name">Select Model Name</label>
    &nbsp;
    <select v-model="model_name" class="form-control">
      <option v-for="item in model_name_list"  :key="item.index" :value="item">{{item}}</option>
    </select>
    </div>

    <br>
    
    <button @click="Accept()" class="btn btn-success">Accept</button>
    &nbsp;&nbsp;&nbsp;
    <button @click="Reject()" class="btn btn-success">Reject</button>
  
  </div>
</template>

<script>
import store from '../../../store'
import db from '../../../db'
import { ex,fs,os,node_path,dialog } from '../../../import_package.js'
import { handle_file_path, handle_input_column_string, check_assistor_interaction, handle_Algorithm_return_value, change_db_param_to_string, generate_unittest_parameters, execute_unittest_list, add_prefix } from '../../../utils'

// const fs = window.fs;
// const ex = window.ex;
// const node_path = window.node_path;
// const os = window.os;
// const dialog = window.dialog

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
      manual_target_column: '',
      task_id: '',
      test_id: '',
      task_description: '',
      task_mode: '',
      model_name: '',
      metric_name: '',
      test_indicator: '',
      test_description: '',
      task_name: '',
      ptitles:"",
      pdatas:"",
      select_data:false,
      model_name_list:['linear'],
    }
  },

  methods: {

    get_manual_file_path() {
      let vm = this
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

          if (handle_file_path(path) == false){
            dialog.showErrorBox('Data Path not Correct, Please do not contain space', 'Sorry')
            return
          }

          fs.statSync(path);
          vm.manual_file_path = path
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

    train_unread_request(unittest_callbacks){

      let vm = this;

      console.log('jin train', vm.manual_file_path, vm.manual_id_column, vm.manual_data_column, vm.manual_target_column)

      let both_path_validation = true

      let handle_data_column_res = handle_input_column_string(vm.manual_data_column, 'data', vm.ptitles.length)
      let handle_id_column_res = handle_input_column_string(vm.manual_id_column, 'id', vm.ptitles.length)

      let interaction_indicator = check_assistor_interaction(vm.manual_id_column, vm.manual_data_column)

      if ( handle_data_column_res == false) {
        dialog.showErrorBox('Please Type in manual_data_column in corrent form', 'Thank you very much')
      } else if ( handle_id_column_res == false) {
        dialog.showErrorBox('Please Type in manual_id_column in corrent form', 'Thank you very much')
      } else if ( interaction_indicator == false){
        dialog.showErrorBox('Please follow the form: id, data, target (no interaction)', 'Thank you very much')
      } else if (handle_file_path(vm.manual_file_path) == false){
        dialog.showErrorBox('Data Path not Correct, Please do not contain space', 'Sorry')
      } else {

        try {
          fs.statSync(vm.manual_file_path);
        } catch (err) {
          dialog.showErrorBox('File Path not Correct', 'Please Select A Correct File Path')
          console.log('Please Select A Correct File Path')
          both_path_validation = false
        }

        if (both_path_validation == true){
          let sentence = `INSERT INTO User_Assistor_Table (user_id, task_id, test_id, task_name, task_description, test_name, test_description, train_file_path,` +
          ` train_id_column, train_data_column, train_target_column, test_file_path, test_id_column,` +
          ` test_data_column, test_target_column, mode, test_indicator, model_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
        
          let param = [vm.sharedState.user_id, vm.task_id, '', '', '', '', '', vm.manual_file_path, vm.manual_id_column, vm.manual_data_column, 
                      vm.manual_target_column, '', '', '', '', 'manual', 'train', vm.model_name]

          vm.$db.run(sentence, change_db_param_to_string(param), function(err){
            if (err){
              console.log('err info',err);
            }

            let unittest_parameters = generate_unittest_parameters()
            execute_unittest_list(unittest_callbacks, 1, "PendItem_unittest", unittest_parameters)
            // const stmt = vm.$db.prepare('INSERT INTO User_Assistor_Table VALUES' +
            //     ' ( @user_id, @task_id, @test_id, @task_name, @task_description, @test_name, @test_description, @train_file_path,' +
            //     ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
            //     ' @test_data_column, @test_target_column, @mode, @test_indicator, @model_name)');
                  
            //     stmt.run({
            //       user_id: vm.sharedState.user_id, 
            //       task_id: vm.task_id,
            //       test_id: '',
            //       task_name: '', 
            //       task_description: '', 
            //       test_name: '',
            //       test_description: '',
            //       train_file_path: vm.manual_file_path, 
            //       train_id_column: vm.manual_id_column, 
            //       train_data_column: vm.manual_data_column, 
            //       train_target_column: vm.manual_target_column, 
            //       test_file_path: '',
            //       test_id_column: '',
            //       test_data_column: '',
            //       test_target_column: '',
            //       mode: 'manual',
            //       test_indicator: 'train',
            //       model_name: vm.model_name
            //     });

            console.log("2.1 Update request notification response")
            if(vm.test_id == undefined){
              vm.test_id = null
            }
          
            const delete_pending = {
              train_id: vm.task_id,
              test_id: vm.test_id,
              test_indicator: vm.test_indicator
            }
            console.log('wokan4', vm.test_indicator)

            vm.$axios.post(add_prefix(`/delete_pending/${vm.sharedState.user_id}/`, `/main_flow`), delete_pending)
              .then((response) => {
                // handle success
                console.log("delete_pending response", response.data)
                let unittest_parameters = generate_unittest_parameters(response.data)
                execute_unittest_list(unittest_callbacks, 2, "PendItem_unittest", unittest_parameters)

                let task_id = vm.task_id
                let hash_id_file_address = null;
                let Log_address = null;

                vm.$toasted.success(`Training: Assistor Accepts Task ` + task_id, { icon: 'fingerprint' })
                vm.$toasted.success( `Training Starts`, { icon: 'fingerprint' })

                try{
                  console.log('asa', vm.manual_file_path, vm.manual_id_column)
                  hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                          + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + vm.manual_file_path
                                          + ' --id_idx ' + vm.manual_id_column, {encoding: 'utf8'})

                  hash_id_file_address = hash_id_file_address.split('?')

                  let indicator = handle_Algorithm_return_value("hash_id_file_address", hash_id_file_address, "200", "make_hash")
                  Log_address = vm.handle_train_log_address(task_id)
                  if (indicator == false){
                    console.log("hash_id_file_address wrong")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: error" + ", Content: hash_id_file_address wrong")
                    return 
                  }
                }catch(err){
                    console.log(err)
                }

                try {
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: You are Assistor\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: Task ID: " + task_id + "\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2. Unread Request\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2.1 Update the request notification\n")
                } catch (err) {
                  console.log(err)
                }
                let hash_id_file_data = fs.readFileSync(hash_id_file_address[2], {encoding:'utf8', flag:'r'});
                hash_id_file_data = hash_id_file_data.split(/[\r\n]+/)
                console.log('hash_id_file_data', hash_id_file_data)

                const match_assistor_id_data = {
                  train_id: task_id,
                  identifier_content: hash_id_file_data,
                }
                
                vm.$axios.post(add_prefix(`/match_identifier_content/${vm.sharedState.user_id}/`, `/main_flow`), match_assistor_id_data)
                  .then((response) => {
                    // handle success
                    console.log("2.2 assistor uploads id file")
                    // vm.$toasted.success(`2.2 assistor uploads id file`, { icon: 'fingerprint' })
                    
                    let unittest_parameters = generate_unittest_parameters(response.data)
                    execute_unittest_list(unittest_callbacks, 3, "PendItem_unittest", unittest_parameters)
                    
                    try {
                      fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2.2 assistor uploads id file\n")
                      fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2. Unread Request Done\n")
                    } catch (err) {
                      console.log(err)
                    }

                  })
                  .catch((error) => {
                    console.log(error)
                    // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })

                  }) // axios match_assistor_id ends

              })
              .catch((error) => {
                console.log(error)
              }) // axios delete_pending

          }) // db Insert Row to User_Assistor_Table
        } // if both_path_validation == true
      } // else 
    }, // function train_unread_request

    test_unread_request(unittest_callbacks){
      console.log('jin test')

      let vm = this
      let both_path_validation = true

      let handle_data_column_res = handle_input_column_string(vm.manual_data_column, 'data', vm.ptitles.length)
      let handle_id_column_res = handle_input_column_string(vm.manual_id_column, 'id', vm.ptitles.length)

      let interaction_indicator = check_assistor_interaction(vm.manual_id_column, vm.manual_data_column)

       if ( handle_data_column_res == false) {
        dialog.showErrorBox('Please Type in manual_data_column in corrent form', 'Thank you very much')
      } else if ( handle_id_column_res == false) {
        dialog.showErrorBox('Please Type in manual_id_column in corrent form', 'Thank you very much')
      } else if ( interaction_indicator == false){
        dialog.showErrorBox('Please follow the form: id, data, target (no interaction)', 'Thank you very much')
      } else if (handle_file_path(vm.manual_file_path) == false){
        dialog.showErrorBox('Data Path not Correct, Please do not contain space', 'Sorry')
      } else {

        try {
          fs.statSync(vm.manual_file_path);
        } catch (err) {
          dialog.showErrorBox('File Path not Correct', 'Please Select A Correct File Path')
          console.log('Please Select A Correct File Path')
          both_path_validation = false
        }

        if (both_path_validation == true){

          let sentence = `INSERT INTO User_Assistor_Table (user_id, task_id, test_id, task_name, task_description, test_name, test_description, train_file_path,` +
          ` train_id_column, train_data_column, train_target_column, test_file_path, test_id_column,` +
          ` test_data_column, test_target_column, mode, test_indicator, model_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          let param = [vm.sharedState.user_id, vm.task_id, vm.test_id, '', '', '', '', '', '', '', '', vm.manual_file_path, 
                      vm.manual_id_column, vm.manual_data_column, vm.manual_target_column,'manual', 'test', vm.model_name]

          vm.$db.run(sentence, change_db_param_to_string(param), function(err){
            if (err){
              console.log('err info',err);
            }

            let unittest_parameters = generate_unittest_parameters()
            execute_unittest_list(unittest_callbacks, 1, "PendItem_unittest", unittest_parameters)
            // let insert_sentence = `INSERT INTO "User_Assistor_Table"("pending_test_file_path", "pending_test_id_column", "pending_test_data_column", "pending_test_target_column","user_id", "test_id") VALUES 
            //         (`+`"`+vm.manual_file_path +`", "`+vm.manual_id_column+`", "`+vm.manual_data_column+`", "`+vm.manual_target_column+`", "`+vm.sharedState.user_id+ `", "` + vm.test_id + `")`
            // console.log("insert_sentence", insert_sentence)

            // const stmt = vm.$db.prepare('INSERT INTO User_Assistor_Table VALUES' +
            //     ' ( @user_id, @task_id, @test_id, @task_name, @task_description, @test_name, @test_description, @train_file_path,' +
            //     ' @train_id_column, @train_data_column, @train_target_column, @test_file_path, @test_id_column,' +
            //     ' @test_data_column, @test_target_column, @mode, @test_indicator, @model_name)');
                  
            //     stmt.run({
            //       user_id: vm.sharedState.user_id, 
            //       task_id: '',
            //       test_id: vm.test_id,
            //       task_name: '', 
            //       task_description: '', 
            //       test_name: '',
            //       test_description: '',
            //       train_file_path: '', 
            //       train_id_column: '', 
            //       train_data_column: '', 
            //       train_target_column: '', 
            //       test_file_path: vm.manual_file_path,
            //       test_id_column: vm.manual_id_column,
            //       test_data_column: vm.manual_data_column,
            //       test_target_column: vm.manual_target_column,
            //       mode: 'manual', 
            //       test_indicator: 'test',
            //       model_name: vm.model_name
            //     });
            
            console.log("2.1 Update Test request notification response")
            // vm.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })

            const delete_pending = {
              train_id: vm.task_id,
              test_id: vm.test_id,
              test_indicator: vm.test_indicator
            }
            console.log("222222")
            vm.$axios.post(add_prefix(`/delete_pending/${vm.sharedState.user_id}/`, `/main_flow`), delete_pending)
              .then((response) => {
                // handle success
                console.log("delete_pending response", response.data)
                let unittest_parameters = generate_unittest_parameters(response.data)
                execute_unittest_list(unittest_callbacks, 2, "PendItem_unittest", unittest_parameters)
                
                let task_id = vm.task_id
                let test_id = vm.test_id
                let test_hash_id_file_address = null
                let Log_address = null
                vm.$toasted.success(`Testing: Assistor Accepts Test` + test_id, { icon: 'fingerprint' })
                vm.$toasted.success( `Testing Starts`, { icon: 'fingerprint' })


                try{
                  test_hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root 
                                            + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id
                                            + ' --mode test' + ' --test_id ' + test_id
                                            + ' --dataset_path ' + vm.manual_file_path + ' --id_idx ' + vm.manual_id_column, {encoding: 'utf8'})

                  test_hash_id_file_address = test_hash_id_file_address.split("?")
                  let indicator = handle_Algorithm_return_value("test_hash_id_file_address", test_hash_id_file_address, "200", "make_hash")
                  Log_address = vm.handle_test_log_address(task_id, test_id)
                  if (indicator == false){
                    console.log("test_hash_id_file_address wrong")
                    fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: error" + ", Content: test_hash_id_file_address wrong")
                    return 
                  }
                }catch(err){
                  console.log(err)
                }

                try {
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: You are Assistor\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: Test ID: " + test_id + "\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: Test Stage: 2.Unread Test Request\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2.1 Test: Update Test request notification\n")
                  fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2.2 Test: Hashing Done\n")
                } catch (err) {
                  console.log(err)
                }

                let test_hash_id_file_data = fs.readFileSync(test_hash_id_file_address[2], {encoding:'utf8', flag:'r'});
                test_hash_id_file_data = test_hash_id_file_data.split(/[\r\n]+/)

                const match_test_assistor_id_data = {
                  identifier_content: test_hash_id_file_data,
                  test_id: test_id,
                  train_id: task_id
                }

                vm.$axios.post(add_prefix(`/match_test_identifier_content/${vm.sharedState.user_id}/`, `/main_flow`), match_test_assistor_id_data)
                  .then((response) => {
                    // handle success
                    console.log("2.2 Test: assistor uploads id file")
                    // vm.$toasted.success(`2.2 Test: assistor uploads id file`, { icon: 'fingerprint' })
                    
                    let unittest_parameters = generate_unittest_parameters(response.data)
                    execute_unittest_list(unittest_callbacks, 3, "PendItem_unittest", unittest_parameters)

                    try {
                      fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2.2 Test: assistor uploads id file\n")
                      fs.appendFileSync(Log_address, "Timestamp: " + vm.timeNow() + ", Level: info" + ", Content: 2. Unread Test Request Done\n")
                    } catch (err) {
                      console.log(err)
                    }
                  })
                  .catch((error) => {
                    console.log(error)
                    // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
                  }) // axios match_test_assistor_id


              })
              .catch((error) => {
                console.log(error)
              }) // axios delete_pending
              
          }) // db Insert row into User_Assistor_Table
        } // if both_path_validation == true
      } // else
    }, // function test_unread_request ends

    Accept(unittest_callbacks){
      let vm = this
      // vm.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })
      
      if (vm.test_indicator == 'train'){
        let unittest_parameters = generate_unittest_parameters()
        execute_unittest_list(unittest_callbacks, 0, "PendItem_unittest", unittest_parameters)
        vm.train_unread_request(unittest_callbacks)
      }else{
        let unittest_parameters = generate_unittest_parameters()
        execute_unittest_list(unittest_callbacks, 0, "PendItem_unittest", unittest_parameters)
        vm.test_unread_request(unittest_callbacks)
      }

      if (vm.$route != undefined){
        vm.$router.push('/notifications')
      }
      
    }, // function Accept()

    
    Reject(unittest_callbacks) {
      console.log('delete')
      let vm = this;

      const delete_pending = {
        train_id: vm.task_id,
        test_id: vm.test_id,
        test_indicator: vm.test_indicator
      }

      vm.$axios.post(add_prefiex(`/delete_pending/${vm.sharedState.user_id}/`, `/main_flow`), delete_pending)
        .then((response) => {
          // handle success
          console.log("delete_pending response", response.data)
          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 0, "PendItem_unittest", unittest_parameters)
        })
        .catch((error) => {
          console.log(error)
        }) // axios delete_pending

      if (vm.$route != undefined){
        vm.$router.push('/notifications')
      }
      
    } // function Reject()

  },// end method(){}


  created () {
    console.log('PendItem_created')

    // When unittesting, this.$route == undefined
    if (this.$route != undefined){
      this.task_description = this.$route.params.task_description
      this.task_id = this.$route.params.task_id
      this.task_name = this.$route.params.task_name
      this.task_mode = this.$route.params.task_mode,
      this.model_name = this.$route.params.model_name,
      this.metric_name = this.$route.params.metric_name,
      this.test_id = this.$route.params.test_id
      console.log('guolai',this.test_id,this.task_id);
      if (this.test_id == undefined){
        this.test_indicator = 'train'
      }
      else{
        this.test_indicator = 'test'
      }
      // this.test_indicator = this.$route.params.test_indicator
      console.log('test indicator is', this.test_indicator)
      this.test_description = this.$route.params.test_description

      console.log('wudi', this.task_description,
      this.task_id,
      this.task_name,
      this.task_mode,
      this.model_name,
      this.metric_name,
      this.test_id,
      this.test_indicator,
      this.test_description,)
    }

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },//end created

}
// exports.default = Home
</script>