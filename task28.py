def max_number(*nums: int) -> int:
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print(max_number(a, b, c))