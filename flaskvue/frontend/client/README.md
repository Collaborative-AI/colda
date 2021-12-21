# client
1. first time launch:
    1. cd into frontend/client
    2. sudo apt install npm 
    3. #update node
    
        sudo npm cache clean -f

        sudo npm install -g n

        sudo n stable

        PATH="$PATH"
    4. sudo snap install vue
    5. npm install
    6. ./node_modules/.bin/electron-rebuild (If bug on windows: .\node_modules\.bin\electron-rebuild.cmd)

2. launch after first time:
    1. cd into frontend/client, npm install
    2. npm run electron:serve

3. package:
    1. cd into frontend/client, npm install
    2. npm run electron:build

4. Unittest:
    1. npm run test
    "test": "ELECTRON_RUN_AS_NODE=true ./node_modules/.bin/electron ./node_modules/.bin/jest"
    2. jest path/to/my-test.js => test single file

    
Simple Test Flow:
    1. After lauching the packaged APP, Open 2 operation interfaces. 
        - Account 1(Sponsor): Username: testa password: 123
        - Account 2(Assistor): Username: testb password: 123
    2. In Account 2 operation interface, go to setting, update 4 default data paths. Then, click ResponsePicked in the top bar.
    3. In Account 1 operation interface, click call for help and start training.



    mac os install environment procedure:

    1. first time lauch:

        1. download node package and install it(this will install node and npm)

        2. su

           input your password

    2. lauch after first time

        1. cd into frontend/client

        2. npm install

        3. npm run electron:serve

    3. package:

        1. cd into frontend/client

        2. npm install

        3. npm run electron:build


test procedure:

format:
    目标，当前块在测试什么？期望的结果是什么？
    可能的错误，可能的错误有哪些？
    执行步骤：list

Auto train procedure: expect history page complete log, no crash during training and testing process
step: 1. assistor sets setting page, set mode auto, update setting
      2. sponsor starts a task on request page
      3. sponsor and assistor check history page for log info

Auto test procedure: expect history page complete log, no crash during training and testing process
step: 1. sponsor press test on history record page, go to test request page
      2. sponsor starts a test request
      3. sponsor and assistor check history page for log info

Manual train procedure: expect history page complete log, no crash during training and testing process
step: 1. assistor sets setting page, set mode manual, update setting
      2. sponsor starts a task on request page
      3. assistor goes to pending page, choose pending record, go to pending record page
      4. 
        4.1 assistor fill in path info, accept
        4.2 assistor reject
      5. sponsor and assistor check history page for log info

Manual test procedure: expect history page complete log, no crash during training and testing process
step: 1. sponsor press test on history record page, go to test request page
      2. sponsor starts a test request
      3. assistor goes to pending page, choose pending record, go to pending record page
      4. 
        4.1 assistor fill in path info, accept
        4.2 assistor reject
      5. sponsor and assistor check history page for log info

sponsor and assistor swap roles
multiple assistor test

better-sqlite3: https://github.com/JoshuaWise/better-sqlite3/blob/master/docs/api.md
    




