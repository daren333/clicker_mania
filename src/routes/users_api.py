from flask import Blueprint, jsonify, request
from src.services.serialization_services.users_serialization_service import create_user, get_all_users, delete_user, update_user, get_user

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'users api ok'})


@users_blueprint.route('/users', methods=['POST'])
def api_add_user():
    """Create a new user object via POST request"""
    user = create_user(request.get_json())
    if user:
        return jsonify({'message': 'User created successfully', 'user': user})
    else:
        return jsonify({'message': 'Error - could not create user'})


@users_blueprint.route('/users/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404


@users_blueprint.route('/users', methods=['GET'])
def api_get_users():
    """Get all users"""
    return jsonify({'users': get_all_users()})


@users_blueprint.route('/users/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):
    """Update an existing user object via PUT request"""
    updated_user = update_user(user_id, request.get_json())
    if updated_user:
        return jsonify({'message': 'User updated successfully', 'user': updated_user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404


@users_blueprint.route('/users/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """Delete user from DB"""
    deleted_user = delete_user(user_id=user_id)
    if deleted_user:
        return jsonify({'message': 'User deleted successfully', 'user': deleted_user})
    else:
        return jsonify({'error': f'User with id {user_id} not found'}), 404