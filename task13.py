def fibbonacci(num: int) -> int:
    if num < 2:
        return 1
    return fibbonacci(num-2) + fibbonacci(num-1)


n = int(input("How many numbers to generate: "))
a = []

for i in range(1, n+1):
    a.append(fibbonacci(i))

print("The sequence:", a)