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
# dictionary of contributions to nodes
contribs = {}

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
          	contribs[key] = contribs.get(key, 0) + value

        if len(adj_nodes) > 0:
            # note that vals already has newline in it
            sys.stdout.write('%s\tAdj%s\t%d\n' %(node[7:], ','.join(adj_nodes), num_walks))

for key in contribs:
    sys.stdout.write('%s\tRnk%f\n' %(key, contribs[key]))

# output is always node number
# tab
# Rnk or Adj
# rank contribution or currRank, prevRank, adjNodes\n










