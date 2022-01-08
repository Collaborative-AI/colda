import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_output_helper_function(current_round, max_round){
  test('unread_output_helper', (done) => { 
    let unread_output_1 = (data) => {
      try{
        let output_dict = data[0]
        console.log('output_dict', output_dict)
  
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('unread_output_1')
      }catch (error){
        done(error)
        console.log('Error: unread_output_1', error)
      }
    }
  
    let unread_output_2 = (data) => {
      try{
        expect(data[0]).toBe(true)
        console.log('unread_output_2')
      }catch (error){
        done(error)
        console.log('Error: unread_output_2', error)
      }
    }
  
    let unread_output_3 = (data) => {
      try{

        let train_file_path = data[0]
        let train_target_column = data[1]
        let task_mode = data[2]
        let metric_name = data[3]
        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_target_column).toEqual(row.train_target_column)
        expect(task_mode).toEqual(row.task_mode)
        expect(metric_name).toEqual(row.metric_name)
        console.log('unread_output_3')
        // done()
      }catch (error){
        done(error)
        console.log('Error: unread_output_3', error)
      }
    }
    let unread_output_3_done = (data) => {
      try{

        let train_file_path = data[0]
        let train_target_column = data[1]
        let task_mode = data[2]
        let metric_name = data[3]
        
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  
        expect(train_file_path).toEqual(row.train_file_path)
        expect(train_target_column).toEqual(row.train_target_column)
        expect(task_mode).toEqual(row.task_mode)
        expect(metric_name).toEqual(row.metric_name)
        console.log('unread_output_3')
        done()
      }catch (error){
        done(error)
        console.log('Error: unread_output_3', error)
      }
    }
  
    let unread_output_4 = (data) => {
      try{
        let send_situation_response = data[0].message
        console.log('unread_output_4')
        expect(send_situation_response).toEqual(
          "send situation successfully!"
        )
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_output_1)
    cur_parameters.push(unread_output_2)
    
    if (current_round >= max_round){
      console.log('666666')
      cur_parameters.push(unread_output_3_done)
    } else{
      cur_parameters.push(unread_output_3)
      cur_parameters.push(unread_output_4)
    }
    cur_parameters.push('unread_output_unittest')
    
    console.log('sada', current_round, max_round)
    modify_parameter("max_round", max_round)
    Navbar_wrapper.setData({max_round: unittest_parameters.max_round})
    Navbar_wrapper.vm.unread_output(unittest_parameters.unread_output_notification, cur_parameters)
  })
}
let unread_output_helper = {}
unread_output_helper.unread_output = unread_output_helper_function

export { unread_output_helper }
