import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_test_output_helper_function(){
  test('unread_output_helper', (done) => { 
    let unread_test_output_1 = (data) => {
      try{
        let output_dict = data[0]
        console.log('output_dict', output_dict)
  
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log('unread_output_1')
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_output_2 = (data) => {
      try{
        expect(data[0]).toBe(true)
        // done()
      }catch (error){
        done(error)
      }
    }

    let unread_test_output_3 = (data) => {
      try{
        console.log('gfds', data)
        data = data[0]
        let test_dict = {
          "1": {
            "MAD": 3.54763,
            "RMSE": 5.21270,
            "R2": 0.46997,
          },
          "2": {
            "MAD": 3.54221,
            "RMSE": 5.19744,
            "R2": 0.45141,
          }
        }
        
        for (let i in data){
          let cur_running_res = data[i]
          let cur_testing_dict = test_dict[i]
          for (let j in cur_running_res){
            let cur_number = cur_running_res[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            console.log('spo_eval', cur_number, cur_testing_dict[j])
            expect(cur_number).toEqual(
              cur_testing_dict[j]
            )
          }
        }

        console.log('unread_test_output_3')

      }catch (error){
        done(error)
      }
    }
    

    let unread_test_output_4 = (data) => {
      try{
        console.log('unread_test_output_4')
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_test_output_1)
    cur_parameters.push(unread_test_output_2)
    cur_parameters.push(unread_test_output_3)
    cur_parameters.push(unread_test_output_4)
    cur_parameters.push('unread_test_output_unittest')
    
    Navbar_wrapper.vm.unread_test_output(unittest_parameters.unread_test_output_notification, cur_parameters)
  })
}
let unread_test_output_helper = {}
unread_test_output_helper.unread_test_output = unread_test_output_helper_function

export { unread_test_output_helper }
