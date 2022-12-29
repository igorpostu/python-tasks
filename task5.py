import random

a = [random.randint(1, 10) for i in range(random.randint(5, 10))]
b = [random.randint(1, 10) for i in range(random.randint(5, 10))]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print("a:", a)
print("b:", b)
print("c:", c)
