from flask import Blueprint, jsonify, request

clicks_blueprint = Blueprint('clicks', __name__)


@clicks_blueprint.route('/clicks/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'clicks endpoint ok'})
