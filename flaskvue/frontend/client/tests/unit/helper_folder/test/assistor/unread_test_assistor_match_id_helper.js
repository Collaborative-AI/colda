import { unittest_parameters, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper, Find_Test_Assistor_Wrapper} from '../../Apollo_unittest_init'
import { generate_parameters } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_test_assistor_match_id(){
  test('unread_test_assistor_match_id', (done) => {
    let unread_test_assistor_match_id_1 = (data) => {
      try{
        let test_match_id_dict = data[0]
  
        expect(test_match_id_dict[unittest_parameters.test_id]).not.toBeNull()
  
        console.log('1_unread_test_assistor_match_id')
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_assistor_match_id_2 = (data) => {
      try{
        let response_data = data[0]
        let match_id_file = response_data.match_id_file
        let assistor_random_id_pair = response_data.assistor_random_id_pair
        // let row = retrieve_User_assistor_Table_record(unittest_parameters.user_id, unittest_parameters.task_id)
  
        expect(match_id_file).not.toBeNull()
        expect(assistor_random_id_pair).not.toBeNull()
        
        console.log('1_unread_test_assistor_match_id')
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_assistor_match_id_3 = (data) => {
      try{
        console.log('1_unread_test_assistor_match_id')
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
        
        console.log('1_unread_test_assistor_match_id')
      }catch (error){
        done(error)
      }
    }
    


    let unread_test_assistor_match_id_5 = (data) => {
      try{
        // console.log('sdfad', data)
        // data = data[0]

        // let test_array = [9.26144, -8.06623, 12.61785, -10.33504, 0.22978,  1.46820, -1.38115, -0.88841]
        // let test_array_index = 0
        // for (let i in data){
        //   let cur_list = data[i]
        //   console.log('assistor_cur_list', cur_list)
        //   for (let j = 0; j < cur_list.length; j++){
        //     let cur_number = cur_list[j]
        //     cur_number = parseFloat(cur_number.toFixed(5))
        //     console.log('number_ass', cur_number, test_array[test_array_index])
        //     expect(cur_number).toEqual(
        //       test_array[test_array_index]
        //     )
        //     test_array_index += 1
        //   }
        // }
        console.log('unread_assistor_test_match_id_5')
        
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
        console.log('unread_assistor_test_match_id_5')
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
    cur_parameters.push(unread_test_assistor_match_id_5)
    cur_parameters.push(unread_test_assistor_match_id_6)
    cur_parameters.push('unread_test_match_id_unittest')

    Navbar_wrapper.vm.unread_test_match_id(unittest_parameters.unread_test_match_id_notification, cur_parameters)
  })
}

let unread_test_assistor_match_id_helper = {}
unread_test_assistor_match_id_helper.unread_test_assistor_match_id = unread_test_assistor_match_id

export { unread_test_assistor_match_id_helper }