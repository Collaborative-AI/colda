const sqlite3 = window.require('sqlite3').verbose();


let db = new sqlite3.Database('Apollo_Client_db');

db.serialize(function() {
  db.run("CREATE TABLE IF NOT EXISTS User_Default_Path (id                    int primary key, \
                                                   user_id                    int, \
                                                   default_train_data_path    text, \
                                                   default_train_id_path      text, \
                                                   default_test_data_path     text, \
                                                   default_test_id_path       text)");

  db.run("CREATE TABLE IF NOT EXISTS User_Chosen_Path (id     int primary key, \
                                           task_name          text,\
                                           task_description   text,\
                                           user_id            int, \
                                           test_indicator     text, \
                                           task_id            text, \
                                           test_id            text, \
                                           train_data_path    text, \
                                           train_id_path      text, \
                                           train_target_path  text, \
                                           test_data_path     text, \
                                           test_id_path       text, \
                                           test_target_path   text)");

    db.run("CREATE TABLE IF NOT EXISTS User_Pending_Page (id                  int primary key, \
                                                   task_name                  text,\
                                                   task_description           text,\
                                                   user_id                    int, \
                                                   task_id                    int,\
                                                   default_train_data_path    text, \
                                                   default_train_id_path      text, \
                                                   default_test_data_path     text, \
                                                   default_test_id_path       text)");
                                                   
                                         
                                           
});
// let db=5;
export default db
// exports.default = db