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
        builderOptions: {
          "productName": "Apollo",
          "appId": "com.apollo.app",
          "compression": "store",
          // "win": {
          //   "target": [
          //     {
          //       "target": "nsis",
          //       "arch": [
          //         "x64"
          //       ]
          //     }
          //   ]
          // },
          // "nsis": {
          //   "oneClick": false,
          //   "perMachine": true,
          //   "allowElevation": true,
          //   "allowToChangeInstallationDirectory": true,
          //   "createDesktopShortcut": true,
          //   "createStartMenuShortcut": true
          // },
          "linux": {
            "target": [
              "AppImage"
            ]
          },
          "extraResources": ["./dist/**"],
          "directories": {
            "output": "./build"
          }

        }
      }
    }
    
  }