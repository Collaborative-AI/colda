import { login_helper } from './helper_folder/Apollo_login_helper';
import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper'
import { profile_helper } from './helper_folder/Apollo_profile_helper'
import { unread_sponsor_match_id_helper } from './helper_folder/Apollo_unread_sponsor_match_id_helper'
import { unread_assistor_match_id_helper } from './helper_folder/Apollo_unread_assistor_match_id_helper';
import { get_notification } from './helper_folder/Apollo_unittest_init'
jest.setTimeout(10000);

afterAll(() => {
  window.localStorage.setItem('Apollo-token', null)
  console.log('afterAll')
});

describe('test_unread_request', () => {
  // Sponsor logins
  login_helper.check_login_first_user
  // Sponsor gets train id
  find_assistor_helper.get_train_id
  // Sponsor finds assistor
  find_assistor_helper.onSubmit

  // Assistor logins
  login_helper.check_login_second_user
  // Assistor updates default_train_file_path, default_train_id_column, 
  // default_train_data_column
  profile_helper.onSubmit
  // Assistor gets notification
  await get_notification
  // Assistor runs unread request()
  unread_request_helper.unread_request

  // Sponsor logins
  login_helper.check_login_first_user
  await get_notification
  // Sponsor runs unread match id()
  unread_sponsor_match_id_helper.unread_sponsor_match_id

  // Assistor logins
  login_helper.check_login_second_user
  await get_notification
  // Sponsor runs unread match id()
  unread_assistor_match_id_helper.unread_assistor_match_id

})
