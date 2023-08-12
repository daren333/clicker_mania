import pymysql


class DefaultConfig(object):
    DEBUG = False
    PORT = 5000
    db_config = {
        'host': 'localhost',  # Change this to the IP of your MySQL container if needed
        'port': 3306,
        'user': 'root',
        'password': 'mysecretpassword',  # The password you set when starting the container
        #'db': 'mydatabase',  # Change this to your database name
    }


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    PORT = 8080
