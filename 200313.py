#의석이의 세로로 말해요
def _5356():
    for t in range(int(input())):
        arr = [list(input()) for _ in range(5)]
        r = ''
        for i in range(15):
            for j in range(5):
                try:
                    r = r+arr[j][i]
                except:
                    pass
        print(f'#{t+1} {r}')
# _5356()

#상호의 배틀필드
def _1873():
    u=input
    key=['UDLR','^v<>']
    dy, dx = [-1,1,0,0], [0,0,-1,1]
    for t in range(int(u())):
        H, W = list(map(int, u().split()))
        gameMap = [list(u()) for _ in range(H)]
        u()
        y, x, sts = 0, 0, ''
        con = list(u())
        for i in range(H):
            for j in range(W):
                if gameMap[i][j] in key[1]:
                    y, x = i, j
                    sts = gameMap[i][j]

        for o in con:
            if o in key[0]:
                idx = key[0].index(o)
                ny, nx = y+dy[idx], x+dx[idx]
                if 0 <= ny <H and 0 <= nx < W and gameMap[ny][nx] =='.':
                    gameMap[y][x] = '.'
                    sts = key[1][idx]
                    gameMap[ny][nx] = sts
                    y, x = ny, nx
                else:
                    gameMap[y][x] = key[1][idx]
                    sts = key[1][idx]
                    
            else:
                idx = key[1].index(sts)
                sy, sx = y, x
                while True:
                    sy, sx = sy+dy[idx], sx+dx[idx]
                    if 0 <= sy <H and 0 <= sx < W:
                        if gameMap[sy][sx] in '.-':
                            continue
                        elif gameMap[sy][sx] == '*':
                            gameMap[sy][sx] = '.'
                            break
                        else:
                            break
                    else:
                        break
            # print(o, sts, idx)
        print(f'#{t+1} ',end='')
        for arg in gameMap:
            print(''.join(arg))
            # print() 
_1873()

        