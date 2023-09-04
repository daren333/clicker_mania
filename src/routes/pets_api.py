from flask import Blueprint, jsonify, request
from src.services.serialization_services.pets_serialization_service import create_pet, get_all_pets, delete_pet, update_pet, get_pet

pets_blueprint = Blueprint('pets', __name__)


@pets_blueprint.route('/users/<string:user_id>/pets', methods=['POST'])
def api_add_pet(user_id):
    """Create a new pet object via POST request"""
    pet = create_pet(user_id=user_id, json_data=request.get_json())
    if pet:
        return jsonify({'message': 'Pet created successfully', 'pet': pet})
    else:
        return jsonify({'message': 'Error - could not create pet'})


@pets_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>', methods=['GET'])
def api_get_pet(user_id, pet_id):
    pet = get_pet(pet_id=pet_id)
    if pet:
        return jsonify({'pet': pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404


@pets_blueprint.route('/users/<string:user_id>/pets', methods=['GET'])
def api_get_pets(user_id):
    """Get all pets"""
    return jsonify({'pets': get_all_pets(user_id=user_id)})


@pets_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>', methods=['PUT'])
def api_update_pet(user_id, pet_id):
    """Update an existing pet object via PUT request"""
    updated_pet = update_pet(pet_id=pet_id, json_data=request.get_json())
    if updated_pet:
        return jsonify({'message': 'Pet updated successfully', 'pet': updated_pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404


@pets_blueprint.route('/users/<string:user_id>/pets/<string:pet_id>', methods=['DELETE'])
def api_delete_pet(user_id, pet_id):
    """Delete pet from DB"""
    deleted_pet = delete_pet(pet_id=pet_id)
    if deleted_pet:
        return jsonify({'message': 'Pet deleted successfully', 'pet': deleted_pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404
