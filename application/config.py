import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configration"""


class ProductionConfig(Config):
    """Production configration"""


class DevelopmentConfig(Config):
    """Development configration"""


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
