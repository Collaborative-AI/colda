import { unittest_parameters, switch_default_values, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'

jest.setTimeout(10000);

function switch_default(sponsor_mode, assistor_username_list, match_ratio){
  test('switch_dataset',()=>{  
    let assistor_num = assistor_username_list.split(",").length
    console.log('zzz999',assistor_num)
    console.log('zzz998',assistor_username_list)
    switch_default_values(sponsor_mode, assistor_num, match_ratio)
    console.log('zzzz', unittest_parameters)
    console.log(generate_unittest_log("switch_dataset"))
  })
}

let switch_default_values_helper = {}
switch_default_values_helper.switch_default = switch_default

export { switch_default_values_helper}