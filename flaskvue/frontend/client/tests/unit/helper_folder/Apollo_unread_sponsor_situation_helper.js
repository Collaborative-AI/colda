import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_sponsor_situation_helper_function(){
  test('unread_sponsor_situation_helper', (done) => { 
    let unread_sponsor_situation_1 = (data) => {
      try{
        let situation_dict = data[0]
        console.log('situation_dict', situation_dict)
  
        expect(situation_dict[unittest_parameters.task_id]).not.toBeNull()
        done()
        console.log('unread_sponsor_situation_1')
      }catch (error){
        done(error)
      }
    }
  
    // let unread_sponsor_situation_2 = (data) => {
    //   try{
    //     let row_data = data[0]
  
    //     expect(row_data).not.toBeNull()
    //     done()
    //     console.log('unread_sponsor_situation_2')
    //   }catch (error){
    //     done(error)
    //   }
    // }
  
    // let unread_sponsor_match_id_3 = (data) => {
    //   try{
        
    //     console.log('unread_sponsor_match_id_3')
    //   }catch (error){
    //     done(error)
    //   }
    // }
  
    // let unread_sponsor_match_id_4 = (data) => {
    //   try{
  
    //     let response_data = data[0]
    //     let message = response_data.message
  
    //     expect(message).toEqual(
    //       "send situation successfully!"
    //     )
  
    //     done()
    //     console.log('unread_sponsor_match_id_4')
    //   }catch (error){
    //     done(error)
    //   }
    // }
  
    let cur_parameters = [];
    cur_parameters.push(unread_sponsor_situation_1)
    // cur_parameters.push(unread_sponsor_situation_2)
    // cur_parameters.push(unread_sponsor_match_id_3)
    // cur_parameters.push(unread_sponsor_match_id_4)
    cur_parameters.push('unread_situation_unittest')
    
    Navbar_wrapper.vm.unread_situation(unittest_parameters.unread_situation_notification, cur_parameters)
  })
}



let unread_sponsor_situation_helper = {}

unread_sponsor_situation_helper.unread_sponsor_situation = unread_sponsor_situation_helper_function


export { unread_sponsor_situation_helper }