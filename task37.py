class Student:
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name
        self.age = age
        self.grade = grade


stud1 = Student('Alexandr Sirbu', 18, 12)

print(stud1.name)
print(stud1.age)
print(stud1.grade)