import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Profile_wrapper } from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function check_profile_onSubmit_db(default_mode){
  test('check_profile_onSubmit_db',(done)=>{
    let check_profile_onSubmit_db = (data) => {
      try{
        console.log('woshidata',data)
        let default_file_path = data[0] 
        let default_id_column = data[1]
        let default_data_column = data[2]
        console.log('user_id3', unittest_parameters.user_id)
        let row = retrieve_User_Default_Table_record(unittest_parameters.user_id)
        console.log('rowshi', row)
        expect(default_file_path).toEqual(
          row.default_file_path
        )
        expect(default_id_column).toEqual(
          row.default_id_column
        )
        expect(default_data_column).toEqual(
          row.default_data_column
        )
  
        done()
      }catch (error){
        done(error)
      }
    }
  
    // let login_parameters = generate_parameters(train_callback_functions.login)
    let cur_parameters = []
    cur_parameters.push(check_profile_onSubmit_db)
    cur_parameters.push('profile_unittest')
    // sponsor
    if (default_mode != undefined){
      unittest_parameters.default_mode = default_mode
    }
    let user_id = unittest_parameters.user_id.toString()
    Profile_wrapper.setData({default_file_path: unittest_parameters.default_file_path[user_id], 
                             default_id_column: unittest_parameters.default_id_column[user_id], 
                             default_data_column: unittest_parameters.default_data_column[user_id],
                             default_model_name: unittest_parameters.default_model_name[user_id],
                             sharedState: {'mode': unittest_parameters.default_mode}  })
                             
    console.log('zzz997', unittest_parameters.default_mode, unittest_parameters.default_file_path[user_id],  unittest_parameters.default_id_column[user_id], unittest_parameters.default_data_column[user_id], unittest_parameters.default_model_name[user_id])
    console.log('zzz996', unittest_parameters.default_file_path, typeof(user_id),user_id)
    Profile_wrapper.vm.onSubmit(cur_parameters)
  })
}

let profile_helper = {}
// train_helper_functions.login = {}

profile_helper.onSubmit = check_profile_onSubmit_db


export { profile_helper }