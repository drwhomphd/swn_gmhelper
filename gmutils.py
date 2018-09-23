import random

class dice:
    """ Class for rolling dice. """
    def __init__(self, count, sides):
            self.number = count
            self.sides = sides

    def roll(self):
        result = 0
        for i in range(0,self.number):
            result = result + random.randint(1,self.sides)
        print result
    #End Roll

class table:
    """ Class for loading table descriptors. """
    def __init__(self, filename, table_name):
        self.filename = filename
        self.name = table_name
        self.stages = [] # Array of dice objects for each stage
        self.entries = [] # Generation of the game table in the rule book

    def _load(self):
        filehandle = open(self.filename, "r")
        for line in filehandle:
            line = line.strip()
            # Metadata
            if line[0] == "#":
                # Valid fields:
                # Stages = Number of die rolls until we get to a result
                # S#Dice = One entry for each stage relating to the dice type
                # <count>D<sides> =
                print line[1:].split(':')
            # Table definition
            else:
                print line.split(',')


