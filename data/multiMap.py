import time
import sys
import os
from tqdm import *

MAX_ITER = 50
machines = 10

def collect(fInNames, fOutNames, num):

    dic = {}
    for fIn in fInNames:
        with open(fIn, 'r') as lines:
            for line in lines:
                if line[-1] != '\n':
                    line += '\n'
                key, val = line.split('\t')
                dic[key] = dic.get(key, []) + [line]

    idx = 0
    split = len(dic) / num
    fOuts = [open(fOutName, 'w') for fOutName in fOutNames]
    for key in dic:
        for val in dic[key]:
            try:
                fOuts[min(idx / split, num - 1)].write(val)
            except:
                print('error: idx=%d, split=%d' %(idx, split))
                raise
                      

        idx += 1

    for f in fOuts:
        f.close()
if len(sys.argv) > 1:
    MAX_ITER = int(sys.argv[1])

    
fIn = 'input.txt'
if len(sys.argv) > 2:
    fIn = sys.argv[2]
if not os.path.exists('testing'):
    os.makedirs('testing')

# pagerankInput > pagerank_map > pagerankReduce > pagerank_reduce 
# > processInput > process_map > processReduce > process_reduce
# > input
input = 'testing/input'
pagerankInput = ['testing/pagerankInput' + str(i) for i in range(machines)]
pagerankMapOut = ['testing/pagerankMapOut' + str(i) for i in range(machines)]
pagerankReduce = ['testing/pagerankReduce' + str(i) for i in range(machines)]
pagerankReduceOut = ['testing/pagerankReduceOut' + str(i) for i in range(machines)]
processInput = 'testing/processInput'
processReduce = 'testing/processReduce'

os.system('cp %s %s' %(fIn, input))


start = time.time()
for iter in tqdm(range(MAX_ITER)):
    collect([input], pagerankInput, machines)
    for i in range(machines):
        os.system('python pagerank_map.py < %s > %s' %(pagerankInput[i], pagerankMapOut[i]))


    # pagerank_reduce
    collect(pagerankMapOut, pagerankReduce, machines)
    for i in range(machines):
        os.system('python pagerank_reduce.py < %s > %s' %(pagerankReduce[i], pagerankReduceOut[i]))

    collect(pagerankReduceOut, [processInput], 1)
    
    # process_map
    os.system('python process_map.py < %s > %s' %(processInput, processReduce))

    # process_reduce
    os.system('python process_reduce.py < %s > %s' %(processReduce, input))

print('%f Seconds' %(time.time() - start))


    


