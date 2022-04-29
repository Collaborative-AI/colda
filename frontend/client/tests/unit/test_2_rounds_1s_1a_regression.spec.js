import { login_helper } from './helper_folder/Apollo_login_helper';
import { logout_helper } from './helper_folder/Apollo_logout_helper';
import { delete_db_helper } from './helper_folder/Apollo_delete_db_helper'
import { profile_helper } from './helper_folder/Apollo_profile_helper'
import { notification_helper } from './helper_folder/Apollo_notification_helper';
import { switch_default_values_helper } from './helper_folder/Apollo_switch_default_values_helper';

import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper'
import { unread_request_helper } from './helper_folder/train/assistor/unread_request_helper';
import { unread_sponsor_match_id_helper } from './helper_folder/train/sponsor/unread_sponsor_match_id_helper'
import { unread_assistor_match_id_helper } from './helper_folder/train/assistor/unread_assistor_match_id_helper';
import { unread_sponsor_situation_helper } from './helper_folder/train/sponsor/unread_sponsor_situation_helper';
import { unread_assistor_situation_helper } from './helper_folder/train/assistor/unread_assistor_situation_helper';
import { unread_output_helper } from './helper_folder/train/sponsor/unread_output_helper';

import { find_test_assistor_helper } from './helper_folder/Apollo_find_test_assistor_helper';
import { unread_test_request_helper } from './helper_folder/test/assistor/unread_test_request_helper'
import { unread_test_sponsor_match_id_helper } from './helper_folder/test/sponsor/unread_test_sponsor_match_id_helper'
import { unread_test_assistor_match_id_helper } from './helper_folder/test/assistor/unread_test_assistor_match_id_helper'
import { unread_test_output_helper } from './helper_folder/test/sponsor/unread_test_output_helper'

jest.setTimeout(10000);

afterAll(() => {
  
  window.localStorage.removeItem('Apollo-token')
  console.log('afterAll')

});

describe('test_multiple_rounds_regression', () => {
  
  let max_round = 2
  let verify_algo = true
  let match_ratio = "1.0"
  let default_mode = 'auto'
  let sponsor_mode = 'regression'
  let assistor_mode = 'regression'
  let assistor_username_list = 'xie2'

  switch_default_values_helper.switch_default(sponsor_mode, assistor_username_list, match_ratio, default_mode)
  // Sponsor logins

  login_helper.login_first_user()
  
  delete_db_helper.delete_db()
  // Sponsor gets train id
  find_assistor_helper.get_train_id()
  // Sponsor finds assistor
  find_assistor_helper.find_assistor(sponsor_mode, assistor_username_list)
  // Sponsor logouts
  logout_helper.logout()

  // Assistor logins
  login_helper.login_second_user()
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
  login_helper.login_second_user()
  //assistor gets nofification
  notification_helper.update_notification()
  //sponsor runs unread match id
  unread_assistor_match_id_helper.unread_assistor_match_id()
  //assistor logouts
  logout_helper.logout()

  //sponsor logins
  login_helper.login_first_user()
  //sponsor gets nofification
  notification_helper.update_notification()
  //sponsor runs unread match id
  unread_sponsor_match_id_helper.unread_sponsor_match_id()
  //sponsor logouts
  logout_helper.logout()

  for (let current_round = 1; current_round <= max_round; current_round++){
    //sponsor logins
    login_helper.login_first_user()
    //sponsor gets nofification
    notification_helper.update_notification()
    //sponsor runs unread situation
    unread_sponsor_situation_helper.unread_sponsor_situation()
    //sponsor logouts
    logout_helper.logout()

    //assistor logins
    login_helper.login_second_user()
    //assistor gets nofification
    notification_helper.update_notification()
    //assistor runs unread situation
    unread_assistor_situation_helper.unread_assistor_situation()
    //sponsor logouts
    logout_helper.logout()

    // sponsor logins
    login_helper.login_first_user()
    // sponsor gets nofification
    notification_helper.update_notification()
    //sponsor runs unread situation
    
    unread_output_helper.unread_output(current_round, max_round)
    //sponsor logouts
    logout_helper.logout()
  }
  

  // Sponsor logins
  login_helper.login_first_user()
  // Sponsor gets test id
  find_test_assistor_helper.get_test_id()
  // Sponsor finds assistor
  find_test_assistor_helper.find_test_assistor()
  // Sponsor logouts
  logout_helper.logout()

  // assistor logins
  login_helper.login_second_user()
  //assistor updates nofifications
  notification_helper.update_notification()
  //unread request
  unread_test_request_helper.unread_test_request()
  //logout
  logout_helper.logout()

  //sponsor logins
  login_helper.login_first_user()
  //sponsor updates notifications
  notification_helper.update_notification()
  //sponsor unread test match id
  unread_test_sponsor_match_id_helper.unread_test_sponsor_match_id(sponsor_mode, assistor_mode, verify_algo)
  //sponsor logouts
  logout_helper.logout()

  //assistor logins
  login_helper.login_second_user()
  //assistor updates notifications
  notification_helper.update_notification()
  //assistor runs unread match id
  unread_test_assistor_match_id_helper.unread_test_assistor_match_id(sponsor_mode, assistor_mode, verify_algo)
  //assistor logouts
  logout_helper.logout()

  //sponsor logins
  login_helper.login_first_user()
  //sponsor updates notifications
  notification_helper.update_notification()
  // //sponsor unread test output
  unread_test_output_helper.unread_test_output(sponsor_mode, assistor_mode, verify_algo)
  //sponsor logouts
  logout_helper.logout()


})