import sys
from datetime import datetime, timezone

from flask import jsonify, abort, request
from sqlalchemy import exc

from models.models import Category
from models.request_schema import *
from utils import *
from auth import requires_auth
from . import controllers_blueprint, paginate_transactions


@controllers_blueprint.route('/categories')
@requires_auth('get:category')
def get_categories(payload):
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


@controllers_blueprint.route('/categories/search', methods=['POST'])
@requires_auth('get:category')
def search_categories(payload):
    body = request.get_json()
    # Validate request
    schema = SearchCategoryRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Get search term
    search_term = body.get('searchTerm')
    # Query to find matched questions
    try:
        categories = Category.query.\
            filter(Category.type.ilike(f'%{search_term}%')).\
            all()
    except:
        print(sys.exc_info())
        abort (500)
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
@requires_auth('create:category')
def create_category(payload):
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


@controllers_blueprint.route('/categories/<string:id>', methods=['PATCH'])
@requires_auth('update:category')
def update_category(payload, id):
    body = request.get_json()
    # Validate request
    schema = UpdateCategoryRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Get title and recipe
    transaction_type_id = body.get('transaction_type_id')
    type = body.get('type')
    try:
        to_be_updated_category = Category.query.filter(Category.id == id).one_or_none()
    except:
        print(sys.exc_info())
        abort (500)
    # If cannot find category id, return 404
    if to_be_updated_category is None:
        abort (404)
    # Update
    try:
        to_be_updated_category.transaction_type_id = transaction_type_id
        to_be_updated_category.type = type
        # Commit
        to_be_updated_category.update()
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'category': to_be_updated_category.format()
    })


@controllers_blueprint.route('/categories/<string:id>', methods=['DELETE'])
@requires_auth('delete:category')
def delete_category(payload, id):
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
