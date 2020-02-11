import sys
sys.stdin = open('0211.findnum.txt','r')

def numbers():

    T= int(input())
    for i in range(1,1+T):
        N = int(input())
        val = [list(map(int,input().split())) for j in range(N)]

        newlist=[]
        for a in range(N):
            for b in range(N):
                a1 = a
                b1 = b
                if a1+1<N and val[a1+1][b1]:
                    while a1+1<N and val[a1+1][b1]:
                        a1 += 1
                if b1+1<N and val[a1][b1+1]:
                    while b1+1<N and val[a1][b1+1]:
                        b1 += 1

                length = (a1-a)+1
                vertical = (b1-b)+1
                multi = length*vertical

                newlist += [[multi,vertical,length]]
                
                for a in range(a,a1+1):
                    for b in range(b,b1+1):
                        val[a][b] = 0
        newlist.sort()


        print('#{} {}'.format(i,len(newlist)),end='')

        for i in range(len(newlist)):
            print('',end=' ')
            print(*newlist[i][1:],end='')
        print()
numbers()