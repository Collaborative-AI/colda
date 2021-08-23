# client
1. first time launch:
    1. cd into frontend/client
    2. sudo apt install npm 
    3. npm install --global yarn
    4. #update node
    
        sudo npm cache clean -f

        sudo npm install -g n

        sudo n stable

        PATH="$PATH"
    5. sudo snap install vue
    6. yarn install

2. launch after first time:
    1. cd into frontend/client, yarn install
    2. yarn run electron:serve

3. package:
    1. cd into frontend/client, yarn install
    2. yarn run electron:build

Simple Test Flow:
    1. After lauching the packaged APP, Open 2 operation interfaces. 
        - Account 1(Sponsor): Username: testa password: 123
        - Account 2(Assistor): Username: testb password: 123
    2. In Account 2 operation interface, go to setting, update 4 default data paths. Then, click ResponsePicked in the top bar.
    3. In Account 1 operation interface, click call for help and start training.




