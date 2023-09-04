import json
import random
from datetime import datetime
from enum import Enum


class TreatLikelihood(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    SMART = "smart"


class Click:

    def __init__(self, user_id, pet_id, trick_id, timestamp, treat_likelihood):
        self.timestamp = datetime.now() if not timestamp else timestamp
        self.treat_likelihood = TreatLikelihood(treat_likelihood)
        self.user_id = user_id
        self.pet_id = pet_id
        self.trick_id = trick_id
        self.treated = self.determine_if_treating(self.treat_likelihood)

    def determine_if_treating(self, treat_likelihood: TreatLikelihood) -> bool:
        match treat_likelihood:
            case TreatLikelihood.SMART:
                return random.random() < self.get_smart_treat_likelihood()
            case TreatLikelihood.LOW:
                return random.random() < 0.25
            case TreatLikelihood.MEDIUM:
                return random.random() < 0.50
            case TreatLikelihood.HIGH:
                return random.random() < 0.75

    def get_smart_treat_likelihood(self):
        """calculates the likelihood that should be used based on smart treat algo"""
        return 1


class ClickEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Click):
                return {
                    'user_id': obj.user_id,
                    'pet_id': obj.pet_id,
                    'trick_id': obj.trick_id,
                    'timestamp': obj.timestamp.strftime('%m/%d/%Y %H:%M:%S'),
                    'treated': obj.treated,
                    'treat_likelihood': obj.treat_likelihood.value
                }
            return super().default(obj)


class ClickDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self._decode_click, *args, **kwargs)

    def _decode_click(self, obj):
        if 'timestamp' in obj and 'treat_likelihood' in obj and 'user_id' in obj and 'pet_id' in obj and 'trick_id' in obj and 'treated' in obj:
            timestamp = datetime.fromisoformat(obj['timestamp'])
            treat_likelihood = TreatLikelihood(obj['treat_likelihood'])
            return Click(user_id=obj['user_id'], pet_id=obj['pet_id'], trick_id=obj['trick_id'], timestamp=timestamp,
                         treat_likelihood=treat_likelihood)
        return obj
