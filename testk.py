# cnt = 0
# cnt_lst = []
# x_lst = []
# y_lst = []
def DFS(cnt,i,j,arr):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # for i in range(n):
    #     for j in range(n):
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0<=x<len(arr) and 0<=y<len(arr):
            if arr[i][j] + 1 == arr[x][y]:
                # cnt+=1
                return [DFS(cnt+1,x,y,arr)[0],i,j]
    else:
        # cnt_lst.append(cnt)
        # x_lst.append(x)
        # y_lst.append(y)
        # return cnt_lst,x_lst,y_lst
        return [cnt,i,j]
# t = int(input())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(DFS(1,i,j,arr))


# DFS(cnt,0,0)
# print(cnt_lst)