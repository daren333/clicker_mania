from uuid import uuid4


class Trick:

    def __init__(self, uuid, name):
        self.trick_id = str(uuid4()) if not uuid else uuid
        self.name = name

