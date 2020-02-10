t=int(input())
for tc in range(1,t+1):
    input()
    tmp = input().split()
    r = []
    alp = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for x in tmp:
        alp[x] +=1
    for x in alp.keys():
        r+=[x]*alp[x]
    print(f'#{tc}')
    print(*r)