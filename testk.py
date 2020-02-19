def ladder2():
    for tc in range(10):
        t = int(input())
        arr = [[0] + list(map(int,input().split()))+[0] for i in range(100)]
        result = 0
        for i in range(1,101):
            if arr[1][i] == 1:
                x,y = i,0
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
                        if arr[y][x] == 2:
                            result = i-1
                        break
 
                    while arr[y][x+vx]:
                        x += vx
 
 
        print (f'#{tc+1} {result}')
ladder2()