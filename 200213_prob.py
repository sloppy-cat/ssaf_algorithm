import collections

def paper():
    t = int(input())
    for tc in range(1,t+1):
        n = int(input())//10
        list_=[1,3]
        for i in range(2,n):
            list_.append(list_[i-1]+list_[i-2]*2)
        print(f'#{tc} {list_[n-1]}')


def gwalhow():
    t = int(input())
    for tc in range(1,t+1):
        stack = []
        txt = input()
        r = 1
        for x in txt:
            if x in '{(':
                stack.append(x)
            elif x in '})':
                if not stack:
                    r = 0
                    break
                else:
                    if x=='}'and stack[-1] == '{':
                        stack.pop()
                    elif x==')'and stack[-1] == '(':
                        stack.pop()
                    else:
                        r=0
                        break
        if stack:
            r = 0
        print(f'#{tc} {r}')

def graph_():
    t = int(input())
    for tc in range(1,t+1):
        V,E = list(map(int,input().split()))
        GAN = [list(map(int,input().split())) for i in range(E)]
        S,G = list(map(int,input().split()))
        queue = collections.deque()
        queue.append(S)

        r=0
        while queue:
            node = queue.popleft()
            if node == G:
                r = 1
                break
            for nodee in GAN:
                if nodee[0] == node:
                    queue.append(nodee[1])
        print(f'#{tc} {r}')

def repeat():
    t = int(input())
    for tc in range(1,t+1):
        txt = list(input())
        T=1
        while T:
            for i in range(len(txt)-1):
                if txt[i] == txt[i+1]:
                    txt.pop(i)
                    txt.pop(i)
                    break
            else:
                T= 0
        print(f'#{tc} {len(txt)}')    


#paper()
#gwalhow()
#graph_()
repeat()