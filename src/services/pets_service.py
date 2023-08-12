import json
import uuid

from src.classes.Pet import PetEncoder, Pet
from src.services import pets_db_service

pets = {}


def insert_pet(pet: Pet):
    pets_db_service.create_pet(pet=pet)
    return pet


def create_pet(name, birthday, gender):
    """Create a new pet object"""
    pet = Pet(name=name, dob=birthday, gender=gender)
    pets_db_service.create_pet(pet=pet)
    return json.dumps(pet, cls=PetEncoder)


def get_pet(pet_id: str):
    return json.dumps(pets_db_service.get_pet(pet_id=pet_id), cls=PetEncoder)


def get_all_pets():
    """Get all pets"""
    return [json.dumps(pet, cls=PetEncoder) for pet in pets_db_service.get_all_pets()]


def update_pet(pet_id, data):
    """Upsert pet"""
    pet = get_pet(pet_id=pet_id)

    pet.update(data) if pet else None


def delete_pet(pet_id):
    return pets.pop(pet_id)

