def p(a):
    for n in range(100,0,-1):
        for i in range(100):
            for j in range(101-n):
                t = [a[k][i] for k in range(j,j+n)]
                b=a[i][j:j+n]
                if b==list(reversed(b)) or t == list(reversed(t)):
                    return n
for c in range(1,11):
    input()
    a = [list(input()) for i in range(100)]
    r = p(a)
    print(f'#{c} {r}')

    
    def pel(arr):
    for n in range(100,0,-1):
        for i in range(100):
            for j in range(101-n):
                if arr[i][j:j+n] == list(reversed(arr[i][j:j+n])):
                    return n
                tmp = [arr[k][i] for k in range(j,j+n)]
                if tmp == list(reversed(tmp)):
                    return n
 
for tc in range(1,11):
    input()
    arr = [list(input()) for i in range(100)]
    r = pel(arr)
    print(f'#{tc} {r}')