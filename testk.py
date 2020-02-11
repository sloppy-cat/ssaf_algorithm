arr = [0]*6
sub_arr = []
while True:
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 1:
            arr[i] = 0
        else :
            arr[i] = 1
            break
        sub_arr += [arr]
    if arr.count(1) == 6:
        break
print(sub_arr)