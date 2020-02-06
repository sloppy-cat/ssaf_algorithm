def sero():
    t = int(input())
    for tc in range(1,t+1):
        a = [input() for i in range(5)]
        result = ''
        
        for i in range(15):
            for j in range(5):
                try:
                    result += a[j][i]
                except:
                    pass
        print (f'#{tc} {result}')




def change(arr,go_sub):
    x,y,c = go_sub
    x-=1
    y-=1
    arr[y][x] = c
    vec = []
        
    for x2 in range(x-1,x+2):
        for y2 in range(y-1,y+2):
            if 0<= x2 < len(arr) and 0<= y2 < len(arr):
                if arr[y2][x2] != 0 and arr[y2][x2] != c:
                    vec += [(y2-y,x2-x)]

    for v_xy in vec:
        trg = 1
        a = x + v_xy[1]
        b = y + v_xy[0]

        while arr[b][a] != c and arr[b][a] != 0:
            if not(0<= a+v_xy[1] < len(arr) and 0<= b+v_xy[0] < len(arr)):
                trg = 0
                break
            a += v_xy[1]
            b += v_xy[0]
            
        if arr[b][a] == c and trg == 1:
            a2 = x + v_xy[1]
            b2 = y + v_xy[0]
            while arr[b2][a2] != c and arr[b2][a2] != 0:
                arr[b2][a2] = c
                a2 += v_xy[1]
                b2 += v_xy[0]
def osello():
    t = int(input())
    for tc in range(1,t+1):
        N, M = list(map(int,input().split()))
        arr = [[0]*N for i in range(N)]
        arr[N//2-1][N//2-1],arr[N//2][N//2-1],arr[N//2-1][N//2],arr[N//2][N//2] = 2,1,1,2
        go = [list(map(int,input().split())) for i in range(M)]
        
        for go_sub in go:
            change(arr,go_sub)

        bw = [0,0]
        for i in arr:
            for j in i:
                if j == 1:
                    bw[0]+=1
                if j == 2:
                    bw[1]+=1
        print (f'#{tc} ',end='')
        print (*bw)

def fly():
    t = int(input())
    for tc in range(1,t+1):
        N,M = list(map(int,input().split()))
        arr = [list(map(int,input().split())) for i in range(N)]
        result = []
        for i in range(N-M+1):
            for j in range(N-M+1):
                tmp = 0
                for i1 in range(i,i+M):
                    for j1 in range(j,j+M):
                        tmp += arr[i1][j1]
                result.append(tmp)
        print (f'#{tc} {max(result)}')

import sys
sys.stdin = open("input.txt", "r")

def ladder2():
    for tc in range(10):
        t = int(input())
        arr = [[0]+list(map(int,input().split()))+[0] for i in range(100)]
        result = [1000000,0]
        for i in range(1,101):
            if arr[1][i] == 1:
                x,y = i,0
                move = 0
                done = False
                while True:
                    vx = 0
                    while True: #하강
                        y+=1
                        if y == 99:
                            done = True
                            break
                        if arr[y][x-1]:
                            vx = -1
                            break
                        if arr[y][x+1]:
                            vx = 1
                            break
                    if done:
                        if result[0]>=move:
                            result = [move,i]
                        break

                    while arr[y][x+vx]: #이동
                        move +=1
                        x += vx


        print (f'#{tc+1} {result[1]-1}')




#sero()
#osello()
#fly()
#ladder2()