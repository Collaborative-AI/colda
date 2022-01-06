import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_sponsor_test_match_id_helper_function(){
  test('unread_sponsor_test_match_id_helper', (done) => { 
    let unread_sponsor_test_match_id_1 = (data) => {
      try{
        let test_match_id_dict = data[0]
        console.log('test_match_id_dict', test_match_id_dict)
  
        expect(test_match_id_dict[unittest_parameters.test_id]).not.toBeNull()
  
        console.log('unread_sponsor_match_id_1')
      }catch (error){
        done(error)
      }
    }
  
    let unread_sponsor_test_match_id_2 = (data) => {
      try{
        let response_data = data[0]
        let match_id_file = response_data.match_id_file
        let sponsor_random_id = response_data.sponsor_random_id
        // let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(match_id_file).not.toBeNull()
        expect(sponsor_random_id).not.toBeNull()
        
        console.log('unread_sponsor_test_match_id_2')
      }catch (error){
        done(error)
      }
    }
  
    let unread_sponsor_test_match_id_3 = (data) => {
      try{
        done()
        console.log('unread_sponsor_test_match_id_3')
      }catch (error){
        done(error)
      }
    }
  
    
  
    let cur_parameters = [];
    cur_parameters.push(unread_sponsor_test_match_id_1)
    cur_parameters.push(unread_sponsor_test_match_id_2)
    cur_parameters.push(unread_sponsor_test_match_id_3)
    cur_parameters.push('unread_test_match_id_unittest')
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
    Navbar_wrapper.vm.unread_test_match_id(unittest_parameters.unread_test_match_id_notification, cur_parameters)
  })
}



let unread_sponsor_test_match_id_helper = {}

unread_sponsor_test_match_id_helper.unread_sponsor_test_match_id = unread_sponsor_test_match_id_helper_function


export { unread_sponsor_test_match_id_helper }