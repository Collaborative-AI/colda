# Apollo

**AWS EC2:**

1. **Create EC2:**

   Apollo_EC2_Server1

   **Amazon Machine Image(AMI):**
   Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - ami-0b9064170e32bde34 (64-bit x86) / ami-026141f3d5c6d2d0c (64-bit Arm)
   **Instance Type:**
   t2.micro
   **Storage:**
   8GB
   **Security Group:**
   HTTP Port 80 Source: Anywhere
   Custom TCP Port 8080 Source: Anywhere
   SSH Port 22 Source: Anywhere
   HTTPS Port 443 Source: Anywhere
   **Launch and create a key pair**

2. **Connect to EC2:**

   0. Download the **key**

   1. cd into the key file, ls | grep keyname.pem  (first time)

   2. sudo chmod 0600 keyname.pem (first time)

   3. ssh-add keyname.pem (every time)

   4. ssh ubuntu@<YOUR_IP_ADDRESS> (IPV4 address of the EC2 Instance, for example, 18.222.25.78)

   5. ssh -i keyname.pem ubuntu@server (server is the IPV4 DNS of the EC2 Instance, for example: ec2-18-222-25-78.us-east-2.compute.amazonaws.com (our first instance))    (**do (4 or 5) for connection**)

      **First Login to EC2:**

      1. sudo apt update
      2. sudo apt install python3 python3-pip tmux htop
      3. sudo pip3 install pipenv
      4. sudo apt-get install python-flask
      5. sudo apt install python3-flask


**Clone File from Github:**
git clone https://github.com/AI-Apollo/Apollo.git (first time)

sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1  (first time)

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2 (first time)

sudo update-alternatives --config python (type in 2, enter; first time)

cd Application/flaskvue/backend

sudo passwd (first time)

su (password: 1) (every time)

pipenv install (every time)

pipenv shell (every time)

pipenv install gunicorn==19.7.1 （every time）

screen

gunicorn --bind 0.0.0.0:80 manage:app ((every time for running)

ctrl a + d

```py

```

**Some Bugs:**
OSError: [Errno 98] Address already in use
ps -fA | grep python
kill kidnum



sudo fuser -k 80/tcp (gunicorn connection fail)

screen

ctrl a + d (detached screen inside)

ctrl a + k (kill screen inside)

screen -D -r screenID (cant connect attached)

screen -ls

screen -r screenID (login screen)

screen -S screenID (new screen)



screen -D screenID (detach screen outside)

screen -XS screenID quit (kill screen outside)



tmux 

**Client:**

1. **first time launch:**
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


2. **launch after first time:**
   1. cd into frontend/client, npm install
   2. npm run electron:serve



**Server**:

1. **First time launch:**
   1. cd into backend
   2. pip install pipenv
   3. pipenv lock
   4. pipenv install
   5. pipenv shell
   6. flask run
   7. flask --app application run --debug --port 5000

2. **launch after first time**
   1. pipenv install
   2. pipenv shell
   3. flask run

