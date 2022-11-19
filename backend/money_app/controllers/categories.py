import sys
from datetime import datetime, timezone

from flask import jsonify, abort, request
from sqlalchemy import exc

from models.models import Category
from models.request_schema import *
from utils import *
from . import controllers_blueprint, paginate_transactions

@controllers_blueprint.route('/categories')
def get_categories():
    # Get users
    try:
        categories = Category.query.all()
    except:
        print(sys.exc_info())
        abort (500)
    # If there is no category, return 404
    if len(categories) == 0:
        abort (404)
    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = {
            'transaction_type_id': category.transaction_type_id,
            'transaction_type': category.transaction_type.type,
            'type': category.type

        }
    return jsonify({
        'success': True,
        'categories': categories_dict,
        'total_categories': len(categories),
    })


@controllers_blueprint.route('/categories', methods=['POST'])
def create_category():
    # Request input
    body = request.get_json()
    # Validate request
    schema = CreateCategoryRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Create a new category
    new_category = Category(
        id=str(generate_uuid()),
        transaction_type_id=body.get('transaction_type_id'),
        type=body.get('type')
    )
    # Insert
    try:
        new_category.insert()
    except exc.IntegrityError:
        print(sys.exc_info())
        abort (422)
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'created': new_category.id,
        'total_categories': len(Category.query.all())
    })


@controllers_blueprint.route('/categories/<string:id>', methods=['DELETE'])
def delete_category(id):
    try:
        category = Category.query.filter(Category.id == id).one_or_none()
    except:
        print(sys.exc_info())
        abort (500)
    # If cannot find requested id, return 404
    if category is None:
        abort (404)
    try:
        category.delete()
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'deleted': id,
        'total_categories': len(Category.query.all())
    })