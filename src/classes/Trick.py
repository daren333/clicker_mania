from uuid import uuid4


class Trick:

    def __init__(self, name, user_id, pet_id, uuid=None):
        self.trick_id = str(uuid4()) if not uuid else uuid
        self.name = name
        self.user_id = user_id
        self.pet_id = pet_id


