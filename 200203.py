def updncheck():
    T = int(input())
    for test_case in range(1, T + 1):
        #ary[0...n-1][0...n-1]
        ary = [
            [1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [4,5,6,7],
        ]
        N = int(input())
        result = [[0]*N for x in range(N)]

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        print(result)
        for x in range (len(ary)):
            for y in range (len(ary)):
                for I in range(4):	#현재 위치의 상하좌우를 효율적으로 체크하는 코드
                    testX = x+dx[I]
                    testY = y+dy[I]
                    if 0<=testX<N and 0<=testY<N:
                        result[x][y] += abs(ary[testX][testY]- ary[x][y])
        print (result)
import sys
sys.stdin = open("input.txt", "r")


def list_sum():
    T=10
    for t in range(1,T+1):
        input()
        arr = [list(map(int,input().split())) for x in range(100)]
        c = []
        a,b = 0,0
        for i in range(100):
            p = [sum(arr[i]), 0]
            for x in arr:
                p[1] += x[i]
            c += p
            a += arr[i][i]
            b += arr[i][99-i]
        print(f'#{t} {max(c+[a,b])}') 



list_sum()