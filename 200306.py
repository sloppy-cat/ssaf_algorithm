# import copy
# def DFS(arr, v, yx):
#     if len(v) == 7:
#         return [v]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     return_box = []

#     for i in range(4):
#         y, x = yx
#         if 0<=y+dy[i]<4 and 0<=x+dx[i]<4:
#             tmp = DFS(arr, v+arr[x][y], (y+dy[i], x+dx[i]))
#             return_box += tmp
#     return list(set(return_box))

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = [0]

    for i in range (0, N):
        for j in range(0, len(result)):
            result.append(result[j]+nums[i])
        result = list(set(result))
    print (f'#{tc} {len(result)}')
