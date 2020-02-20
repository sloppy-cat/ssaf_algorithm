def forth():
    t = int(input())
    for tc in range(1, t+1):
        cal = input().split()

        stack = []
        for token in cal:
            if token == '.':
                continue
            elif token.isdecimal():
                stack.append(token)
            else:
                try:
                    a, b = int(stack.pop()), int(stack.pop())
                    if token == "+":
                        stack.append(b+a)
                    elif token == "-":
                        stack.append(b-a)
                    elif token == "*":
                        stack.append(b*a)
                    elif token == "/":
                        stack.append(b//a)
                except:
                    break
        else:
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack[-1]))
                continue
        print('#{} error'.format(tc))

def maze():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        arr = [list(map(int,list(input()))) for i in range(N)]

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        stack = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    stack.append((i, j))
        r = 0
        while stack:
            i, j = stack.pop()
            if arr[i][j] == 3:
                r = 1
                break
            arr[i][j] = 1
            for n in range(4):
                if 0 <= i+dr[n] < N and 0 <= j+dc[n] < N:
                    if arr[i+dr[n]][j+dc[n]] != 1:
                        stack.append((i+dr[n], j+dc[n]))
        print('#{} {}'.format(tc, r))

def devied(sub):
    if len(sub) == 1:
        return sub
    else:
        a = devied(sub[0:(len(sub)+1)//2])
        b = devied(sub[(len(sub)+1)//2:len(sub)])

        if a[0][1] == b[0][1]:
            if a[0][0] < b[0][0]:
                return a
            else:
                return b
        elif (a[0][1] + 1) % 3 == b[0][1] % 3:
            return b
        else:
            return a

def cardgame():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        rsp = list(enumerate(map(int, input().split()), 1))
        r = devied(rsp)
        print('#{} {}'.format(tc, r[0][0]))

import copy

min_ = 10000
def make_sub(arr, N, idx_list, sum):
    global min_
    if sum < min_:
        if N == len(idx_list):
            min_ = sum
            return [idx_list]
        return_box = []
        for i in range(N):
            new_sum = sum
            if i not in idx_list:
                new_sum += arr[len(idx_list)][i]

                tmp = copy.copy(idx_list)
                tmp.append(i)
                a = make_sub(arr, N, tmp, new_sum)
                if a:
                    return_box.append(a)
        return return_box

def min_sum():
    global min_
    t = int(input())
    for tc in range(1, t + 1):
        min_ = 10000
        N = int(input())
        arr = [list(map(int, input().split())) for i in range(N)]

        make_sub(arr, N, [], 0)

        print('#{} {}'.format(tc, min_))

#forth()

#maze()

#cardgame()

#min_sum()