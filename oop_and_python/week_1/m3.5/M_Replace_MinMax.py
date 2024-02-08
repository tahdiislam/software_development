input()
s = input().split(" ")
n = []
mx = -9999999999999999
mn = 9999999999999999
for a in s:
    b = int(a)
    n.append(b)
    if b > mx:
        mx = b
    if b < mn:
        mn = b
for i, v in enumerate(n):
    if v == mx:
        n[i] = mn
    elif v == mn:
        n[i] = mx
ans = ""
for i, a in enumerate(n):
    ans += str(a)
    if i != (len(n) - 1):
        ans += " "
print(ans)
