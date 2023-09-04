import json

from src.classes.Pet import PetEncoder
from src.services.business_logic_services import pets_business_service


def create_pet(user_id, json_data):
    """Create a new pet object"""

    pet = pets_business_service.create_pet(user_id=user_id,
                                           name=json_data.get('name'),
                                           birthday=json_data.get('dob'),
                                           gender=json_data.get('gender'))

    return json.dumps(pet, cls=PetEncoder)


def get_pet(user_id: str, pet_id: str):
    pet = pets_business_service.get_pet(user_id=user_id, pet_id=pet_id)
    return json.dumps(pet, cls=PetEncoder) if pet else None


def get_all_pets(user_id):
    """Get all pets"""
    return [json.dumps(pet, cls=PetEncoder) for pet in pets_business_service.get_all_pets(user_id=user_id)]


def update_pet(user_id, pet_id, json_data):
    """Update pet"""
    updated_pet = pets_business_service.update_pet(user_id=user_id,
                                                   pet_id=pet_id,
                                                   new_name=json_data.get("name"),
                                                   new_dob=json_data.get("dob"),
                                                   new_gender=json_data.get("gender"))

    return json.dumps(updated_pet, cls=PetEncoder) if updated_pet else None


def delete_pet(user_id, pet_id):
    pet = pets_business_service.delete_pet(user_id=user_id, pet_id=pet_id)

    return json.dumps(pet, cls=PetEncoder) if pet else None

