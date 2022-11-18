import os

class AppConfig(object):
    SECRET_KEY = os.urandom(32)
    ENV = 'dev'

    # IMPLEMENT DATABASE URL
    DATABASE_NAME = 'budget_db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}/{}'.format('postgres:abc@localhost:5432', DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
