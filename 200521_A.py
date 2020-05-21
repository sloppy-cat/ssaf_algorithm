# 5648 원자 소멸 시뮬레이션
# import copy

# for tc in range(int(input())):
#   a=[[2*x,2*y,m,k] for x,y,m,k in [list(map(int,input().split())) for _ in range(int(input()))]]
#   dx,dy,r=[0,0,-1,1],[1,-1,0,0],0
#   for _ in range(4002):
#     axy=[(x,y) for x,y,m,k in a]
#     nxy=list(set([tuple(xy) for xy in axy]))
#     if len(nxy)!=len(axy):
#       ta=copy.deepcopy(axy)
#       for t in nxy:
#         ta.remove(t)
#       for xy in ta:
#         for _ in range(axy.count((xy[0],xy[1]))):
#           i=axy.index(xy)
#           axy.pop(i)
#           r+=a.pop(i)[3]
#     a=[[x+dx[m],y+dy[m],m,k] for x,y,m,k in a]
#   print(f'#{tc+1} {r}')

#5653 줄기세포 배양
import copy
for tc in range(int(input())):
  n, m, k = list(map(int, input().split()))
  arr_cell_pan = [list(map(int, input().split())) for _ in range(n)]
  di, dj = [0,0,1,-1], [1,-1,0,0]

  # 초기 dict 세팅
  cell_dict = {}
  for i in range(n):
    for j in range(m):
      if arr_cell_pan[i][j]:
        cell_dict[(i,j)] = [1,arr_cell_pan[i][j]]
  active = list(cell_dict.keys())

  for k_time in range(k):
    new = []
    dead = []
    for key in active:
      ex_time, life = cell_dict[key]
      if ex_time == life+1:
        #활성화시키고 번식하자
        cell_dict[key] = [-1, life]
        for idx in range(4):
          n_key = (key[0]+di[idx], key[1]+dj[idx])
          try:
            if cell_dict[n_key][0] != -99:
              if n_key not in active:
                if n_key in new:
                  if life <= cell_dict[n_key][1]:
                    continue
                cell_dict[n_key] = [1,life]
                new.append(n_key)
          except:
            cell_dict[n_key] = [1,life]
            new.append(n_key)
      elif ex_time == -life:
        #쥬금
        cell_dict[key] = [-99, life]
        dead.append(key)
      else:
        #성장중
        cell_dict[key] = [ex_time + (ex_time//abs(ex_time)), life]
        
    #살아있는거랑 죽은거(확인용) 정리하기
    for key in new:
      active.append(key)
    for key in dead:
      active.remove(key)


  for key in active:
    ex_time, life = cell_dict[key]
    if ex_time == -life:
      cell_dict[key] = [0, life]
  res = [x for x,y in list(cell_dict.values())]
  r = len(res) - res.count(0) - res.count(-99)
  print(f'#{tc+1} {r}')

  