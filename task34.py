import json

def get_data(file: str) -> dict:
    with open(file, 'r') as f:
        return dict(json.load(f))

def look_for(name: str) -> None:
    data = get_data('task34_birthdays.json')
    print(name, '\'s birthday is ', data[name], sep='')

def add(name: str, birthday: str) -> None:
    data = get_data('task34_birthdays.json')
    with open('task34_birthdays.json', 'w') as f:
        data[name] = birthday
        json.dump(data, f)


print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in get_data('task34_birthdays.json'):
    print('-', name)

print('Do you want to add or read?')
command = input('>> ')

if command == 'read':
    name = input('Enter the name: ')
    look_for(name)
elif command == 'add':
    name = input('Enter the name: ')
    date = input('Enter the birthday: ')
    add(name, date)
else:
    print('Wrong command!')