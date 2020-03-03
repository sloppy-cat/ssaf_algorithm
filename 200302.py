# import copy
# def sub(fee, idx, plan, sum_):
#     if idx >= len(plan):
#         return sum_
#     else :
#         if plan[idx]:
#             a = sub(fee, idx+1, plan, sum_ + plan[idx]*fee[0])
#             b = sub(fee, idx+1, plan, sum_ + fee[1])
#             c = sub(fee, idx+3, plan, sum_ + fee[2])
#             d = sub(fee, idx+12, plan, sum_ + fee[3])
#             return min(a,b,c,d)
#         else:
#             return sub(fee, idx+1, plan, sum_)

# t = int(input())
# for tc in range(1,t+1):
#     fee = list(map(int,input().split()))
#     plan = list(map(int,input().split()))

#     result = sub(fee, 0, plan, 0)
#     print(f'#{tc} {result}')


# import copy
# def sub(fee, idx, plan, sum_):
#     if idx >= len(plan):
#         return sum_
#     else :
#         if plan[idx]:
#             a = sub(fee, idx+1, plan, sum_ + plan[idx]*fee[0])
#             b = sub(fee, idx+1, plan, sum_ + fee[1])
#             c = sub(fee, idx+3, plan, sum_ + fee[2])
#             d = sub(fee, idx+12, plan, sum_ + fee[3])
#             return min(a,b,c,d)
#         else:
#             return sub(fee, idx+1, plan, sum_)

# t = int(input())
# for tc in range(1,t+1):
#     fee = list(map(int,input().split()))
#     plan = list(map(int,input().split()))

#     result = sub(fee, 0, plan, 0)
#     print(f'#{tc} {result}')


def f(nums, idx, r, op1, op2, op3, op4):
    return_box = []
    if idx == len(nums):
        return [r]
    if op1:
        return_box += f(nums, idx+1, r+nums[idx], op1-1, op2, op3, op4)
    if op2:
        return_box += f(nums, idx+1, r-nums[idx], op1, op2-1, op3, op4)
    if op3:
        return_box += f(nums, idx+1, r*nums[idx], op1, op2, op3-1, op4)
    if op4:
        return_box += f(nums, idx+1, int(r/nums[idx]), op1, op2, op3, op4-1)
    return return_box

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    op1, op2, op3, op4 = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    result = f(nums, 1, nums[0], op1, op2, op3, op4)
    print(f'#{tc} {max(result) - min(result)}')