def num_input():
    a = input()
    b = int(a)
    return b


n = num_input()
a = 0
b = 1
c = 0
fibo = [0, 1]
for i in range(2, n):
    c = a + b
    a = b
    b = c
    fibo.append(b)
for num in fibo:
    print(num)
