import json
from uuid import uuid4

from src.classes import Click
from src.classes.Click import ClickDecoder, ClickEncoder


class Trick:

    def __init__(self, user_id: str, pet_id: str, name: str, trick_id: str = None, clicks: dict = None):
        self.trick_id = str(uuid4()) if not trick_id else trick_id
        self.name = name
        self.user_id = user_id
        self.pet_id = pet_id
        self.clicks = {} if not clicks else clicks


class TrickEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Trick):
            return {
                "trick_id": obj.trick_id,
                "name": obj.name,
                "user_id": obj.user_id,
                "pet_id": obj.pet_id,
                "clicks": {click_timestamp: json.dumps(click, cls=ClickEncoder) for click_timestamp, click in obj.clicks.items()}
            }
        return super().default(obj)


class TrickDecoder(json.JSONDecoder):
    def _decode(self, s):
        obj = super().decode(s)
        if 'trick_id' in obj:
            trick = Trick(
                user_id=obj['user_id'],
                pet_id=obj['pet_id'],
                name=obj['name'],
                trick_id=obj['trick_id'],
                clicks=obj['clicks']
            )
            if 'clicks' in obj:
                for click_id, click_data in obj['clicks'].items():
                    trick.clicks[click_id] = ClickDecoder().decode(json.dumps(click_data))
            return trick
        return obj
