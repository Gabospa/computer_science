#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the bfs function below.
def bfs(n, m, edges, s):
    #Create adjacency list empty on array
    neighbors = [[] for i in range(n) for j in range(1)]
    #Include neighbors of each vertex, with index minus 1
    for e in edges:
        neighbors[e[0]-1].append(e[1]-1)
        neighbors[e[1]-1].append(e[0]-1)
    
    #Seen and Distance begin in False and -1 each
    seen = [False for i in range(n)]
    distance = [-1 for i in range(n)]
    
    #Start vertex as True and distance 0
    seen[s - 1] = True
    distance[s - 1] = 0
    print(seen)
    print(distance)

    q = deque()
    q.append(s - 1)
    
    while len(q):
        v = q.popleft()
        for u in neighbors[v]:
            if seen[u] == False:
                distance[u] = distance[v] + 6
                seen[u] = True
                q.append(u)
        seen[v] = True
    
    return [distance[i] for i in range(n) if i != s-1]  
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()