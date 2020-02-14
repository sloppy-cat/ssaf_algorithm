import copy
def rc_():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        arr = [input().split() for i in range(N)]
        arr2 = copy.deepcopy(arr)
        for i in range(N):
            for j in range(i+1):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        arr1 = copy.deepcopy(arr)
        arr3 = copy.deepcopy(arr)
        for x in arr1:
            x.reverse()
        arr3.reverse()
        arr2.reverse()
        for x in arr2:
            x.reverse()

    r = []
    for i in range(N):
        r.append([''.join(arr1[i]), ''.join(arr2[i]), ''.join(arr3[i])])
    print(f'#{tc}')
    for x in r:
        print(*x)


def farm():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        arr = [list(map(int,list(input()))) for i in range(N)]
        r = 0
        for i in range(N):
            for j in range(N):
                if (abs(i-N//2) + abs(j-N//2))<= N//2:
                    r += arr[i][j]
        print(f'#{tc} {r}')



#rc_()
farm()