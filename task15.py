s = input("Enter a sentence: ").split()
s = s[::-1]

print("This sentence backwards: ")
for i in s:
    print(i, end=' ')