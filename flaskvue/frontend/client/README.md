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






