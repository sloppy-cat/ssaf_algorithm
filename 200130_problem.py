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
    result = []
    for test_case in range(1, T + 1):
        K, N, M = list(map(int,input().split()))
        
        

    for i,x in zip(range(1,T+1),result):
        print(f'#{i} {x}')


if __name__ == '__main__':
    #jomang_joa()
    #min_max()
    #electronic_bus()