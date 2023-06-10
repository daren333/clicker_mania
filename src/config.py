class DefaultConfig(object):
    DEBUG = False
    PORT = 5000


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    PORT = 8080
