def moon_ja():
    t = int(input())
    for tc in range(1,t+1):
        r, t1, t2 = 0, input(), input()

        if t1 in t2:
            r = 1
        print(f'#{tc} {r}')

def pel():
    t = int(input())
    for tc in range(1,t+1):
        N,M = list(map(int,input().split()))
        arr = [list(input()) for i in range(N)]
        r=[]
        for i in range(N):
            for j in range(N+1-M):
                if arr[i][j:j+M] == list(reversed(arr[i][j:j+M])):
                    r = arr[i][j:j+M]
                tmp = [arr[k][i] for k in range(j,j+M)]
                if tmp == list(reversed(tmp)):
                    r = tmp
        print(f'#{tc} ',end='')
        print(''.join(r))

def str_num():
    t = int(input())
    for tc in range(1,t+1):
        t_1, t_2 = input(), input()
        r = []
        for t1 in t_1:
            r.append(t_2.count(t1))
        print(f'#{tc} {max(r)}')

#moon_ja()
#pel()
#str_num()