import json
from uuid import uuid4
from datetime import datetime
from src.classes import Trick
from src.classes.Trick import TrickDecoder


class Pet:
    def __init__(self, user_id: str, name: str, dob: str, gender: str, pet_id: str = None,
                 creation_timestamp: datetime = None, age: int = None, tricks: dict[Trick] = None):
        self.user_id = user_id
        self.pet_id = str(uuid4()) if not pet_id else pet_id
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y').date()
        self.gender = gender
        self.creation_timestamp = datetime.now() if not creation_timestamp else datetime.strptime(creation_timestamp, '%m/%d/%Y %H:%M:%S').date()
        self.age = self.calculate_age(dob, self.creation_timestamp) if not age else age
        self.tricks = {} if not tricks else tricks

    def calculate_age(self, birthdate, creation_timestamp):
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y').date()
        age = creation_timestamp.date() - birthdate
        return age.days // 365

    def update_dob(self, new_dob):
        self.dob = datetime.strptime(new_dob, '%m/%d/%Y').date()
        self.age = self.calculate_age(birthdate=new_dob, creation_timestamp=datetime.now())


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
                "tricks": obj.tricks
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
                age=obj['age'],
                tricks=obj['tricks']
            )
            if 'tricks' in obj:
                for trick_id, trick_data in obj['tricks'].items():
                    pet.tricks[trick_id] = TrickDecoder().decode(json.dumps(trick_data))
            return pet
        return obj


#
# class PetEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Pet):
#             return {
#                 'user_id': obj.user_id,
#                 'pet_id': obj.pet_id,
#                 'name': obj.name,
#                 'birthdate': obj.dob.strftime('%m/%d/%Y'),
#                 'gender': obj.gender,
#                 'creation_timestamp': obj.creation_timestamp.strftime('%m/%d/%Y %H:%M:%S'),
#                 'age': obj.age,
#                 'total_clicks': obj.total_clicks
#             }
#         return super().default(obj)
#
#
# class PetDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(object_hook=self._decode_pet, *args, **kwargs)
#
#     def _decode_pet(self, obj):
#         if 'user_id' in obj and 'pet_id' in obj and 'name' in obj and 'birthdate' in obj and 'gender' in obj and 'creation_timestamp' in obj and 'age' in obj:
#             # Convert birthdate and creation_timestamp back to datetime objects
#             obj['creation_timestamp'] = datetime.fromisoformat(obj['creation_timestamp'])
#             obj['dob'] = datetime.fromisoformat(obj['birthdate'])
#             # Remove the temporary 'birthdate' key
#             del obj['birthdate']
#             # Create a new Pet object with the data from the dictionary
#             return Pet(**obj)
#         return obj