def p(arg):
    print(arg)


person = {"name": "kala pakhi", "age": 23, "address": "kaliapur", "job": "facebooker"}

# print(person)
# print(person["name"])
person["job"] = "developer"
# p(person)
p(person.keys())
p(person.values())
del person["age"]
p(person)

for k, v in person.items():
    p({k, v})
