#러시아 국기 같은 깃발
def _4613():
    for t in range(int(input())):
        N,M = list(map(int,input().split()))
        arr = [list(input()) for _ in range(N)]
        wbr = [[M-x.count(T) for x in arr]for T in 'WBR']
        min_ = 2**32
        for i in range(0, N-1):
            for j in range(i+1, N-1):
                tmp = sum(wbr[0][:i+1]+wbr[1][i+1:j+1]+wbr[2][j+1:])
                min_ = min(tmp,min_)
        print(f'#{t+1} {min_}')
_4613()