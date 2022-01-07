import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter, modify_first_been_call} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function check_unread_request(){
  test('check_unread_request', (done) => {
    let check_unread_request_1 = (data) => {
      try{
        let request_dict = data[0]
        console.log('request_dict', request_dict)
  
        expect(request_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('zztoo1')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_2 = (data) => {
      try{
        console.log('zzz9',data)
        let task_id = data[0]
        let setting_mode = data[1]

        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
  
        expect(setting_mode).toEqual(
          'auto'
        )
  
        console.log('zztoo2')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_3 = (data) => {
      try{
        console.log('zztoo3')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_request_4 = (data) => {
      try{
        console.log('xxx',data)
        console.log('good')
        let stored = data[0].stored
        let task_id = data[0].task_id
  
        expect(stored).toEqual(
          'assistor match id stored'
        )
  
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        done()
        console.log('zzoo4')
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
    console.log('wokan', cur_parameters)
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
    // if (unittest_parameters.unread_request_notification_first_been_call == false){
    console.log('zz8', unittest_parameters)
    console.log('zz5', unittest_parameters.unread_request_notification)
    Navbar_wrapper.vm.unread_request(unittest_parameters.unread_request_notification, cur_parameters)
    // }else{
    //   console.log('zz6')
    //   modify_first_been_call('unread_request_notification_first_been_call')
    //   console.log('zz7', unittest_parameters.unread_request_notification_first_been_call)
    // }
    
  
  })
}

let unread_request_helper = {}
unread_request_helper.unread_request = check_unread_request

export { unread_request_helper }