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

    N = int(input())
    arr = [[0]*N for i in range(N)]
    arr[N//2-1][N//2-1],arr[N//2][N//2-1],arr[N//2-1][N//2],arr[N//2][N//2] = 2,1,1,2
    while True:
        go = pointer()
        
        
        change(arr,go_sub)

        for i in range (N):
            print (*arr[i])


def pointer():
