import axios from '../../../src/http'
import db from '../../../src/db'
console.log('dbshi',db)

const fs = require('fs');
const ex = require('child_process');
const node_path = require('path');
const os = require('os');
const dialog = console.log
// const log = require('electron-log')
const log = console.log

import Login from '../../../src/views/Auth/Login.vue'
import Navbar from '../../../src/components/Navbar.vue'
import Profile from '../../../src/views/Settings/Profile.vue'
import Find_Assistor from '../../../src/views/Resources/find_assistor.vue'
import Find_Test_Assistor from '../../../src/views/Resources/find_test_assistor.vue'
import Plist from '../../../src/views/Resources/Pendings/Plist.vue'
import PendItem from '../../../src/views/Resources/Pendings/PendItem.vue'

import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
import VueRouter from 'vue-router'
// import { routes } from '../../../src/router/index'



// https://next.vue-test-utils.vuejs.org/api/#setdata
const unittest_parameters = {}
// const user_id_array = []
// user_id_array[0] = '1'
// unittest_parameters.user_id = user_id_array

unittest_parameters.max_round = 1
unittest_parameters.user_id = ''
unittest_parameters.task_id = ''
unittest_parameters.test_id = ''
unittest_parameters.multiple_task_ids = {}
unittest_parameters.multiple_test_ids = {}
unittest_parameters.manual_multiple_task = []
unittest_parameters.test_indicator = 'train'

unittest_parameters.first_user_username = 'xie1'
unittest_parameters.first_user_password = 'Xie1@123'
unittest_parameters.second_user_username = 'xie2'
unittest_parameters.second_user_password = 'Xie2@123'
unittest_parameters.third_user_username = 'leq1'
unittest_parameters.third_user_password = 'Leq1@123'
unittest_parameters.fourth_user_username = 'leq2'
unittest_parameters.fourth_user_password = 'Leq2@123'

unittest_parameters.unread_request_notification = null
unittest_parameters.unread_match_id_notification = ''
unittest_parameters.unread_situation_notification = ''
unittest_parameters.unread_output_notification = ''
unittest_parameters.unread_test_request_notification = ''
unittest_parameters.unread_test_match_id_notification = ''
unittest_parameters.unread_test_output_notification = ''

unittest_parameters.sponsor_ptitles = null
unittest_parameters.assistor_ptitles = null


// login.vue
unittest_parameters.verification_res = true

// find_assistor.vue
unittest_parameters.task_name = 'test1'
unittest_parameters.task_description = "best test"
unittest_parameters.train_file_path = null
// unittest_parameters.train_file_path = "/Users/qile/Documents/Apollo_Data/data/Wine_2_123_1.0/0/train/dataset.csv"
// unittest_parameters.train_file_path = "/Users/xianjianxie/Downloads/data/BostonHousing_2_123_1.0/0/train/dataset.csv"
unittest_parameters.train_id_column = "1"
unittest_parameters.train_data_column = "2-8"
unittest_parameters.train_target_column = "9"

unittest_parameters.test_description = 'best test'
unittest_parameters.test_file_path = null
// unittest_parameters.test_file_path = "/Users/qile/Documents/Apollo_Data/data/Wine_2_123_1.0/0/test/dataset.csv"

// unittest_parameters.test_file_path = "/Users/xianjianxie/Downloads/data/BostonHousing_2_123_1.0/0/test/dataset.csv"

unittest_parameters.test_id_column = "1"
unittest_parameters.test_data_column = "2-8"
unittest_parameters.test_target_column = "9"

unittest_parameters.assistor_username_list = 'xie2'
unittest_parameters.task_mode = 'regression'
unittest_parameters.model_name = 'linear'
// unittest_parameters.metric_name = 'MAD_RMSE_R2'
unittest_parameters.metric_name = 'Accuracy_F1'
// profile.vue
unittest_parameters.default_file_path = null
// unittest_parameters.default_file_path = "/Users/qile/Documents/Apollo_Data/data/Wine_2_123_1.0/1/all/dataset.csv"
// unittest_parameters.default_file_path = "/Users/xianjianxie/Downloads/data/BostonHousing_2_123_1.0/1/all/dataset.csv"
unittest_parameters.default_id_column = "1"
unittest_parameters.default_data_column = "2-7"
unittest_parameters.default_mode = null
unittest_parameters.default_model_name = null

function modify_parameter(param, val){
  unittest_parameters[param] = val
  // console.log('param1', unittest_parameters)
}

unittest_parameters.unittest_log_index = 1
unittest_parameters.prev_test_name = null
function generate_unittest_log(test_name){
  if (test_name != unittest_parameters.prev_test_name){
    unittest_parameters.unittest_log_index = 0
    unittest_parameters.prev_test_name = test_name
  } 
  unittest_parameters.unittest_log_index += 1
  return unittest_parameters.unittest_log_index.toString() + '_' + test_name
}


