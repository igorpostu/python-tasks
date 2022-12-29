class Square:
    def __init__(self, n: int) -> None:
        self.n = n
    
    def perimeter(self) -> int:
        return self.n * 4
    
    def area(self) -> int:
        return self.n ** 2


mysquare = Square(5)

print(mysquare.perimeter())
print(mysquare.area())