# 5209 최소생산비용

def backtracking(cnt, arr, sum_fac, n, fac_arr):
    global p_min
    if sum_fac >= p_min:
        return
    if cnt == n:
        if sum_fac < p_min:
            p_min = sum_fac
            return
        else:
            return
    return_box = []
    for i in range(n):
        if i not in arr:
            backtracking(cnt+1, arr+[i], sum_fac+fac_arr[cnt][i], n, fac_arr)
    return


for tc in range(int(input())):
    n = int(input())
    fac_arr = [list(map(int,input().split())) for _ in range(n)]
    
    global p_min
    p_min = 100000
    backtracking(0, [], 0, n, fac_arr)
    print(p_min)