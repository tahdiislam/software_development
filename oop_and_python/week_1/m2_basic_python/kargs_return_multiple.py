# arguments order
def arguments_order(first, last):
    result = f"{first} {last}"
    return result


print(arguments_order(last="Islam", first="Tahdi"))


# key arguments
def key_arguments(**kArgs):
    print(kArgs)
    for key, value in kArgs.items():
        result = f"{key} : {value}"
        print(result)


key_arguments(
    first1="Tahdi",
    last1="Islam",
    first2="Zahid",
    last2="Hasan",
    first3="Mehedi",
    last3="Hasan",
)


# return multiple
def return_multiple(num1, num2):
    addition = num1 + num2
    multiply = num1 * num2
    remain = num1 - num2
    return addition, multiply, remain


print(return_multiple(50, 20))
