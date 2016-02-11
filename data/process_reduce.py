#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#


MAX_ITER = 50

# keeps track fo the top 20's scores and which nodes
lst = []

is_done = False

for line in sys.stdin:
    if not is_done:
        res = line.split('\t')
        key = res[0]
        vals = res[1].split(',')
        if key.startswith('NodeId') and int(vals[0]) >= MAX_ITER:
            for vals in lst:
                curr_rank = vals[0]
                node = vals[1]
                sys.stdout.write('FinalRank:' + str(curr_rank) \
                        + '\t' + str(node) + '\n')
            is_done = True
        elif key.startswith('A:'):
            node = key[2:]
            rank = float(res[1])
            if len(lst) < 20:
                lst.append((rank, node))
            else:
                lst[19] = (rank, node)
            lst.sort(key = lambda tup: tup[0], reverse = True)

        else:
            sys.stdout.write(line)


