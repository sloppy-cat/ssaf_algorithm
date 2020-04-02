# 회전
def rotation():
  from collections import deque
  for tc in range(int(input())):
    n, m = list(map(int,input().split()))
    deq = deque(list(map(int,input().split())))
    for _ in range(m):
      deq.append(deq.popleft())
    print(f'#{tc+1} {deq[0]}')


# 피자 굽기
def pizza():
  for tc in range(int(input())):
    n, m = list(map(int,input().split()))
    arr = deque([[x,y]for x,y in enumerate(list(map(int,input().split())))])
    deq = deque()
    r = [0,0]

    while arr or deq:
      if len(deq)<n and arr:
        tmp = arr.popleft()
        tmp[1] = tmp[1]//2
        deq.append(tmp)
      else:
        if deq[0][1]:
          tmp = deq.popleft()
          tmp[1] = tmp[1]//2
          deq.append(tmp)
        else:
          r = deq.popleft()
    print(f'#{tc+1} {r[0]+1}')



#회전
#rotation()

#피자 굽기
#pizza()