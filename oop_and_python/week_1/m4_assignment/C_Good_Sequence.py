input()
s = input().split(" ")
nums = list(map(lambda a: int(a), s))
nums_set = set(nums)
cnt = {}
for num in nums:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
ans = 0
for k, v in cnt.items():
    if v > k:
        ans += v - k
    elif v < k:
        ans += v
print(ans)
