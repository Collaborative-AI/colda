const sqlite3 = window.require('sqlite3').verbose();
const node_path = window.require('path');

console.log(" this.exe_position",  node_path.resolve("./resources/dist/run/run.exe"))
console.log("dir",__dirname)
console.log(node_path.join(__dirname, '../dist/run/run.exe'))
import path from 'path'
const fs = window.require("fs")
console.log("fs", fs)

function createDatabase(file){
  console.log("file_position", file)
  if(!fs.existsSync(file)){
    
    console.log("creating database file");
    fs.openSync(file, "w");
    console.log("file created");
  }

  var db = new sqlite3.Database(
    file, 
    sqlite3.OPEN_READWRITE, 
    function (err) {
        if (err) {
            return console.log(err.message)
        }
        console.log('connect database successfully')
    }
  )
  return db
}
let db = createDatabase(path.join(__dirname,'../../Apollo_Client_data.db'))

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