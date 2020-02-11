def pel(arr):
    for n in range(100,0,-1):
        for i in range(100):
            for j in range(101-n):
                if arr[i][j:j+n] == list(reversed(arr[i][j:j+n])):
                    return n
                tmp = [arr[k][i] for k in range(j,j+n)]
                if tmp == list(reversed(tmp)):
                    return n

# for tc in range(1,11):
#     input()
#     arr = [list(input()) for i in range(100)]
#     r = pel(arr)
#     print(f'#{tc} {r}')
import sys
sys.stdin = open("input.txt", "r")


def find_rc():
    t = int(input())
    for tc in range(1,t+1):
        n = int(input())
        arr = [list(map(int,input().split())) for i in range(n)]
        r = []
        for i in range(n):
            for j in range(n):
                if arr[i][j]:   
                    i2,j2 =i,j
                    while i2+1<n and arr[i2+1][j]:
                        i2+=1
                    while j2+1<n and arr[i][j2+1]:
                        j2+=1
                    n_i = i2+1-i
                    n_j = j2+1-j
                    r += [[n_i*n_j, n_i, n_j]]
                    for a in range(i,i2+1):
                        for b in range(j,j2+1):
                            arr[a][b] = 0
        r.sort()
        print('#{} {}'.format(tc,len(r)),end = "")
        for i in range(len(r)):
            print('',end=" ")
            print(*r[i][1:],end="")
        print()
find_rc()

# for testcase in range(1, int(input())+1):
#     n = int(input())
#     board = []
#     for i in range(n):
#         board.append(list(map(int, input().split())))
 
#     starting_point = []
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] > 0:
#                 if i == 0:
#                     if j == 0:
#                         starting_point.append([0, 0])
#                     elif board[i][j-1] == 0:
#                         starting_point.append([i, j])
#                 else:
#                     if j == 0:
#                         if board[i-1][j] == 0:
#                             starting_point.append([i, j])
#                     elif board[i-1][j] == 0 and board[i][j-1] == 0:
#                         starting_point.append([i, j])
#     # print(starting_point)
 
#     matrixes = []
#     for i in range(len(starting_point)):
#         cntY = 1
#         cntX = 1
#         tempY = starting_point[i][0]
#         tempX = starting_point[i][1]
#         while True:
#             if tempY+1 < n and board[tempY+1][starting_point[i][1]] != 0:
#                 cntY += 1
#                 tempY += 1
#             else:
#                 break
#         while True:
#             if tempX + 1 < n and board[starting_point[i][0]][tempX+1] != 0:
#                 cntX += 1
#                 tempX += 1
#             else:
#                 break
#         matrixes.append([cntY, cntX])
 
#     # print(matrixes)
 
#     # sorting
#     for i in range(len(matrixes)-1):
#         for j in range(len(matrixes)-1-i):
#             if matrixes[j][0] * matrixes[j][1] > matrixes[j+1][0] * matrixes[j+1][1]:
#                 matrixes[j], matrixes[j+1] = matrixes[j+1], matrixes[j]
#             elif matrixes[j][0] * matrixes[j][1] == matrixes[j+1][0] * matrixes[j+1][1]:
#                 if matrixes[j][0] > matrixes[j+1][0]:
#                     matrixes[j], matrixes[j + 1] = matrixes[j + 1], matrixes[j]
 
#     print('#{} {} '.format(testcase, len(matrixes)), end='')
#     for i in range(len(matrixes)):
#         print('{} {}'.format(matrixes[i][0], matrixes[i][1]), end=' ')
#     print()
                

