# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import gmutils

print("\033[1mDetermine Atmosphere\033[0m")
atmospheregen = gmutils.roll_table("roll_tables/world_atmosphere.txt", "Atmosphere")
print(atmospheregen.return_result())

print("\033[1mDetermine Temperature\033[0m")
tempgen = gmutils.roll_table("roll_tables/world_temperature.txt", "Temperature")
print(tempgen.return_result())

print("\033[1mDetermine Biosphere\033[0m")
biospheregen = gmutils.roll_table("roll_tables/world_biosphere.txt", "Biosphere")
print(biospheregen.return_result())

print("\033[1mDetermine Population\033[0m")
popgen = gmutils.roll_table("roll_tables/world_population.txt", "Population")
print(popgen.return_result())

print("\033[1mDetermine Tech Level\033[0m")
techlvlgen = gmutils.roll_table("roll_tables/world_techlevel.txt", "Tech Level")
print(techlvlgen.return_result())

print("\033[1mDetermine World Tag #1\033[0m")
worldtaggen = gmutils.roll_table("roll_tables/world_tags.txt", "World Tags")
print(worldtaggen.return_result())
print("\033[1mDetermine World Tag #2\033[0m")
print(worldtaggen.return_result())

print("\n\tConsider four examples of Enemies, Friends, Complications, Things, and Places based on the generated world tags.")
