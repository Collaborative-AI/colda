import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Profile_wrapper } from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record, retrieve_User_Assistor_Table_record, retrieve_User_Default_Table_record } from './Apollo_unittest_utils'
jest.setTimeout(10000);

function check_profile_onSubmit_db(){
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
    Profile_wrapper.setData({default_file_path: unittest_parameters.default_file_path, 
                             default_id_column: unittest_parameters.default_id_column, 
                             default_data_column: unittest_parameters.default_data_column,
                             default_model_name: unittest_parameters.model_name,
                             sharedState: {'mode':'auto'}  })
    Profile_wrapper.vm.onSubmit(cur_parameters)
  })
}

let profile_helper = {}
// train_helper_functions.login = {}

profile_helper.onSubmit = check_profile_onSubmit_db


export { profile_helper }