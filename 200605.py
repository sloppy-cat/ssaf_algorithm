# 1486 장훈이의 높은선반
# res_min = 0
# def dfs(h, cnt):
#   global res_min
#   if h >= b:
#     res_min = min(res_min, h)
#   elif cnt < n:
#     dfs(h+hs[cnt], cnt+1)
#     dfs(h, cnt+1)

# for tc in range(int(input())):
#   res_min = 10000000
#   n, b = list(map(int,input().split()))
#   hs = list(map(int,input().split()))
#   dfs(0, 0)
#   print(f'#{tc+1} {res_min-b}')

# 1251 하나로
for tc in range(int(input())):
  n = int(input())
  xs = list(map(int, input().split()))
  ys = list(map(int, input().split()))
  e = float(input())
  visit = [0]*n
  INF = float('inf')
  disArr = [INF]*n
  disArr[0] = 0
  dis = 0
  n1, n2 = 0, 0
  for _ in range(n-1):
    dis = INF
    visit[n1] = 1
    for i in range(n):
      if not visit[i]:
        disArr[i] = min(disArr[i], (xs[i]-xs[n1])**2 + (ys[i]-ys[n1])**2)
        if dis > disArr[i]:
          dis = disArr[i]
          n2 = i
    n1 = n2
  total = sum(disArr)
  print(f'#{tc+1} {round(total*e)}')