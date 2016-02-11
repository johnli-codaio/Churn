#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# Note: This reduce function does not concatenate 
#       everything. Things passed in are still individual
#       key,value pairs, and values are not concatenated.


contribs = {}
adjList = {}
for line in sys.stdin:
    key, vals = line.split('\t')
    if key == 'Iters':
        sys.stdout.write(line)
        continue

    if vals[:3] == 'Adj':
        adjList[key] = vals[3:]
        if key not in contribs:
            contribs[key] = 0.0
    # else must be Rnk
    else:
        #assert(vals[:3] == 'Rnk') #error checking, remove for production
        
        # skip last char cause it will be \n
        contribs[key] = contribs.get(key, 0.0) + float(vals[3:-1])

for node in contribs:
    if node not in adjList:
        adjList[node] = ('1.0,%s\n' %node)
        contribs[node] += 1

    # alpha hard coded for optimization
    newRank = .15 + .85 * contribs[node]
    # note that adjacency list contains \n 
    sys.stdout.write('NodeId:%s\t%f,%s' %(node, newRank, adjList[node]))

    

        
'''

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
    nodeVals = res[0].split(',') # nodeVals are in the form (NodeID, "list/rank", currRank, currIter)
    node = nodeVals[0]
    representation = nodeVals[1]
    currRank = nodeVals[2]
    curr_iter = nodeVals[3]

    value = res[1].split(',') # Values are either: (rank, currNode)
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
        if adj_list == "":
            adj_list = '\n'
            rank += 1.0 # Only occurs initially, with no node entry.

        rank = alpha * (rank) + (1 - alpha)
        sys.stdout.write("NodeId:" + key +\
                        "\t" + str(curr_iter) + "," +\
                        str(rank) + "," + str(old_rank) + \
                        adj_list)
        # reset rank, adj_list
        rank = 0.0
        adj_list = ""

    if(representation == "rank"):
        contrib = float(value[0])
        contrib_by = (value[1]).rstrip()
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
'''

