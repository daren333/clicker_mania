import json
from uuid import uuid4
from datetime import datetime
from src.classes import Trick
from src.classes.Trick import TrickDecoder, TrickEncoder


class Pet:
    def __init__(self, user_id: str, name: str, dob: str, gender: str, pet_id: str = None,
                 creation_timestamp: datetime = None, tricks: dict = None):
        self.user_id = user_id
        self.pet_id = str(uuid4()) if not pet_id else pet_id
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y') if isinstance(dob, str) else dob
        self.gender = gender
        self.creation_timestamp = datetime.now() if not creation_timestamp else creation_timestamp #datetime.strptime(str(creation_timestamp), '%m/%d/%Y %H:%M:%S').date()
        self.age = self.calculate_age()
        self.tricks = {} if not tricks else tricks

    def calculate_age(self):
        birthdate = self.dob
        age = datetime.now() - datetime(birthdate.year, birthdate.month, birthdate.day, 0, 0)
        return age.days // 365

    def update_dob(self, new_dob):
        self.dob = datetime.strptime(new_dob, '%m/%d/%Y').date()
        self.age = self.calculate_age()

class PetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pet):
            return {
                "user_id": obj.user_id,
                "pet_id": obj.pet_id,
                "name": obj.name,
                "dob": obj.dob.strftime('%m/%d/%Y'),
                "gender": obj.gender,
                "age": obj.age,
                "tricks": {trick_id: json.dumps(trick, cls=TrickEncoder) for trick_id, trick in obj.tricks.items()}
            }
        return super().default(obj)


class PetDecoder(json.JSONDecoder):
    def _decode(self, s):
        obj = super().decode(s)
        if 'pet_id' in obj:
            pet = Pet(
                user_id=obj['user_id'],
                pet_id=obj['pet_id'],
                name=obj['name'],
                dob=obj['dob'],
                gender=obj['gender'],
                tricks=obj['tricks']
            )
            if 'tricks' in obj:
                for trick_id, trick_data in obj['tricks'].items():
                    pet.tricks[trick_id] = TrickDecoder().decode(json.dumps(trick_data))
            return pet
        return obj
