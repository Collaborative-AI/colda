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

    let unread_test_sponsor_match_id_placeholder = (data) => {
      try{

        console.log(generate_unittest_log('unread_test_sponsor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }

    // sponsor: regression and assistor: regression
    let unread_test_sponsor_match_id_regression_regression_1s_1a = (data) => {
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
    let unread_test_sponsor_match_id_classification_regression_1s_1a = (data) => {
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

    let unread_test_sponsor_match_id_regression_regression_1s_2a = (data) => {
      try{
        data = data[0]
        let test_array = [-15.307662536170138, -6.242823411913374, -3.62703930434807, -2.253609528618039, -3.9262087320814665, 3.987855587724651, -2.980171893125066, -0.8147606613568552]
        let test_array_index = 0

        for (let i in data){
          let cur_list = data[i]
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_test_num = parseFloat(test_array[test_array_index].toFixed(5))
            console.log('number_ass', cur_number, cur_test_num)
            expect(cur_number).toEqual(
              cur_test_num
            )
            test_array_index += 1
          }
        }

        console.log(generate_unittest_log('unread_test_assistor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }


    let unread_test_sponsor_match_id_classification_regression_1s_2a = (data) => {
      try{
        data = data[0]
        let test_array = [-0.4289606386688076, -0.4377188317810896, -0.049991444558729725, -0.3750570533758708, -0.0031278807699227362, -0.0008288206037718598, 0.0007909454176475289, 0.007217208695665757]
        let test_array_index = 0

        for (let i in data){
          let cur_list = data[i]
          for (let j = 0; j < cur_list.length; j++){
            let cur_number = cur_list[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_test_num = parseFloat(test_array[test_array_index].toFixed(5))
            console.log('number_ass', cur_number, cur_test_num)
            expect(cur_number).toEqual(
              cur_test_num
            )
            test_array_index += 1
          }
        }

        console.log(generate_unittest_log('unread_test_assistor_match_id'))
        done()
      }catch (error){
        done(error)
      }
    }
    
    let cur_parameters = [];
    cur_parameters.push(unread_test_sponsor_match_id_1)
    cur_parameters.push(unread_test_sponsor_match_id_2)
    cur_parameters.push(unread_test_sponsor_match_id_3)

    let temp_length = unittest_parameters.assistor_username_list.split(",").length
    if (verify_algo == true){
      if (sponsor_mode == 'regression'){
        if (temp_length == 1){
          cur_parameters.push(unread_test_sponsor_match_id_regression_regression_1s_1a)
        } else if (temp_length == 2){
          cur_parameters.push(unread_test_sponsor_match_id_regression_regression_1s_2a)
        } else if (temp_length == 3){
          cur_parameters.push(unread_test_sponsor_match_id_regression_regression_1s_3a)
        }
      } else if (sponsor_mode == 'classification'){
        if (temp_length == 1){
          cur_parameters.push(unread_test_sponsor_match_id_classification_regression_1s_1a)
        } else if (temp_length == 2){
          cur_parameters.push(unread_test_sponsor_match_id_classification_regression_1s_2a)
        } else if (temp_length == 3){
          cur_parameters.push(unread_test_sponsor_match_id_classification_regression_1s_3a)
        }
      }
    } else {
      cur_parameters.push(unread_test_sponsor_match_id_placeholder)
    }
    
    cur_parameters.push('unread_test_match_id_unittest')
    Navbar_wrapper.vm.unread_test_match_id(unittest_parameters.unread_test_match_id_notification, cur_parameters)
  })
}

let unread_test_sponsor_match_id_helper = {}
unread_test_sponsor_match_id_helper.unread_test_sponsor_match_id = unread_test_sponsor_match_id

export { unread_test_sponsor_match_id_helper }