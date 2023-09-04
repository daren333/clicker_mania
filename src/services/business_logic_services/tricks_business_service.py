import logging

from src.classes.Trick import Trick
from src.services.database_services import tricks_db_service

logger = logging.getLogger("tricks_business_service_logger")


def create_trick(user_id: str, pet_id: str, name: str):
    """Create a new trick object"""
    trick = Trick(user_id=user_id, pet_id=pet_id, name=name)
    return tricks_db_service.create_trick(trick=trick)


def get_trick(trick_id: str):
    return tricks_db_service.get_trick(trick_id=trick_id)


def get_all_tricks_by_pet(pet_id: str):
    """Get all tricks"""
    return tricks_db_service.get_all_tricks_by_pet(pet_id=pet_id)


def update_trick(trick_id, new_name):
    """Update trick"""
    trick = get_trick(trick_id=trick_id)

    if trick:
        logger.debug("Tricks Business Service: trick found - inserting")
        trick.name = new_name
        updated_trick = tricks_db_service.update_trick(trick_id=trick_id, new_trick_obj=trick)
        return updated_trick
    else:
        logger.debug(f"Tricks Business Service: no trick found with id {trick_id}")
        return None


def delete_trick(trick_id):
    return tricks_db_service.delete_trick(trick_id=trick_id)

