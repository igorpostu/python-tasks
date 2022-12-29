def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input("Enter a number: "))

if is_prime(n):
    print("This number is prime")
else:
    print("This number is not prime")