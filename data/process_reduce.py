#!/usr/bin/env python

import sys
import heapq

#
# This program simply represents the identity function.
#


MAX_ITER = 10
# remembers the top 20 scores
top = []
data = []
isDone = False

which_iter = 1

for line in sys.stdin:
    #dis shit slow
    #key, val = line.split('\t')
    #if key == 'Iters':
    #    which_iter = int(val) + 1
    #    continue 

    if line[:5] == 'Iters':
        key, val = line.split('\t')
        which_iter = int(val) + 1
        continue
    data.append(line)

# stopping condition
if which_iter >= MAX_ITER:
    isDone = True

# when done, output a single key, value pair of the following form
# Done:\t 1.4 4,2.3 5,4.5 20
# comma separate tuples of (rank node)
if isDone:
    for line in data:
        key, val = line.split('\t')
        node = key[7:]
        lst = val.split(',')
        curr_rank = float(lst[0])

        if len(top) < 20:
            heapq.heappush(top, (curr_rank, node))

        elif curr_rank > top[0][0]:
            heapq.heappop(top)
            heapq.heappush(top, (curr_rank, node))

    for i in range(len(top)):
        top[i] = [float(top[i][0]), int(top[i][1])]
    top.sort(reverse=True)
    for rank, node in top:
        sys.stdout.write('FinalRank:%f\t%d\n' %(rank, node))
else:
    sys.stdout.write('Iters\t%d\n' %which_iter)
    for line in data:
        sys.stdout.write(line)


