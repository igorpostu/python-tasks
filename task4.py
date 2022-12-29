num = int(input("Enter a number: "))
divisors = []

for i in range(1, num // 2 + 1):
    if num % i == 0:
        divisors.append(i)

print("Divisors:", divisors)
