#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#




# keeps track fo the top 20's scores and which nodes
lst = []

is_done = False

for line in sys.stdin:
    # will only be passed 1 key, value pair when done
    key, vals = line.split('\t')
    if key == 'Done:':
        is_done = True
        top = [val.split(' ') for val in vals.split(',')]
        for i in range(len(top)):
            top[i] = [float(top[i][0]), int(top[i][1])]
        top.sort(reverse=True)
        for rank, node in top:
            sys.stdout.write('FinalRank:%f\t%d\n' %(rank, node))
    if not is_done:
        sys.stdout.write(line)


