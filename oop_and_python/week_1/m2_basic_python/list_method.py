#          0    1   2   3   4   5   6   7
numbers = [12, 33, 22, 33, 55, 66, 23, 32]
#          -8  -7  -6  -5  -4  -3   -2   -1

numbers.append(59)
print(numbers)

numbers.insert(1, 62)
print(numbers)

if 55 in numbers:
    numbers.remove(55)

print(numbers)

last = numbers.pop()
print(last)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)