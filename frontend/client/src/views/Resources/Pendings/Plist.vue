<template>
  <div class="container my-5">
        <div class="row">
       
        <div class="col-lg-9 right">
         
            <div class="box shadow-sm rounded bg-white mb-3">
                <div class="box-title border-bottom p-3">
                    <h6 class="m-0">Pending Tasks </h6>
                </div>
                <div class="box-body p-0" v-for="(pend, index) in pending" v-bind:key="index">
                    
                    <div class="p-3 d-flex align-items-center border-bottom osahan-post-header">
                        <!-- <div class="dropdown-list-image mr-3"><img class="rounded-circle" src="https://bootdey.com/img/Content/avatar/avatar3.png" alt="" /></div> -->
                        <div class="font-weight-bold mr-3">
                            <div v-if="pend.test_indicator == 'train'" class="text-truncate">Task Name: {{ pend.task_name }}</div>
                            <div v-if="pend.test_indicator == 'test'" class="text-truncate">Test Name: {{ pend.test_name }}</div>
                            <div class="small">Task ID:  {{ pend.task_id }}</div>
                            <div class='small'>Test ID: {{ pend.test_id }}</div>
                            <div class='small'>Task Mode: {{ pend.task_mode }}</div>
                            <div class='small'>Model Name: {{ pend.model_name }}</div>
                            <div class='small'>Metric Name: {{ pend.metric_name }}</div>

                            <div class="small">Task Description:  {{ pend.pending_task_description }}</div>
                            <div v-if="pend.pending_test_indicator == 'test'" class="small">Test Description:  {{ pend.test_description }}</div>
                        </div>
                        <span class="ml-auto mb-auto">
                            <!-- <div class="btn-group">
                                <button type="button" class="btn btn-light btn-sm rounded" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i class="mdi mdi-dots-vertical"></i>
                                </button>
                                <div class="dropdown-menu dropdown-menu-right">
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-delete"></i> Delete</button>
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-close"></i> Turn Off</button>
                                </div>
                            </div> -->
                            <br />
                            <div class="text-right text-muted pt-1">
                              <router-link v-bind:to="{ name: 'PendItem', params: { 
                                                        task_description: pend.task_description, 
                                                        task_id: pend.task_id, 
                                                        task_name: pend.task_name, 
                                                        task_mode: pend.task_mode,
                                                        model_name: pend.model_name,
                                                        metric_name: pend.metric_name,
                                                        test_id: pend.test_id, 
                                                        test_description: pend.test_description } }">
                                <button class="btn btn-block u-btn-outline-primary g-rounded-20 g-px-10">Details</button>
                              </router-link>
                            </div>
                        </span>
                    </div>
                 
               
                   
                    
                    
                    
                </div>
            </div>
        </div>
    </div>



    <!-- <div class="card border-0 g-mb-15 my-5" >
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

    
    </div> -->
  </div>
</template>

<script>
// import store from '../../../store.js'
import store from '../../../store'
import { generate_unittest_parameters, execute_unittest_list, add_prefix } from '../../../utils'
// import db from '../../../db'
// import { set } from 'vue/types/umd'
// import penditem from "../Penditem.vue"

export default {
  name: 'Plist',  // Name of the component
  // props: ['log'],
  
  data () {
    return {
      sharedState: store.state,
      pending: "",
      cur_pending_num: -10000,
      // test_indicator: ""
    }
  },

  methods: {

    check_if_new_pending(unittest_callbacks){
      let vm = this;
      console.log("----wowowowwo")
      // when the cur_pending_num in Plist page is not equals to the pending_num in store.js, it means we have new pending_page.
      // cal get_all_pending one more time
      if (vm.cur_pending_num != vm.sharedState.pending_num){
        vm.cur_pending_num = vm.sharedState.pending_num;
        console.log("----miemiemie")
        vm.$axios.get(add_prefix(`/get_all_pending/${vm.sharedState.user_id}/`, `/main_flow`))
        .then((response) => {
          // handle success
          console.log("get_all_pending response", response.data)
          vm.pending = response.data.all_pending_items
          // if (vm.pending.test_id == undefined){
          //   vm.test_indicator = 'train'
          // }
          // else{
          //   vm.test_indicator = 'test'
          // }

          let unittest_parameters = generate_unittest_parameters(response.data)
          execute_unittest_list(unittest_callbacks, 0, "plist_unittest", unittest_parameters)
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })
      }

      // recall check_if_new_pending function every 5 seconds
      const timer = setTimeout(() => {
        vm.check_if_new_pending()
      }, 5000)
      
      // destroy the setTimeout function when leave this page
      vm.$once('hook:beforeDestroy', function () {
			    clearTimeout(timer)
			})

    },
  },

created () {
    if (this.$route != undefined){
      this.check_if_new_pending()
    }
    
  },
  
}
// exports.default = Home
</script>

