import json

from src.classes.Click import ClickEncoder
from src.services.business_logic_services import clicks_business_service


def create_click(user_id, pet_id, trick_id, json_data):
    """Create a new click object"""

    click = clicks_business_service.create_click(user_id=user_id,
                                                 pet_id=pet_id,
                                                 trick_id=trick_id,
                                                 name=json_data.get('name'),
                                                 birthday=json_data.get('dob'),
                                                 gender=json_data.get('gender'))

    return json.dumps(click, cls=ClickEncoder)


def get_click(user_id: str, pet_id: str, trick_id: str, click_id: str):
    click = clicks_business_service.get_click(user_id=user_id, pet_id=pet_id, trick_id=trick_id, click_id=click_id)
    return json.dumps(click, cls=ClickEncoder) if click else None


def get_all_clicks(user_id, pet_id, trick_id):
    """Get all clicks"""
    return [json.dumps(click, cls=ClickEncoder) for click in clicks_business_service.get_all_clicks(user_id=user_id, pet_id=pet_id, trick_id=trick_id)]
