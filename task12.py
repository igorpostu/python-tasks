import random

def new_list(a: list) -> list:
    return [a[0], a[len(a)-1]]


a = [random.randint(1, 10) for i in range(random.randint(5, 10))]
b = new_list(a)

print("a:", a)
print("New list:", b)