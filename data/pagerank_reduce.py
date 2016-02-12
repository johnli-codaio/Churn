#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# Note: This reduce function does not concatenate
#       everything. Things passed in are still individual
#       key,value pairs, and values are not concatenated.

curr_node = ''
adjList = ''
newRank = 0.0
for line in sys.stdin:
    key, vals = line.split('\t')
    if key == 'Iters':
        sys.stdout.write(line)
        continue
    if not curr_node:
        # to set the first curr_node
        curr_node = key

    if key != curr_node:
        # switched keys. time to print

        # doesn't point to anything
        if not adjList:
            adjList = ('1.0,%s\n' %curr_node)
            newRank += 1.0

        # alpha hard coded for optimization
        newRank = .15 + .85 * newRank

        # note that adjacency list contains \n
        sys.stdout.write('NodeId:%s\t%f,%s' %(curr_node, newRank, adjList))
        curr_node = key
        adjList = ''
        newRank = 0.0

    if key == curr_node and vals[:3] == 'Adj':
        adjList = vals[3:]
    elif key == curr_node:
        #else must be Rnk
        newRank += float(vals[3:-1])

#output the last node
if not adjList:
    adjList = ('1.0,%s\n' %curr_node)
    newRank += 1.0

# alpha hard coded for optimization
newRank = .15 + .85 * newRank

# note that adjacency list contains \n
sys.stdout.write('NodeId:%s\t%f,%s' %(curr_node, newRank, adjList))


