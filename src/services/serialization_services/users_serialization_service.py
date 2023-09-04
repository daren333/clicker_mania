import json

from src.classes.User import UserEncoder
from src.services.business_logic_services import users_business_service


def create_user(json_data):
    """Create a new user object"""

    user = users_business_service.create_user(user_id=json_data.get('user'),
                                              name=json_data.get('name'),
                                              birthday=json_data.get('dob'),
                                              gender=json_data.get('gender'))

    return json.dumps(user, cls=UserEncoder)


def get_user(user_id: str):
    user = users_business_service.get_user(user_id=user_id)
    return json.dumps(user, cls=UserEncoder) if user else None


def get_all_users(user_id):
    """Get all users"""
    return [json.dumps(user, cls=UserEncoder) for user in users_business_service.get_all_users(user_id=user_id)]


def update_user(user_id, json_data):
    """Update user"""
    updated_user = users_business_service.update_user(user_id=user_id,
                                                      new_name=json_data.get("name"),
                                                      new_dob=json_data.get("dob"),
                                                      new_email=json_data.get("email_address"),
                                                      new_phone_number=json_data.get("phone_number"))

    return json.dumps(updated_user, cls=UserEncoder) if updated_user else None


def delete_user(user_id):
    user = users_business_service.delete_user(user_id=user_id)

    return json.dumps(user, cls=UserEncoder) if user else None

