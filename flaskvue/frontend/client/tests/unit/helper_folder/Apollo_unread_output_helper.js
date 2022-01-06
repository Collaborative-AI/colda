import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_output_helper_function(){
  test('unread_output_helper', (done) => { 
    let unread_output_1 = (data) => {
      try{
        let output_dict = data[0]
        console.log('output_dict', output_dict)
  
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('unread_output_1')
      }catch (error){
        done(error)
      }
    }
  
    let unread_output_2 = (data) => {
      try{
        expect(data).toBe(true)
      }catch (error){
        done(error)
      }
    }
  
    let unread_output_3 = (data) => {
      try{

        let train_file_path = data[0]
        let train_target_column = data[1]
        let task_mode = data[2]
        let metric_name = data[3]
        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_target_column).toEqual(row.train_target_column)
        expect(task_mode).toEqual(row.task_mode)
        expect(metric_name).toEqual(row.metric_name)
        done()
        
      
      }catch (error){
        done(error)
      }
    }
  
    
  
    let cur_parameters = [];
    cur_parameters.push(unread_output_1)
    cur_parameters.push(unread_output_2)
    cur_parameters.push(unread_output_3)
    cur_parameters.push('unread_output_unittest')
    

    Navbar_wrapper.vm.unread_output(unittest_parameters.unread_output_notification, cur_parameters)
  })
}
let unread_output_helper = {}
unread_output_helper.unread_output = unread_output_helper_function

export { unread_output_helper }
