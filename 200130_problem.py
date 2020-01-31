import sys
sys.stdin = open("input.txt", "r")

def jomang_joa():
    T = 10
    result = []
    for test_case in range(1, T + 1):
        jomang = 0
        N = int(input())
        datas = list(map(int,input().split()))

        for i in range(2,len(datas)-2):
            jo = datas[i] - max(datas[i-2],datas[i-1],datas[i+1],datas[i+2])
            if jo>0:
                jomang += jo
        result.append(jomang)
    for i,x in zip(range(1,11),result):
        print(f'#{i} {x}')

def min_max():
    T = int(input())
    result = []
    for test_case in range(1, T + 1):
        N = int(input())
        datas = list(map(int,input().split()))
        minmin = 1000000
        maxmax = 0
        for data in datas:
            if data > maxmax:
                maxmax = data
            elif data < minmin:
                minmin = data
        result.append(maxmax-minmin)
    for i,x in zip(range(1,T+1),result):
        print(f'#{i} {x}')

def electronic_bus():
    T = int(input())
    for test_case in range(1, T + 1):
        K, N, M = list(map(int,input().split()))
        bus = [0]*(N+K)
        charger = list(map(int,input().split()))
        for x in charger:
            bus[x] = 1
        result = 0
        i = 0
        while i<(N):
            for j in range ((i+K),i,-1):
                if j >= N :
                    i = j
                    break
                elif bus[j] == 1:
                    i = j
                    result += 1
                    break
                elif j == i+1:
                    result = 0
            if result == 0:
                break
        print(f'#{test_case} {result}')

def num_card():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        ai = input()
        #print(ai)
        result = [0]*10
        for a in ai:
            result[int(a)] += 1
        a = result.count(max(result))
        #print(result)
        if a>1:
            for i in range(1,a):
                result[result.index(max(result))] = 0
        print(f'#{test_case} {result.index(max(result))} {max(result)}')

def gugan_sum():
    T = int(input())
    for test_case in range(1, T + 1):
        N, M = map(int,input().split())
        ai = list(map(int,input().split()))      
        
        minmin = 1000000
        maxmax = 0

        for i in range(0,N-M+1):
            if sum(ai[i:i+M])> maxmax:
                maxmax = sum(ai[i:i+M])
            if sum(ai[i:i+M]) < minmin:
                minmin = sum(ai[i:i+M])
        print(f'#{test_case} {maxmax-minmin}')

def flatten():
    T = 10
    for test_case in range(1, T + 1):
        N = int(input())
        ai = list(map(int,input().split()))
        while N>0:
            M = ai.index(max(ai))
            m = ai.index(min(ai))
            ai[M] -=1
            ai[m] +=1
            N-=1
        print(f'#{test_case} {max(ai)-min(ai)}')
    


if __name__ == '__main__':
    #jomang_joa()
    #min_max()
    #electronic_bus()
    #num_card()
    #gugan_sum()
    #flatten()