import {delete_db} from './Apollo_unittest_utils'

function delete_db_function(){
    test('delete_db_rows',(done)=>{
        async function clear_database(){
        let res1 = await delete_db()
        console.log('output res1', res1)
        done()
        }
        clear_database()
    })
}

  let delete_db_helper = {}
  // train_helper_functions.login = {}
  
  delete_db_helper.delete_db = delete_db_function
  
  
  export { delete_db_helper }