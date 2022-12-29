class Staff:
    worktime = 8

class Teacher(Staff):
    def __init__(self, name: str, subject: str) -> None:
        self.name = name
        self.subject = subject


teacher1 = Teacher('Galina Nedu', 'Biology')

print(teacher1.name)
print(teacher1.subject)
print(teacher1.worktime)