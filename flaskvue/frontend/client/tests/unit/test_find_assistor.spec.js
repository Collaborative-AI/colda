import { login_helper } from './helper_folder/Apollo_login_helper';
import { find_assistor_helper } from './helper_folder/Apollo_find_assistor_helper'
jest.setTimeout(10000);

afterAll(() => {
  window.localStorage.setItem('Apollo-token', null)
  console.log('1 - afterAll')
});

describe('test_find_assistor', () => {
  console.log("876766767")
  login_helper.check_login_first_user
  find_assistor_helper.get_train_id
  
})
