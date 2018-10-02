import random
import sys
import json

class dice:
    """ Class for rolling dice. """
    def __init__(self, count, sides):
            self.number = count
            self.sides = sides

    def roll(self):
        result = 0
        for i in range(0,self.number):
            result = result + random.randint(1,self.sides)
        return result
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
        parsed_table = json.load(filehandle)

        self.stages_cnt = parsed_table["stages"]

        for diecount in parsed_table["dice"]:
            (count, sides) = diecount.split("D")
            self.stages.append(dice(int(count), int(sides)))

        self.entries = parsed_table["entries"]
    # END _load

    def return_result(self):
        tag_result = None
        for dice in self.stages:
            if (tag_result == None):
                # String conversion because JSON-based dict's have keys stored as strings.
                tag_result = self.entries[str(dice.roll())]
            else:
                # String conversion because JSON-based dict's have keys stored as strings.
                tag_result = tag_result[str(dice.roll())]
        return tag_result
    #END return_table_entry



