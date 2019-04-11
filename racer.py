from string import ascii_uppercase
from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
    def __init__(self):
        self.length = randint (0,10)
        self.terrain = TERRAINS[randint(0,3)]
        self.complexity = COMPLEXITIES[randint(0,2)]


track = TrackPart()



