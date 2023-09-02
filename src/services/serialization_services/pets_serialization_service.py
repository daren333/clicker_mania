import json

from src.classes.Pet import PetEncoder, Pet
from src.services.business_logic_services import pets_business_service


def create_pet(json_data):
    """Create a new pet object"""

    pet = pets_business_service.create_pet(name=json_data.get('name'),
                                           birthday=json_data.get('dob'),
                                           gender=json_data.get('gender'))

    return json.dumps(pet, cls=PetEncoder)


def get_pet(pet_id: str):
    return json.dumps(pets_business_service.get_pet(pet_id=pet_id), cls=PetEncoder)


def get_all_pets():
    """Get all pets"""
    return [json.dumps(pet, cls=PetEncoder) for pet in pets_business_service.get_all_pets()]


def update_pet(pet_id, json_data):
    """Upsert pet"""
    return json.dumps(pets_business_service.update_pet(pet_id=pet_id,
                                                       new_name=json_data.get("name"),
                                                       new_dob=json_data.get("dob"),
                                                       new_gender=json_data.get("dob")))


def delete_pet(pet_id):
    return json.dumps(pets_business_service.delete_pet(pet_id=pet_id))

