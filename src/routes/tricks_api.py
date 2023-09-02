from flask import Blueprint, jsonify, request

from src.classes.Trick import Trick

clicks_blueprint = Blueprint('clicks', __name__)


@clicks_blueprint.route('/tricks/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'clicks endpoint ok'})


@clicks_blueprint.route('/tricks', methods=['POST'])
def create_trick():
    """Register a new click"""
    data = request.get_json()

    trick = Trick(name=data.get("trick_name"))
    # TODO call tricks service add trick

    return jsonify({'message': f'New trick {trick.name} created. Trick id: {trick.trick_id}'})


@clicks_blueprint.route('/tricks', methods=['POST'])
def create_trick():