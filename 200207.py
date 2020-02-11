import copy
def dano():
    t = int(input())
    for tc in range(1,t+1):
        N, K = list(map(int,input().split()))
        arr = [list(map(int,input().split()))+[0] for i in range(N)]
        arr += [[0]*(N+1)]
        result = 0
        for i in range(N):
            r_r = 0
            t_t = 0
            for j in range(N+1):
                if arr[i][j]==0:
                    if r_r == K:
                        result +=1
                    r_r = 0
                else :
                    r_r += 1
                if arr[j][i]==0:
                    if t_t == K:
                        result +=1
                    t_t = 0
                else :
                    t_t += 1
        
        print('#{} {}'.format(tc, result))

def new_com():
    t = int(input())
    for tc in range(1,t+1):
        p,q = list(map(int,input().split()))
        x,y = 0,0
        for i in range(1,200):
            a = (i-1)*i//2
            b = (i+1)*i//2
            if a < p <= b:
                x += p-a
                y += b-p+1
            if a < q <= b:
                x += q-a
                y += b-q+1
        print('#{} {}'.format(tc, (x+y-2)*(x+y-1)//2 +x))

        
def two_num():
    t = int(input())
    for tc in range(1,t+1):
        N, M = list(map(int,input().split()))
        Ai = list(map(int,input().split()))
        Bj = list(map(int,input().split()))
        if M>N:
            M,N = N,M
            Ai,Bj = Bj,Ai
        result = []
        for i in range(0,N-M+1):
            num = 0
            for j in range(i,i+M):
                num += Ai[j]*Bj[j-i]
            result += [num]
        print('#{} {}'.format(tc,max(result)))


def sudokuku():
    t = int(input())
    for tc in range(1,t+1):
        result = 1
        N = [list(map(int,input().split())) for i in range(9)]
        for i in range(9):
            c = []
            cell = []
            for j in range(9):
                c += [N[j][i]]
                cell += [N[j//3 + (i//3)*3][j%3 + (i//3)*3]]
            sn, sc, sce = set(N[i]),set(c),set(cell)
            if len(sn) !=9 or len(sc) !=9 or len(sce) !=9:
                result = 0
        print('#{} {}'.format(tc,result))



def clear(a,dx,dy,arr,n):
    for k in range(n-1):
        for i in range(n):
            for j in range(n):                
                x = ((1-dx[a])//2)*(n-1) + ((dx[a]+1)//2*2 + (dx[a]+1)%2*2-1)*i
                y = ((1-dy[a])//2)*(n-1) + ((dy[a]+1)//2*2 + (dy[a]+1)%2*2-1)*j
                if 0<=y+dy[a]<n and 0<= x+dx[a] <n:
                    if arr[y+dy[a]][x+dx[a]] == 0:
                        new = arr[y+dy[a]][x+dx[a]]
                        arr[y+dy[a]][x+dx[a]] = arr[y][x]
                        arr[y][x] = new
def move(arr,go,n):
    dx,dy,arrow = [1,-1,0,0],[0,0,1,-1],['right','left','down','up']
    dx1,dy1 = [-1,1,0,0],[0,0,-1,1]
    a = arrow.index(go)
    clear(a,dx,dy,arr,n)

    for i in range(n):
        for j in range(n):
            x = ((1-dx1[a])//2)*(n-1) + ((dx1[a]+1)//2*2 + (dx1[a]+1)%2*2-1)*i
            y = ((1-dy1[a])//2)*(n-1) + ((dy1[a]+1)//2*2 + (dy1[a]+1)%2*2-1)*j
            if 0<=y+dy1[a]<n and 0<= x+dx1[a] <n:
                if arr[y+dy1[a]][x+dx1[a]] == arr[y][x]:
                    arr[y][x]*=2
                    arr[y+dy1[a]][x+dx1[a]] = 0
    clear(a,dx,dy,arr,n)
    
def choo2048():
    t = int(input())
    for tc in range(1,1+t):
        n, go = list(input().split())
        N = int(n)
        arr = [list(map(int,input().split())) for i in range(N)]
        move(arr,go,N)
        print(f'#{tc}')
        for x in arr:
            print(*x)



def find_sagak(arr,cnt,x,y):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    for i in range(4):
        if 0<=y+dy[i]<len(arr) and 0<=x+dx[i]<len(arr):
            if arr[y][x] + 1 == arr[y+dy[i]][x+dx[i]]:
                return find_sagak(arr,cnt+1,x+dx[i],y+dy[i])
        return cnt
def sagak():
    t = int(input())
    for tc in range(1,1+t):
        n = int(input())
        arr = [list(map(int,input().split())) for i in range(n)]
        result = [0,0]
        for i in range(n):
            for j in range(n):
                a = find_sagak(arr,1,i,j)
                print(a)
                print(type(a))
                if a>result[1]:
                    result = [arr[j][i],a]
        print(f'#{tc} ',end='')
        print(*result)

sagak()



        