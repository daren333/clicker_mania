from flask import Blueprint, jsonify, request

from src.classes.Click import Click

clicks_blueprint = Blueprint('clicks', __name__)


@clicks_blueprint.route('/clicks/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'clicks endpoint ok'})


@clicks_blueprint.route('/clicks', methods=['POST'])
def click():
    """Register a new click"""
    data = request.get_json()
    click = Click(data.get("pet_id"), data.get("treat_likelihood"))
    return jsonify({'message': f'New click at {click.timestamp}. Treated: {click.treated}'})