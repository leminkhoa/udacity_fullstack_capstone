import random
import sys

from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from models.models import setup_db
from .controllers import (
    controllers_blueprint, 
    controllers_transactions,
    controllers_users
)
from .error_handler import errorhandler_blueprint


TRANSACTIONS_PER_PAGE = 5


def paginate_transactions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * TRANSACTIONS_PER_PAGE
    end = start + TRANSACTIONS_PER_PAGE

    transactions = [transaction.format() for transaction in selection]
    current_transactions = transactions[start:end]
    return current_transactions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # Load config
    app.config.from_object('config')
    # Set up error handler
    app.register_blueprint(error_handler.errorhandler_blueprint)
    # Set up app route
    app.register_blueprint(controllers_blueprint)
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
