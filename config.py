import os
basedir = os.path.abspath(os.path.dirname(__file__))


###note - in the system folder, file where / before you run python ... (flask app)
##will need to run ```export APP_SETTINGS="config.DevelopmentConfig"``` in order 
##to transfer over, tell python which config settings to bring over 


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    POSTGRES = {
    'user': 'hants2',
    'pw': '46566656',
    'db': 'mytest4',
    'host': 'localhost',
    'port': '5432',}

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
