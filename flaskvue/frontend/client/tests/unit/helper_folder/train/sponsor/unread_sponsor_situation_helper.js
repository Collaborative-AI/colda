import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_sponsor_situation(){
  test('unread_sponsor_situation', () => { 
    let unread_sponsor_situation_1 = (data) => {
      try{
        let situation_dict = data[0]
        expect(situation_dict[unittest_parameters.task_id]).not.toBeNull()
        
        console.log(generate_unittest_log('unread_sponsor_situation'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_sponsor_situation_2 = (data) => {
      try{
        let train_file_path = data[0]
        let train_data_column = data[1]
        let model_name = data[2]
        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_data_column).toEqual(row.train_data_column)
        expect(model_name).toEqual(row.model_name)

        console.log(generate_unittest_log('unread_sponsor_situation'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_sponsor_situation_3 = (data) => {
      try{
        let indicator = data[0]
        expect(indicator).toEqual(true)

        console.log(generate_unittest_log('unread_sponsor_situation'))
      }catch (error){
        console.log(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_sponsor_situation_1)
    cur_parameters.push(unread_sponsor_situation_2)
    cur_parameters.push(unread_sponsor_situation_3)
    cur_parameters.push('unread_situation_unittest')
    
    Navbar_wrapper.vm.unread_situation(unittest_parameters.unread_situation_notification, cur_parameters)
  })
}

let unread_sponsor_situation_helper = {}
unread_sponsor_situation_helper.unread_sponsor_situation = unread_sponsor_situation

export { unread_sponsor_situation_helper }