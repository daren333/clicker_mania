from flask import Blueprint, jsonify, request
from src.services.serialization_services.tricks_serialization_service import create_trick, get_all_tricks, delete_trick, update_trick, get_trick

tricks_blueprint = Blueprint('tricks', __name__)


@tricks_blueprint.route('users/<string:user_id>/tricks', methods=['POST'])
def api_add_trick():
    """Create a new trick object via POST request"""
    trick = create_trick(request.get_json())
    if trick:
        return jsonify({'message': 'trick created successfully', 'trick': trick})
    else:
        return jsonify({'message': 'Error - could not create trick'})


@tricks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>', methods=['GET'])
def api_get_trick(trick_id):
    trick = get_trick(trick_id)
    if trick:
        return jsonify({'trick': trick})
    else:
        return jsonify({'error': f'trick with id {trick_id} not found'}), 404


@tricks_blueprint.route('users/<string:user_id>/tricks', methods=['GET'])
def api_get_tricks():
    """Get all tricks"""
    return jsonify({'tricks': get_all_tricks()})


@tricks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>', methods=['PUT'])
def api_update_trick(trick_id):
    """Update an existing trick object via PUT request"""
    updated_trick = update_trick(trick_id, request.get_json())
    if updated_trick:
        return jsonify({'message': 'trick updated successfully', 'trick': updated_trick})
    else:
        return jsonify({'error': f'trick with id {trick_id} not found'}), 404


@tricks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>', methods=['DELETE'])
def api_delete_trick(trick_id):
    """Delete trick from DB"""
    deleted_trick = delete_trick(trick_id=trick_id)
    if deleted_trick:
        return jsonify({'message': 'trick deleted successfully', 'trick': deleted_trick})
    else:
        return jsonify({'error': f'trick with id {trick_id} not found'}), 404
