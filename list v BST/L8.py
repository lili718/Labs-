import random
from BST import BST, Node
import time
import matplotlib.pyplot as plt

def populate(length):
    out = []
    bst = BST()
    for i in range(0,length):
        n = random.randint(0,length)
        out.append(n)
        bst.append(n)
    return (out, bst)

def _in(n, l):
    #return n in l #built in solution lmao
    for val in l:
        if n == val:
            return True
    return False

times = []
times2 = []
for n in range(0,10000,1000):
    print(n)
    tup = populate(n)
    l = tup[0]
    bst = tup[1]
    count = 0
    for item in l:
        if bst.isin(item):
            count += 1
    print(count)
    t = time.time()
    for i in l:
        _in(i, l)
    times.append(time.time() - t)
    t2 = time.time()
    for i in l:
        bst.isin(i)
    times2.append(time.time() - t2)

plt.plot(range(0,10000, 1000), times, label = 'list')
plt.plot(range(0,10000, 1000), times2, label = 'bst')
plt.legend()
plt.show()






