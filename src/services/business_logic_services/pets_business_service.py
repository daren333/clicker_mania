import json
import logging
from datetime import datetime

from src.classes.Pet import PetEncoder, Pet, calculate_age
from src.services.database_services import pets_db_service

logger = logging.getLogger("pets_business_service_logger")


def create_pet(name, birthday, gender):
    """Create a new pet object"""
    pet = Pet(name=name, dob=birthday, gender=gender)
    return pets_db_service.create_pet(pet=pet)


def get_pet(pet_id: str):
    return pets_db_service.get_pet(pet_id=pet_id)


def get_all_pets():
    """Get all pets"""
    return pets_db_service.get_all_pets()


def update_pet(pet_id, new_name, new_dob, new_gender):
    """Update pet"""
    pet = get_pet(pet_id=pet_id)

    if pet:
        logger.debug("Pets Business Service: pet found - inserting")
        pet.name = new_name
        pet.dob = datetime.strptime(new_dob, '%m/%d/%Y').date()
        pet.gender = new_gender
        pet.age = calculate_age(new_dob, datetime.now())
        updated_pet = pets_db_service.update_pet(pet_id=pet_id, pet_obj=pet)
        return updated_pet
    else:
        logger.debug(f"Pets Business Service: no pet found with id {pet_id}")
        return None


def delete_pet(pet_id):
    return pets_db_service.delete_pet(pet_id=pet_id)

