import json
import uuid
from datetime import datetime, date


class Pet:
    def __init__(self, name: str, dob: str, gender: str):
        self.uuid = uuid.uuid4()
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y').date()
        self.gender = gender
        self.creation_timestamp = datetime.now()
        self.age = self._calculate_age(dob, self.creation_timestamp)

    def _calculate_age(self, birthdate, creation_timestamp):
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y').date()
        age = creation_timestamp.date() - birthdate
        return age.days // 365


class PetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pet):
            return {
                'uuid': obj.uuid,
                'name': obj.name,
                'birthdate': obj.dob.strftime('%m/%d/%Y'),
                'gender': obj.gender,
                'creation_timestamp': obj.creation_timestamp.strftime('%m/%d/%Y %H:%M:%S'),
                'age': obj.age
            }
        return super().default(obj)