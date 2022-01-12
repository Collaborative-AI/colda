import { unittest_parameters, generate_unittest_log, Login_wrapper, PendItem_Wrapper } from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function train_accept(){
  test('train_accept',(done)=>{
    let train_accept_1 = (data) => {
      try{
        
        console.log(generate_unittest_log('train_accept'))
      }catch (error){
        console.log(error)
      }
    }

    let train_accept_2 = (data) => {
      try{

        console.log(generate_unittest_log('train_accept'))
      }catch (error){
        done(error)
      }
    }

    let train_accept_3 = (data) => {
      try{
        let delete_pending_res = data[0]

        expect(delete_pending_res).toEqual(
          'Sucessfully delete'
        )
        
        console.log(generate_unittest_log('train_accept'))
      }catch (error){
        done(error)
      }
    }

    let train_accept_4 = (data) => {
      try{
        let match_assistor_id_res = data[0]
        let stored = match_assistor_id_res['stored']
        let task_id = match_assistor_id_res['task_id']

        expect(stored).toEqual(
          "assistor match id stored"
        )
        expect(unittest_parameters.multiple_task_ids[task_id]).not.toBeNull()
        
        console.log(generate_unittest_log('train_accept'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(train_accept_1)
    cur_parameters.push(train_accept_2)
    cur_parameters.push(train_accept_3)
    cur_parameters.push(train_accept_4)
    cur_parameters.push('PendItem_unittest')
    
    let user_id = unittest_parameters.user_id.toString()
    for (let i = 0; i < unittest_parameters.manual_multiple_task.length; i++){
      let cur_task = unittest_parameters.manual_multiple_task[i]
      console.log('cur+task', cur_task, user_id)
      PendItem_Wrapper.setData({task_description: cur_task.pending_task_description,
                                task_id: cur_task.pending_task_id, 
                                task_name: cur_task.pending_task_name,
                                task_mode: cur_task.pending_task_mode,
                                model_name: cur_task.pending_model_name,
                                metric_name: cur_task.pending_metric_name,
                                test_id: cur_task.pending_test_id,
                                test_indicator: cur_task.pending_test_indicator,
                                test_description: cur_task.pending_test_description,
                                manual_file_path: unittest_parameters.default_file_path[user_id], 
                                manual_id_column: unittest_parameters.default_id_column[user_id], 
                                manual_data_column: unittest_parameters.default_data_column[user_id],
                                ptitles: unittest_parameters.assistor_ptitles})
      PendItem_Wrapper.vm.Accept(cur_parameters)
    }
    unittest_parameters.manual_multiple_task = []  
  })
}

function test_accept(){
  test('test_accept',(done)=>{
    let test_accept_1 = (data) => {
      try{
        
        console.log(generate_unittest_log('test_accept'))
      }catch (error){
        done(error)
      }
    }

    let test_accept_2 = (data) => {
      try{
        
        console.log(generate_unittest_log('test_accept'))
      }catch (error){
        done(error)
      }
    }

    let test_accept_3 = (data) => {
      try{
        let delete_pending_res = data[0]

        expect(delete_pending_res).toEqual(
          'Sucessfully delete'
        )
        
        console.log(generate_unittest_log('test_accept'))
      }catch (error){
        done(error)
      }
    }

    let test_accept_4 = (data) => {
      try{
        let match_test_assistor_id_res = data[0]
        let stored = match_test_assistor_id_res['stored']
        let test_id = match_test_assistor_id_res['test_id']

        expect(stored).toEqual(
          "assistor test match id stored"
        )
        expect(unittest_parameters.multiple_task_ids[test_id]).not.toBeNull()
        
        console.log(generate_unittest_log('test_accept'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(test_accept_1)
    cur_parameters.push(test_accept_2)
    cur_parameters.push(test_accept_3)
    cur_parameters.push(test_accept_4)
    cur_parameters.push('PendItem_unittest')

    let user_id = unittest_parameters.user_id.toString()
    for (let i = 0; i < unittest_parameters.manual_multiple_task.length; i++){
      let cur_task = unittest_parameters.manual_multiple_task[i]
      if (cur_task.pending_test_indicator == 'test'){
        console.log('testcurtask', cur_task.pending_test_indicator)
        PendItem_Wrapper.setData({task_description: cur_task.pending_task_description,
                                  task_id: cur_task.pending_task_id, 
                                  task_name: cur_task.pending_task_name,
                                  task_mode: cur_task.pending_task_mode,
                                  model_name: cur_task.pending_model_name,
                                  metric_name: cur_task.pending_metric_name,
                                  test_id: cur_task.pending_test_id,
                                  test_indicator: cur_task.pending_test_indicator,
                                  test_description: cur_task.pending_test_description,
                                  manual_file_path: unittest_parameters.default_file_path[user_id], 
                                  manual_id_column: unittest_parameters.default_id_column[user_id], 
                                  manual_data_column: unittest_parameters.default_data_column[user_id],
                                  ptitles: unittest_parameters.assistor_ptitles})
        PendItem_Wrapper.vm.Accept(cur_parameters)
      }
    }   
    unittest_parameters.manual_multiple_task = []
  })
}

function manual_reject(){
  test('manual_reject',(done)=>{
    let manual_reject_1 = (data) => {
      try{
        let delete_pending = data[0]
        expect(delete_pending).toEqual(
          'Sucessfully delete'
        )

        console.log(generate_unittest_log('manual_reject'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(manual_reject_1)
    cur_parameters.push('PendItem_unittest')
    // let user_id = unittest_parameters.user_id.toString()
   
    for (let i = 0; i < unittest_parameters.manual_multiple_task.length; i++){
      let cur_task = unittest_parameters.manual_multiple_task[i]
      PendItem_Wrapper.setData({task_id: cur_task.pending_task_id, 
                                test_id: cur_task.pending_test_id,
                                test_indicator: cur_task.pending_test_indicator })
      PendItem_Wrapper.vm.Reject(cur_parameters)
    }
  })
}

let PendItem_helper = {}
// train_helper_functions.login = {}

PendItem_helper.train_accept = train_accept
PendItem_helper.test_accept = test_accept
PendItem_helper.reject = manual_reject

export { PendItem_helper }