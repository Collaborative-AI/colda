import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'

jest.setTimeout(10000);

function check_login_first_user(){
  test('check_login_first_user',(done)=>{  
    let check_login_final = (data) => {
      try{
        done()
        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        console.log('param2', unittest_parameters)
        console.log('user_id2', unittest_parameters.user_id)
      }catch (error){
        done(error)
      }
    }
  
    // let cur_parameters = generate_parameters(train_callback_functions.login)
    let cur_parameters = []
    cur_parameters.push(check_login_final)
    cur_parameters.push('Login_unittest')
    // sponsor
    Login_wrapper.setData({loginForm: {username: unittest_parameters.first_user_username, 
                                       password: unittest_parameters.first_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

function check_login_second_user(){
  test('check_login_second_user',(done)=>{
    let check_login_final = (data) => {
      try{
        done()
        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        console.log('param3', unittest_parameters)
  
      }catch (error){
        done(error)
      }
    }
  
    // let cur_parameters = generate_parameters(train_callback_functions.login)
    let cur_parameters = []
    cur_parameters.push(check_login_final)
    cur_parameters.push('Login_unittest')
    // assistor
    Login_wrapper.setData({loginForm: {username: unittest_parameters.second_user_username, 
                                       password: unittest_parameters.second_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

let login_helper = {}
// train_helper_functions.login = {}

login_helper.check_login_first_user = check_login_first_user

login_helper.check_login_second_user = check_login_second_user

export { login_helper}