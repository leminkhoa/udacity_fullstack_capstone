import sys
from datetime import datetime, timezone

from flask import jsonify, abort, request
from sqlalchemy import exc

from models.models import Transaction
from models.request_schema import *
from utils import *
from . import controllers_blueprint, paginate_transactions

@controllers_blueprint.route('/transactions')
def get_transactions():
    # Get users
    try:
        transactions = Transaction.query.all()
    except:
        print(sys.exc_info())
        abort (500)
    # If there is no users, return 404
    if len(transactions) == 0:
        abort (404)
    # Paginate
    try:
        current_transactions = paginate_transactions(request, transactions)
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'transactions': current_transactions,
        'total_transactions': len(transactions),       
    })


@controllers_blueprint.route('/transactions', methods=['POST'])
def create_transactions():
    # Request input
    body = request.get_json()
    # Validate request
    schema = CreateTransactionRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # If no date found in request, use current utc
    if body.get('date'):
        request_date = body.get('date')
    else:
        request_date = datetime.utcnow()
    # Create a new transaction
    new_transaction = Transaction(
        id = str(generate_uuid()),
        user_id = body.get('user_id'),
        category_id = body.get('category_id'),
        date = request_date,
        amount = body.get('amount'),
        currency = body.get('currency')
    )
    # Insert
    try:
        new_transaction.insert()
    except exc.IntegrityError:
        print(sys.exc_info())
        abort (422)
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'created': new_transaction.id,
    })


@controllers_blueprint.route('/transactions/<string:id>', methods=['DELETE'])
def delete_transaction(id):
    try:
        transaction = Transaction.query.filter(Transaction.id == id).one_or_none()
    except:
        print(sys.exc_info())
        abort (500)
    # If cannot find requested id, return 404
    if transaction is None:
        abort (404)
    try:
        transaction.delete()
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'deleted': id,
    })
