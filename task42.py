class Number:
    def __init__(self, num: int):
        self.num = num
    
    def __str__(self):
        return f'{self.num}'
    
    def __add__(self, other):
        num = self.num + other.num
        return Number(num)


num1 = Number(5)
num2 = Number(10)
num3 = Number(1)

print(num1 + num2 + num3)