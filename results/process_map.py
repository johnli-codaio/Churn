#!/usr/bin/env python

import sys
import heapq
#
# This program simply represents the identity function.
#

MAX_ITER = 50
# remembers the top 20 scores
top = []
data = []
isDone = False
for line in sys.stdin:
    res = line.split('\t')
    node = res[0][7:]
    lst = res[1].split(',')
    
    which_iter = int(lst[0])
    
    # stopping condition
    if which_iter >= MAX_ITER:
        isDone = True

    curr_rank = lst[1]
    if len(top) < 20:
        heapq.heappush(top, (float(curr_rank), node))
        '''sys.stdout.write('A:' + str(node) \
                + '\t' + str(curr_rank) + '\n')'''
    elif float(curr_rank) > top[0][0]:
        heapq.heappop(top)
        heapq.heappush(top, (float(curr_rank), node))
    data.append(line)


# when done, output a single key, value pair of the following form
# Done:\t 1.4 4,2.3 5,4.5 20
# comma separate tuples of (rank node)
if isDone:
    sys.stdout.write('Done:\t%s' %','.join(['%s %s' %(str(rank), str(node)) \
                                                for rank, node in top]))
else:
    for line in data:
        sys.stdout.write(line)



