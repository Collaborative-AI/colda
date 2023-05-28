import { unittest_parameters, generate_unittest_log, Login_wrapper, Plist_Wrapper } from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function get_all_pending_task(){
  test('get_all_pending_task',(done)=>{
    let get_all_pending_task_1 = (data) => {
      try{
        let pending_list = data[0].all_pending_items
        console.log('pending_list', pending_list)
        
        console.log('??', unittest_parameters.multiple_task_ids)

        for (let i = 0; i < pending_list.length; i++){    
          let cur_pend_item = pending_list[i]

          if (cur_pend_item.pending_test_id == undefined){
            console.log('train pending', pending_list[i].pending_task_id)
            expect(unittest_parameters.multiple_task_ids[cur_pend_item.pending_task_id]).not.
              toBeNull()
          } else {
            console.log('test pending', pending_list[i].pending_test_id)
            expect(unittest_parameters.multiple_test_ids[cur_pend_item.pending_test_id]).not.
              toBeNull()
          }
          unittest_parameters.manual_multiple_task.push(cur_pend_item)
        }

        unittest_parameters.multiple_task_ids = {}
        unittest_parameters.multiple_test_ids = {}

        console.log(generate_unittest_log('get_all_pending_task'))
        done()
      }catch (error){
        done(error)
      }
    }

    let cur_parameters = []
    cur_parameters.push(get_all_pending_task_1)
    cur_parameters.push('plist_unittest')
    let user_id = unittest_parameters.user_id.toString()
    // Plist_Wrapper.setData({default_file_path: unittest_parameters.default_file_path[user_id], 
    //                          default_id_column: unittest_parameters.default_id_column[user_id], 
    //                          default_data_column: unittest_parameters.default_data_column[user_id],
    //                          default_model_name: unittest_parameters.default_model_name[user_id],
    //                          sharedState: {'mode': unittest_parameters.default_mode}  })
                             
    Plist_Wrapper.vm.check_if_new_pending(cur_parameters)
  })
}

let plist_helper = {}
// train_helper_functions.login = {}
plist_helper.get_all_pending_task = get_all_pending_task

export { plist_helper }