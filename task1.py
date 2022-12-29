year = 2022
name = input("Enter your name: ")
age = int(input("Enter your age: "))
repeats = int(input("Number of repeats: "))

result = f'{name}, in {year + (100-age)} you will be 100 years old!\n'
print(repeats * result)