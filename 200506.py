# 5188 최소합
def min_sum:
  for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    stack = [[0,0,0]]
    res = []
    while stack:
      i, j, tot = stack.pop()
      tot += arr[i][j]
      if i == n-1 and j == n-1:
        res.append(tot)
        continue
      if i < n-1:
        stack.append([i+1, j, tot])
      if j < n-1:
        stack.append([i, j+1, tot])
    print(f'#{tc+1} {min(res)}')

# 5189 전자키트

from itertools import permutations
def elec_kit:
  for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sets = list(map(list, permutations(range(1,n))))
    res = []
    for set_ in sets:
      set_ = [0] + set_ + [0]
      tmp = 0
      for i in range(n):
        tmp += arr[set_[i]][set_[i+1]]
      res.append(tmp)
    print(f'#{tc+1} {min(res)}')