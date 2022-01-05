import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_assistor_situation_helper_function(){
  test('unread_assistor_situation_helper', (done) => {
    let unread_assistor_situation_1 = (data) => {
      try{
        let situation_dict = data[0]
        console.log('situation_dict', situation_dict)
  
        expect(situation_dict[unittest_parameters.task_id]).not.toBeNull()
        done()
        console.log('unread_assistor_situation_1')
        
      }catch (error){
        done(error)
      }
    }
  
    // let unread_assistor_match_id_2 = (data) => {
    //   try{
    //     let response_data = data[0]
    //     let match_id_file = response_data.match_id_file
    //     let assistor_random_id_pair = response_data.assistor_random_id_pair
    //     // let row = retrieve_User_assistor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
    //     expect(match_id_file).not.toBeNull()
    //     expect(assistor_random_id_pair).not.toBeNull()
        
    //     console.log('unread_assistor_match_id_2')
    //   }catch (error){
    //     done(error)
    //   }
    // }
  
    // let unread_assistor_match_id_3 = (data) => {
    //   try{
        
    //     console.log('unread_assistor_match_id_3')
    //     done()
    //   }catch (error){
    //     done(error)
    //   }
    // }
  
    let cur_parameters = [];
    cur_parameters.push(unread_assistor_situation_1)
    // cur_parameters.push(unread_assistor_situation_2)
    // cur_parameters.push(unread_assistor_situation_3)
    cur_parameters.push('unread_situation_unittest')
    
    Navbar_wrapper.vm.unread_situation(unittest_parameters.unread_situation_notification, cur_parameters)
  })
}

let unread_assistor_situation_helper = {}

unread_assistor_situation_helper.unread_assistor_situation = unread_assistor_situation_helper_function

export { unread_assistor_situation_helper }