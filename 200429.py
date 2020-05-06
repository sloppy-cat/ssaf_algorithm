# 5185 이진수
def binary_num():
  for tc in range(int(input())):
    n, v = list(input().split())
    v = '0x' + v.lower()
    res = bin(int(v, 16))[2:]
    res = '0'*(int(n)*4 - len(res)) + res
    print(f'#{tc+1} {res}')


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
