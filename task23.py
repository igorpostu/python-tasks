def num_list(file: str) -> list:
    numbers = []
    with open(file, 'r') as nums:
        for num in nums.readlines():
            numbers.append(int(num))
    return numbers


numbers1 = num_list('task23_numbers1.txt')
numbers2 = num_list('task23_numbers2.txt')
overlapped = []

for number in numbers1:
    if number in numbers2:
        overlapped.append(number)

print('Overlapping numbers:', overlapped)