import sys
from datetime import datetime, timezone

from flask import jsonify, abort, request
from sqlalchemy import exc

from models.models import Transaction
from models.request_schema import *
from utils import *
from auth import requires_auth
from . import controllers_blueprint, paginate_transactions


@controllers_blueprint.route('/transactions')
@requires_auth('get:transaction')
def get_transactions(payload):
    # Get users
    try:
        transactions = Transaction.query.\
            order_by(Transaction.date.desc()).\
            all()       
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


@controllers_blueprint.route('/transactions/search')
@requires_auth('get:transaction')
def search_transactions(payload):
    body = request.get_json()
    # Validate request
    schema = SearchTransactionRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Get search term
    start_date = body.get('start_date')
    end_date = body.get('end_date')
    # Get users
    try:
        transactions = Transaction.query.\
            filter(Transaction.date >= start_date).\
            filter(Transaction.date < end_date).\
            order_by(Transaction.date.desc()).\
            all()
    except:
        print(sys.exc_info())
        abort (500)
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
@requires_auth('create:transaction')
def create_transaction(payload):
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
        category_id = body.get('category_id'),
        date = request_date,
        amount = body.get('amount'),
        currency = body.get('currency'),
        note = body.get('note', '')
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


@controllers_blueprint.route('/transactions/<string:id>', methods=['PATCH'])
@requires_auth('update:transaction')
def update_transaction(payload, id):
    body = request.get_json()
    # Validate request
    schema = CreateTransactionRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Get title and recipe
    category_id = body.get('category_id')
    date = body.get('date')
    amount = body.get('amount')
    currency = body.get('currency')
    note = body.get('note')
    try:
        to_be_updated_transaction = Transaction.query.\
            filter(Transaction.id == id).\
            one_or_none()
    except:
        print(sys.exc_info())
        abort (500)
    # If cannot find transaction id, return 404
    if to_be_updated_transaction is None:
        abort (404)
    # Update
    try:
        to_be_updated_transaction.category_id = category_id
        to_be_updated_transaction.date = date
        to_be_updated_transaction.amount = amount
        to_be_updated_transaction.currency = currency
        to_be_updated_transaction.note = note
        # Commit
        to_be_updated_transaction.update()
    except exc.IntegrityError:
        print(sys.exc_info())
        abort (422)
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'transaction': to_be_updated_transaction.format()
    })


@controllers_blueprint.route('/transactions/<string:id>', methods=['DELETE'])
@requires_auth('delete:transaction')
def delete_transaction(payload, id):
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
