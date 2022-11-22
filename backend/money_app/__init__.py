import collections
import collections.abc
import logging
from logging import Formatter, FileHandler

from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from models.models import setup_db
from .controllers import (
    controllers_blueprint, 
    transactions,
    categories,
    token
)
from .error_handler import errorhandler_blueprint


collections.Callable = collections.abc.Callable


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # Load config
    app.config.from_object('config')
    # Set up error handler
    app.register_blueprint(error_handler.errorhandler_blueprint)
    # Set up app route
    app.register_blueprint(controllers_blueprint)
    # Set up logging
    if not app.debug:
        file_handler = FileHandler('error.log')
        file_handler.setFormatter(
            Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        )
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    # Set up db
    setup_db(app)
    # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    return app
