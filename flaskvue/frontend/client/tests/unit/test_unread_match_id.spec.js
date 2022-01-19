import { login_helper } from './helper_folder/Apollo_login_helper';
import { logout_helper } from './helper_folder/Apollo_logout_helper';
import { delete_db_helper } from './helper_folder/Apollo_delete_db_helper'
import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper'
import { profile_helper } from './helper_folder/Apollo_profile_helper'
import { notification_helper } from './helper_folder/Apollo_notification_helper';
import { switch_default_values_helper } from './helper_folder/Apollo_switch_default_values_helper';

import { unread_request_helper } from './helper_folder/train/assistor/unread_request_helper';
import { unread_sponsor_match_id_helper } from './helper_folder/train/sponsor/unread_sponsor_match_id_helper'
import { unread_assistor_match_id_helper } from './helper_folder/train/assistor/unread_assistor_match_id_helper';

jest.setTimeout(10000);

afterAll(() => {
  window.localStorage.removeItem('Apollo-token')
  console.log('afterAll')
});

describe('test_unread_match_id', () => {

  let max_round = 1
  let sponsor_mode = 'regression'
  let assistor_mode = 'regression'
  let verify_algo = true
  let match_ratio = '1.0'
  let default_mode = 'auto'
  let assistor_username_list = 'xie2'
  // let data_file = 'CreditCard'
  let data_file = 'KCHousing'

  switch_default_values_helper.switch_default(sponsor_mode, assistor_username_list, match_ratio, default_mode, data_file)

  login_helper.login_first_user()

  delete_db_helper.delete_db()
  // Sponsor gets train id
  find_assistor_helper.get_train_id()
  // Sponsor finds assistor
  find_assistor_helper.find_assistor(sponsor_mode, assistor_username_list)
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
  logout_helper.logout()
  // assistor logins
  
  // login_helper.login_second_user()
  // //assistor gets nofification
  // notification_helper.update_notification()
  // //sponsor runs unread match id
  // unread_assistor_match_id_helper.unread_assistor_match_id()
  // logout_helper.logout()

  
  // //sponsor logins
  // login_helper.login_first_user()
  // // sponsor gets nofification
  // notification_helper.update_notification()
  // //sponsor runs unread match id
  // unread_sponsor_match_id_helper.unread_sponsor_match_id()
  // logout_helper.logout()
  
})


 // // Assistor gets notification
  // await get_notifications()
  // // Assistor runs unread request()
  // unread_request_helper.unread_request

  // // Sponsor logins
  // login_helper.login_first_user
  // await get_notifications()
  // // Sponsor runs unread match id()
  // unread_sponsor_match_id_helper.unread_sponsor_match_id

  // // Assistor logins
  // login_helper.login_second_user
  // await get_notifications()
  // // Sponsor runs unread match id()
  // unread_assistor_match_id_helper.unread_assistor_match_id
