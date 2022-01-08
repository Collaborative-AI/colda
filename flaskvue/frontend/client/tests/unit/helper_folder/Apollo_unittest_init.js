import axios from '../../../src/http'
import db from '../../../src/db'

const fs = require('fs');
const ex = require('child_process');
const node_path = require('path');
const os = require('os');
const dialog = require('electron');

import Login from '../../../src/views/Auth/Login.vue'
import Navbar from '../../../src/components/Navbar.vue'
import Profile from '../../../src/views/Settings/Profile.vue'
import Find_Assistor from '../../../src/views/Resources/find_assistor.vue'
import Find_Test_Assistor from '../../../src/views/Resources/find_test_assistor.vue'

import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
// https://next.vue-test-utils.vuejs.org/api/#setdata
const unittest_parameters = {}
// const user_id_array = []
// user_id_array[0] = '1'
// unittest_parameters.user_id = user_id_array

unittest_parameters.max_round = 1
unittest_parameters.user_id = ''
unittest_parameters.task_id = ''
unittest_parameters.test_id = ''
unittest_parameters.test_indicator = 'train'

unittest_parameters.first_user_username = 'xie1'
unittest_parameters.first_user_password = 'Xie1@123'
unittest_parameters.second_user_username = 'xie2'
unittest_parameters.second_user_password = 'Xie2@123'

unittest_parameters.unread_request_notification_first_been_call = true

unittest_parameters.unread_request_notification = null
unittest_parameters.unread_match_id_notification = ''
unittest_parameters.unread_situation_notification = ''
unittest_parameters.unread_output_notification = ''
unittest_parameters.unread_test_request_notification = ''
unittest_parameters.unread_test_match_id_notification = ''
unittest_parameters.unread_test_output_notification = ''

// login.vue
unittest_parameters.verification_res = true

// find_assistor.vue
unittest_parameters.task_name = 'test1'
unittest_parameters.task_description = "good test"
unittest_parameters.train_file_path = "/Users/qile/Documents/Apollo_Data/data/BostonHousing_2_123_1.0/0/train/dataset.csv"
// unittest_parameters.train_file_path = "/Users/xianjianxie/Downloads/data/BostonHousing_2_123_1.0/0/train/dataset.csv"
unittest_parameters.train_id_column = "1"
unittest_parameters.train_data_column = "2-8"
unittest_parameters.train_target_column = "9"

unittest_parameters.test_description = 'new test'
unittest_parameters.test_file_path = "/Users/qile/Documents/Apollo_Data/data/BostonHousing_2_123_1.0/0/test/dataset.csv"
unittest_parameters.test_id_column = "1"
unittest_parameters.test_data_column = "2-8"
unittest_parameters.test_target_column = "9"

unittest_parameters.assistor_username_list = 'xie2'
unittest_parameters.task_mode = 'regression'
unittest_parameters.model_name = 'linear'
unittest_parameters.metric_name = 'MAD_RMSE_R2'

// profile.vue
unittest_parameters.default_file_path = "/Users/qile/Documents/Apollo_Data/data/BostonHousing_2_123_1.0/1/all/dataset.csv"
// unittest_parameters.default_file_path = "/Users/xianjianxie/Downloads/data/BostonHousing_2_123_1.0/1/train/dataset.csv"
unittest_parameters.default_id_column = "1"
unittest_parameters.default_data_column = "2-7"


function modify_parameter(param, val){
  unittest_parameters[param] = val
  // console.log('param1', unittest_parameters)
}

function modify_first_been_call(function_name){
  unittest_parameters[function_name] = false
}




// async fetchPostsList(callback) {
//   return axios.get('https://jsonplaceholder.typicode.com/posts').then(res => {
//     // console.log('res',res)
//     return callback(res.data);
//   })
// }

// async function get_notification(unittest_parameters){
//   console.log('jinlai')
//   console.log('unit_test_param', unittest_parameters)
//   console.log('user_id1', unittest_parameters.user_id)
//   // const path = `/users/`+ unittest_parameters.user_id.toString() + `/notifications/`
//   const path = `/users/`+ `2` + `/notifications/`
//   axios.get(path)
//     .then((response) => {
//       console.log('res1',response)
//       const all_notifications = {
//         response_data: response.data
//       } 
//       axios.post('/update_all_notifications/', all_notifications)
//       .then((response) => {
//         // train stage
//         console.log('res2',response)
//         unittest_parameters.unread_request_notification = response.data["unread request"]
//         unittest_parameters.unread_match_id_notification = response.data["unread match id"]
//         unittest_parameters.unread_situation_notification = response.data["unread situation"]
//         unittest_parameters.unread_output_notification = response.data["unread output"]

//         // test stage
//         unittest_parameters.unread_test_request_notification = response.data["unread test request"]
//         unittest_parameters.unread_test_match_id_notification = response.data["unread test match id"]
//         unittest_parameters.unread_test_output_notification = response.data["unread test output"]
//       })
//   })
// }


let Login_wrapper = mount(Login, {
  mocks: {
    $toasted: {
      success: () => 6,
      error: () => {},
    },
    // $router: {
    //   push: () => 6,
    // },
    // $route: {
    //   query:{
    //     redirect: 'aa'
    //   },
    // },
    $axios: axios,
  },
  stubs: ['router-link','router-view']
});


let Navbar_wrapper = mount(Navbar, {
  mocks: {
     $toasted: {
         success: () => {},
         error: () => {},
     },
    $axios: axios,
    $db: db,
  },
  stubs: ['router-link','router-view']
});


let Find_Assistor_wrapper = mount(Find_Assistor, {
  mocks: {
     $toasted: {
         success: () => {},
         error: () => {},
     },
    $axios: axios,
    $db: db,
    fs: fs,
    ex: ex,
    node_path: node_path,
    os: os,
    dialog: dialog,
    // split: 
  },
  stubs: ['router-link','router-view']
});

const $route = {
  fullPath: 'full/path'
}
let Profile_wrapper = mount(Profile, {
  mocks: {
     $toasted: {
         success: () => {},
         error: () => {},
     },
     $route,
      // query: {
      //         from: {},
      //         from_task_name: {}

      //       }
      
    $axios: axios,
    $db: db,
    fs: fs,
    ex: ex,
    node_path: node_path,
    os: os,
    dialog: dialog,
    // split: 
  },
  stubs: ['router-link','router-view']
});


let Find_Test_Assistor_Wrapper = mount(Find_Test_Assistor, {
  mocks: {
     $toasted: {
         success: () => {},
         error: () => {},
     },
    $axios: axios,
    $db: db,
    fs: fs,
    ex: ex,
    node_path: node_path,
    os: os,
    dialog: dialog,
    // split: 
  },
  stubs: ['router-link','router-view']
});


export { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper, Profile_wrapper, modify_parameter, modify_first_been_call}