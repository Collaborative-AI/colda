import { login_helper } from './helper_folder/Apollo_login_helper';
import { notification_helper } from './helper_folder/Apollo_notification_helper';
import { profile_helper } from './helper_folder/Apollo_profile_helper'
import { unread_request_helper } from './helper_folder/Apollo_unread_request_helper'
import { unread_sponsor_match_id_helper } from './helper_folder/Apollo_unread_sponsor_match_id_helper';
import { unread_assistor_match_id_helper } from './helper_folder/Apollo_unread_assistor_match_id_helper';
import { unread_sponsor_situation_helper } from './helper_folder/Apollo_unread_sponsor_situation_helper';
import { unread_assistor_situation_helper } from './helper_folder/Apollo_unread_assistor_situation_helper';
import { unread_output_helper } from './helper_folder/Apollo_unread_output_helper';
import { find_test_assistor_helper } from './helper_folder/Apollo_find_test_assistor_helper'
import {  unittest_parameters,  modify_parameter, Navbar_wrapper } from './helper_folder/Apollo_unittest_init'
// import {  get_notifications, update_notifications } from './helper_folder/Apollo_unittest_utils'
import { unread_test_request_helper } from './helper_folder/Apollo_unread_test_request_helper';
import { logout_helper } from './helper_folder/Apollo_logout_helper';
import { delete_db_helper } from './helper_folder/Apollo_delete_db_helper';
import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper';
import { unread_test_sponsor_match_id_helper } from './helper_folder/Apollo_unread_test_sponsor_match_id_helper';
import { unread_test_assistor_match_id_helper } from './helper_folder/Apollo_unread_test_assistor_match_id_helper';
import axios from 'axios';
// import store from '../../src/store'
jest.setTimeout(10000);


afterAll(() => {
  window.localStorage.setItem('Apollo-token', null)
  console.log('afterAll')
});

describe('test_unread_test_match_id', () => {
  console.log('test_unread_test_match_id')

  //  Sponsor logins
   logout_helper.logout()
   login_helper.check_login_first_user()
   delete_db_helper.delete_db()
   // Sponsor gets train id
   find_assistor_helper.get_train_id()
   // Sponsor finds assistor
   find_assistor_helper.onSubmit()
   // Sponsor logouts
   logout_helper.logout()
 
   // Assistor logins
   login_helper.check_login_second_user()
   // Assistor updates default_train_file_path, default_train_id_column, 
   // default_train_data_column
   profile_helper.onSubmit()
   //assistor gets notification
   notification_helper.update_notification()
   //assistor runs unread request
   unread_request_helper.unread_request()
   //assistor logouts
   logout_helper.logout()
 
   //assistor logins
   login_helper.check_login_second_user()
   //assistor gets nofification
   notification_helper.update_notification()
   //sponsor runs unread match id
   unread_assistor_match_id_helper.unread_assistor_match_id()
   //assistor logouts
   logout_helper.logout()
 
   // sponsor logins
   login_helper.check_login_first_user()
   // sponsor gets nofification
   notification_helper.update_notification()
   //sponsor runs unread match id
   unread_sponsor_match_id_helper.unread_sponsor_match_id()
   //sponsor logouts
   logout_helper.logout()
 
 
   // sponsor logins
   login_helper.check_login_first_user()
   // sponsor gets nofification
   notification_helper.update_notification()
   //sponsor runs unread situation
   unread_sponsor_situation_helper.unread_sponsor_situation()
   //sponsor logouts
   logout_helper.logout()
 
   //assistor logins
   login_helper.check_login_second_user()
   //assistor gets nofification
   notification_helper.update_notification()
   //assistor runs unread situation
   unread_assistor_situation_helper.unread_assistor_situation()
   //sponsor logouts
   logout_helper.logout()
 
   // sponsor logins
   login_helper.check_login_first_user()
   // sponsor gets nofification
   notification_helper.update_notification()
  //  //sponsor runs unread situation
   let current_round = 1
   let max_round = 1
   unread_output_helper.unread_output(current_round, max_round)
  //  //sponsor logouts
   logout_helper.logout()

  //  Sponsor logins
   login_helper.check_login_first_user()
   // Sponsor gets test id
   find_test_assistor_helper.get_test_id()
   // Sponsor finds assistor
   find_test_assistor_helper.onSubmit()
   // Sponsor logouts
   logout_helper.logout()

  //  assistor logins
   login_helper.check_login_second_user()
   //assistor updates nofifications
   notification_helper.update_notification()
   //unread request
   unread_test_request_helper.unread_test_request()
   //logout
   logout_helper.logout()

  //sponsor logins
  login_helper.check_login_first_user()
  //sponsor updates notifications
  notification_helper.update_notification()
  //sponsor unread test match id
  unread_test_sponsor_match_id_helper.unread_test_sponsor_match_id()
  //sponsor logouts
  logout_helper.logout()

  //assistor logins
  login_helper.check_login_second_user()
  //assistor updates notifications
  notification_helper.update_notification()
  //assistor runs unread match id
  unread_test_assistor_match_id_helper.unread_test_assistor_match_id()
  //assistor logouts
  logout_helper.logout()


})
