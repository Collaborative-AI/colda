import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper} from '../../Apollo_unittest_init'
import { generate_parameters } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_test_assistor_match_id(sponsor_mode, assistor_mode, verify_algo){
  test('unread_test_assistor_match_id', (done) => {
    let unread_test_assistor_match_id_1 = (data) => {
      try{
        let test_match_id_dict = data[0]
        expect(test_match_id_dict[unittest_parameters.test_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_test_assistor_match_id_2 = (data) => {
      try{
        let response_data = data[0]
        let match_id_file = response_data.match_id_file
        let assistor_random_id_pair = response_data.assistor_random_id_pair
        
        expect(match_id_file).not.toBeNull()
        expect(assistor_random_id_pair).not.toBeNull()
        
        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_assistor_match_id_3 = (data) => {
      try{
        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }

    let unread_test_assistor_match_id_4 = (data) => {
      try{
        let test_file_path = data[0]
        let test_data_column = data[1]

        expect(test_file_path).toEqual(
          unittest_parameters.default_file_path
        )
        
        expect(test_data_column).toEqual(
          unittest_parameters.default_data_column
        )
        
        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }
    
    // sponsor: regression and assistor: regression
    let unread_test_assistor_match_id_regression_regression = (data) => {
      try{
        data = data[0]
        
        let test_array = [3.93492, -1.96598, -19.51288, 6.83615, -0.52504, -0.75834, -1.23748, -0.11017]
        let test_array_index = 0
        for (let i in data){
          let cur_list = data[i]
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            console.log('number_ass', cur_number, test_array[test_array_index])
            expect(cur_number).toEqual(
              test_array[test_array_index]
            )
            test_array_index += 1
          }
        }

        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }

    // sponsor: classification and assistor: regression
    let unread_test_assistor_match_id_classification_regression = (data) => {
      try{
        data = data[0]

        let test_array = [-0.40470, -0.41815, -0.19339, -0.38235, -0.00117, -0.00157, -0.00024, -0.00451]
        let test_array_index = 0
        for (let i in data){
          let cur_list = data[i]
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            console.log('number_ass', cur_number, test_array[test_array_index])
            expect(cur_number).toEqual(
              test_array[test_array_index]
            )
            test_array_index += 1
          }
        }

        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }

    let unread_test_assistor_match_id_multiple_assistors = (data) => {
      try{
        
        console.log(generate_unittest_log('unread_test_assistor_match_id'))
      }catch (error){
        done(error)
      }
    }

    let unread_test_assistor_match_id_6 = (data) => {
      try{
        let send_test_output_res = data[0].send_test_output
        expect(send_test_output_res).toEqual(
          "send test output successfully"
        )

        console.log(generate_unittest_log('unread_test_assistor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_test_assistor_match_id_1)
    cur_parameters.push(unread_test_assistor_match_id_2)
    cur_parameters.push(unread_test_assistor_match_id_3)
    cur_parameters.push(unread_test_assistor_match_id_4)
    if (verify_algo == true){
      if (sponsor_mode == 'regression'){
        cur_parameters.push(unread_test_assistor_match_id_regression_regression)
      } else if (sponsor_mode == 'classification'){
        cur_parameters.push(unread_test_assistor_match_id_classification_regression)
      }
    } else {
      cur_parameters.push(unread_test_assistor_match_id_multiple_assistors)
    }
    
    cur_parameters.push(unread_test_assistor_match_id_6)
    cur_parameters.push('unread_test_match_id_unittest')

    Navbar_wrapper.vm.unread_test_match_id(unittest_parameters.unread_test_match_id_notification, cur_parameters)
  })
}

let unread_test_assistor_match_id_helper = {}
unread_test_assistor_match_id_helper.unread_test_assistor_match_id = unread_test_assistor_match_id

export { unread_test_assistor_match_id_helper }