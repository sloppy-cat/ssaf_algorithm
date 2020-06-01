for tc in range(int(input())):
  n, m = list(map(int, input().split()))
  # 사람수와 사탕수중에 적은값 (분배할때 쓸것)
  d = min(n, m)
  # children have candy
  chc = [list(map(int, input().split())) for _ in range(n)]
# 애기들이 기본적으로 들고있는 사탕 종류 갯수 세기 (한사람당 중복사탕은 의미없으니 set으로 지운다)
  tot = 0
  for i in range(len(chc)):
    chc[i].pop(0)
    chc[i] = list(set(chc[i]))
    tot += len(chc[i])
# 가지치기 할 적당한 tot값을 그리디로 만들기
  greedy_c = [1]*(m+1)
  max_tot = tot
  for i in range(d):
    for j in range(1, m+1):
      if (greedy_c[j]==1) and (j not in chc[i]):
        max_tot += 1
        greedy_c[j] = 0
        break

  # 스택을 만들어서 모든 가능한 조합을 dfs로 전체검색한다.
  stack = [[tot, [], 0]]
  while stack:
    key = True
    stk_tot, used_candys, depth = stack.pop()
    # print(stk_tot, depth, used_candys)

    # depth가 아까 미리 정의해논 d만큼 깊어지면 max_tot과 비교하여 큰값 반환
    if depth == d:
      max_tot = max(max_tot, stk_tot, depth)
      continue
    # 현재값 + 앞으로 얻을수 있는 값과 최대값을 비교하여 그보다 작을시 가지치기(dp)
    if stk_tot + d - depth <= max_tot:
      continue

    # 아직 나눠주지 않은 사탕들을 나눠주는 과정(stack에 추가한다)
    for candy in range(1,m+1):
      if candy not in used_candys:
        if candy not in chc[depth]:
          tmp = used_candys[:]
          stack.append([stk_tot+1, tmp+[candy], depth+1])
          key = False
    # 이번 친구에게 하나도 못나눠줬다면 이전값 그대로 depth만 1 늘려서 스택에 담아주기
    if key:
      stack.append([stk_tot, used_candys, depth+1])

  print(f'#{tc+1} {max_tot}')