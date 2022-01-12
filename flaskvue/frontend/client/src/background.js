import { app, protocol, BrowserWindow } from 'electron';
import { createProtocol } from 'vue-cli-plugin-electron-builder/lib';
import installExtension, { VUEJS_DEVTOOLS } from 'electron-devtools-installer';

// const { app, protocol, BrowserWindow } = require('electron')
// const { createProtocol } = require('vue-cli-plugin-electron-builder/lib')
// const installExtension = require('electron-devtools-installer').default
// const { VUEJS_DEVTOOLS } = require('electron-devtools-installer').default
// console.log("app---------", app)
// console.log("protocol", protocol)
// console.log("BrowserWindow", BrowserWindow)

const isDevelopment = process.env.NODE_ENV !== 'production';
const path = require('path');
// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: 'app', privileges: { secure: true, standard: true } },
]);

async function createWindow() {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    // frame: false,
    webPreferences: {

      // Use pluginOptions.nodeIntegration, leave this alone
      // See nklayman.github.io/vue-cli-plugin-electron-builder/guide/
      // security.html#node-integration for more info

      // nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION, (default is false)
      // nodeIntegration: false => cannot use window.require to call node module in rendering process
      nodeIntegration: true,
      enableRemoteModule: true, // 允許在 Render Process 使用 Remote Module
      contextIsolation: false, // 讓在 preload.js 的定義可以傳遞到 Render Process (React)
      // preload: node_path.join(__dirname, "../src/preload.js")
      // contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION, (default is true)
    },
  });
  // win.webContents.openDevTools({mode:'right'});
  if (process.env.WEBPACK_DEV_SERVER_URL) {
    console.log(process.env.WEBPACK_DEV_SERVER_URL)
    // Load the url of the dev server if in development mode
    await win.loadURL(process.env.WEBPACK_DEV_SERVER_URL);
    console.log("process.env.WEBPACK_DEV_SERVER_URL", process.env.WEBPACK_DEV_SERVER_URL)
    // console.log('app get path', app.getAppPath(), path.join(app.getAppPath(), '../src/preload.js'))
    win.webContents.openDevTools();
    if (!process.env.IS_TEST) win.webContents.openDevTools();
  } else {
    createProtocol('app');
    // Load the index.html when not in development
    // win.loadURL('app://./resources/app/index.html');
    // win.loadURL('file://' + __dirname + '/index.html')
    console.log("hello")
    win.loadURL('app://./index.html')
    //win.loadURL(node_path.join(__dirname, '/index.html'))
    //win.loadURL('https://www.google.com/?hl=zh-cn')
    win.webContents.openDevTools();
    console.log("h1")
  }
}

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    try {
      await installExtension(VUEJS_DEVTOOLS);
    } catch (e) {
      console.error('Vue Devtools failed to install:', e.toString());
    }
  }
  createWindow();
});

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === 'win32') {
    process.on('message', (data) => {
      if (data === 'graceful-exit') {
        app.quit();
      }
    });
  } else {
    process.on('SIGTERM', () => {
      app.quit();
    });
  }
}
