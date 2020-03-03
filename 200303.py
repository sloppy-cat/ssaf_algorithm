import copy
def rec(arr, N, p, ar):
    global per
    if len(ar) == N:
        if p > per:
            per = p
        return
    for i in range(N):
        if i not in ar:
            tmp_p = p * arr[len(ar)][i]
            if tmp_p <= per:
                continue
            tmp_ar = copy.copy(ar)
            tmp_ar.append(i)
            rec(arr, N, tmp_p, tmp_ar)

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for i in range(N)]
    global per
    per = 0 
    rec(arr, N, 1, [])

    print (f'#{tc}',format(per*100,'.6f'))
