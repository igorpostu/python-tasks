def number_is_inside(n: int, array: list) -> bool:
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < n:
            low = mid + 1
        elif array[mid] > n:
            high = mid - 1
        else: 
            return True
    return False


a = [i for i in range(1, 11)]
print("a =", a)

num = int(input("Enter a number: "))

if number_is_inside(num, a):
    print("Number", num, "is inside list a")
else:
    print("Number", num, "is not inside list a")