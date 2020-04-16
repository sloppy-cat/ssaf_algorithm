# 5174 subtree
def DFS(tree, root):
  stack = [root]
  cnt = 1
  while stack:
    node = stack.pop()
    cnt += len(tree[node])
    stack = stack + tree[node]
  return cnt

def subtree():
  for tc in range(int(input())):
    e, n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    tree = []
    for _ in range(max(arr)+1):
      tree.append([])
    for i in range(e):
      tree[arr[i*2]].append(arr[i*2+1])
    res = DFS(tree, n)
    print(f'#{tc+1} {res}')


# 5178 노드의 합
def sum_node():
  for tc in range(int(input())):
    n, m, l = list(map(int, input().split()))
    bin_tree = [0]*(n+1)
    for _ in range(m):
      leaf_n, val = list(map(int, input().split()))
      bin_tree[leaf_n] = val
    if n%2 == 0:
      bin_tree[n//2] = bin_tree[n]
      n -= 1
    for i in range(n, 1, -2):
      bin_tree[i//2] = bin_tree[i] + bin_tree[i-1]
    res = bin_tree[l]
    print(f'#{tc+1} {res}')

# 5174 subtree
# subtree()

# 5178 노드의 합
# sum_node()