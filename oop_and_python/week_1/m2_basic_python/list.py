#          0    1   2   3   4   5   6   7
numbers = [12, 33, 22, 33, 55, 66, 23, 32]
#          -8  -7  -6  -5  -4  -3   -2   -1

print(numbers[1], numbers[7])
print(numbers[-7], numbers[-1])


print(numbers[1:7])
print(numbers[1:7:2])
print(numbers[1:7:-2])
print(numbers[7:1:-2])
print(numbers[3::2])
print(numbers[:])
print(numbers[::-1])