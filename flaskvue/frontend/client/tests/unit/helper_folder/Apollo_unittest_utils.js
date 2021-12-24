import db from '../../../src/db'

let retrieve_User_Manual_Table_record = function(user_id, task_id, test_id=null){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Manual_Table WHERE user_id = ? AND task_id = ? AND test_id = ?').get(user_id, task_id, test_id);
    return row
  }
  let row = db.prepare('SELECT * FROM User_Manual_Table WHERE user_id = ? AND task_id = ?').get(user_id, task_id);
  return row
};

let retrieve_User_Sponsor_Table_record = function(user_id, task_id, test_id=null){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ? AND test_id = ?').get(user_id, task_id, test_id);
    return row
  }
  let row = db.prepare('SELECT * FROM User_Sponsor_Table WHERE user_id = ? AND task_id = ?').get(user_id, task_id);
  return row
};

let retrieve_User_Default_Table_record = function(user_id, task_id, test_id=null){
  if (test_id != null){
    // row is a single result and it is a dict
    let row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ? AND task_id = ? AND test_id = ?').get(user_id, task_id, test_id);
    return row
  }
  let row = db.prepare('SELECT * FROM User_Default_Table WHERE user_id = ? AND task_id = ?').get(user_id, task_id);
  return row
};

let generate_parameters = function(parameters_dict){

  let login_parameters = []
  for (let key in parameters_dict){
    login_parameters.push(parameters_dict[key]) 
  }
  return login_parameters

}



export { retrieve_User_Sponsor_Table_record, retrieve_User_Manual_Table_record, retrieve_User_Default_Table_record, generate_parameters}