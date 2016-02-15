#!/usr/bin/env python

import sys



# dictionary of contributions to nodes
contribs = {}

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
        assert vals[-1] == '\n'
        # note we remove the last char of vals, so no newline
        lst = vals[:-1].split(',')
        curr_rank = lst[0]
        #prev_rank = lst[1]
        adj_nodes = lst[2:]

        # nodes with no adj_list is handled by reduce

        for link in adj_nodes:
            # only occurs when len(adj_nodes) > 0
            new_rank = float(curr_rank) / len(adj_nodes)

            contribs[link] = contribs.get(link, 0.0) + new_rank
        if len(adj_nodes) > 0:

            sys.stdout.write('%s\tAdj%s\n' %(node[7:], curr_rank + ',' + ','.join(adj_nodes)))

for key in contribs:
    sys.stdout.write('%s\tRnk%f\n' %(key, contribs[key]))

# output is always node number
# tab
# Rnk or Adj
# rank contribution or currRank, prevRank, adjNodes\n










