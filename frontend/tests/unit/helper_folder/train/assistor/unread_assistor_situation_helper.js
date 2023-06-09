import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters } from '../../Apollo_unittest_utils'
import { retrieve_User_Assistor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_assistor_situation(){
  test('unread_assistor_situation', (done) => {
    let unread_assistor_situation_1 = (data) => {
      try{
        let situation_dict = data[0]  
        expect(situation_dict[unittest_parameters.task_id]).not.toBeNull()
        
        console.log(generate_unittest_log('unread_assistor_situation'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_assistor_situation_2 = (data) => {
      try{
        let response = data[0]
        let sender_random_id = response.data.sender_random_id
        let cur_situation_file = response.data.situation
  
        expect(sender_random_id).not.toBeNull()
        expect(cur_situation_file).not.toBeNull()
        
        console.log(generate_unittest_log('unread_assistor_situation'))
      }catch (error){
        done(error)
      }
    }
  
    let unread_assistor_situation_3 = (data) => {
      try{
        expect(data[0]).toEqual(true)
        console.log(generate_unittest_log('unread_assistor_situation'))
      }catch (error){
        done(error)
      }
    }

    let unread_assistor_situation_4 = (data) => {
      try{
        let train_file_path = data[0]
        let train_data_column = data[1]
        let mode = data[2]
        let model_name = data[3]

        let row = retrieve_User_Assistor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_data_column).toEqual(row.train_data_column)
        expect(mode).toEqual(row.mode)
        expect(model_name).toEqual(row.model_name)
        console.log(generate_unittest_log('unread_assistor_situation'))
      }catch (error){
        done(error)
      }
    }
    
    let unread_assistor_situation_5 = (data) => {
      try{
        let send_output_response = data[0].send_output
        expect(send_output_response).toEqual('send output successfully')
        
        console.log(generate_unittest_log('unread_assistor_situation'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = [];
    cur_parameters.push(unread_assistor_situation_1)
    cur_parameters.push(unread_assistor_situation_2)
    cur_parameters.push(unread_assistor_situation_3)
    cur_parameters.push(unread_assistor_situation_4)
    cur_parameters.push(unread_assistor_situation_5)
    cur_parameters.push('unread_situation_unittest')
    
    Navbar_wrapper.vm.unread_situation(unittest_parameters.unread_situation_notification, cur_parameters)
  })
}

let unread_assistor_situation_helper = {}

unread_assistor_situation_helper.unread_assistor_situation = unread_assistor_situation

export { unread_assistor_situation_helper }