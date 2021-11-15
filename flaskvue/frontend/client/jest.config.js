module.exports = {
    preset: 'ts-jest',
    "moduleFileExtensions": [
        "js",
        "json",
        "vue"
      ],
    transform: {
      '^.+\\.(ts|tsx)?$': 'ts-jest',
      "^.+\\.(js|jsx)$": "babel-jest",
      "^[^.]+.vue$": "vue-jest",
    },
    // "globals": {
    //     "window": {}
    //   }
    runner: '@jest-runner/electron',
    testEnvironment: '@jest-runner/electron/environment',
    // testRunner: "jest-circus/runner"
    // testEnvironment: "jsdom"
  };

//   "jest": {
//     "moduleFileExtensions": [
//       "js",
//       "json",
//       "vue"
//     ],
//     "transform": {
//       ".*\\.(vue)$": "vue-jest",
//       "^.+\\.js$": "<rootDir>/node_modules/babel-jest"
//     },
//     "moduleNameMapper": {
//       "^@/(.*)$": "<rootDir>/src/$1"
//     },
//     "transformIgnorePatterns": [
//       "/node_modules/(?!vue-awesome)"
//     ]
//   },