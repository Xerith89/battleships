# create and initialise an opponent with positions that don't overlap
import random

class Opponent:
    shipPositions = []
    remainingBoats = 3

    def __init__(self, *args, **kwargs):
        self.shipPositions = random.sample(range(1,32),3)
    
    def checkIfHit(self,position):
        if position in self.shipPositions:
            print("Hit!")
            self.remainingBoats -= 1
            print (f'{self.remainingBoats} Left')
        else:
            print("Miss!")

    def checkRemainingBoats(self):
        return self.remainingBoats

        
