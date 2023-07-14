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

    def update(self, data: dict):
        if data.get("name"):
            self.name = data.get("name")
        if data.get("dob"):
            self._update_dob(new_dob=data.get("dob"))
        if data.get("gender"):
            self.gender = data.get("gender")

    def _update_dob(self, new_dob):
        self.dob = datetime.strptime(new_dob, '%m/%d/%Y').date()
        self.age = self._calculate_age(birthdate=new_dob, creation_timestamp=datetime.now())

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