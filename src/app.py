import logging

from flask import Flask
import os
from src.routes.pets_api import pets_blueprint
from src.routes.clicks_api import clicks_blueprint


def create_app(config_name, logger):
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

    app.register_blueprint(pets_blueprint)
    app.register_blueprint(clicks_blueprint)

    return app


if __name__ == '__main__':
    # Get the config name from environment variable or use 'development' as default
    config_name = os.environ.get('FLASK_CONFIG', 'development')
    logger = logging.Logger("api_logger")

    app = create_app(config_name, logger)
    app.run()
