# def double(num):
#     return num * 2

double = lambda num: num * 2
multiply = lambda num: num**2

print(double(22))
print(multiply(22))

numbers = [23, 343, 33, 55, 323, 654, 343, 333]

# new_numbers = map(double, numbers)
# new_numbers = map(lambda a: a * 2, numbers)
new_numbers = map(lambda a: a**a, numbers)

print(list(new_numbers))

actors = [
    {"name": "shabana", "age": 65},
    {"name": "sabnoor", "age": 45},
    {"name": "sabila noor", "age": 30},
    {"name": "srabonti", "age": 38},
    {"name": "shaon", "age": 47},
]

juniors = filter(lambda actor: actor["age"] < 40, actors)
seniors = filter(lambda actor: actor["age"] >= 40, actors)

print(list(juniors))
print(list(seniors))
