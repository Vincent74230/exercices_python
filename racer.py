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
        return "{} {} et {}".format(self.length,self.terrain,self.complexity)

class Track:
    def __init__(self):
        self.parts = []
        i=0
        while i<20:
            (self.parts).append(TrackPart())
            i +=1
    def __getitem__(self,index):
        return self.parts[index]

class Pilot:
    compteur = 0
    def __init__(self):
        self.name = PILOT[Pilot.compteur]
        self.normal_speed = random()+0.5
        self.rapid_speed = random()+0.5
        self.subtle_speed = random()+0.5
        Pilot.compteur += 1

class Car:
    def __init__(self):
        self.name = randint(1,20)
        self.pilot = Pilot()
        self.asphalt_speed = random()+0.5
        self.sand_speed = random()+0.5
        self.mud_speed = random()+0.5
        self.rocky_speed = random()+0.5
    def __str__(self):
        return "car {} avec pilot {}".format(self.name,self.pilot.name)
    #def time_for_part(self,trackPart):
        

track = Track()
i=0
while i<20:
    print (track[i])
    i +=1

combo_car_pilot = []
i = 0
while i<5:
    nom_du_pilote = PILOT[i]
    nom_du_pilote = Car()
    combo_car_pilot.append(nom_du_pilote)
    i += 1
i=0
while i<5:
    print (combo_car_pilot[i])
    i +=1




