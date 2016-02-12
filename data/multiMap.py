import time
import sys
import os
from tqdm import *

MAX_ITER = 50
machines = 10


def divide(fInNames, fOutNames, num):

    data = []
    for fIn in fInNames:
        with open(fIn, 'r') as lines:
            for line in lines:
                data.append(line)

    idx = 0
    split = len(data) / num
    fOuts = [open(fOutName, 'w') for fOutName in fOutNames]
    for line in data:
        try:
            fOuts[min(idx / split, num - 1)].write(line)
        except:
            print('error: idx=%d, split=%d' %(idx, split))
            raise

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
procMaps = 2
processInput = ['testing/processInput' + str(i) for i in range(procMaps)]
processMapOut = ['testing/processMapOut' + str(i) for i in range(procMaps)]
processReduce = 'testing/processReduce'

os.system('cp %s %s' %(fIn, input))


times = [0.0] * 4
start = time.time()
for iter in tqdm(range(MAX_ITER)):
    divide([input], pagerankInput, machines)

    s = time.time()
    for i in range(machines):
        os.system('python pagerank_map.py < %s > %s' %(pagerankInput[i], pagerankMapOut[i]))
    times[0] += (time.time() - s) / machines

    # pagerank_reduce
    collect(pagerankMapOut, pagerankReduce, machines)

    s = time.time()
    for i in range(machines):
        os.system('python pagerank_reduce.py < %s > %s' %(pagerankReduce[i], pagerankReduceOut[i]))
    times[1] += (time.time() - s) / machines

    divide(pagerankReduceOut, processInput, procMaps)
    
    # process_map
    s = time.time()
    for i in range(procMaps):
        os.system('python process_map.py < %s > %s' %(processInput[i], processMapOut[i]))
    times[2] += (time.time() - s) / procMaps

    collect(processMapOut, [processReduce], 1)
    # process_reduce
    s = time.time()
    os.system('python process_reduce.py < %s > %s' %(processReduce, input))
    times[3] += time.time() - s

print('pagerank_map: %f\npagerank_reduce: %f\nprocess_map %f\nprocess_reduce: %f\n' %(times[0], times[1], times[2], times[3]))
print('%s %f Seconds' %(fIn, time.time() - start))


    

