<template>
  <div class="container">
    <div>Task Name: {{pending.task_name}}</div>
    <div>Task Id:{{pending.task_id}}</div>
    <div>Task Description: {{pending.task_description}}</div>
    <button @click="unread_request()" class="btn btn-primary">Accept</button>
    <button class="btn btn-primary">Reject</button>
  </div>
</template>

<script>
import store from '../../../store.js'
import db from '../../../db'
// import penditem from "../Penditem.vue"
const fs = window.require('fs');
const ex = window.require("child_process");

export default {
  name: 'PendItem',  // Name of the component
  // props: ['log'],
  props: ["task_id"],
  
  data () {
    return {
        sharedState: store.state,
        pending:{},

      
    }
  },

  methods: {
    unread_request() {
        let vm = this

        this.$toasted.success("2.1 Update the request notification", { icon: 'fingerprint' })

          let task_id=vm.pending.task_id
          // const assistor_store_folder = 'Local_Data/' + this.sharedState.user_id + '/' + task_id + '/'
          // fs.mkdirSync(assistor_store_folder, { recursive: true})

          let select_default_train_id_path = 'SELECT default_train_id_path FROM User_Default_Path WHERE user_id=' + vm.sharedState.user_id;
          db.get(select_default_train_id_path, function(err, row){
            if (err){ 
              throw err;
            }
            let default_train_id_path = row.default_train_id_path
            console.log("default_train_id_path", default_train_id_path)
            let hash_id_file_address = null;
            try{
              hash_id_file_address = ex.execSync(vm.exe_position + ' make_hash --id_path ' + default_train_id_path + ' --root ' + vm.root 
                                        + ' --self_id ' + vm.sharedState.user_id + ' --task_id ' + task_id + ' --mode train', {encoding: 'utf8'})
              console.log("hash_id_file_address", hash_id_file_address)
            }catch(err){
                console.log(err)
            }
            
            const Log_address = vm.root + '/' + vm.sharedState.user_id + '/task/' + task_id + '/' + 'train/' + 'log.txt'

            try {
              fs.appendFileSync(Log_address, "\n You are Assistor\n")
              fs.appendFileSync(Log_address, "Task ID: " + task_id + "\n")
              fs.appendFileSync(Log_address, "----------------------2. Unread Request\n")
              fs.appendFileSync(Log_address, "2.1 Update the request notification\n")
            } catch (err) {
              console.log(err)
            }
            let hash_id_file_data = fs.readFileSync(hash_id_file_address, {encoding:'utf8', flag:'r'});

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
        
      
         
      
    },
    
    },


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
  },//end created

  


  


  
}
// exports.default = Home
</script>