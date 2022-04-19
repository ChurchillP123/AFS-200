import random
dice = []

class Die:
    def __init__(self, numOfSides, value = 0):
        self.numOfSides = numOfSides
        self.value = value
    def roll(self):
        self.value = random.choice(range(1, self.numOfSides + 1))
        return self.value
    def getCurrentFaceValue(self):
        return self.value
    def showDieFace(self):
        print(self.value)

def printDie(num):
    match num:
        case 1:
            return "⚀"
        case 2:
            return "⚁"
        case 3:
            return "⚂"
        case 4:
            return "⚃"
        case 5:
            return "⚄"
        case 6:
            return "⚅"
       
def rollFive(sides1, sides2, sides3, sides4, sides5):
    global dice
    dice = [Die(sides1).roll(), Die(sides2).roll(), Die(sides3).roll(), Die(sides4).roll(), Die(sides5).roll()]
    for die in dice:
        if all(die < 7 for die in dice):
            print(f"{printDie(die)} ({die})", end =" ")
        else:
            print(f"({die})", end =" ")
       
rollFive(1, 2, 1, 1, 9)

def isYahtzee(dice) :
    if all(die == dice[0] for die in dice):
            print("\nYAHTZEE")

isYahtzee(dice)