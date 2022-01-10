import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_assistor_match_id(){
  test('unread_assistor_match_id', (done) => {
    let unread_assistor_match_id_1 = (data) => {
      try{
        let match_id_dict = data[0]
  
        expect(match_id_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_assistor_match_id'))
      }catch (error){
        console.log(error)
      }

    }
  
    let unread_assistor_match_id_2 = (data) => {
      try{
        let response_data = data[0]
        let match_id_file = response_data.match_id_file
        let assistor_random_id_pair = response_data.assistor_random_id_pair
  
        expect(match_id_file).not.toBeNull()
        expect(assistor_random_id_pair).not.toBeNull()
        
        console.log(generate_unittest_log('unread_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }
  
    let unread_assistor_match_id_3 = (data) => {
      try{
        
        console.log(generate_unittest_log('unread_assistor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = [];
    cur_parameters.push(unread_assistor_match_id_1)
    cur_parameters.push(unread_assistor_match_id_2)
    cur_parameters.push(unread_assistor_match_id_3)
    cur_parameters.push('unread_match_id_unittest')
    Navbar_wrapper.vm.unread_match_id(unittest_parameters.unread_match_id_notification, cur_parameters)
  })
}

let unread_assistor_match_id_helper = {}
unread_assistor_match_id_helper.unread_assistor_match_id = unread_assistor_match_id

export { unread_assistor_match_id_helper }