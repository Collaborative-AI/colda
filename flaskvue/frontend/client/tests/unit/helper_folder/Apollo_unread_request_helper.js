import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

let unread_request_helper = {}

unread_request_helper.unread_request = test('check_unread_request', (done) => {  
  let check_unread_request_1 = (data) => {
    try{
      let request_dict = data[0]
      console.log('request_dict', request_dict)

      expect(request_dict['unittest_parameters.task_id']).not.toBeNull()

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

      let stored = data.stored
      let task_id = data.task_id

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
  Navbar_wrapper.vm.unread_request(unittest_parameters.unread_request_notification, cur_parameters)
})



export { unread_request_helper }