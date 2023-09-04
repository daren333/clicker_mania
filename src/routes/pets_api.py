from flask import Blueprint, jsonify, request
from src.services.serialization_services.pets_serialization_service import create_pet, get_all_pets, delete_pet, update_pet, get_pet

pets_blueprint = Blueprint('pets', __name__)


@pets_blueprint.route('/users', methods=['POST'])
def api_add_user():
    """Create a new pet object via POST request"""
    user = create_user(request.get_json())
    if user:
        return jsonify({'message': 'User created successfully', 'user': user})
    else:
        return jsonify({'message': 'Error - could not create user'})


@pets_blueprint.route('/users/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404


@pets_blueprint.route('/users', methods=['GET'])
def api_get_users():
    """Get all pets"""
    return jsonify({'users': get_all_users()})


@pets_blueprint.route('/users/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):
    """Update an existing user object via PUT request"""
    updated_user = update_user(user_id, request.get_json())
    if updated_user:
        return jsonify({'message': 'User updated successfully', 'user': updated_user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404


@pets_blueprint.route('/users/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """Delete user from DB"""
    deleted_user = delete_user(user_id=user_id)
    if deleted_user:
        return jsonify({'message': 'User deleted successfully', 'user': deleted_user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404


@pets_blueprint.route('users/<string:user_id>/pets', methods=['POST'])
def api_add_pet():
    """Create a new pet object via POST request"""
    pet = create_pet(request.get_json())
    if pet:
        return jsonify({'message': 'Pet created successfully', 'pet': pet})
    else:
        return jsonify({'message': 'Error - could not create pet'})


@pets_blueprint.route('users/<string:user_id>/pets/<string:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    pet = get_pet(pet_id)
    if pet:
        return jsonify({'pet': pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404


@pets_blueprint.route('users/<string:user_id>/pets', methods=['GET'])
def api_get_pets():
    """Get all pets"""
    return jsonify({'pets': get_all_pets()})


@pets_blueprint.route('users/<string:user_id>/pets/<string:pet_id>', methods=['PUT'])
def api_update_pet(pet_id):
    """Update an existing pet object via PUT request"""
    updated_pet = update_pet(pet_id, request.get_json())
    if updated_pet:
        return jsonify({'message': 'Pet updated successfully', 'pet': updated_pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404


@pets_blueprint.route('users/<string:user_id>/pets/<string:pet_id>', methods=['DELETE'])
def api_delete_pet(pet_id):
    """Delete pet from DB"""
    deleted_pet = delete_pet(pet_id=pet_id)
    if deleted_pet:
        return jsonify({'message': 'Pet deleted successfully', 'pet': deleted_pet})
    else:
        return jsonify({'error': f'Pet with id {pet_id} not found'}), 404

