number_list = [i for i in range(101)]

low = 0
high = len(number_list) - 1
counter = 0
answer = ''
while not answer == 'yes':
    mid = (low + high) // 2
    print('Is the number ', number_list[mid], '?', sep='')
    answer = input('Your answer: ')
    if answer == 'low':
        low = mid + 1
    else:
        high = mid - 1
    counter += 1
else:
    print('I took', counter, 'guesses!')