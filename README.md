# Apollo

EC2:
Amazon Machine Image(AMI):
Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - ami-0b9064170e32bde34 (64-bit x86) / ami-026141f3d5c6d2d0c (64-bit Arm)
Instance Type:
t2.micro
Storage:
8GB
Security Group:
HTTP Port 80 Source: Anywhere
Custom TCP Port 8080 Source: Anywhere
SSH Port 22 Source: Anywhere
HTTPS Port 443 Source: Anywhere
Launch and create a key pair

Key Operation:
1. ls | grep keyname.pem
2.  sudo chmod 0600 keyname.pem
3. ssh-add keyname.pem
4. ssh ubuntu@<YOUR_IP_ADDRESS> (IPV4 address of the EC2 Instance, for example, 18.222.25.78)
3. ssh -i keyname.pem ubuntu@server (server is the IPV4 DNS of the EC2 Instance, for example: ec2-18-222-25-78.us-east-2.compute.amazonaws.com (our first instance))
4. sudo apt update
5. sudo apt install python3 python3-pip tmux htop
6. mkdir Apolloapp
7. cd Apolloapp

Create the flask file directly:
python3.6 -m venv venv
source venv/bin/activate
pip install Flask==1.1.2 Flask-Cors==3.0.10
pip install flask-script
sudo nano app.py
python app.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)

Restart the instance need to restart the environment:
source venv/bin/activate

Some Bugs:
OSError: [Errno 98] Address already in use
ps -fA | grep python
kill kidnum
