import logging

from flask import Flask
import os
from src.routes.pets_api import pets_blueprint
from src.routes.clicks_api import clicks_blueprint
from src.routes.tricks_api import tricks_blueprint
from src.routes.users_api import users_blueprint


def create_app(config_name, logger):
    # Get the config name from environment variable or use 'development' as default
    #config_name = os.environ.get('FLASK_CONFIG', 'development')
    #logger = logging.Logger("api_logger")

    app = Flask(__name__)

    # Load configuration based on config_name
    if config_name == 'development':
        app.config.from_object('config.DevelopmentConfig')
        logger.info("Running in development mode")
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')
        logger.info("Running in production mode")
    else:
        app.config.from_object('config.DefaultConfig')
        logger.info("Running in development mode")

    # Import and register routes

    app.register_blueprint(users_blueprint)
    app.register_blueprint(pets_blueprint)
    app.register_blueprint(clicks_blueprint)
    app.register_blueprint(tricks_blueprint)

    return app


if __name__ == '__main__':
    logger = logging.Logger("api_logger")

    config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = create_app(config_name, logger)
    logger.info("after create app before run")
    app.run()
