# 1249 보급로
# from collections import deque
# for tc in range(int(input())):
#   n = int(input())
#   arr = [list(map(int, list(input()))) for _ in range(n)]
#   d_arr = [[9999]*n for _ in range(n)] 
#   d_arr[0][0] = 0
#   dx, dy = [0,0,1,-1],[1,-1,0,0]
#   queue = deque()
#   queue.append([0,0])
#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx, ny = x+dx[i], y+dy[i]
#       if 0 <= nx < n and 0 <= ny < n:
#         if d_arr[nx][ny] > d_arr[x][y] + arr[nx][ny]:
#           queue.append([nx,ny])
#           d_arr[nx][ny] = d_arr[x][y] + arr[nx][ny]
#   print(f'#{tc+1} {d_arr[-1][-1]}')
          

# 5521 상원이의 생일파티
from collections import deque
for tc in range(int(input())):
  n, m = list(map(int,input().split()))
  arr = [[] for _ in range(n+1)]
  for _ in range(m):
    a, b = list(map(int,input().split()))
    arr[a].append(b)
    arr[b].append(a)
  visit = [0]*(n+1)
  
  friends = arr[1]
  for fri in arr[1]:
    visit[fri] = 1
    for frifri in arr[fri]:
      visit[frifri] = 1
  visit[1] = 0
  print(f'#{tc+1} {visit.count(1)}')