#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# Note: This reduce function does not concatenate 
#       everything. Things passed in are still individual
#       key,value pairs, and values are not concatenated.

alpha = 0.85
# this reducer's particular key, since 
# keys are grouped into contiguous blocks
key = ""
rank = 0.0
old_rank = 0.0
adj_list = ""
curr_iter = 0

for line in sys.stdin:

    res = line.split('\t')
    nodeVals = res[0].split(',') # nodeVals are in the form (NodeID, "list/rank")
    node = nodeVals[0]
    representation = nodeVals[1]
    currRank = nodeVals[2]

    value = res[1].split(',') # Values are either: (iter, rank, currNode)
                              # Or                 (prevRank)
                              # Or                 ([adjList])
    #if(len(value) > 1):

    if key == "":
        key = node

    elif node == key:
        pass
    else:
        # moved onto a new block
        # emit the rank of the previous block
        # here we're using the matrix G = alpha*P + (1-alpha)/n * 1_(n*n)
        # and this is where we finalize the computation pi = piG
        # the second term contributes 1-alpha to every element in the vector
        # of pi, and the first term just multiplies the sum
        # of each node's contribution to an element by alpha
        rank = alpha * (rank) + (1 - alpha)
        sys.stdout.write("NodeId:" + key +\
                        "\t" + str(curr_iter) + "," +\
                        str(rank) + "," + str(old_rank) + \
                        adj_list)
        # reset rank, adj_list
        rank = 0.0
        adj_list = ""

    if(representation == "rank"):
        curr_iter = int(value[0])
        contrib = float(value[1])
        contrib_by = (value[2]).rstrip()
        rank += float(contrib)
        key = node

    elif(representation == "list"):
        if(value[0] != "\n"):
            adj_list = "," + ",".join(value[:len(value)])
        else:
            adj_list = "\n"
            rank = float(currRank)
        key = node


    #else:
    #    old_rank = float(value[0])

rank = alpha * (rank) + (1 - alpha)
sys.stdout.write("NodeId:" + key +\
        "\t" + str(curr_iter) + "," +\
        str(rank) + "," + str(old_rank) +\
        adj_list)
# reset rank, adj_list
rank = 0.0
adj_list = []

