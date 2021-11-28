// fetch.js
import db from '../../src/db';

export default {
  async fetchPostsList(callback) {
    let select_default_train_file_path = 'SELECT default_train_file_path, default_train_id_column FROM User_Default_Table WHERE user_id=2';
    // return db.get(select_default_train_file_path).then(res => {
    //   return callback(res.data);
    // })
    db.get(select_default_train_file_path, function(err, row){
        if (err){ 
          console.log(err);
        }
        return callback(row)
    }
    
  )
}
}