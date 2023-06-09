module.exports = {
    // configureWebpack: config => {
    //   if (process.env.NODE_ENV === 'production') {
    //     // mutate config for production...
    //     console.log("vvvv")
    //   } else {
    //     // mutate for development...

    //     console.log("zzzz")
    //   }
    // },

    
    publicPath: './',
    pluginOptions: {
      electronBuilder: {
        nodeIntegration: true,
        builderOptions: {
          "productName": "SynSpot",
          "appId": "com.apollothebest.app",
          "compression": "store",
          "win": {
            "target": [
              {
                "target": "nsis",
                "arch": [
                  "x64"
                ]
              }
            ]
          },
          "nsis": {
            "oneClick": false,
            "perMachine": true,
            "allowElevation": true,
            "allowToChangeInstallationDirectory": true,
            "createDesktopShortcut": true,
            "createStartMenuShortcut": true
          },
          "linux": {
            "target": [
              "AppImage"
            ]
          },
          "mac":{
            "target": [
              {
                "target": "dmg",
                "arch": [
                  "x64"
                ]
              }
            ]
          },
          "extraResources": ["./dist/**", "./src/preload.js"],
          "directories": {
            "output": "./build"
          },
          // "asar":false,

        },
        externals:[
          "nedb",
          "electron-log"
        ],
      }
    }
    
  }