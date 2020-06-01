for tc in range(int(input())):
  n = int(input())
  # 스도쿠 판을 2차원행렬에 입력받는다
  arr = [list(map(int,input().split())) for _ in range(9)]
  res = 0
  key = False
  # 퍼즐 숫자와 좌표를 2차원행렬에 입력받는다
  game = [list(map(int,input().split())) for _ in range(n)]
  for i,j,v in game:
    # 입력받은 좌표의 가로,세로,작은격자 안에 입력값과 같은 숫자가 있는지 찾는다.
    for k in range(9):
      if arr[i][k] == v or arr[k][j] == v or arr[k//3 + 3*(i//3)][k%3 + 3*(j//3)] == v:
        # 있다면 반복문에서 탈출
        key = True
        break
    if key:
      break
    # 반복문 한바퀴를 잘 돌때마다 result값을 1개씩 더한다
    res += 1
  print(f'#{tc+1} {res}')