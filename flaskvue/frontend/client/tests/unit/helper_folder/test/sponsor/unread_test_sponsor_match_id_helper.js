import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record, cut_decimal } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);


function unread_test_sponsor_match_id(sponsor_mode, assistor_mode, verify_algo){
  test('unread_test_sponsor_match_id', (done) => { 
    let unread_test_sponsor_match_id_1 = (data) => {
      try{
        let test_match_id_dict = data[0]  
        expect(test_match_id_dict[unittest_parameters.test_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_test_sponsor_match_id_2 = (data) => {
      try{
        let response_data = data[0]
        let match_id_file = response_data.match_id_file
        let sponsor_random_id = response_data.sponsor_random_id
       
        expect(match_id_file).not.toBeNull()
        expect(sponsor_random_id).not.toBeNull()
        
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
      }catch (error){
        done(error)
      }
    }
  
    let unread_test_sponsor_match_id_3 = (data) => {
      try{        
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
      }catch (error){
        done(error)
      }
    }

    // sponsor: regression and assistor: regression
    let unread_test_sponsor_match_id_regression_regression = (data) => {
      try{
        data = data[0]
        let test_array = [-15.62146, -7.63978, -3.17975, -3.77626, -2.13779, 1.60417, -1.76595, -0.91224]
        let test_array_index = 0
        for (let i in data){
          let cur_list = data[i]
          console.log('cur_list', cur_list)
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            console.log('number_spo', cur_number, test_array[test_array_index])
            expect(cur_number).toEqual(
              test_array[test_array_index]
            )
            test_array_index += 1
          }
        }
        
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }

    // sponsor: classification and assistor: regression
    let unread_test_sponsor_match_id_classification_regression = (data) => {
      try{
        data = data[0]
        let test_array = [-0.46054, -0.45200, -0.06237, -0.43070, -0.01779, -0.00139, 0.00462, -0.00120]
        let test_array_index = 0
        for (let i in data){
          let cur_list = data[i]
          console.log('cur_list', cur_list)
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            console.log('number_spo', cur_number, test_array[test_array_index])
            expect(cur_number).toEqual(
              test_array[test_array_index]
            )
            test_array_index += 1
          }
        }
        
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }

    let unread_test_sponsor_match_id_multiple_assistors = (data) => {
      try{
        
        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }
    
    let cur_parameters = [];
    cur_parameters.push(unread_test_sponsor_match_id_1)
    cur_parameters.push(unread_test_sponsor_match_id_2)
    cur_parameters.push(unread_test_sponsor_match_id_3)
    if (verify_algo == true){
      if (sponsor_mode == 'regression'){
        cur_parameters.push(unread_test_sponsor_match_id_regression_regression)
      } else if (sponsor_mode == 'classification'){
        cur_parameters.push(unread_test_sponsor_match_id_classification_regression)
      }
    } else {
      cur_parameters.push(unread_test_sponsor_match_id_multiple_assistors)
    }
    
    cur_parameters.push('unread_test_match_id_unittest')
    Navbar_wrapper.vm.unread_test_match_id(unittest_parameters.unread_test_match_id_notification, cur_parameters)
  })
}

let unread_test_sponsor_match_id_helper = {}
unread_test_sponsor_match_id_helper.unread_test_sponsor_match_id = unread_test_sponsor_match_id

export { unread_test_sponsor_match_id_helper }