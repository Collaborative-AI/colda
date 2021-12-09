window.fs = require('fs');
window.ex = require("child_process");
window.os = require('os');
window.node_path = require('path');
window.dialog = require('electron').remote.dialog;
window.db = require('better-sqlite3');
window.log = require('electron-log')

console.log("---", window.fs, window.ex , window.os , window.node_path, window.dialog , window.db)

if (process.env.NODE_ENV === 'test') {
    console.log("test environment")
    window.electronRequire = require
  }