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
          <th scope="col" v-for="(pdata, idx) in pdatas[0]" :key="pdata.index">{{idx+1}}</th>
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
    <br>
    
    <button @click="Accept()" class="btn btn-success">Accept</button>
    &nbsp;&nbsp;&nbsp;
    <button @click="Reject()" class="btn btn-success">Reject</button>
  
  </div>
</template>

<script>
import store from '../../../../store'
import db from '../../../../db'
// import penditem from "../Penditem.vue"
const fs = window.fs;
const ex = window.ex;
const node_path = window.node_path;
const os = window.os;
const dialog = window.dialog

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
      task_description: '',
      task_mode: '',
      model_name: '',
      metric_name: '',
      test_indicator: '',
      task_name: '',
      pdatas:"",
      select_data:false,
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
          fs.statSync(path);
          vm.manual_file_path = path
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
            vm.pdatas=vm.pdatas.slice(0,3)
            vm.select_data=true
            console.log('preview',vm.pdatas[0])
          })
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

    train_unread_request(){
      let vm = this;
      console.log('jin train')

      let task_id = vm.task_id
      let insert_sentence = `INSERT INTO "User_Manual_Table"("pending_train_file_path", "pending_train_id_column", "pending_train_data_column", "pending_train_target_column","user_id", "task_id") VALUES 
              (`+`"`+vm.manual_file_path +`", "`+vm.manual_id_column+`", "`+vm.manual_data_column+`", "`+vm.manual_target_column+`", "`+vm.sharedState.user_id+ `", "` + task_id + `")`
      console.log("insert_sentence", insert_sentence)

      const stmt = vm.$db.prepare('INSERT INTO User_Manual_Table VALUES' +
          ' ( @task_name, @task_description, @user_id, @task_id, @test_id, @pending_train_file_path,' +
          ' @pending_train_id_column, @pending_train_data_column, @pending_train_target_column, @pending_test_file_path, @pending_test_id_column,' +
          ' @pending_test_data_column, @pending_test_target_column, @task_mode, @model_name, @metric_name)');
             
          stmt.run({
            task_name: '', 
            task_description: '', 
            user_id: vm.sharedState.user_id, 
            task_id: task_id,
            test_id: '',
            pending_train_file_path: vm.manual_file_path, 
            pending_train_id_column: vm.manual_id_column, 
            pending_train_data_column: vm.manual_data_column, 
            pending_train_target_column: vm.manual_target_column, 
            pending_test_file_path: '',
            pending_test_id_column: '',
            pending_test_data_column: '',
            pending_test_target_column: '',
            task_mode: '', 
            model_name: '',
            metric_name: ''
          });

        console.log("2.1 Update Test request notification response")
      
        const delete_pending = {
          task_id: vm.task_id,
          test_id: vm.test_id,
          test_indicator: vm.test_indicator
        }

        vm.$axios.post('/delete_pending/', delete_pending)
          .then((response) => {
            // handle success
            console.log("delete_pending response", response.data)
            let task_id = vm.task_id
        let hash_id_file_address = null;
        let Log_address = null;
        try{
          hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                  + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + vm.manual_file_path 
                                  + ' --id_idx ' + vm.manual_id_column, {encoding: 'utf8'})


          hash_id_file_address = hash_id_file_address.split('?')
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

          })
          .catch((error) => {
            // handle error
            console.log(error)

          })
        
        
      
          

    },

    test_unread_request(){
      console.log('jin test')
      let vm = this

      let insert_sentence = `INSERT INTO "User_Manual_Table"("pending_test_file_path", "pending_test_id_column", "pending_test_data_column", "pending_test_target_column","user_id", "test_id") VALUES 
              (`+`"`+vm.manual_file_path +`", "`+vm.manual_id_column+`", "`+vm.manual_data_column+`", "`+vm.manual_target_column+`", "`+vm.sharedState.user_id+ `", "` + vm.test_id + `")`
      console.log("insert_sentence", insert_sentence)

      const stmt = vm.$db.prepare('INSERT INTO User_Manual_Table VALUES' +
          ' ( @task_name, @task_description, @user_id, @task_id, @test_id, @pending_train_file_path,' +
          ' @pending_train_id_column, @pending_train_data_column, @pending_train_target_column, @pending_test_file_path, @pending_test_id_column,' +
          ' @pending_test_data_column, @pending_test_target_column, @task_mode, @model_name, @metric_name)');
             
          stmt.run({
            task_name: '', 
            task_description: '', 
            user_id: vm.sharedState.user_id, 
            task_id: '',
            test_id: vm.test_id,
            pending_train_file_path: '', 
            pending_train_id_column: '', 
            pending_train_data_column: '', 
            pending_train_target_column: '', 
            pending_test_file_path: vm.manual_file_path,
            pending_test_id_column: vm.manual_id_column,
            pending_test_data_column: vm.manual_data_column,
            pending_test_target_column: vm.manual_target_column,
            task_mode: '', 
            model_name: '',
            metric_name: ''
          });
      


        console.log("2.1 Update Test request notification response")
        vm.$toasted.success("2.1 Update Test request notification", { icon: 'fingerprint' })


        const delete_pending = {
          task_id: vm.task_id,
          test_id: vm.test_id,
          test_indicator: vm.test_indicator
        }

        vm.$axios.post('/delete_pending/', delete_pending)
          .then((response) => {
            // handle success
            console.log("delete_pending response", response.data)
            let task_id = vm.task_id
        let test_id = vm.test_id
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
          test_id: test_id,
          task_id: task_id
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


          })
          .catch((error) => {
            // handle error
            console.log(error)

          })

        
          
        




    },


    Accept(){
      let vm = this
      vm.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

      let task_id = vm.task_id
      
      if (vm.test_indicator == 'train'){
        vm.train_unread_request()
      }else{
        vm.test_unread_request()
      }
      vm.$router.push('/notifications')
      
    },

    
    

    Reject() {
      console.log('delete')
      let vm = this;

      const delete_pending = {
        task_id: vm.task_id,
        test_id: vm.test_id,
        test_indicator: vm.test_indicator
      }

      vm.$axios.post('/delete_pending/', delete_pending)
        .then((response) => {
          // handle success
          console.log("delete_pending response", response.data)

        })
        .catch((error) => {
          // handle error
          console.log(error)

        })
      vm.$router.push('/notifications')
    },
    

  },// end method(){}


  created () {
  
    
    
    this.task_description = this.$route.params.task_description
    this.task_id = this.$route.params.task_id
    this.task_name = this.$route.params.task_name
    this.task_mode = this.$route.params.task_name,
    this.model_name = this.$route.params.model_name,
    this.metric_name = this.$route.params.metric_name,
    this.test_id = this.$route.params.test_id
    this.test_indicator = this.$route.params.test_indicator

    console.log('chuan', this.$route.params)
    

    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },//end created

}
// exports.default = Home
</script>