class Calculator:
    model = "casio 99 ms"

    def add(self, *args):
        cnt = 0
        for n in args:
            cnt += n
        return cnt

    def deduct(self, n1, n2):
        return n1 - n2

    def multiply(self, *args):
        cnt = 1
        for n in args:
            cnt *= n
        return cnt

    def divide(self, n1, n2):
        return n1 // n2


new_calculation = Calculator()
print(new_calculation.add(10, 20, 30, 40))
print(new_calculation.multiply(10, 20, 30, 40))
print(new_calculation.deduct(100, 50))
print(new_calculation.divide(100, 50))
