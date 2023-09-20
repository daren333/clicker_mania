import json
from datetime import datetime
from uuid import uuid4

from src.classes.Pet import PetDecoder


class User:
    def __init__(self, name: str, dob: str, user_id: str = None, creation_timestamp: datetime = None,
                 email: str = None, phone_number: str = None, pets: dict = None):
        self.user_id = str(uuid4()) if not user_id else user_id
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y') if isinstance(dob, str) else dob
        self.email = email
        self.phone_number = phone_number
        self.creation_timestamp = datetime.now() if not creation_timestamp else creation_timestamp #datetime.strptime(creation_timestamp, '%m/%d/%Y %H:%M:%S').date()
        self.age = self.calculate_age()
        self.pets = {} if not pets else pets

    def add_pet(self, pet):
        if pet.pet_id in self.pets.keys():
            raise KeyError(f"Pet with id {pet.pet_id} already exists")
        self.pets[pet.pet_id] = pet

    def calculate_age(self):
        birthdate = self.dob
        age = datetime.now() - datetime(birthdate.year, birthdate.month, birthdate.day, 0, 0)
        return age.days // 365

    def update_dob(self, new_dob):
        self.dob = datetime.strptime(new_dob, '%m/%d/%Y').date()
        self.age = self.calculate_age()



class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                "user_id": obj.user_id,
                "name": obj.name,
                "dob": obj.dob.strftime('%m/%d/%Y'),
                "email": obj.email,
                "phone_number": obj.phone_number,
                "creation_timestamp": obj.creation_timestamp.strftime('%m/%d/%Y %H:%M:%S'),
                "pets": obj.pets
            }
        return super().default(obj)


class UserDecoder(json.JSONDecoder):
    def _decode(self, s):
        obj = super().decode(s)
        if 'user_id' in obj:
            user = User(
                name=obj['name'],
                dob=obj['dob'],
                user_id=obj['user_id'],
                email=obj['email'],
                phone_number=obj['phone_number'],
                creation_timestamp=datetime.strptime(obj['creation_timestamp'], '%m/%d/%Y'),
                pets=obj['pets']
            )
            if 'pets' in obj:
                for pet_id, pet_data in obj['pets'].items():
                    user.pets[pet_id] = PetDecoder().decode(json.dumps(pet_data))
            return user
        return obj


# class UserEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, (User, Pet)):
#             # Convert the object to a dictionary
#             obj_dict = obj.__dict__
#             # Convert UUID objects to strings
#             for key, value in obj_dict.items():
#                 if isinstance(value, UUID):
#                     obj_dict[key] = str(value)
#             return obj_dict
#         return super().default(obj)
#
#
# class UserDecoder(json.JSONDecoder):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(object_hook=self._decode_user, *args, **kwargs)
#
#     def _decode_user(self, s):
#         obj_dict = super().decode(s)
#         if 'pets' in obj_dict:
#             pets_data = obj_dict['pets']
#             obj_dict['pets'] = {k: Pet(**v) for k, v in pets_data.items()}
#         return User(**obj_dict)
