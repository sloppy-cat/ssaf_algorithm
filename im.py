import sys
sys.stdin = open("input.txt", "r")

def find(x,y,arr):
    if arr[x][y]=='3':
        return 1

    elif arr[x][y] == '0':
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        arr[x][y] = '2'
        return find(x+dx[0],y+dy[0],arr)+find(x+dx[1],y+dy[1],arr)+find(x+dx[2],y+dy[2],arr)+find(x+dx[3],y+dy[3],arr)
    else :
        return 0

        
def miro():
    for tc in range(1,11):
        t = input()
        arr = [list(input()) for i in range(16)]
        arr[1][1] = '0'
        print(f'#{tc} {find(1,1,arr)}')

miro()
