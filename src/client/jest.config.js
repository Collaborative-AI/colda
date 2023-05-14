module.exports = {

    preset: '@vue/cli-plugin-unit-jest/presets/no-babel',
    "moduleFileExtensions": [
        "js",
        "json",
        "vue"
      ],
    // roots: [
    //   '<rootDir>/test',
    // ],
    transform: {
      '^.+\\.(ts|tsx)?$': 'ts-jest',
      "^.+\\.(js|jsx)$": "babel-jest",
      "^[^.]+.vue$": "vue-jest",
    },
    // "globals": {
    //     "window": {}
    //   }
    "verbose": false,
    // testMatch: ['**/__tests__/*.js?(x)'],
    // "runner": "jest-electron/runner",
    // "testEnvironment": "jest-electron/environment"
    
    // "runner": "jest-electron/runner",
    // "testEnvironment": "node"


    // runner: '@jest-runner/electron',
    // testEnvironment: '@jest-runner/electron/environment',
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
