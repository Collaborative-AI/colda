// import Datastore from 'nedb';
// import path from 'path';

const NeDB = window.require('nedb')
const path = window.require('path');
// import { remote } from 'electron';
const a=window.require('electron')
console.log(NeDB)
console.log('ijisfjoej')

var db = new NeDB({
    // filename: './user.db',
    
    autoload: true,
    filename: path.resolve("data.db"),
    timestampData: true,
})

// export default new Datastore({
//     autoload: true,
//     timestampData: true,
//     // filename: path.join(remote.app.getPath('userData'), '/data.db'),
//     filename: path.join(path.resolve("./exp"),'/data.db')
// })

// let db=5;

export default db