# # 5249 최소신장트리
# import heapq

# for tc in range(int(input())):
#   v, e = list(map(int,input().split()))
#   edges = [list(map(int,input().split())) for _ in range(e)]
#   visit = [0]*(v+1)
#   edges_dict = {}
#   for edge in edges:
#     n1, n2, w = edge
#     try:
#       edges_dict[n1] += [(w, n2)]
#     except:
#       edges_dict[n1] = [(w, n2)]
#     try:
#       edges_dict[n2] += [(w, n1)]
#     except:
#       edges_dict[n2] = [(w, n1)]
#   heap = [(0,0)]
#   total = 0
#   while heap:
#     w, node = heapq.heappop(heap)
#     if visit[node]:
#       continue
#     # print(*heap)
#     # print(node, "번 노드, 가중치:",w)
#     # print()
#     visit[node] = 1
#     total += w

#     vals = edges_dict[node]
#     r_box = []
#     for next_w, next_node in vals:
#       if not visit[next_node]:
#         heapq.heappush(heap, (next_w, next_node))
#       else:
#         r_box.append((next_w, next_node))
#     for r in r_box:
#       edges_dict[node].remove(r)
#   print(f'#{tc+1} {total}')


# 5251 최소 이동 거리

# from collections import deque
# for tc in range(int(input())):
#   v, e = list(map(int,input().split()))
#   edges = [list(map(int,input().split())) for _ in range(e)]
#   distance = [100000000]*(v+1)
#   visit = [0]*(v+1)
#   lines = [[]for _ in range(v+1)]
#   for edge in edges:
#     n1, n2, w = edge
#     lines[n1].append([w,n2])
#   stack = deque([0])
#   distance[0] = 0
#   while stack:
#     node = stack.popleft()
#     w = distance[node]
#     if visit[node]:
#       continue
#     visit[node] = 1
#     for n_w, n_node in lines[node]:
#       distance[n_node] = min(distance[n_node], w + n_w)
#       if not visit[n_node]:
#         stack.append(n_node)
#   print(f'#{tc+1} {distance[v]}')
      
      

  