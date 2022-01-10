import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'

jest.setTimeout(10000);

function check_login_first_user(){
  test('check_login_first_user',(done)=>{  
    let check_login_final = (data) => {
      try{

        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        // console.log('param2', unittest_parameters)
        console.log('user_id1', unittest_parameters.user_id)
        done()
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

        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        console.log('user_id2', unittest_parameters.user_id)
        done()
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

function check_login_third_user(){
  test('check_login_third_user',(done)=>{
    let check_login_final = (data) => {
      try{

        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        console.log('user_id2', unittest_parameters.user_id)
        done()
      }catch (error){
        done(error)
      }
    }
  
    // let cur_parameters = generate_parameters(train_callback_functions.login)
    let cur_parameters = []
    cur_parameters.push(check_login_final)
    cur_parameters.push('Login_unittest')
    // assistor
    Login_wrapper.setData({loginForm: {username: unittest_parameters.third_user_username, 
                                       password: unittest_parameters.third_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

function check_login_fourth_user(){
  test('check_login_fourth_user',(done)=>{
    let check_login_final = (data) => {
      try{
        
        console.log('window', window.localStorage.getItem('Apollo-token'))
        // unittest_parameters.user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        console.log('user_id2', unittest_parameters.user_id)
        done()
      }catch (error){
        done(error)
      }
    }
  
    // let cur_parameters = generate_parameters(train_callback_functions.login)
    let cur_parameters = []
    cur_parameters.push(check_login_final)
    cur_parameters.push('Login_unittest')
    // assistor
    Login_wrapper.setData({loginForm: {username: unittest_parameters.fourth_user_username, 
                                       password: unittest_parameters.fourth_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}
// function ceshi(){
//   test('ceshi',()=>{  
//     console.log('zhiyuanlai ssm', unittest_parameters.default_id_column)
//     modify_parameter('default_id_column', "3456")
//     console.log('zhiyuanlai ssm2', unittest_parameters.default_id_column)
//   })

//   test('ceshi2',()=>{  
//     console.log('zhiyuanlai ssm', unittest_parameters.default_id_column)
//     modify_parameter('default_id_column', "5432")
//     console.log('zhiyuanlai ssm2', unittest_parameters.default_id_column)
//   })
// }

let login_helper = {}
login_helper.check_login_first_user = check_login_first_user
login_helper.check_login_second_user = check_login_second_user
login_helper.check_login_third_user = check_login_third_user
login_helper.check_login_fourth_user = check_login_fourth_user

export { login_helper}