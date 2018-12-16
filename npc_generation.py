import json
import sys
import argparse
import gmutils

# GENERAL VARIABLES

name_table_lookup = {
        "arabic": "roll_tables/names_arabic.txt",
        "chinese": "roll_tables/names_chinese.txt",
        "english": "roll_tables/names_english.txt",
        "indian": "roll_tables/names_indian.txt",
        "japanese": "roll_tables/names_japanese.txt",
        "nigerian": "roll_tables/names_nigerian.txt",
        "russian": "roll_tables/names_russian.txt",
        "spanish": "roll_tables/names_spanish.txt"
}


# ARGUMENT PARSING

parser = argparse.ArgumentParser(description="Generate a random NPC for Stars Without Number")
parser.add_argument('-c', '--class',
        help="Argument should be expert, psychic, or warrior.",
        choices=["expert", "psychic", "warrior"],
        required=True)
parser.add_argument('-l', '--level',
        help="Numerical level of the NPC.",
        type=int,
        choices=range(1,11),
        required=True)
parser.add_argument('-n', '--nationality',
        help="Nationality of NPC. Currently only arabic names support.",
        choices=["arabic","english"],
        required=True)

args = parser.parse_args()

npcage = gmutils.roll_table("roll_tables/npc_age.txt", "NPC Age")
age = npcage.return_result()
print(age)

npcgender = gmutils.roll_table("roll_tables/npc_gender.txt", "NPC Gender")
gender = npcgender.return_result()
print(gender)

npcheight = gmutils.roll_table("roll_tables/npc_height.txt", "NPC Height")
height = npcheight.return_result()
print(height)

npcjobmotivate = gmutils.roll_table("roll_tables/npc_jobmotivation.txt", "NPC Job Motivation")
motivation = npcjobmotivate.return_result()
print(motivation)

npcproblems = gmutils.roll_table("roll_tables/npc_problems.txt", "NPC Problems")
problems = npcproblems.return_result()
print(problems)

npcquirks = gmutils.roll_table("roll_tables/npc_quirks.txt", "NPC Quirks")
quirks = npcquirks.return_result()
print(quirks)

npcnames = gmutils.roll_table(name_table_lookup[args.nationality], "NPC Name")
name = npcnames.return_result()[gender.lower()] + " " + npcnames.return_result()['surname']
print(name)


