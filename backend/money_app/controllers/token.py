import sys
from flask import render_template, jsonify
from . import controllers_blueprint

@controllers_blueprint.route('/token')
def get_token():
    return jsonify({
        'success': True,
        'message': 'Successfully retrieve access token' 
    })
