import { unittest_parameters, generate_unittest_log, Login_wrapper, Navbar_wrapper, Find_Assistor_wrapper} from '../../Apollo_unittest_init'
import { generate_parameters, retrieve_User_Sponsor_Table_record } from '../../Apollo_unittest_utils'
jest.setTimeout(10000);

function unread_test_output(sponsor_mode, assistor_mode, verify_algo){
  test('unread_test_output', (done) => { 
    let unread_test_output_1 = (data) => {
      try{
        let output_dict = data[0]
        expect(output_dict[unittest_parameters.task_id]).not.toBeNull()
  
        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        console.log(error)
      }
    }
  
    let unread_test_output_2 = (data) => {
      try{
        expect(data[0]).toBe(true)

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }

    // sponsor: regression and assistor: regression
    let unread_test_output_regression_regression_1s_1a = (data) => {
      try{
        data = data[0]
        let test_dict = {
          "1": {
            "MAD": 3.54763,
            "RMSE": 5.21270,
            "R2": 0.67182,
          },
          "2": {
            "MAD": 3.54221,
            "RMSE": 5.19744,
            "R2": 0.67374,
          }
        }
        
        for (let i in data){
          let cur_running_res = data[i]
          let cur_testing_dict = test_dict[i]
          for (let j in cur_running_res){
            let cur_number = cur_running_res[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_testing_number = cur_testing_dict[j]
            cur_testing_number = parseFloat(cur_testing_number.toFixed(5))
            console.log('spo_eval', cur_number, cur_testing_number)
            expect(cur_number).toEqual(
              cur_testing_number
            )
          }
        }

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }
    

    // sponsor: classification and assistor: regression
    let unread_test_output_classification_regression_1s_1a = (data) => {
      try{
        data = data[0]
        let test_dict = {
          "1": {
            "Accuracy": 0.86111,
            "F1": 0.86127,
          },
          "2": {
            "Accuracy": 0.91667,
            "F1": 0.91308,
          }
        }
        
        for (let i in data){
          let cur_running_res = data[i]
          let cur_testing_dict = test_dict[i]
          for (let j in cur_running_res){
            let cur_number = cur_running_res[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_testing_number = cur_testing_dict[j]
            cur_testing_number = parseFloat(cur_testing_number.toFixed(5))
            console.log('spo_eval', cur_number, cur_testing_number)
            expect(cur_number).toEqual(
              cur_testing_number
            )
          }
        }

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }

    // sponsor: regression and assistor: regression
    let unread_test_output_regression_regression_1s_2a = (data) => {
      try{
        data = data[0]

        let test_dict = {
          "1": {
            "MAD": 3.8372937900807953, 
            "RMSE": 5.641336458075518, 
            "R2": 0.37555098184055447
          },
          "2": {
            "MAD": 3.6513637297118313,
            "RMSE": 5.30278303987191,
            "R2": 0.36121280565236213,
          }
        }
        
        for (let i in data){
          let cur_running_res = data[i]
          let cur_testing_dict = test_dict[i]
          for (let j in cur_running_res){
            let cur_number = cur_running_res[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_testing_number = cur_testing_dict[j]
            cur_testing_number = parseFloat(cur_testing_number.toFixed(5))
            console.log('spo_eval', cur_number, cur_testing_number)
            expect(cur_number).toEqual(
              cur_testing_number
            )
          }
        }

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }

    let unread_test_output_classification_regression_1s_2a = (data) => {
      try{
        data = data[0]
        let test_dict = {
          "1": {
            "Accuracy": 0.8888888888888888, 
            "F1": 0.8864809081527346
          }, 
          "2": {
            "Accuracy": 0.9444444444444444, 
            "F1": 0.9415032679738561
          },
        }
        
        for (let i in data){
          let cur_running_res = data[i]
          let cur_testing_dict = test_dict[i]
          for (let j in cur_running_res){
            let cur_number = cur_running_res[j]
            cur_number = parseFloat(cur_number.toFixed(5))
            let cur_testing_number = cur_testing_dict[j]
            cur_testing_number = parseFloat(cur_testing_number.toFixed(5))
            console.log('spo_eval', cur_number, cur_testing_number)
            expect(cur_number).toEqual(
              cur_testing_number
            )
          }
        }

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }

    // sponsor: regression and multiple assistors
    let unread_test_output_multiple_assistors = (data) => {
      try{
        // data = data[0]
        // let test_dict = {
        //   "MAD": 3.79469,
        //   "RMSE": 5.75070,
        //   "R2": 0.39875,
        // }
        
        // for (let i in data){
        //   let cur_running_res = data[i]

        //   for (let j in cur_running_res){
        //     let cur_number = cur_running_res[j]
        //     cur_number = parseFloat(cur_number.toFixed(5))
        //     console.log('spo_eval', cur_number, test_dict[j])
        //     expect(cur_number).toBeLessThan(
        //       test_dict[j]
        //     )
        //   }
        // }

        console.log(generate_unittest_log('unread_test_output'))
      }catch (error){
        done(error)
      }
    }    

    let unread_test_output_4 = (data) => {
      try{

        console.log(generate_unittest_log('unread_test_output'))
        done()
      }catch (error){
        done(error)
      }
    }
  
    let cur_parameters = [];
    cur_parameters.push(unread_test_output_1)
    cur_parameters.push(unread_test_output_2)

    let temp_length = unittest_parameters.assistor_username_list.split(",").length
    if (verify_algo == true){

      if (sponsor_mode == 'regression'){
        if (temp_length == 1){
          cur_parameters.push(unread_test_output_regression_regression_1s_1a)
        } else if (temp_length == 2){
          cur_parameters.push(unread_test_output_regression_regression_1s_2a)
        } else if (temp_length == 3){
          cur_parameters.push(unread_test_output_regression_regression_1s_3a)
        }
      } else if (sponsor_mode == 'classification'){
        if (temp_length == 1){
          cur_parameters.push(unread_test_output_classification_regression_1s_1a)
        } else if (temp_length == 2){
          cur_parameters.push(unread_test_output_classification_regression_1s_2a)
        } else if (temp_length == 3){
          cur_parameters.push(unread_test_output_classification_regression_1s_3a)
        }
      }
    } else {
      // cur_parameters.push(unread_test_output_multiple_assistors)
    }
    
    cur_parameters.push(unread_test_output_4)
    cur_parameters.push('unread_test_output_unittest')
    
    Navbar_wrapper.vm.unread_test_output(unittest_parameters.unread_test_output_notification, cur_parameters)
  })
}

let unread_test_output_helper = {}
unread_test_output_helper.unread_test_output = unread_test_output

export { unread_test_output_helper }
