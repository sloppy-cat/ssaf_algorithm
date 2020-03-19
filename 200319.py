def _5688():
  a = input
  for tc in range(int(a())):
    N = int(a())
    i = 1
    while i**3 < N:
      i += 1
    if not(i**3 == N):
      i = -1
    print(f'#{tc+1} {i}')

import copy
def DFS(arr, idx, n):
  if idx == n:
    return 1
  else:
    res = 0
    for k in range(n):
      if not(arr[idx][k]):
        n_arr = copy.deepcopy(arr)
        for i in range(n):
          n_arr[idx][i] = 1
          n_arr[i][k] = 1
          try:
            n_arr[idx+i][k+i] = 1
          except:
            pass

          try:
            n_arr[idx-i][k-i] = 1
          except:
            pass

          try:
            n_arr[idx-i][k+i] = 1
          except:
            pass

          try:
            n_arr[idx+i][k-i] = 1
          except:
            pass
        res += DFS(n_arr, idx+1, n)
    return res

a = input
for tc in range(int(a())):
  N = int(a())
  r = DFS([[0]*N]*N, 0, N)
  print(f'#{tc+1} {r}')

    
    
  