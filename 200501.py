# 5186 이진수2
def binary_num2():
  for tc in range(int(input())):
    v = float(input())
    res = ''
    tmp = 0
    for i in range(1,13):
      if tmp + 1/(2**i) <= v:
        tmp += 1/(2**i)
        res = res + '1'
        if tmp == v:
          break
      else:
        res = res + '0'
    else:
      res = 'overflow'
    print(f'#{tc+1} {res}')