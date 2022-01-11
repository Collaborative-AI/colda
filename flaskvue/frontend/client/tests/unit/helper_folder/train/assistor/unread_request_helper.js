import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter, modify_first_been_call} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_request(){
  test('unread_request', (done) => {

    let unread_request_1 = (data) => {
      try{
        let request_dict = data[0]  
        expect(request_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_request'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_request_2 = (data) => {
      try{
        let task_id = data[0]
        let setting_mode = data[1]

        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
  
        expect(setting_mode).toEqual(
          'auto'
        )
  
        console.log(generate_unittest_log('unread_request'))
      }catch (error){
        console.log(error)
      }
    }

    let unread_request_2_Manual = (data) => {
      try{
        let add_train_pending_res = data[0]

        expect(add_train_pending_res).toEqual(
          'add train pending successfully'
        )
  
        console.log(generate_unittest_log('unread_request'))
        done()
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_request_3 = (data) => {
      try{
        console.log(generate_unittest_log('unread_request'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_request_4 = (data) => {
      try{
        let stored = data[0].stored
        let task_id = data[0].task_id
  
        expect(stored).toEqual(
          'assistor match id stored'
        )
  
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        console.log(generate_unittest_log('unread_request'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_request_1)
    if (unittest_parameters.default_mode == 'manual'){
      cur_parameters.push(unread_request_2_Manual)
    } else if (unittest_parameters.default_mode == 'auto'){
      cur_parameters.push(unread_request_2)
      cur_parameters.push(unread_request_3)
      cur_parameters.push(unread_request_4)
    }
    cur_parameters.push('unread_request_unittest')

    Navbar_wrapper.vm.unread_request(unittest_parameters.unread_request_notification, cur_parameters)    
  })
}

let unread_request_helper = {}
unread_request_helper.unread_request = unread_request

export { unread_request_helper }