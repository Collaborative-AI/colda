import axios from 'axios';
// import db from '../../../src/db'
const Database = require('better-sqlite3');
// // console.log("5555")
// // console.log('21312312', Database)
// // console.log('12123', window.db)
const db = new Database('../Apollo_Client_data.db', { verbose: null });
import {unittest_parameters} from './Apollo_unittest_init'

let retrieve_User_Assistor_Table_record = function(user_id, task_id, test_indicator, test_id=null){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?').get(user_id, task_id, test_id, test_indicator);
    
    return row
  }
  let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?').get(user_id, task_id, test_indicator);
  // console.log('zzz7',row)
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

// let generate_parameters = function(parameters_dict){

//   let login_parameters = []
//   for (let key in parameters_dict){
//     login_parameters.push(parameters_dict[key]) 
//   }
//   return login_parameters

// }

// function get_notifications(){
//   const path = `/users/`+ unittest_parameters.user_id.toString() + `/notifications/`
//   console.log('come', path)
//   return axios.get(path)
// }

// function update_notifications(response){
//   const all_notifications = {
//     response_data: response.data
//   } 
//   return axios.post('/update_all_notifications/', all_notifications)
// }

// function delete_db(){
//   return axios.get('/delete_all_rows/')
// }



// let retrieve_User_Assistor_Table_record = function(user_id, task_id, test_indicator, test_id=null){
//   if (test_id != null){
//     // row is a single result and it is a dict
//     // let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?').get(user_id, task_id, test_id, test_indicator);

//     let sentence = `SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?`
//     let param = [user_id, task_id, test_id, test_indicator]
           
//     db.get(sentence, param, (err, row) => {
//       if (err) {
//         return console.error(err.message);
//       }
//       console.log('churow1',row)
//       return row

//     });
    
//   }
//   // let row = db.prepare('SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?').get(user_id, task_id, test_indicator);

//   let sentence = `SELECT * FROM User_Assistor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?`
//   let param = [user_id, task_id, test_indicator]
           
//   db.get(sentence, param, (err, row) => {
//     if (err) {
//       return console.error(err.message);
//     }
//     console.log('churow2',row)
//     return row

//   });
// };

// let retrieve_User_Sponsor_Table_record = function(user_id, task_id, test_indicator, test_id=null){
//   if (test_id != null){
//     // row is a single result and it is a dict
//     // let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?').get(user_id, task_id, test_id, test_indicator);
    
//     let sentence = `SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_id = ? AND test_indicator = ?`
//     let param = [user_id, task_id, test_id, test_indicator]

             
//     return db.get(sentence, param, (err, row) => {
//       if (err) {
//         return console.error(err.message);
//       }
//       console.log('churow3',row)
//       // return row
  
//     });
//   }
//   // let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?').get(user_id, task_id, test_indicator);
//   let sentence = `SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_indicator = ?`
//   let param = [user_id, task_id, test_indicator]
  
//   return new Promise((resolve, reject) => {
//     db.get(sentence, param, function (err,row) {
//       if (err) {
//         console.log(err)
//         reject(err)
//       } else {
//         console.log('outrow2',row)
//         resolve(row)
//       }
//     })
//   })
  // return db.get(sentence, param, (err, row) => {
  //   if (err) {
  //     return console.error(err.message);
  //   }
  //   console.log('churow4',row)
  //   // return row

  // });
// };

// let retrieve_User_Default_Table_record = function(user_id){
  
//   let row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ?').get(user_id);
//   return row
// };

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

// function create_unittest_user(username, password){
//   const new_users = {
//     username: username,
//     password: password,
//   }
//   return axios.post('/create_unittest_user', new_users)
// }




// function cut_decimal(number){
//   if (number == 0){
//     return number
//   }
//   number = number * 100000
//   if (number < 0)
//     number = Math.ceil(number)
//   else {
//     number = Math.floor(number)
//   }
//   return number
// }



export { retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record, generate_parameters, get_notifications, update_notifications, delete_db }