function switch_default_values(sponsor_mode, assistor_num, match_ratio, default_mode){
  let total_participants = assistor_num + 1
  total_participants = total_participants.toString()
  console.log('assistor_num', total_participants)

  function generate_data_path(user_id, folder_indicator) {
    let res = ''

    if (sponsor_mode == 'regression'){
      res = "/Users/qile/Documents/Apollo_Data/data/BostonHousing_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
      // res = "C://Users//Lucky//Desktop//Apollo//Apollo_Data//data//BostonHousing_" + total_participants + "_123_" + match_ratio + "//" + user_id + "//" + folder_indicator + "//dataset.csv"
      // res = "/Users/xianjianxie/Documents/Apollo_Data/data/BostonHousing_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

    } else if (sponsor_mode == 'classification'){
      res = "/Users/qile/Documents/Apollo_Data/data/Wine_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"
      // res = "C://Users//Lucky//Desktop//Apollo//Apollo_Data//data//Wine_" + total_participants + "_123_" + match_ratio + "//" + user_id + "//" + folder_indicator + "//dataset.csv"
      // res = "/Users/xianjianxie/Documents/Apollo_Data/data/Wine_" + total_participants + "_123_" + match_ratio + "/" + user_id + "/" + folder_indicator + "/dataset.csv"

    }
    return res
  }

  function generate_default_id_column(){
    return "1"
  }

  function generate_default_data_column(){
    if (total_participants == 2){
      return '2-7'
    } else if (total_participants == 3){
      return '2-5'
    }
  }

  function generate_default_model_name(){
    return 'linear'
  }
  
  unittest_parameters.train_file_path = generate_data_path("0", "train")
  unittest_parameters.test_file_path = generate_data_path("0", "test")

  let default_file_path_object = {}
  let default_id_column_object = {}
  let default_data_column_object = {}
  let default_model_name_object = {}

  for (let i = 2; i < assistor_num+2; i++){
    let path_user_id = (i-1).toString()
    let cur_user_id = i.toString()
    default_file_path_object[cur_user_id] = generate_data_path(path_user_id, "all")
    default_id_column_object[cur_user_id] = generate_default_id_column()
    default_data_column_object[cur_user_id] = generate_default_data_column()
    default_model_name_object[cur_user_id] = generate_default_model_name()
  }

  unittest_parameters.default_file_path = default_file_path_object
  unittest_parameters.default_id_column = default_id_column_object
  unittest_parameters.default_data_column = default_data_column_object
  unittest_parameters.default_model_name = default_model_name_object
 
  if (total_participants == 2){
    unittest_parameters.train_data_column = "2-8"
    unittest_parameters.train_target_column = "9"
    unittest_parameters.test_data_column = "2-8"
    unittest_parameters.test_target_column = "9"
    unittest_parameters.sponsor_ptitles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    unittest_parameters.assistor_ptitles = [0, 0, 0, 0, 0, 0, 0, 0]

  } else if (total_participants == 3){
    unittest_parameters.train_data_column = "2-6"
    unittest_parameters.train_target_column = "7"
    unittest_parameters.test_data_column = "2-6"
    unittest_parameters.test_target_column = "7"
    unittest_parameters.sponsor_ptitles = [0, 0, 0, 0, 0, 0, 0]
    unittest_parameters.assistor_ptitles = [0, 0, 0, 0, 0, 0]

  }
  unittest_parameters.task_mode = sponsor_mode

  if (sponsor_mode == 'regression'){
    unittest_parameters.metric_name = 'MAD_RMSE_R2'
  } else if (sponsor_mode == 'classification'){
    unittest_parameters.metric_name = 'Accuracy_F1'
  }

  unittest_parameters.default_mode = default_mode

}


const localVue = createLocalVue()
localVue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
  },  
  {
    path: '/33',
    component: Login,
    name: 'Login',
  }
 ]
 const router = new VueRouter({
  routes
 })

 const zz = {
  path: '/login',
  name: 'Login',
  component: Login,
  hash: '',
  params: { id: '123' },
  query: { q: 'hello' }
}

let Login_wrapper = mount(Login, {
  localVue,
  // router,
  mocks: {
    $toasted: {
      success: () => 6,
      error: () => {},
    },
    $route: zz, 
    lihai: 5,
    // $router: router,
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
    // fs: fs,
    ex: ex,
    node_path: node_path,
    os: os,
    // log: log,
    dialog: {
      showErrorBox: dialog,
    }
    
    // split: 
  },
  stubs: ['router-link','router-view']
});

let Profile_wrapper = mount(Profile, {
  mocks: {
     $toasted: {
         success: () => {},
         error: () => {},
     },
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
    dialog: {
      showErrorBox: dialog,
    }
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
    dialog: {
      showErrorBox: dialog,
    }
    // split: 
  },
  stubs: ['router-link','router-view']
});

let Plist_Wrapper = mount(Plist, {
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
    dialog: {
      showErrorBox: dialog,
    }
    // split: 
  },
  stubs: ['router-link','router-view']
});

let PendItem_Wrapper = mount(PendItem, {
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
    dialog: {
      showErrorBox: dialog,
    }
    // split: 
  },
  stubs: ['router-link','router-view']
});

export { unittest_parameters, router, Plist_Wrapper, PendItem_Wrapper, generate_unittest_log, switch_default_values, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper, Profile_wrapper, modify_parameter }