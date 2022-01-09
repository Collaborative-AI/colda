
import { login_helper } from './helper_folder/Apollo_login_helper'
jest.setTimeout(10000);

afterAll(() => {
  window.localStorage.removeItem('Apollo-token')
  console.log('afterAll')
});

describe('test_login', () => {
  // console.log("676766767")
  // train_helper_functions.login.check_login_first_user
  console.log("676766767")
  // train_helper_functions.login.check_login_second_user
  // login_helper.check_login_first_user
  // login_helper.check_login_second_user
  login_helper.check_login_first_user()

  // login_helper.check_login_second_user()
  
})
