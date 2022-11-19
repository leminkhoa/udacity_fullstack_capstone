import flask 
from flask import jsonify

controllers_blueprint = flask.Blueprint('index', __name__)


TRANSACTIONS_PER_PAGE = 5


def paginate_transactions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * TRANSACTIONS_PER_PAGE
    end = start + TRANSACTIONS_PER_PAGE

    transactions = [transaction.format() for transaction in selection]
    current_transactions = transactions[start:end]
    return current_transactions


@controllers_blueprint.route('/hello')
def hello():
    return jsonify(
        {'message': 'Hello World'}
    ), 200
