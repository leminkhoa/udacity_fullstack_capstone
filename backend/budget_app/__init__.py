import random
import sys

from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from . import error_handler, controllers


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
    app.config.from_object('config.AppConfig')
    # Set up error handler
    app.register_blueprint(error_handler.blueprint)
    # Set up app route
    app.register_blueprint(controllers.blueprint)
    # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    return app
