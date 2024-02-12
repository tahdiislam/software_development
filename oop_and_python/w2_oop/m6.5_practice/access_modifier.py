# what is encapsulation and access modifier? explain with example.

""" 
encapsulation is principle of OOP which protects the internal data of a class using access modifier.
there are three types of access modifier to protect data: public, protected and private.
1. public access modifier --> every variable and method are public in default. this data is
                              available to everywhere.
2. protected access modifier --> we need to use a underscore '_' before the name of the variable or 
                                the method, after that the variable or the method will be consider as as protected. this is just a naming convention for the other developer may understand that this is protected modifier. but anyone can access this
3. private access modifier --> similar to protected access modifier. but now we need to use 
                                double underscore '__' instead of one. this is not accessible to the outside of the class.
"""
# example
class BankAccount:
    def __init__(self, name, initial_balance, branch) -> None:
        self.name = name #public access modifier
        self._branch = branch #protected access modifier
        self.__balance = initial_balance #private access modifier
    def check_balance(self):
        return self.__balance