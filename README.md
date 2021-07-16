# Apollo

EC2:

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

**Key Operation:**

1. ls | grep keyname.pem

2. sudo chmod 0600 keyname.pem

3. ssh-add keyname.pem

4. ssh ubuntu@<YOUR_IP_ADDRESS> (IPV4 address of the EC2 Instance, for example, 18.222.25.78)

5. ssh -i keyname.pem ubuntu@server (server is the IPV4 DNS of the EC2 Instance, for example: ec2-18-222-25-78.us-east-2.compute.amazonaws.com (our first instance))    (do 3 and (4 or 5))

   **First Login:**

6. sudo apt update

7. sudo apt install python3 python3-pip tmux htop

8. sudo pip3 install pipenv

**Clone File from Github:**
git clone https://github.com/AI-Apollo/Apollo.git
cd Apollo/flaskvue/backend

sudo passwd(first time)

su (password: 1)

pipenv install
pipenv shell

```py
pipenv install flask
```

gunicorn --bind 0.0.0.0:80 manage:app (run)

```py
sudo fuser -k 8000/tcp (清除端口)
```

**Some Bugs:**
OSError: [Errno 98] Address already in use
ps -fA | grep python
kill kidnum
