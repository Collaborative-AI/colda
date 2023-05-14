import { unittest_parameters, router, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'

jest.setTimeout(10000);

function login_first_user(){
  test('login_first_user',(done)=>{  
    let login_first_user_1 = (data) => {
      try{
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)

        console.log('user_id1', unittest_parameters.user_id)
        console.log(generate_unittest_log('login_first_user'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(login_first_user_1)
    cur_parameters.push('Login_unittest')
    // sponsor
    // router.push({ name: 'Login', params: {
    //   id: 1,
    //   postcode: 'KT18 7LJ',
    //   address: '3 The Crescent'
    // }})
    
    Login_wrapper.setData({loginForm: {username: unittest_parameters.first_user_username, 
                                       password: unittest_parameters.first_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

function login_second_user(){
  test('login_second_user',(done)=>{
    let login_second_user_1 = (data) => {
      try{
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        
        console.log('user_id2', unittest_parameters.user_id)
        console.log(generate_unittest_log('login_second_user'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = []
    cur_parameters.push(login_second_user_1)
    cur_parameters.push('Login_unittest')
    Login_wrapper.setData({loginForm: {username: unittest_parameters.second_user_username, 
                                       password: unittest_parameters.second_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

function login_third_user(){
  test('login_third_user',(done)=>{
    let login_third_user_1 = (data) => {
      try{
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
       
        console.log('user_id3', unittest_parameters.user_id)
        console.log(generate_unittest_log('login_third_user'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(login_third_user_1)
    cur_parameters.push('Login_unittest')
    Login_wrapper.setData({loginForm: {username: unittest_parameters.third_user_username, 
                                       password: unittest_parameters.third_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

function login_fourth_user(){
  test('login_fourth_user',(done)=>{
    let login_fourth_user_1 = (data) => {
      try{
        modify_parameter('user_id', JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id)
        
        console.log('user_id4', unittest_parameters.user_id)
        console.log(generate_unittest_log('login_fourth_user'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = []
    cur_parameters.push(login_fourth_user_1)
    cur_parameters.push('Login_unittest')
    // assistor
    Login_wrapper.setData({loginForm: {username: unittest_parameters.fourth_user_username, 
                                       password: unittest_parameters.fourth_user_password}, 
                                       verification_res: unittest_parameters.verification_res})
    Login_wrapper.vm.onSubmit(cur_parameters)
  })
}

let login_helper = {}
login_helper.login_first_user = login_first_user
login_helper.login_second_user = login_second_user
login_helper.login_third_user = login_third_user
login_helper.login_fourth_user = login_fourth_user

export { login_helper}