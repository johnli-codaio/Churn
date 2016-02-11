#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# remembers the top 20 scores
top = []
for line in sys.stdin:
    res = line.split('\t')
    node = res[0][7:]
    lst = res[1].split(',')

    which_iter = int(lst[0])
    curr_rank = lst[1]
    if len(top) < 20:
        top.append(float(curr_rank))
        top.sort(reverse=True)
        sys.stdout.write('A:' + str(node) \
                + '\t' + str(curr_rank) + '\n')
    elif float(curr_rank) > top[19]:
        top[19] = float(curr_rank)
        top.sort(reverse=True)
        sys.stdout.write('A:' + str(node) \
                + '\t' + str(curr_rank) + '\n')
        
    sys.stdout.write(line)

