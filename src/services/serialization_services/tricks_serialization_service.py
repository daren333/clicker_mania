import json

from src.classes.Trick import TrickEncoder
from src.services.business_logic_services import tricks_business_service


def create_trick(user_id, pet_id, json_data):
    """Create a new trick object"""

    trick = tricks_business_service.create_trick(user_id=user_id,
                                                 pet_id=pet_id,
                                                 name=json_data.get('name'))

    return json.dumps(trick, cls=TrickEncoder)


def get_trick(trick_id: str):
    trick = tricks_business_service.get_trick(trick_id=trick_id)
    return json.dumps(trick, cls=TrickEncoder) if trick else None


def get_all_tricks(pet_id):
    """Get all tricks"""
    return [json.dumps(trick, cls=TrickEncoder) for trick in tricks_business_service.get_all_tricks_by_pet(pet_id=pet_id)]


def update_trick(trick_id, json_data):
    """Update trick"""
    updated_trick = tricks_business_service.update_trick(trick_id=trick_id,
                                                         new_name=json_data.get("name"))

    return json.dumps(updated_trick, cls=TrickEncoder) if updated_trick else None


def delete_trick(trick_id):
    trick = tricks_business_service.delete_trick(trick_id=trick_id)

    return json.dumps(trick, cls=TrickEncoder) if trick else None

