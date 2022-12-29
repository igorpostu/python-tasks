class Teacher:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__sallary = 5000
    
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nSallary: {self.__sallary}'
    
    def set_sallary(self, sallary: int):
        self.__sallary = sallary

teacher1 = Teacher('Galina Nedu', 53)
print(teacher1)

teacher1.set_sallary(8000)
print(teacher1)