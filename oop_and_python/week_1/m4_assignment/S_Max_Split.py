# s = input()
# arr = []
# a = s[0]
# cnt = 0
# index = 0
# i = 0
# while i < len(s):
#     if s[i] == a:
#         cnt += 1
#         i += 1
#     else:
#         s2 = s[index : i + cnt]
#         arr.append(s2)
#         i += cnt
#         index = i
#         cnt = 0
#         if i < len(s):
#             a = s[i]
# print(len(arr))
# for a in arr:
#     print(a)

# arr = []
# L = ""
# R = ""
# for i in range(len(s)):
#     if s[i] == "R":
#         R += "R"
#     else:
#         L += "L"
#     if len(L) > 0 and len(L) == len(R):
#         s2 = ""
#         if s[i] == "L":
#             s2 += R + L
#         else:
#             s2 += L + R
#         arr.append(s2)
#         L = ""
#         R = ""
# print(len(arr))
# for a in arr:
#     print(a)

# arr = [[""] * 1000 for _ in range(1000)]
# row, col, cnt, l, r = 0, 0, 0, 0, 0
# for c in s:
#     if c == "R":
#         arr[row][col] = "R"
#         r += 1
#     else:
#         arr[row][col] = "L"
#         l += 1
#     col += 1
#     if l != 1 and l == r:
#         row += 1
#         cnt += 1
#         r = 0
#         l = 0
#         col = 0

# if len(s) == 2:
#     print(1)
# else: print(cnt)

# for i in range(1000):
#     if arr[i][0] != "R" and arr[i][0] != "L":
#         continue
#     else:
#         print("".join(arr[i]))
s = input()
arr = []
s2 = ''
for char in s:
    s2 += char
    if s2.count('L') == s2.count('R'):
        arr.append(s2)
        s2 = ''
print(len(arr))
for w in arr:
    print(w)