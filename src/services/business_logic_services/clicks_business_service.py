import logging

from src.classes.Click import Click
from src.services.database_services import clicks_db_service

logger = logging.getLogger("clicks_business_service_logger")


def create_click(user_id: str, pet_id: str, trick_id: str, treat_likelihood: str):
    """Create a new click object"""
    click = Click(user_id=user_id, pet_id=pet_id, trick_id=trick_id, treat_likelihood=treat_likelihood)
    return clicks_db_service.create_click(click=click)


def get_click(user_id: str, pet_id: str, trick_id: str, click_timestamp: str):
    """Get single click by its trick id and timestamp"""
    return clicks_db_service.get_click(user_id=user_id, pet_id=pet_id, trick_id=trick_id, click_timestamp=click_timestamp)


def get_all_clicks(user_id: str, pet_id: str, trick_id: str):
    """Get all clicks for a given trick id"""
    return clicks_db_service.get_all_clicks(user_id=user_id, pet_id=pet_id, trick_id=trick_id)