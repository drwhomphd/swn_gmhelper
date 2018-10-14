#This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import gmutils

star_cnt_die = gmutils.dice(1, 10)
star_column_die = gmutils.dice(1, 8)
star_row_die = gmutils.dice(1,10)


star_cnt = star_cnt_die.roll() + 20

print("Generating positions for %d stars..." % (star_cnt,))

for i in range(0, 20):
    # Die rolls are -1 as the SWN Sector Map uses 0-index coordinates.
    print("Star ID %d located at position (%d, %d)" % (i, int(star_column_die.roll())-1, int(star_row_die.roll())-1))

print("Please place the final %d stars manually..." % (star_cnt-20))
