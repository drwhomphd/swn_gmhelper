import random
import sys

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
        self.stage_cnt = 0
        self.stages = list() # Array of dice objects for each stage
        self.entries = dict() # Generation of the game table in the rule book
        self._load()

    def _load(self):
        filehandle = open(self.filename, "r")

        # First meta data field:
        # Stages = Number of die rolls until we get to a result
        stages = filehandle.readline()
        stages = stages.strip()
        assert stages[0] == "#"

        tokens = stages[1:].split(':')
        if(tokens[0] == "Stages"):
            self.stage_cnt = int(tokens[1])
        else:
            print("Table file parsing error. Exiting.")
            sys.exit(1)

        # Second metadata field
        # S#Dice <count>D<sides> = One entry for each stage relating to the dice type
        for i in range(1, self.stage_cnt+1):
            dicedef = filehandle.readline()
            dicedef = dicedef.strip()
            assert dicedef[0] == "#"
            assert int(dicedef[2]) == i # Note this assumes we'll have less than 10 stages... a reasonable assumption.

            # Parsing out <count>D<sides> and storing in the stages object
            tokens = dicedef[1:].split(':')
            tokens = tokens[1].split('D')
            self.stages.append(dice(tokens[0], tokens[1]))

        # All further lines are table definitions
        for line in filehandle:
            line = line.strip()
            # <die range>,"<Table Entry>"
            tokens=line.split(',', 1) # Stop after splitting the die range as entries may have commas as well

            # Table entries can either be a single number or a range denoted with a '-'
            dierange=tokens[0].split('-')
            if(len(dierange) > 1):
                # We have multiple enteries to add to a table
                for i in range(int(dierange[0]), int(dierange[1])+1):
                    self.entries[i] = tokens[1]
            else:
                # We have a single entry
                self.entries[int(dierange[0])] = tokens[1]
        print(self.entries)
        print(self.stages)
    # END _load

    def return_table_entry(self):
        print self.stages
    #END return_table_entry



