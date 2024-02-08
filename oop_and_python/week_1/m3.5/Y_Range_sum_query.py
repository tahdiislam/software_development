q = int(input().split(" ")[1])
s = input().split(" ")
nums = list(map(lambda a: int(a), s))
new_nums = [nums[0]]
for i in range(1, len(nums)):
    new_nums.append(new_nums[i - 1] + nums[i])

for i in range(0, q):
    s2 = input().split(" ")
    if s2[0] != "1":
        print(new_nums[int(s2[1]) - 1] - new_nums[int(s2[0]) - 2])
    else:
        print(new_nums[int(s2[1]) - 1])
