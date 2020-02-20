def calc():
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

    return out



def forth():
    t = 10
    for tc in range(1, t+1):
        input()
        cal = calc()

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
forth()