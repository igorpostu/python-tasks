class Stack:
    def __init__(self):
        self.__items = 0
    
    def check(self):
        print(self.__items, 'items in stack.')
    
    def push(self):
        self.__items += 1
    
    def pop(self):
        if self.__items:
            self.__items -= 1
        else:
            print('Stack is empty.')


mystack = Stack()

print('Available operators:')
print('1. Push')
print('2. Pop')
print('3. Check')
print('4. Exit')

while True:
    command = input('Your action: ').lower()

    if command == 'push':
        mystack.push()
    elif command == 'pop':
        mystack.pop()
    elif command == 'check':
        mystack.check()
    else:
        break