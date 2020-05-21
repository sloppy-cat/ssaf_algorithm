from collections import deque
# 5247 연산
# def bfs_cal(n, m):
#   visit = [False]*1000001
#   queue = deque()
#   queue.append([n,0])
#   while queue:
#     tmpNumber, cnt = queue.popleft()
#     visit[tmpNumber] = True
#     if tmpNumber > 1000000 or tmpNumber < 1:
#       continue
#     if visit[tmpNumber]:
#       continue
#     if tmpNumber == m:
#       return cnt
#     queue.append([tmpNumber*2,cnt+1])
#     queue.append([tmpNumber+1,cnt+1])
#     queue.append([tmpNumber-1,cnt+1])
#     queue.append([tmpNumber-10,cnt+1])
#   return 0

# for tc in range(int(input())):
#   n, m = list(map(int,input().split()))
#   res = bfs_cal(n, m)
#   print(f'#{tc+1} {res}')


# 5248 그룹나누기
# def dfs_search(n, m_dict):
#   visit = [0]*(n+1)
#   stack = []
#   cnt = 0
#   for i in range(1, n+1):
#     if not visit[i]:
#       cnt += 1
#       stack.append(i)
#       while stack:
#         node = stack.pop()
#         if not visit[node]:
#           visit[node] = 1
#           try:
#             stack += m_dict[node]
#           except:
#             pass
#   return cnt

# for tc in range(int(input())):
#   n, m = list(map(int,input().split()))
#   m_arr = list(map(int,input().split()))
#   m_couples = [[m_arr[i*2], m_arr[i*2+1]] for i in range(m)]
#   m_couples = m_couples + [[m_arr[i*2+1], m_arr[i*2]] for i in range(m)]
#   m_dict = {}
#   for key, val in m_couples:
#     if key in m_dict.keys():
#       m_dict[key] += [val]
#     else:
#       m_dict[key] = [val]
#   res = dfs_search(n, m_dict)

#   print(f'#{tc+1} {res}')