#강사님 바뀌셨음
def color():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        P = [[0]*10 for x in range(10)]
        r = 0
        for n in range(N):
            r1, c1, r2, c2, c = list(map(int,input().split()))
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    if P[i][j] != 0:
                        if P[i][j] != c:
                            P[i][j] = 3
                    else :
                        P[i][j] = c
        for i in range(0,10):
            for j in range(0,10):
                if P[i][j] == 3:
                    r += 1

        print(f'#{test_case} {r}')    


import copy
def sub_set():
    T = int(input())
    for test_case in range(1, T + 1):
        N, K = list(map(int,input().split()))

        arrr = []
        arr = [0]*12
        while True:
            for i in range(len(arr)-1,-1,-1):
                if arr[i] == 1:
                    arr[i] = 0
                else :
                    arr[i] = 1
                    break
            if arr.count(1) == N:
                arrr.append(copy.copy(arr))
            elif arr.count(1) == 12:
                break
        r = 0
        for ar in arrr:
            check = 0
            for i in range(len(ar)):
                if ar[i] == 1:
                    check += (i+1)
            if check == K:
                r += 1
            print(ar)

        print(f'#{test_case} {r}')
    



def find_bibi(l,r,F,n):
    c = int((l+r)/2)
    if c == F:
        return n
    elif c > F:
        return find_bibi(c,r,F,n+1)
    else :
        return find_bibi(l,c,F,n+1)
def binary():
    T = int(input())
    for test_case in range(1, T + 1):
        P, A, B = list(map(int,input().split()))
        l,r = 1,P
        a = find_bibi(l,r,A,0)
        b = find_bibi(l,r,B,0)
        R = 0
        if a>b:
            R = 'A'
        elif b>a:
            R = 'B'
        print(f'#{test_case} {R}')


def spc_sort():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        nums = list(map(int,input().split()))
        nums.sort(reverse=True)
        R = []
        for i in range(5):
            R += [nums[i],nums[-1-i]]
        print(f'#{tc} ',end="")
        print(*R)


#color()
#sub_set()
#binary()
#spc_sort()