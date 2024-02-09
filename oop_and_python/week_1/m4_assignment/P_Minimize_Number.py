input()
s = input().split(" ")
nums = list(map(lambda a: int(a), s))
cnt = 0
is_even = True
while is_even:
    for i, v in enumerate(nums):
        if v % 2 == 0:
            nums[i] = v / 2
        else:
            is_even = False
            break
    if is_even:
        cnt += 1
print(cnt)
