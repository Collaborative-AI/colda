// import { update_notifications, get_notifications } from './Apollo_unittest_utils'
import {  unittest_parameters,  modify_parameter } from './Apollo_unittest_init'
import axios from 'axios'
import { add_prefix } from '../../../src/utils.js'




function update_notification(){
    test('update_notification', (done) => {
        function get_notifications(){
          const path = `/users/`+ unittest_parameters.user_id.toString() + `/`
          console.log('come', path)
          return axios.get(add_prefix(path, `/user`))
        }
        
        function update_notifications(response){
          const all_notifications = {
            response_data: response.data
          } 
          return axios.get(add_prefix(`/get_notifications/${unittest_parameters.user_id}`, `/main_flow`))
        }
    
        async function notification(){
          // let res1 = await get_notification(unittest_parameters)
          // console.log('haha1', res1)
          // let res2 = await get_notification()
          // console.log('haha2', res2)
          // console.log(res1, res2)
          console.log('come2')
          let res1 = await get_notifications()
          // console.log('zz1get_notifications', res1)
          // console.log('zz2', res1.data, res1.data.length)
          // console.log('zz3', res1.data != undefined, res1.data != [])
          
          let has_payload_greater_than_zero = false
          // for (let item of res1.data){
            // console.log('item is', item)
            if (true){
              console.log('lihaine')
              has_payload_greater_than_zero = true
              let res2 = await update_notifications(res1)
              console.log('zz2', res2.data.notification_result.category)
              // console.log('zz4', res2.data.notification_result.category['unread_request']['task_id_dict'])
              if(res2.data.notification_result.category['unread_request'] != undefined){
                modify_parameter("unread_request_notification", res2.data.notification_result.category['unread_request']['task_id_dict'])
              }
              if(res2.data.notification_result.category['unread_match_identifier'] != undefined){
                modify_parameter("unread_match_id_notification", res2.data.notification_result.category['unread_match_identifier']['task_id_dict'])
              }
              if(res2.data.notification_result.category['unread_situation'] != undefined){
              modify_parameter("unread_situation_notification", res2.data.notification_result.category['unread_situation']['task_id_dict'])
              }
              if(res2.data.notification_result.category['unread_output'] != undefined){
              modify_parameter("unread_output_notification", res2.data.notification_result.category['unread_output']['task_id_dict'])
              }

              // modify_parameter("unread_request_notification", res2.data["unread request"])
              // modify_parameter("unread_match_id_notification", res2.data["unread match id"])
              // modify_parameter("unread_situation_notification", res2.data["unread situation"])
              // modify_parameter("unread_output_notification", res2.data["unread output"])
              // test stage

              if(res2.data.notification_result.category['unread_test_request'] != undefined){
                modify_parameter("unread_test_request_notification", res2.data.notification_result.category['unread_test_request']['test_id_dict'])
              }
              if(res2.data.notification_result.category['unread_test_match_identifier'] != undefined){
                modify_parameter("unread_test_match_id_notification", res2.data.notification_result.category['unread_test_match_identifier']['test_id_dict'])
              }
              if(res2.data.notification_result.category['unread_test_output'] != undefined){
              modify_parameter("unread_test_output_notification", res2.data.notification_result.category['unread_test_output']['test_id_dict'])
              }

              // modify_parameter("unread_test_request_notification", res2.data["unread test request"])
              // modify_parameter("unread_test_match_id_notification", res2.data["unread test match id"])
              // modify_parameter("unread_test_output_notification", res2.data["unread test output"])
            }
          // }
          if (has_payload_greater_than_zero == false){
            console.log('get_notification_null')
          }
          done()
        }
        notification()
      })
}

let notification_helper = {}
// train_helper_functions.login = {}

notification_helper.update_notification = update_notification


export { notification_helper }