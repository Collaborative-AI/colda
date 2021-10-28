<template>
  <div class="container my-5">
    <div class="card border-0 g-mb-15 my-5" >
      <div class="d-flex justify-content-start g-brd-around g-brd-gray-light-v4 g-brd-left-1 g-pa-20 g-mb-10"
        v-for="(pend, index) in pending" v-bind:key="index">
        <div class="align-self-center g-px-10">
          <p class="m-0">Task Name: {{ pend.task_name }}</p>
          <p class="m-0">Task ID:  {{ pend.task_id }} </p>
          <br>
        </div>
        <div class="align-self-center ml-auto">
          <router-link v-bind:to="{ name: 'PendItem', params: { task_id: pend.task_id } }">
            <button class="btn btn-block u-btn-outline-primary g-rounded-20 g-px-10">Details</button>
          </router-link>
        </div>
        
      </div>

    <!-- {{pending}} -->
    <!-- {{sharedState.pending}} -->
    <!-- <button type="submit" @click="shan()" class="btn btn-primary">delete</button> -->
    </div>
  </div>
</template>

<script>
import store from '../../../store.js'
import db from '../../../db'
// import penditem from "../Penditem.vue"

export default {
  name: 'Plist',  // Name of the component
  // props: ['log'],
  
  data () {
    return {
      sharedState: store.state,
      pending: "",
    }
  },

  methods: {
    shan() {
      this.sharedState.receive_request = 'not_receive'
      // this.sharedState.pending.a='apple'
      // this.sharedState.pending.b='big'
    //   this.sharedState.pending.push({
    //     a: 'add',
    //     b: 'bust'
    // })
      // this.sharedState.pending.splice(0, 1);
      this.sharedState.pending.pop()
    //   console.log(this.sharedState.pending)
    },
  },

created () {
    
    // this.getUserMessagesSenders(this.sharedState.user_id)
    let select_sentence = 'SELECT * FROM User_Pending_Page WHERE user_id=?';
    let vm=this;
            db.all(select_sentence, [this.sharedState.user_id], function(err, row){
            if (err){ 
              console.log(err);
            }
            else{
              console.log(row)
              vm.pending=row
              console.log(vm.pending)
            }
        
            })//end db.get
  },
  


  
}
// exports.default = Home
</script>

