from src import config
import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine
import src.config


def connect_to_db():
    try:
        cnx = mysql.connector.connect(user=config.mysql_user,
                                      password=config.mysql_pw,
                                      host=config.mysql_host,
                                      port=config.mysql_port)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx


def init_mysql_db(engine):
    create_database(engine, "clicker_mania")
    create_sql_tables(engine)


def create_database(engine, db_name):
    connection = engine.connect()
    try:
        connection.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

    try:
        connection.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database {} created successfully.".format(db_name))
            connection.database = db_name
        else:
            print(err)
            exit(1)


def create_sql_tables(engine):
    cursor = engine.connect()
    cursor.execute("USE %s" % config.mysql_db)

    for table in config.sql_table_configs.keys():
        try:
            print("Creating table {}: ".format(table), end='')
            cursor.execute(config.sql_table_configs[table])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("Created Table: %s" % table)


if __name__ == "__main__":
    print(config.mysql_host)
    engine = create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    init_mysql_db(engine)
