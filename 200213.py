# def DFS(G,V,v):
#     visit = []
#     stack = []

#     stack.append(v)
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             for nodee in G:
#                 if nodee[0] == node:
#                     stack.append(nodee[1])
#     if len(visit) == V:
#         return visit
#     return False

import collections
import sys
sys.stdin = open("input.txt","r")

def queue(G,V):
    visit = []
    queue = collections.deque(range(1,V+1))
    while queue:
        trg = 0
        node = queue.popleft()
        for nodee in G:
            if nodee[1] == node:
                if nodee[0] not in visit:
                    trg = 1
                    break
        if trg:
            queue.append(node)
        else :
            visit.append(node)

    
    return visit


def work_order():
    for tc in range(1,11):
        V, E = list(map(int,input().split()))
        G_notsort = list(map(int,input().split()))
        G = []
        for i in range(0,len(G_notsort),2):
            G.append([G_notsort[i], G_notsort[i+1]])
        result = queue(G,V)
        if result:
            print(f'#{tc} ',end="")
            print(*result)
work_order()
