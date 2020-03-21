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


def check(arr):
  for a in arr:
    print(*a)
  print()

import copy
def DFS(arr, i, n):
  if i == n:
    return 1
  else:
    res = 0
    for j in range(n):
      if not(arr[i][j]):
        n_arr = copy.deepcopy(arr)
        for di, dj in (1,-1),(1,0),(1,1):
          ii, jj= i, j
          while(0<=ii<n and 0<=jj<n):
            n_arr[ii][jj] = 1
            ii += di
            jj += dj
        res += DFS(n_arr, i+1, n)
    return res

a = input
for tc in range(int(a())):
  N = int(a())
  r = DFS([[0]*N]*N, 0, N)
  print(f'#{tc+1} {r}')

    
    
  