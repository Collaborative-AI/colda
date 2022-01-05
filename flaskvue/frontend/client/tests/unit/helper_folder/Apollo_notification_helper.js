// import { update_notifications, get_notifications } from './Apollo_unittest_utils'
import {  unittest_parameters,  modify_parameter } from './Apollo_unittest_init'
import axios from 'axios'




function update_notification(){
    test('update_notification', (done) => {
        function get_notifications(){
          const path = `/users/`+ unittest_parameters.user_id.toString() + `/notifications/`
          console.log('come', path)
          return axios.get(path)
        }
        
        function update_notifications(response){
          const all_notifications = {
            response_data: response.data
          } 
          return axios.post('/update_all_notifications/', all_notifications)
        }
    
        async function notification(){
          // let res1 = await get_notification(unittest_parameters)
          // console.log('haha1', res1)
          // let res2 = await get_notification()
          // console.log('haha2', res2)
          // console.log(res1, res2)
          console.log('come2')
          let res1 = await get_notifications()
          console.log('zz1', res1)
          let res2 = await update_notifications(res1)
          console.log('zz2', res2)
          console.log('zz4', res2.data["unread request"])
          modify_parameter("unread_request_notification", res2.data["unread request"])
          modify_parameter("unread_match_id_notification", res2.data["unread match id"])
          modify_parameter("unread_situation_notification", res2.data["unread situation"])
          modify_parameter("unread_output_notification", res2.data["unread output"])
          // test stage
          modify_parameter("unread_test_request_notification", res2.data["unread test request"])
          modify_parameter("unread_test_match_id_notification", res2.data["unread test match id"])
          modify_parameter("unread_test_output_notification", res2.data["unread test output"])
          done()
        }
        notification()
      })
}

let notification_helper = {}
// train_helper_functions.login = {}

notification_helper.update_notification = update_notification


export { notification_helper }