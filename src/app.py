import logging
import sys

from flask import Flask
import os

from src.routes.pets_api import pets_blueprint
from src.routes.clicks_api import clicks_blueprint
from src.routes.tricks_api import tricks_blueprint
from src.routes.users_api import users_blueprint


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


def create_app():
    # Get the config name from environment variable or use 'development' as default
    config_name = os.environ.get('FLASK_CONFIG', 'development')
    logger = logging.Logger("api_logger")

    app = Flask(__name__)
    app.config.from_object(DefaultConfig)

    # Load configuration based on config_name
    # if config_name == 'development':
    #     app.config.from_object('config.DevelopmentConfig')
    #     logger.info("Running in development mode")
    # elif config_name == 'production':
    #     app.config.from_object('config.ProductionConfig')
    #     logger.info("Running in production mode")
    # else:
    #     app.config.from_object('config.DefaultConfig')
    #     logger.info("Running in development mode")

    # Import and register routes
    app.register_blueprint(users_blueprint)
    app.register_blueprint(pets_blueprint)
    app.register_blueprint(clicks_blueprint)
    app.register_blueprint(tricks_blueprint)

    return app


if __name__ == '__main__':
    logger = logging.Logger("api_logger")

    print("current dir: %s" % os.getcwd(), flush=True)
    print("ls: %s" % os.listdir(os.getcwd()), flush=True)
    print("python path: %s" % sys.path, flush=True)

    config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = create_app()
    # logger.info("after create app before run")
    app.run()
