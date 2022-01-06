
export function generate_unittest_parameters(){
  let unittest_parameters = []
  for (let i = 0; i < arguments.length; i++){
    unittest_parameters.push(arguments[i])
  }
  return unittest_parameters
}

export function execute_unittest_list(unittest_list, index, indicator, unittest_parameters){
  console.log('unittest_list',unittest_list)
  if (Array.isArray(unittest_list)) {
    if (unittest_list.length > 1 && unittest_list[unittest_list.length-1] == indicator){
      unittest_list[index](unittest_parameters)
      console.log(unittest_list)
      return true
    }
    return false
  } 
  console.log(indicator + ' wrong')
  return false
}

export function generate_message_string(){
  let message_list = []
  for (let i = 0; i < arguments.length; i++){
    message_list.push(arguments[i])
  }
  return message_list.join(" ")
}

export function Log(message, level, file_name){
  console.log(message, level)
}