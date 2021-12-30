import { login_helper } from './helper_folder/Apollo_login_helper';
import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper'
import { profile_helper } from './helper_folder/Apollo_profile_helper'
// import { unread_request_helper } from './helper_folder/Apollo_unread_request_helper'
import {  unittest_parameters,  modify_parameter, Navbar_wrapper } from './helper_folder/Apollo_unittest_init'
import {  get_notifications, update_notifications } from './helper_folder/Apollo_unittest_utils'
jest.setTimeout(10000);



afterAll(() => {
  window.localStorage.setItem('Apollo-token', null)
  console.log('afterAll')
});

describe('test_unread_request', () => {
  console.log('des1')
  

// }
  // Sponsor logins
  login_helper.check_login_first_user
  // Sponsor gets train id
  find_assistor_helper.get_train_id
  // Sponsor finds assistor
  find_assistor_helper.onSubmit

  // Assistor logins
  login_helper.check_login_second_user
  // Assistor updates default_train_file_path, default_train_id_column, 
  // default_train_data_column
  profile_helper.onSubmit

  
  test('update_notification', (done) => {

    async function notification(){
      // let res1 = await get_notification(unittest_parameters)
      // console.log('haha1', res1)
      // let res2 = await get_notification()
      // console.log('haha2', res2)
      // console.log(res1, res2)
      console.log('come2')
      let res1 = await get_notifications()
      console.log('zz1', res1)
      let res2 = await update_notifications(res1)
      console.log('zz2', res2)
      console.log('zz4', res2.data["unread request"])
      modify_parameter("unread_request_notification", res2.data["unread request"])
      modify_parameter("unread_match_id_notification", res2.data["unread match id"])
      modify_parameter("unread_situation_notification", res2.data["unread situation"])
      modify_parameter("unread_output_notification", res2.data["unread output"])
      // test stage
      modify_parameter("unread_test_request_notification", res2.data["unread test request"])
      modify_parameter("unread_test_match_id_notification", res2.data["unread test match id"])
      modify_parameter("unread_test_output_notification", res2.data["unread test output"])
      done()
    }
    notification()
  })
  console.log('rsee')
  test('check_unread_request', (done) => {  
    let check_unread_request_1 = (data) => {
      try{
        let request_dict = data[0]
        console.log('request_dict', request_dict)
  
        expect(request_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('check_unread_request_1')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_2 = (data) => {
      try{
        let task_id = data[0]
        let setting_mode = data[1]
        // let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
  
        expect(setting_mode).toEqual(
          'Auto'
        )
  
        console.log('check_unread_request_2')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_3 = (data) => {
      try{
        
        console.log('check_unread_request_3')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_4 = (data) => {
      try{
        console.log('xxx',data)
        let stored = data[0].stored
        let task_id = data[0].task_id
  
        expect(stored).toEqual(
          'assistor match id stored'
        )
  
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        done()
        console.log('check_unread_request_4')
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(check_unread_request_1)
    cur_parameters.push(check_unread_request_2)
    cur_parameters.push(check_unread_request_3)
    cur_parameters.push(check_unread_request_4)
    cur_parameters.push('unread_request_unittest')
    // assistor
    // Navbar_wrapper.setData({task_id: unittest_parameters.task_id,
    //                                task_name: unittest_parameters.task_name, 
    //                                task_description: unittest_parameters.task_description,
    //                                train_file_path: unittest_parameters.train_file_path,
    //                                train_id_column: unittest_parameters.train_id_column,
    //                                train_data_column: unittest_parameters.train_data_column,
    //                                train_target_column: unittest_parameters.train_target_column,
    //                                assistor_username_list: unittest_parameters.assistor_username_list,
    //                                task_mode: unittest_parameters.task_mode,
    //                                model_name: unittest_parameters.model_name,
    //                                metric_name: unittest_parameters.metric_name})
    console.log('zz5', unittest_parameters.unread_request_notification)
    Navbar_wrapper.vm.unread_request(unittest_parameters.unread_request_notification, cur_parameters)
  })

})
