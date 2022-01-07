import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter, modify_first_been_call} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function check_unread_test_request(){
  test('check_unread_test_request', (done) => {
    let check_unread_test_request_1 = (data) => {
      try{
        let test_request_dict = data[0]
        console.log('test_request_dict', test_request_dict)
  
        expect(request_dict[unittest_parameters.test_id]).not.toBeNull()
  
        console.log('check_unread_test_request')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_test_request_2 = (data) => {
      try{
        let test_id = data[0]
        let setting_mode = data[1]
        // let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(test_id).toEqual(
          unittest_parameters.test_id
        )
  
        expect(setting_mode).toEqual(
          'auto'
        )
  
        console.log('check_unread_test_request_2')
      }catch (error){
        done(error)
      }
    }
  
    let check_unread_test_request_3 = (data) => {
      try{
        expect(data[0]).toEqual(true)
        console.log('check_unread_test_request_3')
      }catch (error){
        done(error)
      }
    }


    let check_unread_test_request_1 = (data) => {
      try{
        console.log('woshidata', data)
  
        expect(data).not.toBeNull()
  
        console.log('check_unread_test_request')
      }catch (error){
        done(error)
      }
    }
  
  
    let cur_parameters = [];
    cur_parameters.push(check_unread_test_request_1)
    cur_parameters.push(check_unread_test_request_2)
    cur_parameters.push(check_unread_test_request_3)
    cur_parameters.push(check_unread_test_request_4)
    cur_parameters.push('unread_test_request_unittest')
    console.log('wokan', cur_parameters)
    
    console.log('zz8', unittest_parameters)
    console.log('zz5', unittest_parameters.unread_request_notification)
    Navbar_wrapper.vm.unread_request(unittest_parameters.unread_test_request_notification, cur_parameters)
    
    
  
  })
}

let unread_test_request_helper = {}

unread_test_request_helper.unread_test_request = check_unread_test_request

export { unread_test_request_helper }