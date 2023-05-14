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
    5. vue add electron-builder
    6. npm install
    7. npm run electron:serve


2. launch after first time:
    1. cd into frontend/client, npm install
    2. npm run electron:serve

3. package:
    1. npm run dist






