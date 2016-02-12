#!/usr/bin/env python

import sys
import random


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

alpha = 0.85

num_walk = 500

def travel(prob):
    tmp = random.random()
    if tmp < prob: return True
    return False

# parse all raw input first
for line in sys.stdin:
    node, vals = line.split('\t')

    # pass along iterations, incrementing by one
    if node == 'Iters':
        sys.stdout.write(line)


    # if not iteration key, must be a node
    else:
        # DATA SPLICING:
        # First index is the current rank.
        # Second index is the previous rank.
        # Remaining are integers, correspong to
        # Node ID's.

        # note we remove the last char of vals, so no newline
        lst = vals[:-1].split(',')

        coupons = num_walk
        num_walks = num_walk
        if isInt(lst[0]) and isInt(lst[1]):
            coupons = int(lst[0])
            num_walks = int(lst[1])

        adj_nodes = lst[2:]

        d = {}
        if coupons > 0:
            walks_to_link = 0
            for i in range(coupons):
                if travel(alpha) and len(adj_nodes) > 0:
                    # pick a random neighbor
                    neighbor = random.sample(adj_nodes, 1)[0]
                    d[neighbor] = d.get(neighbor, 0) + 1

        for key, value in d.iteritems():
            sys.stdout.write('%s\tRnk%s\n' %(key, str(value)) )

        if len(adj_nodes) > 0:
            # note that vals already has newline in it
            sys.stdout.write('%s\tAdj%s\t%d\n' %(node[7:], ','.join(adj_nodes), num_walks))


# output is always node number
# tab
# Rnk or Adj
# rank contribution or currRank, prevRank, adjNodes\n



'''

# parses the raw input
for line in sys.stdin:
    res = line.split('\t')

    # Node ID is at index 0
    node = res[0]

    # DATA SPLICING:
    # First index is the current rank.
    # Second index is the previous rank.
    # Remaining are integers, corresponding to
    # Node ID's.

    # The graph is directed!
    lst = res[1].split(',')

    which_iter = 1


    # AFTER ONE ITERATIONS
    # First index: iteration number (integer)
    # Second index: current rank
    # Third index: previous rank
    # Remaining: Integers corresponding to Node ID's.

    # This determines whether or not this is the
    # first iteration or any subsequent iterations.

    # If statement occurs for subsequent iterations.
    # In this case, lst[0] is an iteration number.
    if isInt(lst[0]):
        which_iter = int(lst[0]) + 1
        curr_rank = lst[1]
        prev_rank = lst[2]
        adj_nodes = lst[3:]

    # Else statements occurs for the first iteration.
    # In this case, lst[0] is the current rank.
    else:
        curr_rank = lst[0]
        prev_rank = lst[1]
        adj_nodes = lst[2:]



    for link in adj_nodes:
        new_rank = float(curr_rank)/len(adj_nodes)
        # emit the amount of rank a node contributes to a neighbor,
        # the current iteration,
        # and remember this node

        # "adjNode \t iter,newRank,currentNode"
        result = str(link).rstrip() + ",rank" + "," + str(curr_rank) + "," + str(which_iter) \
            + "\t" + str(new_rank) + ","\
            + str(node[7:]) + "\n"
        sys.stdout.write(result)


        # its to-be previous rank
    #result2 = str(node[7:]).rstrip() + "\t" + str(curr_rank) + "\n"
    # sys.stdout.write(result2)

    if(len(adj_nodes) != 0):
        adjResult = str(node[7:]).rstrip() + ",list" + "," + str(curr_rank) + "," + str(which_iter) \
                     + "\t" + ",".join(adj_nodes)
        sys.stdout.write(adjResult)
    else:
        adjResult = str(node[7:]).rstrip() + ",list" + "," + str(curr_rank) + "," + str(which_iter) \
                     + "\t\n"
        sys.stdout.write(adjResult)
    # its to-be previous rank
    #"currentNode \t currRank"
    #result2 = str(node[7:]).rstrip() + "\t" + str(curr_rank) + "\n"
    #sys.stdout.write(result2)
'''


# dict = {}
# for line in sys.stdin:
#     res = line.split('\t')
#     node = res[0][7:]
#     adj = res[1].split(',')
#     dict[str(node)] = adj
#
# # construct a matrix
# num_nodes = len(dict)
# mat = [[0.0] * num_nodes for _ in range(num_nodes)]
# for key, value in dict.iteritems():
#     num_adj = (len(value)) - 2
#     print key
#     for val in value[2:]:
#         mat[int(key)][int(val)] = float(value[0])/num_adj
#
#
# numpy.dot(











