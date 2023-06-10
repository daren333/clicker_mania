import json

from src.classes.Pet import PetEncoder, Pet

pets = []


def create_pet(name, birthday, gender):
    """Create a new pet object"""
    pet = Pet(name=name, dob=birthday, gender=gender)
    pets.append(pet)
    return json.dumps(pet, cls=PetEncoder)


def get_all_pets():
    """Get all pets"""
    return [json.dumps(pet, cls=PetEncoder) for pet in pets]
