def num_input():
    a = input()
    b = int(a)
    return b


x = num_input()
n = num_input()

cnt = 0
if n < 2:
    print(0)
else:
    for a in range(2, n):
        if a % 2 == 0:
            cnt += x**a
    print(cnt)
