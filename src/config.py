from os import environ as env


class DefaultConfig(object):
    DEBUG = False
    PORT = 5000
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_pass = 'example'
    db_name = 'clicker_mania'
    db_config = {
        'host': '127.0.0.1',  # Change this to the IP of your MySQL container if needed
        'port': 3306,
        'user': 'root',
        'password': 'mysecretpassword',  # The password you set when starting the container
        'db': 'clicker_mania',  # Change this to your database name
    }


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_pass = 'example'
    db_name = 'clicker_mania'
    # db_config = {
    #     'host': '127.0.0.1',  # Change this to the IP of your MySQL container if needed
    #     'port': 3306,
    #     'user': 'root',
    #     'password': 'mysecretpassword',  # The password you set when starting the container
    #     'db': 'clicker_mania',  # Change this to your database name
    # }


class ProductionConfig(DefaultConfig):
    PORT = 8080


# Docker
mysql_user = env.get("MYSQL_USER", "root")
mysql_pw = env.get("MYSQL_PW", "example")
mysql_host = env.get("MYSQL_HOST", "127.0.0.1")
mysql_port = env.get("MYSQL_PORT", "3306")
mysql_db = env.get("MYSQL_DB", "clicker_mania")

sql_table_configs = {

    "users_table": ("CREATE TABLE IF NOT EXISTS `users_table` ("
                    "`user_id` VARCHAR(255) PRIMARY KEY,"
                    "`name` VARCHAR(255) NOT NULL,"
                    "`dob` DATE NOT NULL,"
                    "`email` VARCHAR(255) NOT NULL,"
                    "`phone_number` VARCHAR(255) NOT NULL,"
                    "`creation_timestamp` TIMESTAMP NOT NULL,"
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),

    "pet_table": ("CREATE TABLE IF NOT EXISTS `pets_table` ("
                  "`pet_id` VARCHAR(255) PRIMARY KEY,"
                  "`name` VARCHAR(255) NOT NULL,"
                  "`dob` DATE NOT NULL,"
                  "`gender` VARCHAR(10) NOT NULL,"
                  "`creation_timestamp` TIMESTAMP NOT NULL,"
                  "`age` INT NOT NULL,"
                  "`total_clicks` INT NOT NULL"
                  "`user_id` VARCHAR(255) NOT NULL"
                  " FOREIGN KEY (`user_id`) REFERENCES users_table (`user_id`),"
                  ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),

    "tricks_table": ("CREATE TABLE IF NOT EXISTS `tricks_table` ("
                     "`trick_id` VARCHAR(255) PRIMARY KEY,"
                     "`trick_name` VARCHAR(255) NOT NULL"
                     "`pet_id` VARCHAR(255) NOT NULL"
                     " FOREIGN KEY (`pet_id`) REFERENCES pets_table (`pet_id`),"
                     ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"),

    "clicks_table": ("CREATE TABLE IF NOT EXISTS `clicks_table` ("
                     "`click_id` VARCHAR(255) PRIMARY KEY,"
                     "`timestamp` TIMESTAMP NOT NULL,"
                     "`treat_likelihood` INT NOT NULL,"
                     "`treated` BOOLEAN NOT NULL,"
                     "`pet_id` VARCHAR(255) NOT NULL,"
                     "`trick_id` VARCHAR(255) NOT NULL,"
                     "FOREIGN KEY (`pet_id`) REFERENCES pets_table (`pet_id`),"
                     "FOREIGN KEY (`trick_id`) REFERENCES tricks_table (`trick_id`)"
                     ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin")
}
