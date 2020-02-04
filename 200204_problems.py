import sys
sys.stdin = open("input.txt", "r")

def iron_stick():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        stick = list(map(int,input().split()))
        new_ = [(stick[i*2],stick[i*2+1])for i in range(N)]
        for i in range(N):
            no_friend = 0
            for j in range(N):
                if new_[i][0] == new_[j][1]:
                    no_friend = 1
            if no_friend == 0 and i != 0:
                new_[i], new_[0] = new_[0], new_[i]

        for i in range(N-1):
            for j in range(i+1,N):
                if new_[i][1] == new_[j][0]:
                    new_[j], new_[i+1] = new_[i+1], new_[j]
                    break
        stick = []
        for x in new_:
            stick += [x[0],x[1]] 

        print(f'#{tc} ',end="")
        print(*stick)
iron_stick()
