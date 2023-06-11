import random
from datetime import datetime
from enum import Enum


class TreatLikelihood(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    SMART = "smart"


class Click:

    def __init__(self, pet_id, likelihood):
        self.timestamp = datetime.now()
        self.treat_likelihood = TreatLikelihood(likelihood)
        self.pet_id = pet_id
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