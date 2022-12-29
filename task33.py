birthdays = {'Albert Einstein': '03/14/1879', 'Benjamin Franklin': '10/27/1776'}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays:
    print(name)

print('Who\'s birthday do you want to look up?')
look = input('>> ')

if look in birthdays:
    print(look, '\'s birthday is ', birthdays[look], sep='')
else:
    print('We don\'t know the birthday of', look)