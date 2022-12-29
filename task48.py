class DictMixin:
    def to_dict(self) -> dict:
        return self.__dict__

class ListMixin:
    def to_list(self) -> list:
        args_dict = self.to_dict()
        result = []
        for key in args_dict:
            result.append(args_dict[key])
        return result

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

class Student(Person, ListMixin, DictMixin):
    def __init__(self, name: str, faculty: str, grade: int) -> None:
        super().__init__(name)
        self.faculty = faculty
        self.grade = grade

stud1 = Student('Shawn', 'Law', 10)

print(stud1.to_dict())
print(stud1.to_list())