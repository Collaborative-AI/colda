window.fs = require('fs');
window.ex = require("child_process");
window.os = require('os');
window.node_path = require('path');
window.dialog = require('electron').remote.dialog;
window.db = require('better-sqlite3');
window.log = require('electron-log')

// log.transports.file.level = false; // 禁用写Log文件
// log.transports.console.level = false; //禁用console输出
// level: error, warn, info, verbose, debug
window.log.transports.file.resolvePath = () => window.node_path.join(__dirname, 'logs/main.log');
console.log('log_path', window.node_path.join(__dirname, 'logs/main.log'));
window.log.transports.file.level = 'silly';
window.log.transports.console.level = 'silly'; // 修改输出到文件的时候，默认的输出日志级别, 默认为warn。

window.log.error("error");
window.log.warn("warn");
window.log.info("info");
window.log.verbose("verbose");
window.log.debug("debug");
window.log.silly("silly");
window.log.warn('这是个警告日志');
console.log("---", window.fs, window.ex , window.os , window.node_path, window.dialog , window.db)

if (process.env.NODE_ENV === 'test') {
    console.log("test environment")
    window.electronRequire = require
  }