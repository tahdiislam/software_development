# multiple inheritance
class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level
class Sport:
    def __init__(self, game) -> None:
        self.game = game
class Family:
    def __init__(self, address, ) -> None:
        self.address = address
class Student(School, Sport, Family):
    def __init__(self, id, level, game, address) -> None:
        School.__init__(self, id, level)
        Sport.__init__(self, game)
        Family.__init__(self, address)
    def __repr__(self) -> str:
        return f"Student class is {self.level} with id: {self.id}"
    
new_student = Student(23, 10, 'football', 'Bangladesh')
print(new_student)