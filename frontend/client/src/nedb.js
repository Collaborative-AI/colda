import {sqlite3,node_path, fs, nedb } from './import_package'

console.log('wolaile',__dirname)

// let db = createDatabase(node_path.join(__dirname,'../../Apollo_Client_data.db'))

var nedb1 = window.require('nedb')

var db = new nedb1({
    filename: node_path.join(__dirname,'../../../nedb_data.db'),
    autoload: true,
})

db.insert({
    name: 'Alice',
    age: 20,
    rank: 1,
}, function(err, doc) {
    console.log('inserted:', doc)
})
export default db