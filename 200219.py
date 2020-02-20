def cal():
    stack = []
    out = []
    pr = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,
    }

    text = input()
    for x in text:
        if x in '+-*/':
            if stack:
                if pr[x] > pr[stack[-1]]:
                    stack.append(x)
                else:
                    while True:
                        if stack and pr[x] <= pr[stack[-1]]:
                            out.append(stack.pop())
                        else:
                            break
                    stack.append(x)
            else:
                stack.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while True:
                a = stack.pop()
                if a == '(':
                    break
                else:
                    out.append(a)
        else:
            out.append(x)
    while stack:
        out.append(stack.pop())

    print(*out)
    print(stack)

# n_dict = [1,2,3,4,5,6,7,8,9,10]
# result = []
# import copy
# def power_set(set_, i):
#     if i==5:
#         result.append(set_)
#         return
#     else:
#         a = copy.copy(set_)
#         b = copy.copy(set_)
#         a.append(n_dict[i])
#         return power_set(a, i+1), power_set(b, i+1)
# power_set([],0)
# print(*result)



def magnetic():
    for tc in range(1,11):
        N = int(input())
        arr = [list(map(int,input().split())) for i in range(N)]
        result = 0
        for j in range(N):
            r = 0
            for i in range(N):
                if arr[i][j] == 1:
                    r = 1
                if arr[i][j] == 2 and r == 1:
                    r = 0
                    result += 1

        print('#{tc} {result}'.format())
cal()
#magnetic()