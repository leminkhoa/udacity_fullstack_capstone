import flask 
from flask import jsonify
from . import controllers_blueprint

@controllers_blueprint.route('/users')
def test_users():
    return jsonify(
        {'message': 'Success find transactions'}
    ), 200
