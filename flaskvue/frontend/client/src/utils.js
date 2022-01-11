// const log = require('electron-log')
// import {db} from './db'
// console.log('dbdachu',db)
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


// export function sqlite3_run(sql, params) {
//   return new Promise((resolve, reject) => {
//     db.run(sql, params, function (err) {
//       if (err) {
//         console.log('Error running sql ' + sql)
//         console.log(err)
//         reject(err)
//       } else {
//         resolve({ id: this.lastID })
//       }
//     })
//   })
// }

export function handle_Algorithm_return_value(name, return_val, first_val, second_val) {
  console.log(name, return_val)
  // check if return_val obeys the correct return value
  if (first_val != null){
    if (return_val[0] != first_val){
      return false
    }
  }
  if (second_val != null){
     if (return_val[1] != second_val){
       return false
     }
  }  
  return true
}

export function handle_assistor_username_list(assistor_username_string){
  
  if (assistor_username_string == undefined || assistor_username_string == ''){
    return false
  }

  // trim leading and trailing spaces
  assistor_username_string = assistor_username_string.trim()

  let new_assistor_username_list = assistor_username_string.split(",")
  
  let return_assistor_username_list = []
  for (let i = 0; i < new_assistor_username_list.length; i++){
    let cur_username = new_assistor_username_list[i].trim()

    // if username contains space, return false
    if (cur_username.indexOf(' ') >= 0){
      return false
    }
    return_assistor_username_list.push(cur_username)
  }

  return return_assistor_username_list
}


export function handle_input_column_string(input_string, kind, max_column_index){
  // if input_string is null, return false
  if (input_string == undefined || input_string == ''){
    return false
  }

  // if input string length < 1, return false
  if (input_string.length < 1){
    return false
  }

  // trim leading and trailing spaces
  let new_string = input_string.trim()

  if (kind == 'target' || kind == 'id'){
    // if the string is not Integer, return false
    if (isNaN(new_string)) {
      return false
    }
    
    // if the string has leading 0, return false
    if (new_string[0] == '0'){
      return false
    }

    let cur_num = parseInt(new_string)
    // if the index is smaller than 1 or larger than the max column index, return false
    if (cur_num < 1 || cur_num > max_column_index){
      return false
    }

    return cur_num.toString()

  } else if (kind == 'data') {

      // if string contains special symbol, return false
      let special_symbol = RegExp(/[(\~)(\!)(\@)(\#)(\$)(\%)(\^)(\&)(\*)(\()(\))(\)(\_)(\+)(\=)(\[)(\])(\{)(\})(\|)(\\)(\;)(\:)(\')(\")(\,)(\.)(\/)(\<)(\>)(\?)(\)]+/);  
      if (special_symbol.test(new_string)) {
        console.log('wtf')
        return false
      }

      // if string does not contains '-', return false
      let need_symbol = RegExp(/[(\-)]+/);  
      if (!need_symbol.test(new_string)){
        return false
      }

      new_string = new_string.split('-')
      // if new string length is not 2, return false
      if (new_string.length != 2){
        return false
      }

      let return_string = []
      let prev_num = 0
      for (let i = 0; i < new_string.length; i++){
        // trim leading and trailing spaces
        let cur_string = new_string[i].trim()

        // if there is leading 0, return false
        if (cur_string[0] == '0'){
          return false
        }
        let cur_num = parseInt(cur_string)
        // if the index is out of range, return false
        if (cur_num < 1 || cur_num > max_column_index){
          return false
        }
        
        // second index cannot be smaller than the first index
        if (cur_num < prev_num){
          return false
        }
        prev_num = cur_num
        return_string.push(cur_string)
      }
      
      return return_string.join('-')
  }
}

export function check_interaction(id_column, data_column, target_column){
  if (id_column == false || data_column == false || target_column == false){
    return false
  }

  if (id_column == '' || data_column == '' || target_column == ''){
    return false
  }

  if (id_column == undefined || data_column == undefined || target_column == undefined){
    return false
  }

  let id = parseInt(id_column)
  let target = parseInt(target_column)

  let data_list = data_column.split("-")
  let first_data_index = parseInt(data_list[0])
  let second_data_index = parseInt(data_list[1])

  if (id >= first_data_index || second_data_index >= target){
    return false
  }
  return true
}

export function check_assistor_interaction(id_column, data_column){
  if (id_column == false || data_column == false){
    return false
  }

  if (id_column == '' || data_column == ''){
    return false
  }

  if (id_column == undefined || data_column == undefined){
    return false
  }

  let id = parseInt(id_column)

  let data_list = data_column.split("-")
  let first_data_index = parseInt(data_list[0])
  let second_data_index = parseInt(data_list[1])

  if (id >= first_data_index){
    return false
  }
  return true
}

