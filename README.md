# fria

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## How to Deploy the Website
### Move staff to AWS
```
ssh -i ~/Downloads/SynSpot_Website_RSA.pem ubuntu@ec2-18-117-134-124.us-east-2.compute.amazonaws.com
```
```
sudo cp -r ~/dist/* /var/www/html/
```