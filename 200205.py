def isdanzo(n):
    for i in range(0,len(n)-2):
        if n[i]>n[i+1]:
            return False
    return True
def danzo():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        integer =  list(map(int,input().split()))
        new_int=[]
        for i in range(N) :
            for j in range(i+1,N):
                a=integer[i]*integer[j]
                if a>10:
                    if isdanzo(str(a)):
                        new_int.append(a)
        temp = []
        for x in new_int:
            trg = 1
            tmp = 0
            for i in str(x):
                if int(i)<tmp:
                    trg = 0
                    break
                else:
                    tmp = int(i)
            if trg == 1:
                temp.append(x)
        if len(temp) == 0:
            temp.append(-1)
        print(f'#{t} {max(temp)}')


def dasol():
    T = int(input())
    for t in range(1, T + 1):
        arr = list(input())
        l = len(arr)

        print('..',end='')
        print('#',end='')
        print('...#',end='')*(l-1)
        print('..')

        print('.#.#'*l,end='')
        print('.')

        for i in arr:
            print(f'#.{i}',end='')
        print('.#')

        print('.#.#'*l,end='')
        print('.')

        print('..',end='')
        print('#',end='')
        print('...#'*(l-1),end='')
        print('..')

def cc():
    T = int(input())
    for t in range(1, T + 1):
        inp = input()
        list_ = []
        result1 = [0,0,0,0]
        a = 'SDHC'
        for i in range(len(inp)):
            list_ +=[inp[i:i+3]]
        if len(list_) != len(set(list_)):
            result = ['ERROR']
            break
        else:
            for li in list_:
                for l in a:
                    if l == li[0]:
                        result1[a.index(l)]+=1
            result = [13-a for a in result1]
        print(f'#{t} ',end='')
        print(*result)

def pascal():
    T = int(input())
    for t in range(1, T + 1):   
        N = int(input())
        paspas = []
        for i in range(0,N):
            if i == 0:
                paspas += [[1]]
            else :
                paspas += [[]]
                for j in range(0,i+1):
                    if j == 0 or j == i:
                        paspas[i] += [1]
                    else :
                        paspas[i] += [paspas[i-1][j-1]+paspas[i-1][j]]
        print(f'#{t}')
        for pas in paspas:
            print(*pas)
            	
pascal()