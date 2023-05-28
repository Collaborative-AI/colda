# README

## Usage

Run the following command to launch the software for the first time:

```bash
cd client

sudo apt install npm

# update node
sudo npm cache clean -f
dudo npm install -g n
sudo n stable
PATH = "$PATH"

sudo snap install vue

npm install

npm run electron:serve

./node_modules/.bin/electron-rebuild # If there is bug on windows: .\node_modules\.bin\electron-rebuild

```

Run the following command to launch the software after first time:

```bash
cd client

npm install

npm run electron:serve
```

Run the following command to package the software:

```bash
cd client

npm install

npm run electron:build
```

Run the following command to run unittest:

```bash
npm run test
```

## Instructions

 - `Navbar.vue` presents the software navigation bar, and the communication between the software and the backend is mainly completed by the functions in this file
 - `assets` folder contains image, font, css resources used in the software
 - `components` folder contains reusable interface components
 - `network` folder contains request sending and interception configuration
 - `router` folder conatins routing configuration file
 - `store` folder is used store some local information
 - `Notifications` folder contains functions that handle notifications and history
 - `Auth` folder contains functions that handle user registration and login
 - `Settings` folder contains functions that handle user customized settings
 - `tests` folder contains unittest function
 