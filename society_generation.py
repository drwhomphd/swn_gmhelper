# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import gmutils


# Mapping Government types to table files
gov_table_evolution_lookup = {
        "Autocracy": "roll_tables/society_autocracy.txt",
        "Corporatism": "roll_tables/society_corporatism.txt",
        "Democracy": "roll_tables/society_democracy.txt",
        "Feudalism": "roll_tables/society_feudalism.txt",
        "Hydraulic Despotism": "roll_tables/society_hydraulicdespotism.txt",
        "Military Dictatorship": "roll_tables/society_mildictatory.txt",
        "Monarchy": "roll_tables/society_monarchy.txt",
        "Oligarchy": "roll_tables/society_oligarchy.txt",
        "Republic": "roll_tables/society_republic.txt",
        "Technocracy": "roll_tables/society_technocracy.txt",
        "Theocracy": "roll_tables/society_theocray.txt",
        "Tribalism": "roll_tables/society_tribalism.txt"
}

gov_table_conflicts_lookup = {
        "Bigotry": "roll_tables/society_bigotry.txt",
        "Freedom": "roll_tables/society_freedom.txt",
        "Inequality": "roll_tables/society_inequality.txt",
        "Land": "roll_tables/society_land.txt",
        "Nationalism": "roll_tables/society_nationalism.txt",
        "Privation": "roll_tables/society_privation.txt",
        "Resentment": "roll_tables/society_resentment.txt",
        "Resources": "roll_tables/society_resources.txt",
        "Schism": "roll_tables/society_schism.txt",
        "War": "roll_tables/society_war.txt"
}


def main():
    # Determine the reason the world was colonized.
    print("Initial Colonization")
    colonizationgen = gmutils.roll_table("roll_tables/society_colonization.txt", "Colonization")
    print(colonizationgen.return_result())
    print("")

    # Choose initial Culture.
    print("Deltermine if there was a predominant original culture.")

    # Choose initial Government
    print("Initial Government Type")
    govgen = gmutils.roll_table("roll_tables/society_govtype.txt", "Government Type")
    gov_type = govgen.return_result()
    print(gov_type)
    print("")

    # Choose societal traits
    print("Initial Societal Traits")
    traitgen = gmutils.roll_table("roll_tables/society_traits.txt", "Societal Traits")
    # 2-3 Rolls
    for i in range(0, 3):
        print(traitgen.return_result())
    print("")

    # Choose main pre-scream conflict
    print("Pre-Scream Conflict")
    conflictgen = gmutils.roll_table("roll_tables/society_conflicts.txt", "Conflicts")
    prescreamconflict = conflictgen.return_result()
    print(prescreamconflict)

    conflict_details_gen(prescreamconflict)

    # Evolve the government based on pre-screm initial conflict
    print("Evolved government")
    evolvegovgen = gmutils.roll_table(gov_table_evolution_lookup[gov_type], "Government Evolution")
    evolvegovtype = evolvegovgen.return_result()
    print(evolvegovtype)

    # Optional second conflict
    print("Post-Scream Conflict")
    postscreamconflict = conflictgen.return_result()
    print(postscreamconflict)

    conflict_details_gen(postscreamconflict)

    # Optional Government Evolution

    # Personalize the conflicts
    print("Make sure to personalize the conflicts for this world.")
# END Main

def conflict_details_gen(conflictresult):
    # Then choose source, constraints, and changes based on chosen conflict
    conflictdetailsgen = gmutils.roll_table(gov_table_conflicts_lookup[conflictresult], "Conflict Details")
    changes = conflictdetailsgen.return_result()['changes']
    details = conflictdetailsgen.return_result()['details']
    constraints = conflictdetailsgen.return_result()['constraints']

    print(changes)
    print("")
    print(details)
    print("")
    print(constraints)
    print("")
# END conflict_details_gen

if __name__ == "__main__":
    main()
