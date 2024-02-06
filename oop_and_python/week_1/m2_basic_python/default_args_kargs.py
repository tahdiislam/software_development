# default argument
def default_args(*numbers):
    print(numbers)
    cnt = 0
    for num in numbers:
        cnt+= num
    return cnt
total = default_args(34, 3432, 22, 23, 45, 21)
print(total)