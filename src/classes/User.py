from uuid import uuid4
import json
from uuid import uuid4
from datetime import datetime


class User:
    def __init__(self, name: str, dob: str, gender: str, uuid=None, creation_timestamp=None, email=None, phone_number=None):
        self.user_id = str(uuid4()) if not uuid else uuid
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y').date()
        self.email = email
        self.phone_number = phone_number
        self.creation_timestamp = datetime.now() if not creation_timestamp else datetime.strptime(creation_timestamp, '%m/%d/%Y %H:%M:%S').date()
        self.pets = {}

    def add_pet(self, pet):
        if pet.pet_id in self.pets.keys():
            raise KeyError(f"Pet with id {pet.pet_id} already exists")
        self.pets[pet.pet_id] = pet
