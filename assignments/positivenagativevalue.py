negativeCounter = 0
positiveCount = 0
zeroCount = 0

for i in range(5):
    number = float(input("Please enter number {i+1}: "))

    if number < 0:
        negativeCount = negativeCount + 1
    elif number > 0:
        positiveCount = positive + 1
    else:
        zeroCount = zeroCount + 1

print(Results:")
print("Negative numbers: {negativeCount}")
print("Positive numbers: {positiveCount}")
print("Zeros: ,zeroCount}")