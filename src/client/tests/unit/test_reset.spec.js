import { login_helper } from './helper_folder/Apollo_login_helper'
import { switch_default_values_helper } from './helper_folder/Apollo_switch_default_values_helper';
import { reset_helper } from './helper_folder/Apollo_forgot_password_helper'
jest.setTimeout(10000);

afterAll(() => {
  window.localStorage.removeItem('Apollo-token')
  console.log('afterAll')
});

describe('test_reset', () => {
  // console.log("676766767")
  // train_helper_functions.login.login_first_user
  console.log("676766767")
  // train_helper_functions.login.login_second_user
  // login_helper.login_first_user
  // login_helper.login_second_user
  reset_helper.forgot_password()
  
})
