def args(*numbers):
    sum = 0
    # access as a tuple
    for number in numbers:
        sum += number
    return sum

# send a variable number of parameter 
sm = args(10, 20, 30, 40, 50)
print(sm)


def kargs(**info):
    # use dictionary method to access the value
    print(info["name"])
    print(info["age"])

# sending parameter with keys
kargs(name="Tahdi Islam", age="22")
