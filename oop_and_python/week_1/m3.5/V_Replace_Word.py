s = input()

n = len(s)
i = 0
ans = ""
while i < n:
    if i + 4 < len(s) and s[i : i + 5] == "EGYPT":
        ans += " "
        i += 5
    else:
        ans += s[i]
        i += 1
print(ans)
