import flask 
from flask import jsonify

controllers_blueprint = flask.Blueprint('index', __name__)

@controllers_blueprint.route('/hello')
def hello():
    return jsonify(
        {'message': 'Hello World'}
    ), 200
