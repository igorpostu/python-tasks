class Person():
    def __init__(self, value: str):
        self.__name = value

    def get_name(self):
        print('Name:', end=' ')
        return self.__name
    
    def set_name(self, value: str):
        self.__name = value
    
    name = property(get_name, set_name)


p1 = Person('Nick')
print(p1.name)

p1.name = 'Dilan'
print(p1.name)