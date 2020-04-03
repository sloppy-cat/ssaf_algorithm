from collections import deque
# 미로의 거리
def bfs_miro(arr, start_point):
  n = len(arr)
  di = [0,0,1,-1]
  dj = [1,-1,0,0]
  que = deque([start_point+[0]])
  while que:
    i, j, c = que.popleft()
    arr[i][j] = 1
    for k in range(4):
      ni, nj = i+di[k], j+dj[k]
      if 0 <= ni < n and 0 <= nj < n:
        if arr[ni][nj] == 0:
          que.append([ni,nj,c+1])
        elif arr[ni][nj] == 3:
          return c
  return 0
def distance_or_miro():
  for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(n)]
    res = 0
    for i in range(n):
      for j in range(n):
        if arr[i][j] == 2:
          res = bfs_miro(arr, [i,j])
    print(f'#{tc+1} {res}')


# 노드의 거리
def dfs_node(dic, s, g):
  que = deque([[s,0]])
  visit = []
  while que:
    node = que.popleft()
    if node[0] == g:
      return node[1]
    elif node[0] not in visit:
      visit.append(node[0])
      for x in dic[node[0]]:
        que.append([x,node[1]+1])
  return 0
    
def distance_of_node():
  for tc in range(int(input())):
    v, e = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(e)]
    s, g = list(map(int,input().split()))
    dic = {}
    for x in arr:
      if x[0] in dic.keys():
        dic[x[0]].append(x[1])
      else :
        dic[x[0]] = [x[1]]
      if x[1] in dic.keys():
        dic[x[1]].append(x[0])
      else :
        dic[x[1]] = [x[0]]
    res = dfs_node(dic, s, g)
    print(f'#{tc+1} {res}')



#미로의 거리
#distance_or_miro()

#노드의 거리
#distance_of_node()