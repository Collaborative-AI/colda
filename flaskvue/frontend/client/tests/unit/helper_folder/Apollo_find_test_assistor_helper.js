import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function check_find_test_assistor_sponsor_get_train_id(){
  test('check_find_test_assistor_sponsor_get_test_id', (done) => {
    let check_find_test_assistor_sponsor_get_test_id = (data) => {
      try{
        let test_id = data[0]
        done()
        unittest_parameters.test_id = test_id
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(check_find_test_assistor_sponsor_get_test_id)
    cur_parameters.push('find_test_assistor_unittest')
    Find_Assistor_wrapper.vm.get_test_id(cur_parameters)
  })
}

function check_find_test_assistor_sponsor_onSubmit_1(){
  test('check_find_test_assistor_sponsor_onSubmit_1',(done) => { 
    let check_find_test_assistor_sponsor_onSubmit_1 = (data) => {
      try{
        let test_file_path = data[0]
        let test_id_column = data[1]
        let test_data_column = data[2]
        let test_target_column = data[3]
  
        console.log('bxbx')
        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(test_file_path).toEqual(
          row.test_file_path
        )
        expect(test_id_column).toEqual(
          row.test_id_column
        )
        expect(test_data_column).toEqual(
          row.test_data_column
        )
        expect(test_target_column).toEqual(
          row.test_target_column
        )
        console.log('aqaqaq')
        console.log('check_find_test_assistor_sponsor_onSubmit_1')
      }catch (error){
        done(error)
      }
    }
  
    let check_find_test_assistor_sponsor_onSubmit_2 = (data) => {
      try{
        
        let find_test_assistor_response_data = data[0]
        console.log('find_test_assistor_response_data', find_test_assistor_response_data)
        console.log('check_find_test_assistor_sponsor_onSubmit_2')
        let task_id = find_test_assistor_response_data.task_id
        let assistor_num = find_test_assistor_response_data.assistor_num
        
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        expect(assistor_num).toEqual(
          1
        )
        done()
        // console.log('check_find_assistor_sponsor_onSubmit_2')
      }catch (error){
        done(error)
      }
    }
  
    let check_find_test_assistor_sponsor_onSubmit_3 = (data) => {
      try{
  
        console.log('check_find_test_assistor_sponsor_onSubmit_3')
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(check_find_test_assistor_sponsor_onSubmit_1)
    cur_parameters.push(check_find_test_assistor_sponsor_onSubmit_2)
    cur_parameters.push(check_find_test_assistor_sponsor_onSubmit_3)
    cur_parameters.push('find_assistor_unittest')
    // assistor
    Find_Test_Assistor_Wrapper.setData({task_id: unittest_parameters.task_id,
                                   task_name: unittest_parameters.task_name, 
                                   task_description: unittest_parameters.task_description,
                                   train_file_path: unittest_parameters.test_file_path,
                                   train_id_column: unittest_parameters.test_id_column,
                                   train_data_column: unittest_parameters.test_data_column,
                                   train_target_column: unittest_parameters.test_target_column,
                                   assistor_username_list: unittest_parameters.assistor_username_list,
                                   task_mode: unittest_parameters.task_mode,
                                   model_name: unittest_parameters.model_name,
                                   metric_name: unittest_parameters.metric_name})
                                   
    Find_Test_Assistor_Wrapper.vm.onSubmit(cur_parameters)
  })
}

let find_test_assistor_helper = {}
find_test_assistor_helper.get_test_id = check_find_test_assistor_sponsor_get_test_id
find_test_assistor_helper.onSubmit = check_find_test_assistor_sponsor_onSubmit_1

export { find_test_assistor_helper }