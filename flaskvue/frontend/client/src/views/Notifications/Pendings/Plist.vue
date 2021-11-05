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
                            <div class="text-truncate">Task Name: {{ pend.pending_task_name }}</div>
                            <div class="small">Task ID:  {{ pend.pending_task_id }}</div>
                            <div class='small'>Test ID: {{ pend.pending_test_id }}</div>
                            <div class="small">Task Description:  {{ pend.pending_task_description }}</div>
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
                              <router-link v-bind:to="{ name: 'PendItem', params: { task_description: pend.pending_task_description, task_id: pend.pending_task_id, task_name: pend.pending_task_name, test_id: pend.pending_test_id,  test_indicator: pend.test_indicator } }">
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
  },

created () {

    let vm = this
  
    this.$axios.get('/get_all_pending/')
      .then((response) => {
        // handle success
        console.log("get_all_pending response", response.data)
        vm.pending =  response.data.all_pending_items
      })
      .catch((error) => {
        // handle error
        console.log(error)
      })

  },
  
}
// exports.default = Home
</script>

