input()
for tc in range(10):
  v, e, n1, n2 = map(int,input().split())
  c_tree = [[] for _ in range(v+1)]
  p_tree = [0]*(v+1)
  e_list = list(map(int,input().split()))
  for i in range(e):
    c_tree[e_list[i*2]].append(e_list[i*2+1])
    p_tree[e_list[i*2+1]] = e_list[i*2]
  p_lst = []
  for n in (n1, n2):
    p_box = []
    while p_tree[n]:
      p_box.append(p_tree[n])
      n = p_tree[n]
    p_lst.append(p_box)
  r_p = p_lst[0][-min(len(p_lst[0]),len(p_lst[1]))]
  for i in range(1, min(len(p_lst[0]),len(p_lst[1]))+1):
    if p_lst[0][-i] != p_lst[1][-i]:
      r_p = p_lst[0][-i+1]
      break

  cnt = 0
  stk = [r_p]
  while stk:
    cnt += 1
    ns = stk.pop()
    if c_tree[ns]:
      stk = stk + c_tree[ns]
  print(f'#{tc+1} {r_p} {cnt}')