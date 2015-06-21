#!/usr/bin/env python

import sys
import rubik.view as rv
from rubik import *

if __name__ == "__main__":
    p = box([4, 8, 4])
    rv.color(p, start_color=2)
    p.zorder(0)
    print p
    r = box([8, 4, 8])
    r.zorder(1)
    print r
    r.map(p)
    print r

    f = open('mapfile', 'w')
    r.write_map_file(f)
    f.close()

