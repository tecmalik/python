number = int(input("Enter number :"))

for i in range(1, number + 1):
    print(" " * (number - i), end="")
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()
    
for i in range(number - 1, 0, -1):
    print(" " * (number - i), end="")
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()