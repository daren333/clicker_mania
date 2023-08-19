import json
from uuid import uuid4
from datetime import datetime, date


class Pet:
    def __init__(self, name: str, dob: str, gender: str, uuid=None, creation_timestamp=None, age=None, total_clicks=None):
        self.pet_id = str(uuid4()) if not uuid else uuid
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y').date() #if not dob else dob
        self.gender = gender
        self.creation_timestamp = datetime.now() if not creation_timestamp else datetime.strptime(creation_timestamp, '%m/%d/%Y %H:%M:%S').date()
        self.age = self._calculate_age(dob, self.creation_timestamp) if not age else age
        self.total_clicks = 0 if not total_clicks else total_clicks

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
                'pet_id': obj.pet_id,
                'name': obj.name,
                'birthdate': obj.dob.strftime('%m/%d/%Y'),
                'gender': obj.gender,
                'creation_timestamp': obj.creation_timestamp.strftime('%m/%d/%Y %H:%M:%S'),
                'age': obj.age,
                'total_clicks': obj.total_clicks
            }
        return super().default(obj)


class PetDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self._decode_pet, *args, **kwargs)

    def _decode_pet(self, obj):
        if 'pet_id' in obj and 'name' in obj and 'birthdate' in obj and 'gender' in obj and 'creation_timestamp' in obj and 'age' in obj:
            # Convert birthdate and creation_timestamp back to datetime objects
            obj['dob'] = obj['birthdate'] #datetime.strptime(obj['birthdate'], '%m/%d/%Y').date()
            #obj['creation_timestamp'] = datetime.strptime(obj['creation_timestamp'], '%m/%d/%Y %H:%M:%S').date()
            # Remove the temporary 'birthdate' key
            del obj['birthdate']
            # Create a new Pet object with the data from the dictionary
            return Pet(**obj)
        return obj