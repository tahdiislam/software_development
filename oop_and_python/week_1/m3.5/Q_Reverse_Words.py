s = input().split(" ")
rev = list(map(lambda w: w[::-1], s))
ans = ""
for i, w in enumerate(rev):
    ans += w
    if i != len(rev) - 1:
        ans += " "
print(ans)
