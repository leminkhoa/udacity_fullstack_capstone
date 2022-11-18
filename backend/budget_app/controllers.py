import flask 
from flask import jsonify

blueprint = flask.Blueprint('route', __name__)

@blueprint.route('/hello')
def hello():
    return jsonify(
        {'message': 'Hello World'}
    ), 200
