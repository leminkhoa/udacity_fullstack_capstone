import flask 
from flask import jsonify
from . import controllers_blueprint

@controllers_blueprint.route('/transactions')
def test_transactions():
    return jsonify(
        {'message': 'Success find transactions'}
    ), 200
