import pymysql
from os import environ as env


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


# Docker
mysql_user = env.get("MYSQL_USER", "root")
mysql_pw = env.get("MYSQL_PW", "example")
mysql_host = env.get("MYSQL_HOST", "127.0.0.1")
mysql_port = env.get("MYSQL_PORT", "3306")
mysql_db = env.get("MYSQL_DB", "clicker_mania")


sql_table_configs = {
    "pet_table": ("CREATE TABLE IF NOT EXISTS `pets_table` ("
                          "  `pet_id` INT AUTO_INCREMENT PRIMARY KEY,"
                          "  `name` VARCHAR(255) NOT NULL,"
                          "  `dob` DATE NOT NULL,"
                          "  `gender` VARCHAR(10) NOT NULL,"
                          "  `creation_timestamp` TIMESTAMP NOT NULL,"
                          "  `age` INT NOT NULL,"
                          "  `total_clicks` INT NOT NULL,"
                          ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),

    "clicks_table": ("CREATE TABLE IF NOT EXISTS `clicks_table` ("
                          "  `click_id` INT AUTO_INCREMENT PRIMARY KEY,"
                          "  `timestamp` TIMESTAMP NOT NULL,"
                          "  `treat_likelihood` INT NOT NULL,"
                          "  `pet_id` INT NOT NULL,"
                          "  `treated` BOOLEAN NOT NULL,"
                          "  `trick_id` INT NOT NULL,"
                          "  FOREIGN KEY (`pet_id`) REFERENCES Pet (`pet_id`)"
                          "  FOREIGN KEY (`trick_id`) REFERENCES Trick (`trick_id`)"  
                          ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),

    "tricks_table": ("CREATE TABLE IF NOT EXISTS `tricks_table` ("
                     "  `trick_id` INT AUTO_INCREMENT PRIMARY KEY,"
                     "  `trick_name` VARCHAR(255) NOT NULL,"
                     ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),
}
