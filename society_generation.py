# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import gmutils


# Mapping Government types to table files
gov_table_evolution_lookup = {
        "Autocracy": "tables/society_autocracy.txt",
        "Corporatism": "tables/society_corporatism.txt",
        "Democracy": "tables/society_democracy.txt",
        "Feudalism": "tables/society_feudalism.txt",
        "Hydraulic Despotism": "tables/society_hydraulicdespotism.txt",
        "Military Dictatorship": "tables/society_mildictatory.txt",
        "Monarchy": "tables/society_monarchy.txt",
        "Oligarchy": "tables/society_oligarchy.txt",
        "Republic": "tables/society_republic.txt",
        "Technocracy": "tables/society_technocracy.txt",
        "Theocracy": "tables/society_theocray.txt",
        "Tribalism": "tables/society_tribalism.txt"
}

gov_table_conflicts_lookup = {
        "Bigotry": "tables/society_bigotry.txt",
        "Freedom": "tables/society_freedom.txt",
        "Inequality": "tables/society_inequality.txt",
        "Land": "tables/society_land.txt",
        "Nationalism": "tables/society_nationalism.txt",
        "Privation": "tables/society_privation.txt",
        "Resentment": "tables/society_resentment.txt",
        "Resources": "tables/society_resources.txt",
        "Schism": "tables/society_schism.txt",
        "War": "tables/society_war.txt"
}


def main():
    # Determine the reason the world was colonized.
    print("Initial Colonization")
    colonizationgen = gmutils.table("tables/society_colonization.txt", "Colonization")
    print(colonizationgen.return_result())
    print("")

    # Choose initial Culture.
    print("Deltermine if there was a predominant original culture.")

    # Choose initial Government
    print("Initial Government Type")
    govgen = gmutils.table("tables/society_govtype.txt", "Government Type")
    gov_type = govgen.return_result()
    print(gov_type)
    print("")

    # Choose societal traits
    print("Initial Societal Traits")
    traitgen = gmutils.table("tables/society_traits.txt", "Societal Traits")
    # 2-3 Rolls
    for i in range(0, 3):
        print(traitgen.return_result())
    print("")

    # Choose main pre-scream conflict
    print("Pre-Scream Conflict")
    conflictgen = gmutils.table("tables/society_conflicts.txt", "Conflicts")
    prescreamconflict = conflictgen.return_result()
    print(prescreamconflict)

    conflict_details_gen(prescreamconflict)

    # Evolve the government based on pre-screm initial conflict
    print("Evolved government")
    evolvegovgen = gmutils.table(gov_table_evolution_lookup[gov_type], "Government Evolution")
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
    conflictdetailsgen = gmutils.table(gov_table_conflicts_lookup[conflictresult], "Conflict Details")
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
