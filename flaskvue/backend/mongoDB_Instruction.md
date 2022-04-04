1. How to install and run MongoDB on local computer? How to create a new Database?
2. How to connect MongoDB on cloud?
3. How to connect MongoDB with flask?
4. Which MongoDB GUI should I choose?
5. How to write query?
6. How to test query?

# 1. How to install and run MongoDB on local computer? How to create a new Database?
Mac Installation: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
Create Database Instruction: https://www.mongodb.com/basics/create-database

1. Download the official Homebrew formula for MongoDB and the Database Tools
brew tap mongodb/brew
2. Install MongoDB
brew install mongodb-community@5.0
3. Run MongoDB as a macOS service
brew services start mongodb-community@5.0
4. Check if MongoDB is started, you should see the service mongodb-community listed as started.
brew services list
5. If you type 127.0.0.1:27017 in your brower, you shall see
'It looks like you are trying to access MongoDB over HTTP on the native driver port.'
5. Begin using MongoDB, connect mongosh to the running instance
mongosh
6. create database. mysynspot_db will be created when the insert command has been applied.
use mysynspot_db
db.user.insert({name: "Ada Lovelace", age: 205})
7. Check if new db has been created
show dbs
8. Stop a mongod running as a macOS service
brew services stop mongodb-community@5.0

# 2. How to connect MongoDB on cloud?
Follow the link: https://www.mongodb.com/basics/create-database

# 3. How to connect MongoDB with flask?
We use flask-PyMongo to connect mongoDB and flask instead of Mongoengine or MongoAlchemy due to the restriction of ORM (https://stackoverflow.com/questions/9447629/mongokit-vs-mongoengine-vs-flask-mongoalchemy-for-flask). flask-PyMongo is a wrapper of PyMongo. If you want to check the api, go find the documentation of PyMongo.

Here is the link for PyMongo Collection-level Api: https://www.osgeo.cn/mongo-python-driver/api/pymongo/collection.html

1. In setting.py, add config as following:
# You can change Database_name to the db you created
local_host = '127.0.0.1'
Database_name = 'mysynspot_db'
MONGO_URI = "mongodb://%s:27017/%s" % (local_host, Database_name)
mongodb://127.0.0.1:27017/mysynspot_db
mongodb://127.0.0.1:27017/unittest_db
2. In extensions.py, add:
from flask_pymongo import PyMongo
pyMongo = PyMongo()
3. In __init__.py, add:
# add in configure_extensions()
pyMongo.init_app(app)

# 4. Which MongoDB GUI should I choose?



# 5. How to write query?
pyMongo.db.Test_Match.find_one({key: value})
pyMongo.db.Test_Match.insert_one({key: value})

# 6. How to test query?
改unittest


assistor_random_id_pair => assistor_random_id