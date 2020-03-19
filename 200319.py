a = input
for tc in range(int(a())):
  N = int(a())
  i = 1
  while i**3 < N:
    i += 1
  if not(i**3 == N):
    i = -1
  print(f'#{tc} {i}')
  
    
    
  