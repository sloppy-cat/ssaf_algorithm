import copy
def sub(G, idx, Hs, subset):
    if sum(subset) >= G:
        return sum(subset)-G
    elif idx == len(Hs):
        if sum(subset) >= G:
            return sum(subset)-G
        else:
            return 999999
    else :
        tmp1 = copy.copy(subset)
        tmp1.append(Hs[idx])
        a = sub(G, idx+1, Hs, tmp1)
        b = sub(G, idx+1, Hs, subset)
        return min(a,b)

t = int(input())
for tc in range(1,t+1):
    N, B = list(map(int,input().split()))
    Hs = list(map(int,input().split()))

    result = sub(B, 0, Hs, [])
    print(f'#{tc} {result}')