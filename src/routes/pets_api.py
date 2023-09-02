from flask import Blueprint, jsonify, request
from src.services.business_logic_services.pets_business_service import create_pet, get_all_pets, delete_pet, update_pet, get_pet

pets_blueprint = Blueprint('pets', __name__)


@pets_blueprint.route('/pets/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'pets api ok'})


@pets_blueprint.route('/pets', methods=['POST'])
def api_add_pet():
    """Create a new pet object via POST request"""
    data = request.get_json()
    pet = create_pet(data.get('name'), data.get('dob'), data.get('gender'))
    return jsonify({'message': 'Pet created successfully', 'pet': pet})

@pets_blueprint.route('/pets/<string:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    return jsonify(get_pet(pet_id))


@pets_blueprint.route('/pets', methods=['GET'])
def api_get_pets():
    """Get all pets"""
    return jsonify({'pets': get_all_pets()})


@pets_blueprint.route('/pets/<string:pet_id>', methods=['PUT'])
def api_update_pet(pet_id):
    """Update an existing pet object via PUT request"""
    data = request.get_json()
    updated_pet = update_pet(pet_id, data)
    if updated_pet:
        return jsonify({'message': 'Pet updated successfully', 'pet': updated_pet})
    else:
        return jsonify({'error': 'Pet not found'}), 404


@pets_blueprint.route('/pets/pet_id', methods=['DELETE'])
def api_delete_pet(pet_id):
    """Delete pet from DB"""
    pet = delete_pet(pet_id=pet_id)
    return jsonify({'message': 'Pet deleted successfully', 'pet': pet})

