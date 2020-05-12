# 5202 화물도크

for tc in range(int(input())):
  n = int(input())
  start_end_time = [list(map(int, input().split())) for _ in range(n)]

  sorted_list = sorted(start_end_time, key=lambda time: time[1])
  p_time = 0
  res = 0
  for s, e in sorted_list:
    if s >= p_time:
      res += 1
      p_time = e

  print(f'#{tc+1} {res}')

# 5201 컨테이너 운반
for tc in range(int(input())):
  n, m = list(map(int, input().split()))
  conteiner_w = list(map(int, input().split()))
  truck_t = list(map(int, input().split()))
  conteiner_w.sort(reverse=True)
  truck_t.sort(reverse=True)
  res = 0
  for t in truck_t:
    for i in range(len(conteiner_w)):
      if t >= conteiner_w[i]:
        res += conteiner_w[i]
        m = m-i
        conteiner_w = conteiner_w[i+1:]
        break
  print(f'#{tc+1} {res}')