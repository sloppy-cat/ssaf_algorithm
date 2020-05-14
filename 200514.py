# 5207 이진 탐색
for tc in range(int(input())):
  n, tmp = list(map(int, input().split()))
  n_arr = list(map(int, input().split()))
  m_arr = list(map(int, input().split()))
  n_arr.sort()
  res = 0
  for m in m_arr:
    l, r = 0, n-1
    b = 2
    while True:
      mid = n_arr[(l+r)//2]
      if m == mid:
        res += 1
        break
      elif l == r:
        break
      elif m > mid and b != 1:
        l = (l+r)//2+1
        b = 1
      elif m < mid and b != 0:
        r = (l+r)//2-1
        b = 0
      else:
        break
  print(f'#{tc+1} {res}')