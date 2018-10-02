import gmutils

star_cnt_die = gmutils.dice(1, 10)
star_column_die = gmutils.dice(1, 8)
star_row_die = gmutils.dice(1,10)


star_cnt = star_cnt_die.roll() + 20

print("Generating positions for %d stars..." % (star_cnt,))

for i in range(0, 20):
    print("Star ID %d located at position (%d, %d)" % (i, star_column_die.roll(), star_row_die.roll()))

print("Please place the final %d stars manually..." % (star_cnt-20))
