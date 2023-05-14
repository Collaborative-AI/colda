import { unittest_parameters, router, generate_unittest_log, Login_wrapper, Reset_wrapper, Navbar_wrapper, Find_Assistor_wrapper, modify_parameter} from './Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from './Apollo_unittest_utils'

jest.setTimeout(10000);

function forgot_password(){
    test('forgot_password', (done) => {
        let forgot_password_1 = (data) => {
            try{
                // console.log('dachu',data)
                let message = data[0].message
                expect(message).toEqual(
                    'A password reset email has been sent via email.'
                  )
                done()
            }catch(error){
                done(error)
            }
        }
        let cur_parameters = []
        cur_parameters.push(forgot_password_1)
        cur_parameters.push('forgot_password_unittest')
        
        
        Reset_wrapper.setData({resetForm: {username: unittest_parameters.first_user_username, 
                                        email: unittest_parameters.first_user_email}, 
                                        verifivation_res: unittest_parameters.verification_res})
        Reset_wrapper.setData({verifivation_res: true})
        console.log('veri res is', unittest_parameters.verification_res)
        Reset_wrapper.vm.onSubmit(cur_parameters)
        
        
    })
}

let reset_helper = {}
reset_helper.forgot_password = forgot_password



export { reset_helper }