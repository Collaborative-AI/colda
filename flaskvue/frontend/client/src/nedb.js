import Datastore from 'nedb';
import path from 'path';

// rendering process

// ipc

// main process 


// import { data } from 'jquery';

// const NeDB = require('nedb')
// const path = window.require('path');
// import { remote } from 'electron';
const {remote} = window.require('electron')
console.log("zzzz", remote)
console.log("gggg", path.join(remote.app.getPath('userData'), '../data.db'))
// console.log(NeDB)
// console.log('ijisfjoej')
// console.log(__dirname)
// console.log(path.join(__dirname,'../../data.db'))
// var db = new NeDB({
//     // filename: './user.db',

//     autoload: true,
//     filename: path.join(__dirname,'../../data.db'),
//     timestampData: true,
// })
let db = new Datastore({
    autoload: true,
    timestampData: true,
    // filename: path.join(remote.app.getPath('userData'), '../data.db'),
    // filename: path.join(path.resolve("./exp"),'/data.db')
    filename: path.join(__dirname,'../../data.db'),
})

export default db

// let db=5;

// export default db