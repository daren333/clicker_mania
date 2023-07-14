import json
import uuid

from src.classes.Pet import PetEncoder, Pet

pets = {}


def get_pet(pet_id: uuid):
    return pets[pet_id]


def insert_pet(pet: Pet):
    pets[pet.uuid] = pet
    return pet


def create_pet(name, birthday, gender):
    """Create a new pet object"""
    pet = Pet(name=name, dob=birthday, gender=gender)
    pets[pet.uuid] = pet
    return json.dumps(pet, cls=PetEncoder)


def get_all_pets():
    """Get all pets"""
    return [json.dumps(pet, cls=PetEncoder) for pet in pets]


def update_pet(pet_id, data):
    """Upsert pet"""
    pet = pets[pet_id]
    pet.update(data) if pet else None


def delete_pet(pet_id):
    return pets.pop(pet_id)

