#늘어지는 소리 만들기
def _4676():
    i=input
    for tc in range(int(i())):
        a=list(i())
        i()
        h=list(sorted(map(int,i().split()),reverse=True))
        for x in h:
            a.insert(x,"-")
        print(f'#{tc+1}',''.join(a))
