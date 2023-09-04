import logging
from datetime import datetime

from src.classes.User import User
from src.services.database_services import users_db_service

logger = logging.getLogger("users_business_service_logger")


def create_user(name, dob, email, phone_number):
    """Create a new user object"""
    user = User(name=name, dob=dob, email=email, phone_number=phone_number)
    return users_db_service.create_user(user=user)


def get_user(user_id: str):
    return users_db_service.get_user(user_id=user_id)


def get_all_users(user_id):
    """Get all users"""
    return users_db_service.get_all_users()


def update_user(user_id, new_name, new_dob, new_email, new_phone_number):
    """Update user"""
    user = get_user(user_id=user_id)

    if user:
        logger.debug("Users Business Service: user found - inserting")
        user.name = new_name
        user.update_dob(new_dob=new_dob)
        user.email = new_email
        user.phone_number = new_phone_number
        updated_user = users_db_service.update_user(user_id=user_id, user_obj=user)
        return updated_user
    else:
        logger.debug(f"Users Business Service: no user found with id {user_id}")
        return None


def delete_user(user_id):
    return users_db_service.delete_user(user_id=user_id)

