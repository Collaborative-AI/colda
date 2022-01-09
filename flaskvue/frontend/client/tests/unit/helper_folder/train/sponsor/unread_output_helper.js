import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_output(current_round, max_round){
  test('unread_output', (done) => { 
    let unread_output_1 = (data) => {
      try{
        let output_dict = data[0]
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_output'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_output_2 = (data) => {
      try{
        expect(data[0]).toBe(true)

        console.log(generate_unittest_log('unread_output'))
      }catch (error){
        done(error)
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

        console.log(generate_unittest_log('unread_output'))
      }catch (error){
        done(error)
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
        
        console.log(generate_unittest_log('unread_output'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let unread_output_4 = (data) => {
      try{
        let send_situation_response = data[0].message
        
        expect(send_situation_response).toEqual(
          "send situation successfully!"
        )

        console.log(generate_unittest_log('unread_output'))
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
    
    modify_parameter("max_round", max_round)
    Navbar_wrapper.setData({max_round: unittest_parameters.max_round})
    Navbar_wrapper.vm.unread_output(unittest_parameters.unread_output_notification, cur_parameters)
  })
}

let unread_output_helper = {}
unread_output_helper.unread_output = unread_output

export { unread_output_helper }
