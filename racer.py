from string import ascii_uppercase
from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
    def __init__(self):
        self.length = randint (0,10)
        self.terrain = TERRAINS[randint(0,3)]
        self.complexity = COMPLEXITIES[randint(0,2)]
    def __str__(self):
        return "{} {} et {}".format(self.length,self.terrain,self.complexity)

class Track:
    def __init__(self):
        self.parts = []
        i=1
        while i<20 :
            (self.parts).append(TrackPart())
            i +=1

x = Track()

print(x.parts[2])