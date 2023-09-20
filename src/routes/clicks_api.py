from flask import Blueprint, jsonify, request
from src.services.serialization_services.clicks_serialization_service import create_click, get_click, get_all_clicks

clicks_blueprint = Blueprint('clicks', __name__)


@clicks_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>/tricks/<string:trick_id>/clicks', methods=['POST'])
def api_add_click(user_id, pet_id, trick_id):
    """Create a new click object via POST request"""
    click = create_click(user_id=user_id, pet_id=pet_id, trick_id=trick_id, json_data=request.get_json())
    if click:
        return jsonify({'message': 'click created successfully', 'click': click})
    else:
        return jsonify({'message': 'Error - could not create click'})


@clicks_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>/tricks/<string:trick_id>/clicks/<string:click_timestamp>', methods=['GET'])
def api_get_click(user_id, pet_id, trick_id, click_timestamp):
    click = get_click(click_timestamp=click_timestamp)
    if click:
        return jsonify({'click': click})
    else:
        return jsonify({'error': f'click with timestamp {click_timestamp} not found'}), 404


@clicks_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>/tricks/<string:trick_id>/clicks', methods=['GET'])
def api_get_clicks(user_id, pet_id, trick_id):
    """Get all clicks"""
    return jsonify({'clicks': get_all_clicks(trick_id=trick_id)})
