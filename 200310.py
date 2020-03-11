



#올림픽 종목 투표
def olimphic():
    t = int(input())
    for tc in range(1,t+1):
        input()
        arr_N = list(map(int, input().split()))
        arr_M = list(map(int, input().split()))

        result = [[0, x] for x in arr_N]
        for ar_M in arr_M:
            for i in range(len(arr_N)):
                if arr_N[i] <= ar_M:
                    result[i][0] += 1
                    break
        r = result.index(max(result)) +1
        print('#{} {}'.format(tc, r))

#자기 방으로 돌아가기


# t = int(input())
# for tc in range(1, t+1):
#     N = int(input())
#     arr = [[(x+1)//2 for x in list(map(int, input().split()))] for _ in range(N)]
#     i=0
#     while arr:
#         area = []
#         for x in arr:
#             for a in area:
#                 if a[0] <= x[0] <= a[1] or a[0] <= x[1] <= a[1] or x[0] <= a[0] <= x[1]:
#                     break
#             else:
#                 area.append(x)
#         for ar in area:
#             arr.remove(ar)
#         i += 1
#     print('#{} {}'.format(tc, i))

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [[(x+1)//2 for x in list(map(int, input().split()))] for _ in range(N)]
    cnt = [0]*202
    for l, r in arr:
        for i in range(l, r+1):
            cnt[i] += 1
    print('#{} {}'.format(tc, max(cnt)))
    


    while arr:
        area = []
        for x in arr:
            for a in area:
                if a[0] <= x[0] <= a[1] or a[0] <= x[1] <= a[1] or x[0] <= a[0] <= x[1]:
                    break
            else:
                area.append(x)
        for ar in area:
            arr.remove(ar)
        i += 1
    print('#{} {}'.format(tc, i))