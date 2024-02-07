numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])

numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)

student = {"name": "Amir", "class": 10, "marks": 85}

student.pop("marks")
print(student)

try:
    result = 20 // 5
except:
    print("error happened")
finally:
    print("finally here")

from math import *

result = ceil(5.00001)
print(result)


num = lambda a:a*a
print(num(2**2))
