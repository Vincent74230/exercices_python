from string import ascii_uppercase
from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]
PILOT = ["A","B","C","D","E"]

class TrackPart:
    def __init__(self):
        self.length = randint (0,10)
        self.terrain = TERRAINS[randint(0,3)]
        self.complexity = COMPLEXITIES[randint(0,2)]
    def __str__(self):
        return "{} {} {}".format(self.length,self.terrain,self.complexity)

class Track:
    def __init__(self):
        self.parts = []
        i=1
        while i<20 :
            (self.parts).append(TrackPart())
            i +=1

class Pilot:
    compteur = 0
    def __init__(self):
        self.name = PILOT[Pilot.compteur]
        self.normal_speed = random()+0.5
        self.rapid_speed = random()+0.5
        self.subtle_speed = random()+0.5
        Pilot.compteur += 1

class Car:
    def __init__(self,pilot):
        self.name = randint(1,20)
        self.pilot = pilot
        self.asphalt_speed = random()+0.5
        self.sand_speed = random()+0.5
        self.mud_speed = random()+0.5
        self.rocky_speed = random()+0.5

track = TrackPart()
#track=str(track)
liste = track.split(" ")
print(liste)
a = liste[0]
a=int(a)
print(a)