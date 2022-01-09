const log = require('electron-log')
// console = log

export function generate_unittest_parameters(){
  let unittest_parameters = []
  for (let i = 0; i < arguments.length; i++){
    unittest_parameters.push(arguments[i])
  }
  return unittest_parameters
}

export function execute_unittest_list(unittest_list, index, indicator, unittest_parameters){
  // console.log('unittest_list',unittest_list)
  if (Array.isArray(unittest_list)) {
    if (unittest_list.length > 1 && unittest_list[unittest_list.length-1] == indicator){
      unittest_list[index](unittest_parameters)
      // console.log(unittest_list)
      index += 1
      return true
    }
    // console.log(indicator + ' wrong')
    return false
  } 
  // console.log(indicator + ' wrong')
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
  if (level == 'error'){
    log.error(message);
  }
  else if (level == 'warn'){
    log.warn(message);
  }
  else if (level == 'info'){
    log.info(message);
  }
  else if (level == 'verbose'){
    log.verbose(message);
  }
  else if (level == 'debug'){
    log.debug(message);
  }
  else{
    log.silly(message);
  }
  
}

export function check_if_notification_is_null(notification, name){
  console.log(name,'qwedas', notification)
  if (notification == null || notification == {}){
    Log(name + 'is null')
    return true
  }
  return false
}