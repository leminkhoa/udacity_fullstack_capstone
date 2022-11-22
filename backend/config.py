import os

SECRET_KEY = os.urandom(32)
ENV = 'dev'
FLASK_RUN_PORT = 8000

# IMPLEMENT DATABASE URL
DATABASE_NAME = os.getenv('DB_NAME', 'budget_db')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://{}/{}'.format('postgres:abc@localhost:5432', DATABASE_NAME))
SQLALCHEMY_TRACK_MODIFICATIONS = False
