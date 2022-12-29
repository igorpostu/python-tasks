import random

def create_list_by_sets(array: list) -> list:
    return list(set(array))

def create_list_by_loop(array: list) -> list:
    result = []
    for elem in array:
        if elem not in result:
            result.append(elem)
    return result


a = [random.randint(1, 10) for i in range(random.randint(5, 10))]

print("Original list:", a)
print("New list by using sets:", create_list_by_sets(a))
print("New list by using loop:", create_list_by_loop(a))