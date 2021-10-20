<template>
  <div class="container">
    <div>Task Name: {{pending.task_name}}</div>
    <div>Task Id:{{pending.task_id}}</div>
    <div>Task Description: {{pending.task_description}}</div>
    <button @click="unread_request()" class="btn btn-primary">Accept</button>
    <button class="btn btn-primary" @click="delete_record">Reject</button>
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

export default {
  name: 'PendItem',  // Name of the component
  // props: ['log'],
  props: ["task_id"],
  
  data () {
    return {
        sharedState: store.state,
        pending:{},
        exe_position: '',
      
    }
  },

  methods: {
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

    unread_request() {
        let vm = this

        this.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

          let task_id=vm.pending.task_id
          // const assistor_store_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/'
          // fs.mkdirSync(assistor_store_folder, { recursive: true})

          let select_default_train_id_path = 'SELECT default_train_file_path, default_train_id_colomn FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_id_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_file_path = row.default_train_file_path
            let default_train_id_colomn = row.default_train_id_colomn
            // console.log("default_train_id_path", default_train_id_path)
            let hash_id_file_address = null;
            try{
              hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --root ' + vm.root + ' --self_id ' + vm.sharedState.user_id
                                      + ' --task_id ' + task_id + ' --mode train' + ' --dataset_path ' + default_train_file_path 
                                      + ' --id_idx ' + default_train_id_colomn, {encoding: 'utf8'})
    

              hash_id_file_address = hash_id_file_address.split("?")
              console.log("hash_id_file_address", hash_id_file_address)
            }catch(err){
                console.log(err)
            }
            
            // const Log_address = vm.root + '/' + vm.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'
            const Log_address = vm.handle_train_log_address(task_id)

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
    let select_sentence = 'DELETE FROM User_Pending_Page WHERE task_id=?';
      db.run(select_sentence, [vm.task_id], function(err){
      if (err){ 
        console.log(err);
      }
      })
    },//end method
    

    delete_record() {
      console.log('delete')
      let vm = this;
      let select_sentence = 'DELETE FROM User_Pending_Page WHERE task_id=?';
      db.run(select_sentence, [vm.task_id], function(err){
      if (err){ 
        console.log(err);
      }
      
    
    })
    this.$router.push({ name: 'Plist' })
    },
    

    },//method(){}


  created () {
    // this.getUserMessagesSenders(this.sharedState.user_id)
    let select_sentence = 'SELECT * FROM User_Pending_Page WHERE user_id=? AND task_id=?';
    let vm=this;
            db.get(select_sentence, [this.sharedState.user_id, this.task_id], function(err, row){
            if (err){ 
              console.log(err);
            }
            else{
              console.log(row)
              vm.pending=row
              console.log(vm.pending)
            }
        
            })//end db.get
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
  },//end created

  


  


  
}
// exports.default = Home
</script>