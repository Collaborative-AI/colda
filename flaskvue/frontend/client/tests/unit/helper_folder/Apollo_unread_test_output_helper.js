import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_test_output_helper_function(){
  test('unread_output_helper', (done) => { 
    let unread_test_output_1 = (data) => {
      try{
        let output_dict = data[0]
        console.log('output_dict', output_dict)
  
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('unread_output_1')
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_output_2 = (data) => {
      try{
        expect(data).toBe(true)
        done()
      }catch (error){
        done(error)
      }
    }
  
  
    
  
    let cur_parameters = [];
    cur_parameters.push(unread_test_output_1)
    cur_parameters.push(unread_test_output_2)
    cur_parameters.push('unread_test_output_unittest')
    

    Navbar_wrapper.vm.unread_test_output(unittest_parameters.unread_output_notification, cur_parameters)
  })
}
let unread_test_output_helper = {}
unread_test_output_helper.unread_test_output = unread_test_output_helper_function

export { unread_test_output_helper }
