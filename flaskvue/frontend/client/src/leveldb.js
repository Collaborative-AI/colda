var levelup = window.require('levelup');
var leveldown = window.require('leveldown');
console.log("levelup", levelup)
import path from 'path'

var db = levelup(leveldown("./mydb"))

db.put('name', 'levelup', function (err) {
  if (err) return console.log('Ooops!', err) // some kind of I/O error

  // 3) Fetch by key
  db.get('name', function (err, value) {
    if (err) return console.log('Ooops!', err) // likely the key was not found

    // Ta da!
    console.log('name=' + value)
  })
})

export default db