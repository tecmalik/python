negativeCounter = 0
positiveCounter = 0
zeroCounter = 0

for i in range(5):
    number = float(input(f"Please enter number {i+1}: "))

    if number < 0:
        negativeCounter = negativeCounter + 1
    elif number > 0:
        positiveCounter = positiveCounter + 1
    else:
        zeroCounter = zeroCounter + 1

print(f"Negative numbers: {negativeCounter}")
print(f"Positive numbers: {positiveCounter}")
print(f"Zeros: ,{zeroCounter}")