from flask import Blueprint, jsonify, request
from src.services.serialization_services.clicks_serialization_service import create_click, get_all_click, delete_click, update_click, get_click

clicks_blueprint = Blueprint('clicks', __name__)


@clicks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>/clicks', methods=['POST'])
def api_add_click():
    """Create a new click object via POST request"""
    click = create_click(request.get_json())
    if click:
        return jsonify({'message': 'click created successfully', 'click': click})
    else:
        return jsonify({'message': 'Error - could not create click'})


@clicks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>/clicks/<string:click_id>', methods=['GET'])
def api_get_click(click_id):
    click = get_click(click_id)
    if click:
        return jsonify({'click': click})
    else:
        return jsonify({'error': f'click with id {click_id} not found'}), 404


@clicks_blueprint.route('users/<string:user_id>/clicks', methods=['GET'])
def api_get_clicks():
    """Get all clicks"""
    return jsonify({'clicks': get_all_clicks()})


@clicks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>/clicks/<string:click_id>', methods=['PUT'])
def api_update_click(click_id):
    """Update an existing click object via PUT request"""
    updated_click = update_click(click_id, request.get_json())
    if updated_click:
        return jsonify({'message': 'click updated successfully', 'click': updated_click})
    else:
        return jsonify({'error': f'click with id {click_id} not found'}), 404


@clicks_blueprint.route('users/<string:user_id>/tricks/<string:trick_id>/clicks/<string:click_id>', methods=['DELETE'])
def api_delete_click(click_id):
    """Delete click from DB"""
    deleted_click = delete_click(click_id=click_id)
    if deleted_click:
        return jsonify({'message': 'click deleted successfully', 'click': deleted_click})
    else:
        return jsonify({'error': f'click with id {click_id} not found'}), 404
