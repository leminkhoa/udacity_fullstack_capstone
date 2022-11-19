import sys

from flask import jsonify, abort, request
from sqlalchemy import exc

from models.models import User
from models.request_schema import *
from utils import *
from . import controllers_blueprint


@controllers_blueprint.route('/users')
def get_users():
    # Get users
    try:
        users = User.query.order_by(User.id).all()
    except:
        print(sys.exc_info())
        abort (500)
    # If there is no users, return 404
    if len(users) == 0:
        abort (404)
    users_dict = {}
    for user in users:
        users_dict[user.id] = user.name
    return jsonify({
        'success': True,
        'users': users_dict,
        'total_users': len(users),
    })


@controllers_blueprint.route('/users', methods=['POST'])
def create_user():
    # Request input
    body = request.get_json()
    # Validate request
    schema = CreateUserRequestSchema()
    try:
        # Validate request body against schema data types
        schema.load(body)
    except ValidationError:
        print(sys.exc_info())
        abort (400)
    # Create a new user
    new_user = User(
        id=str(generate_uuid()),
        name=body.get('name'),
    )
    # Insert
    try:
        new_user.insert()
    except exc.IntegrityError:
        print(sys.exc_info())
        abort (422)
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'created': new_user.id,
        'total_users': len(User.query.all())
    })


@controllers_blueprint.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter(User.id == id).one_or_none()
    except:
        print(sys.exc_info())
        abort (500)
    # If cannot find requested id, return 404
    if user is None:
        abort (404)
    try:
        user.delete()
    except:
        print(sys.exc_info())
        abort (500)
    return jsonify({
        'success': True,
        'deleted': id,
        'total_users': len(User.query.all())
    })