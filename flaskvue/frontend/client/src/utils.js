// const log = require('electron-log')
import {db} from './db'
console.log('dbdachu',db)
// console = log

export function generate_unittest_parameters(){
  let unittest_parameters = []
  for (let i = 0; i < arguments.length; i++){
    unittest_parameters.push(arguments[i])
  }
  return unittest_parameters
}

export function change_db_param_to_string(db_parameters){
  let new_db_parameters = []
  for (let i = 0; i < db_parameters.length; i++){
    let db_param_i = db_parameters[i]
    if (db_param_i == undefined){
      console.log('db_sentence_param_wrond')
    }
    // console.log('db_param_i', db_param_i)
    if (db_param_i.length > 0){
      new_db_parameters.push(db_param_i.toString())
    }
    else{
      new_db_parameters.push(db_param_i)
    }
  }
  return new_db_parameters
}

export function execute_unittest_list(unittest_list, index, indicator, unittest_parameters){
  console.log('execute_unittest_list',unittest_list)
  if (Array.isArray(unittest_list)) {
    if (unittest_list.length > 1 && unittest_list[unittest_list.length-1] == indicator){
      unittest_list[index](unittest_parameters)
      // console.log('zzzzzzz0',unittest_list)
      index += 1
      return true
    }
    console.log(indicator + ' execute_unittest_list wrong')
    return false
  } 
  console.log(indicator + ' execute_unittest_list wrong')
  return false
}

export function generate_message_string(){
  let message_list = []
  for (let i = 0; i < arguments.length; i++){
    message_list.push(arguments[i])
  }
  return message_list.join(" ")
}


export function Log(message, level){
  console.log(message)
  // if (level == 'error'){
  //   log.error(message);
  // }
  // else if (level == 'warn'){
  //   log.warn(message);
  // }
  // else if (level == 'info'){
  //   log.info(message);
  // }
  // else if (level == 'verbose'){
  //   log.verbose(message);
  // }
  // else if (level == 'debug'){
  //   log.debug(message);
  // }
  // else{
  //   log.silly(message);
  // }
  
}

export function check_if_notification_is_null(notification, name){
  console.log(name,'qwedas', notification)
  if (notification == null || notification == {}){
    Log(name + 'is null')
    return true
  }
  return false
}


export function sqlite3_run(sql, params) {
  return new Promise((resolve, reject) => {
    db.run(sql, params, function (err) {
      if (err) {
        console.log('Error running sql ' + sql)
        console.log(err)
        reject(err)
      } else {
        resolve({ id: this.lastID })
      }
    })
  })
}