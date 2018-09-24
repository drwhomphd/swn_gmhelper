import gmutils

print("Atmosphere Generation")
atmospheregen = gmutils.table("tables/world_atmosphere.txt", "Atmosphere")
atmospheregen.return_result()

print("World Tags Generation")
worldtaggen = gmutils.table("tables/world_tags.txt", "World Tags")
worldtaggen.return_result()
