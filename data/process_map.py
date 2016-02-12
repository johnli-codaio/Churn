#!/usr/bin/env python

import sys
#import heapq


for line in sys.stdin:
    sys.stdout.write(line)
'''
#
# This program simply represents the identity function.
#

MAX_ITER = 50
# remembers the top 20 scores
top = []
data = []
isDone = False

which_iter = 1
for line in sys.stdin:
    key, val = line.split('\t')
    if key == 'Iters':
        which_iter = int(val) + 1
        continue
    node = key[7:]
    
    lst = val.split(',')
    
    curr_rank = float(lst[0])
    if len(top) < 20:
        heapq.heappush(top, (curr_rank, node))

    elif curr_rank > top[0][0]:
        heapq.heappop(top)
        heapq.heappush(top, (curr_rank, node))
    data.append(line)

# stopping condition 
if which_iter >= MAX_ITER:
    isDone = True

# when done, output a single key, value pair of the following form
# Done:\t 1.4 4,2.3 5,4.5 20
# comma separate tuples of (rank node)
if isDone:
    sys.stdout.write('Done:\t%s' %','.join(['%s %s' %(str(rank), str(node)) \
                                                for rank, node in top]))
else:
    sys.stdout.write('Iters\t%d\n' %which_iter)
    for line in data:
        sys.stdout.write(line)

'''

