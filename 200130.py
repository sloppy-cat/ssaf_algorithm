import copy
def baby_gin():
    card = list(map(int,input().split()))
    card.sort()
    set_card = copy.copy(set(card))
    if len(set_card) == 1:
        return True
    for x in set_card:
        if card.count(x) >= 3:
            #print('catch1')
            for i in range(3):
                card.remove(x)
                #print(card)

        if len(card) != 0:
            a = len(card)
            for i in range (a//3,0,-1):
                if card[i*3-1] == card[i*3-2]+1 and card[i*3-3]+1 == card[i*3-2]:
                    #print('catch2')
                    for i in range(3):
                        card.pop()
                        #print(card)
    if len(card) == 0:
        return True
    else:
        return False

def baby_gin2():
    card = [0]*10
    
    inputX = input().split()
    for x in inputX:
        card[int(x)] += 1
    for i in range(0,len(card)):
        if card[i]>=3:
            card[i]-=3
        if bool(card[i]) and bool(card[i+1]) and bool(card[i+2]):
            card[i] -= 1
            card[i+1] -=1
            card[i+2] -=1
    if card.count(0) == 10:


        return True
    return False 




def build_data(): 
    data = []
    for i in range (0,10):
        data += [int(input())]
    return data

def gravity():
    data = build_data()
    nak = 0
    for i in range(0,9):
        new_nak = 9-i
        if nak >= new_nak:
            break
        for j in range (i+1,9):
            if data[i] <= data[j]:
                new_nak -= 1
        if new_nak > nak:
            nak = new_nak
    return nak

def bubble(list_data):
    for i in range(1,len(list_data)):
        for j in range(0,len(list_data)-i):
            if list_data[j] > list_data[j+1]:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
    return list_data

def count_sort(A):
    C = [0]*(max(A)+1)
    B = [0]*(len(A)+1)
    for i in range (0,len(A)):
        C[A[i]] += 1
    
    for i in range (1,len(C)):
        C[i] += C[i-1]

    for i in range (len(B)-1, -1, -1):
        B[C[A[i]]] = A[i] 
        C[A[i]] -= 1

if __name__ == '__main__':
    print(count_sort([9,8,7,6,5,4]))