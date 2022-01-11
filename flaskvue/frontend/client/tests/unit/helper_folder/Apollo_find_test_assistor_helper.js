import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function get_test_id_helper(){
  test('get_test_id_helper', (done) => {
    let get_test_id_helper_1 = (data) => {
      try{
        let test_id = data[0]     
        unittest_parameters.test_id = test_id
        unittest_parameters.multiple_test_ids[test_id] = 1
        console.log(generate_unittest_log('get_test_id_helper'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(get_test_id_helper_1)
    cur_parameters.push('find_test_assistor_unittest')
    Find_Test_Assistor_Wrapper.vm.get_test_id(cur_parameters)
  })
}

function find_test_assistor(){
  test('find_test_assistor',(done) => { 
    let find_test_assistor_1 = (data) => {
      try{
        let task_mode = data[0]
        let model_name = data[1]
        let metric_name = data[2]
        
        expect(task_mode).toEqual(
          unittest_parameters.task_mode
        )
        expect(model_name).toEqual(
          unittest_parameters.model_name
        )
        expect(metric_name).toEqual(
          unittest_parameters.metric_name
        )
 
        console.log(generate_unittest_log('find_test_assistor'))
      }catch (error){
        done(error)
      }
    }
  

    let find_test_assistor_2 = (data) => {
      try{        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'test', unittest_parameters.test_id)
  
        expect(row.test_file_path).toEqual(
          row.test_file_path
        )
        expect(row.test_id_column).toEqual(
          row.test_id_column
        )
        expect(row.test_data_column).toEqual(
          row.test_data_column
        )
        expect(row.test_target_column).toEqual(
          row.test_target_column
        )

        console.log(generate_unittest_log('find_test_assistor'))
      }catch (error){
        done(error)
      }
    }
  
    let find_test_assistor_3 = (data) => {
      try{
        let task_id = data[0].task_id
        let assistor_num = data[0].assistor_num
        let test_id = data[0].test_id
        
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        
        expect(assistor_num).toEqual(
          unittest_parameters.assistor_username_list.split(",").length
        )
        expect(test_id).toEqual(
          unittest_parameters.test_id
        )

        console.log(generate_unittest_log('find_test_assistor'))
        done()
      }catch (error){
        done(error)
      }
    }
  
  
    let cur_parameters = [];
    cur_parameters.push(find_test_assistor_1)
    cur_parameters.push(find_test_assistor_2)
    cur_parameters.push(find_test_assistor_3)
    cur_parameters.push('find_test_assistor_unittest')
    // assistor
    Find_Test_Assistor_Wrapper.setData({task_id: unittest_parameters.task_id,
                                        task_name: unittest_parameters.task_name, 
                                        test_id: unittest_parameters.test_id,
                                        test_description: unittest_parameters.test_description,
                                        test_file_path: unittest_parameters.test_file_path,
                                        test_id_column: unittest_parameters.test_id_column,
                                        test_data_column: unittest_parameters.test_data_column,
                                        test_target_column: unittest_parameters.test_target_column})
                                   
    Find_Test_Assistor_Wrapper.vm.onSubmit(cur_parameters)
  })
}

let find_test_assistor_helper = {}
find_test_assistor_helper.get_test_id = get_test_id_helper
find_test_assistor_helper.find_test_assistor = find_test_assistor

export { find_test_assistor_helper }