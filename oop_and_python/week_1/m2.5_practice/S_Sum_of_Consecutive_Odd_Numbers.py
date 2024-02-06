def num_input():
    a = input()
    b = int(a)
    return b


t = num_input()

cnt = 0

for i in range(0, t):
    a = num_input()
    b = num_input()
    if b >= a:
        for num in range(a, b):
            if num != a and num % 2 != 0:
                cnt += num
    else:
        for num in range(b, a):
            if num != b and num % 2 != 0:
                cnt += num
    print(cnt)
    cnt = 0