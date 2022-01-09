let Database = null
let fs = null
let ex = null
let os = null
let node_path = null
let dialog = null
let log = null

console.log('5412312312')
if (window.require != undefined){
  // console.log(window.require('sqlite3'))
  // Database = window.require('better-sqlite3')
  fs = window.require('fs');
  ex = window.require("child_process");
  os = window.require('os');
  node_path = window.require('path');
  dialog = window.require('electron').remote.dialog;
  console.log('ss', dialog)
  log = window.require('electron-log')
  console.log('wudi', log)
} else {
  Database = require('better-sqlite3')
  fs = require('fs');
  ex = require("child_process");
  os = require('os');
  node_path = require('path');
  // console.log('ssss', require('electron'))
  // dialog = require('electron').remote.dialog;
  log = require('electron-log')
  
}


export { Database, fs, ex, os, node_path, dialog, log }