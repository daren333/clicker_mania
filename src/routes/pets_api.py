from flask import Blueprint, jsonify, request
from src.services.pets_service import create_pet, get_all_pets

pets_blueprint = Blueprint('pets', __name__)


@pets_blueprint.route('/pets/health', methods=['GET'])
def health():
    """Health route to check if the application is running"""
    return jsonify({'status': 'pets api ok'})


@pets_blueprint.route('/pets', methods=['POST'])
def add_pet():
    """Create a new pet object via POST request"""
    data = request.get_json()
    pet = create_pet(data.get('name'), data.get('dob'), data.get('gender'))
    return jsonify({'message': 'Pet created successfully', 'pet': pet})


@pets_blueprint.route('/pets', methods=['GET'])
def get_pets():
    """Get all pets"""
    return jsonify({'pets': get_all_pets()})
