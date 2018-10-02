import gmutils

print("\033[1mDetermine Atmosphere\033[0m")
atmospheregen = gmutils.table("tables/world_atmosphere.txt", "Atmosphere")
print(atmospheregen.return_result())

print("\033[1mDetermine Temperature\033[0m")
tempgen = gmutils.table("tables/world_temperature.txt", "Temperature")
print(tempgen.return_result())

print("\033[1mDetermine Biosphere\033[0m")
biospheregen = gmutils.table("tables/world_biosphere.txt", "Biosphere")
print(biospheregen.return_result())

print("\033[1mDetermine Population\033[0m")
popgen = gmutils.table("tables/world_population.txt", "Population")
print(popgen.return_result())

print("\033[1mDetermine Tech Level\033[0m")
techlvlgen = gmutils.table("tables/world_techlevel.txt", "Tech Level")
print(techlvlgen.return_result())

print("\033[1mDetermine World Tag #1\033[0m")
worldtaggen = gmutils.table("tables/world_tags.txt", "World Tags")
print(worldtaggen.return_result())
print("\033[1mDetermine World Tag #2\033[0m")
print(worldtaggen.return_result())

print("\n\tConsider four examples of Enemies, Friends, Complications, Things, and Places based on the generated world tags.")
