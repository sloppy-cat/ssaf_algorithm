# 2814. 최장경로
def DFS(node,arr,visit,s):
  tmp = [s]
  for i,j in arr:
    if node == i:
      if j not in visit:
        tmp.append(DFS(j,arr,visit+[j],s+1))
  for j,i in arr:
    if node == i:
      if j not in visit:
        tmp.append(DFS(j,arr,visit+[j],s+1))
  return max(tmp)
      
for tc in range(int(input())):
  N, M = list(map(int,input().split()))
  arr = [list(map(int,input().split())) for _ in range(M)]
  arr.sort()
  result = []
  for i in range(1,N+1):
    result.append(DFS(i,arr,[i],1))
  print(f'#{tc+1} {max(result)}')
