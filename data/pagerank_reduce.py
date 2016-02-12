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
newCount = 0
newCoupon = 500
for line in sys.stdin:
    tmp = line.split('\t')
    key = tmp[0]
    vals = tmp[1]
    count = "0"

    if key == 'Iters':
        sys.stdout.write(line)
        continue
    if not curr_node:
        # to set the first curr_node
        curr_node = key

    if key != curr_node:
        # switched keys. time to print
		# note that adjacency list contains \n
		#output the last node
		if not adjList:
    		adjList = ('%s\n' %curr_node)
        sys.stdout.write('NodeId:%s\t%d,%d,%s' %(curr_node, newCoupon, newCount, adjList))
        curr_node = key
        adjList = ''
        newRank = 0
		newCoupon = 500
    # else must be Rnk
    else:
		if vals[:3] == 'Adj':
        	adjList = vals[3:]
			newCount = count
		else:
        # skip last char cause it will be \n
        # contribs[key] = contribs.get(key, 0.0) + float(vals[3:-1])
        	newRank = count


#output the last node
if not adjList:
    adjList = ('%s' %curr_node)
sys.stdout.write('NodeId:%s\t%d,%d,%s' %(curr_node, newRank, adjList))




