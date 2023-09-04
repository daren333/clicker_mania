import json

from src.classes.Click import ClickEncoder
from src.services.business_logic_services import clicks_business_service


def create_click(user_id, pet_id, trick_id, json_data):
    """Create a new click object"""

    click = clicks_business_service.create_click(user_id=user_id,
                                                 pet_id=pet_id,
                                                 trick_id=trick_id,
                                                 treat_likelihood=json_data.get("treat_likelihood"))

    return json.dumps(click, cls=ClickEncoder)


def get_click(click_timestamp: str):
    click = clicks_business_service.get_click(click_timestamp=click_timestamp)
    return json.dumps(click, cls=ClickEncoder) if click else None


def get_all_clicks(trick_id):
    """Get all clicks"""
    return [json.dumps(click, cls=ClickEncoder) for click in clicks_business_service.get_all_clicks(trick_id=trick_id)]
