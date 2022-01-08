import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters } from './Apollo_unittest_utils'
import { retrieve_User_Assistor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_assistor_situation_helper_function(){
  test('unread_assistor_situation_helper', (done) => {
    let unread_assistor_situation_1 = (data) => {
      try{
        let situation_dict = data[0]
        console.log('situation_dict', situation_dict)
  
        expect(situation_dict[unittest_parameters.task_id]).not.toBeNull()
        
        console.log('unread_assistor_situation_1_xxxxx')
        
      }catch (error){
        done(error)
        console.log('unread_assistor_situation_1', error)
      }
    }
  
    let unread_assistor_situation_2 = (data) => {
      try{
        let response = data[0]
        let sender_random_id = response.data.sender_random_id
        let cur_situation_file = response.data.situation
  
        expect(sender_random_id).not.toBeNull()
        expect(cur_situation_file).not.toBeNull()
        console.log('situation33333')

      }catch (error){
        done(error)
        console.log('unread_assistor_situation_2', error)
      }
    }
  
    let unread_assistor_situation_3 = (data) => {
      try{
        expect(data[0]).toEqual(true)
        console.log('situation33333')
      }catch (error){
        done(error)
        console.log('unread_assistor_situation_3', error)
      }
    }

    let unread_assistor_situation_4 = (data) => {
      try{
        let train_file_path = data[0]
        let train_data_column = data[1]
        let mode = data[2]
        let model_name = data[3]
        console.log('situation44444')
        let row = retrieve_User_Assistor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_data_column).toEqual(row.train_data_column)
        expect(mode).toEqual(row.mode)
        expect(model_name).toEqual(row.model_name)
      }catch (error){
        done(error)
        console.log('unread_assistor_situation_4', error)
      }
    }
    
    let unread_assistor_situation_5 = (data) => {
      try{
        let send_output_response = data[0].send_output
  
        expect(send_output_response).toEqual('send output successfully')
        
        done()
        console.log('situation55555')
      }catch (error){
        done(error)
        console.log('unread_assistor_situation_5', error)
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

unread_assistor_situation_helper.unread_assistor_situation = unread_assistor_situation_helper_function

export { unread_assistor_situation_helper }