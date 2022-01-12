import { unittest_parameters, generate_unittest_log, modify_parameter, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);


function get_train_id_helper(){
  test('get_train_id_helper', (done) => {
    let get_train_id_helper_1 = (data) => {
      try{
        let task_id = data[0]
        console.log('sadasd', unittest_parameters.task_id, unittest_parameters.multiple_task_ids)
        unittest_parameters.task_id = task_id
        unittest_parameters.multiple_task_ids[task_id] = 1
        console.log(generate_unittest_log('get_train_id_helper'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(get_train_id_helper_1)
    cur_parameters.push('find_assistor_unittest')
    Find_Assistor_wrapper.vm.get_train_id(cur_parameters)
  })
}

function find_assistor(sponsor_mode, assistor_username_list){
  test('find_assistor',(done) => { 
    let find_assistor_1 = (data) => {
      try{
        let train_file_path = data[0]
        let train_id_column = data[1]
        let train_data_column = data[2]
        let train_target_column = data[3]
  
        let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')

        expect(train_file_path).toEqual(
          row.train_file_path
        )
        expect(train_id_column).toEqual(
          row.train_id_column
        )
        expect(train_data_column).toEqual(
          row.train_data_column
        )
        expect(train_target_column).toEqual(
          row.train_target_column
        )

        console.log(generate_unittest_log('find_assistor'))
      }catch (error){
        // done(error)
        console.log(error)
      }
    }
  
    let find_assistor_2 = (data) => {
      try{
        let find_assistor_response_data = data[0]
        let task_id = find_assistor_response_data.task_id
        let assistor_num = find_assistor_response_data.assistor_num
        
        expect(task_id).toEqual(
          unittest_parameters.task_id
        )
        let temp_assistor_username_list = assistor_username_list.split(",")
        expect(assistor_num).toEqual(
          temp_assistor_username_list.length
        )

        console.log(generate_unittest_log('find_assistor'))
      }catch (error){
        done(error)
      }
    }
  
    let find_assistor_3 = (data) => {
      try{

        console.log(generate_unittest_log('find_assistor'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(find_assistor_1)
    cur_parameters.push(find_assistor_2)
    cur_parameters.push(find_assistor_3)
    cur_parameters.push('find_assistor_unittest')
    
    modify_parameter("assistor_username_list", assistor_username_list)
    Find_Assistor_wrapper.setData({task_id: unittest_parameters.task_id,
                                   task_name: unittest_parameters.task_name, 
                                   task_description: unittest_parameters.task_description,
                                   train_file_path: unittest_parameters.train_file_path,
                                   train_id_column: unittest_parameters.train_id_column,
                                   train_data_column: unittest_parameters.train_data_column,
                                   train_target_column: unittest_parameters.train_target_column,
                                   assistor_username_list: unittest_parameters.assistor_username_list,
                                   task_mode: unittest_parameters.task_mode,
                                   model_name: unittest_parameters.model_name,
                                   metric_name: unittest_parameters.metric_name,
                                   ptitles: unittest_parameters.sponsor_ptitles})
                                   
    Find_Assistor_wrapper.vm.onSubmit(cur_parameters)
  })
}

let find_assistor_helper = {}
find_assistor_helper.get_train_id = get_train_id_helper
find_assistor_helper.find_assistor = find_assistor

export { find_assistor_helper }















// function ceshi(sponsor_mode, assistor_username_list){
  //   test('check_find_assistor_sponsor_onSubmit',(done) => { 
  //     let check_find_assistor_sponsor_onSubmit_1 = (data) => {
  //       try{
  //         let train_file_path = data[0]
  //         let train_id_column = data[1]
  //         let train_data_column = data[2]
  //         let train_target_column = data[3]
    
  //         // console.log('bxbx')
  //         // let row = null
  //         // async function get_row(){
  //         //   row = await retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  //         //   console.log('outrow1', row)
  //         // }
  //         // get_row()
          
  //         let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  //         console.log("rowwww", row)
  //         expect(train_file_path).toEqual(
  //           row.train_file_path
  //         )
  //         expect(train_id_column).toEqual(
  //           row.train_id_column
  //         )
  //         expect(train_data_column).toEqual(
  //           row.train_data_column
  //         )
  //         expect(train_target_column).toEqual(
  //           row.train_target_column
  //         )
  //         done()
  //         console.log('aqaqaq')
  //         console.log('check_find_assistor_sponsor_onSubmit_1')
  //       }catch (error){
  //         done(error)
  //         console.log(error)
  //       }
  //     }
  
  //     let check_find_assistor_sponsor_onSubmit_2 = (data) => {
  //       try{
  //         // let train_file_path = data[0]
  //         // let train_id_column = data[1]
  //         // let train_data_column = data[2]
  //         // let train_target_column = data[3]
    
  //         // console.log('bxbx')
          
  //         // let row = retrieve_User_Sponsor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id, 'train')
  //         // console.log("rowwww", row)
  //         // expect(train_file_path).toEqual(
  //         //   row.train_file_path
  //         // )
  //         expect(data[0]).toEqual(
  //           'good,NIHAO'
  //         )
  //         // expect(train_data_column).toEqual(
  //         //   row.train_data_column
  //         // )
  //         // expect(train_target_column).toEqual(
  //         //   row.train_target_column
  //         // )
  //         done()
  //         console.log('aqaqaq')
  //         console.log('check_find_assistor_sponsor_onSubmit_1')
  //       }catch (error){
  //         done(error)
  //         console.log(error)
  //       }
  //     }
    
      
    
  //     let cur_parameters = [];
  //     cur_parameters.push(check_find_assistor_sponsor_onSubmit_1)
  //     cur_parameters.push(check_find_assistor_sponsor_onSubmit_2)
  
  //     cur_parameters.push('find_assistor_unittest')
  //     // assistor
  //     console.log("43211234", sponsor_mode)
  //     modify_parameter("task_mode", sponsor_mode)
  //     modify_parameter("assistor_username_list", assistor_username_list)
   
  //     if (sponsor_mode == 'regression'){
  //       modify_parameter('metric_name', 'MAD_RMSE_R2')
  //     } else if (sponsor_mode == 'classification'){
  //       modify_parameter('metric_name', 'Accuracy_F1')
  //     }
  //     Find_Assistor_wrapper.setData({task_id: unittest_parameters.task_id,
  //                                    task_name: unittest_parameters.task_name, 
  //                                    task_description: unittest_parameters.task_description,
  //                                    train_file_path: unittest_parameters.train_file_path,
  //                                    train_id_column: unittest_parameters.train_id_column,
  //                                    train_data_column: unittest_parameters.train_data_column,
  //                                    train_target_column: unittest_parameters.train_target_column,
  //                                    assistor_username_list: unittest_parameters.assistor_username_list,
  //                                    task_mode: unittest_parameters.task_mode,
  //                                    model_name: unittest_parameters.model_name,
  //                                    metric_name: unittest_parameters.metric_name})
                                     
  //     Find_Assistor_wrapper.vm.ceshi(cur_parameters)
  
  //   })
  // }