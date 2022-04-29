import axios from 'axios';
axios.defaults.timeout = 5000  // 超时时间
axios.defaults.baseURL = 'http://127.0.0.1:5000'

jest.setTimeout(10000);

function set_unittest_user(username, password){
  test('set_unittest_user',(done)=>{ 

    function create_unittest_user(username, password){
      const new_users = {
        username: username,
        password: password,
      }
      return axios.post('/create_unittest_user', new_users)
    }

    async function set_user(username, password){
      let res1 = await create_unittest_user(username, password)
    
      expect(res1.data).toEqual(
        'gg'
      )

      console.log('1_set_unittest_user')
      done()
    }
    set_user(username, password)
  })
}

function delete_unittest_db(){
  test('delete_unittest_db',(done)=>{ 

    function delete_action(){
      return axios.get('/delete_unittest_db')
    }

    async function delete_db(){
      let res1 = await delete_action()
    
      expect(res1.data).toEqual(
        'gg'
      )

      console.log('1_delete_unittest_db')
      done()
    }
    delete_db()
  })
}

let modify_unittest_user_helper = {}
modify_unittest_user_helper.set_unittest_user = set_unittest_user
modify_unittest_user_helper.delete_unittest_db = delete_unittest_db

export { modify_unittest_user_helper }