import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter, modify_first_been_call} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_test_request(){
  test('unread_test_request', (done) => {
    let unread_test_request_1 = (data) => {
      try{
        let cur_unread_test_request_Testid_dict = data[0]
        let test_id_to_task_id = data[1]
        
        expect(cur_unread_test_request_Testid_dict[unittest_parameters.test_id]).not.toBeNull()
        expect(test_id_to_task_id[unittest_parameters.test_id]).toEqual(
          unittest_parameters.task_id
        )
  
        console.log(generate_unittest_log('unread_test_request'))
      }catch (error){
        console.log(error)
      }
    }
    
    let unread_test_request_2_Manual = (data) => {
      try{
        let add_test_pending_res = data[0]
        
        expect(add_test_pending_res).toEqual(
          'add test pending successfully'
        )

        console.log(generate_unittest_log('unread_test_request'))
        done()
      }catch (error){
        done(error)
      }
    }

    let unread_test_request_2 = (data) => {
      try{
        let test_id = data[0]
        let setting_mode = data[1]
        
        expect(test_id).toEqual(
          unittest_parameters.test_id
        )
  
        expect(setting_mode).toEqual(
          'auto'
        )
  
        console.log(generate_unittest_log('unread_test_request'))
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_request_3 = (data) => {
      try{
        expect(data[0]).toEqual(true)
        console.log(generate_unittest_log('unread_test_request'))
      }catch (error){
        done(error)
      }
    }

    let unread_test_request_4 = (data) => {
      try{
        let match_test_assistor_id_response = data[0].stored
  
        expect(match_test_assistor_id_response).toEqual(
          "assistor test match id stored"
        )

        console.log(generate_unittest_log('unread_test_request'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_test_request_1)
    if (unittest_parameters.default_mode == 'manual'){
      cur_parameters.push(unread_test_request_2_Manual)
    } else if (unittest_parameters.default_mode == 'auto'){
      cur_parameters.push(unread_test_request_2)
      cur_parameters.push(unread_test_request_3)
      cur_parameters.push(unread_test_request_4)
    }
    cur_parameters.push('unread_test_request_unittest')
    Navbar_wrapper.vm.unread_test_request(unittest_parameters.unread_test_request_notification, cur_parameters)
  })
}

let unread_test_request_helper = {}
unread_test_request_helper.unread_test_request = unread_test_request

export { unread_test_request_helper }