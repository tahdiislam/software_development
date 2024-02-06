numbers = [12, 33, 22, 33, 55, 66, 23, 32, 70, 33, 90, 85]

odd_num = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odd_num.append(num)

print("odd numbers 1", odd_num)

odd_nums_2 = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print("odd numbers 2", odd_nums_2)

# nested loop
player = ["sakib", "tamim", "musfiq"]
ages = [38, 37, 34]

age_comb = []
for name in player:
    for age in ages:
        age_comb.append([name, age])

print("age combination 1", age_comb)

age_comb_2 = [[name, age] for name in player for age in ages]

print(age_comb_2)
