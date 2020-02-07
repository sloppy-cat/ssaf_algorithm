arr =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = 4
go = 'up'

dx,dy,arrow = [1,-1,0,0],[0,0,1,-1],['right','left','down','up']
a = arrow.index(go)
for i in range(n):
    for j in range(n):
        x = ((1-dx[a])//2)*(n-1)  +  ((dx[a]+1)//2*2 + (dx[a]+1)%2*2-1)*i
        y = ((1-dy[a])//2)*(n-1)+((dy[a]+1)//2*2 + (dy[a]+1)%2*2-1)*j
        print(arr[y][x])
