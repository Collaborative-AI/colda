import axios from 'axios';
import db from '../../../src/db'
import {unittest_parameters} from './Apollo_unittest_init'

let retrieve_User_Assistor_Table_record = function(user_id, task_id, test_indicator, test_id=null ){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?').get(user_id, task_id, test_id, test_indicator);
    
    return row
  }
  let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?').get(user_id, task_id, test_indicator);
  console.log('zzz7',row)
  return row
};

let retrieve_User_Sponsor_Table_record = function(user_id, task_id, test_indicator, test_id=null){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?').get(user_id, task_id, test_id, test_indicator);
    
    return row
  }
  let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?').get(user_id, task_id, test_indicator);
  return row
};

let retrieve_User_Default_Table_record = function(user_id){
  
  let row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ?').get(user_id);
  return row
};

let generate_parameters = function(parameters_dict){

  let login_parameters = []
  for (let key in parameters_dict){
    login_parameters.push(parameters_dict[key]) 
  }
  return login_parameters

}

function get_notifications(){
  const path = `/users/`+ unittest_parameters.user_id.toString() + `/notifications/`
  console.log('come', path)
  return axios.get(path)
}

function update_notifications(response){
  const all_notifications = {
    response_data: response.data
  } 
  return axios.post('/update_all_notifications/', all_notifications)
}

function delete_db(){
  return axios.get('/delete_all_rows/')
}



export { retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record, generate_parameters, get_notifications, update_notifications, delete_db }