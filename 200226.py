t = int(input())
for tc in range(t):
    N = int(input())

    noson = [list(map(int,input().split())) for i in range(N)]

    P = int(input())

    busstop = {}
    P_ = []
    for i in range(P):
        P_.append(int(input()))
        busstop[P_[-1]] = 0
    
    
    for no in noson:
        for i in range(no[0],no[1]+1):
            try:
                busstop[i] += 1
            except:
                continue
    
    print(f'#{tc+1}',end='')
    for p in P_:
        print(f' {busstop[p]}',end='')
    # print(*busstop.values())
    print()