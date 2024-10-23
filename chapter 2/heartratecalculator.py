
userAge = int(input('enter your age'))
maximumHeartRate = (220 - userAge)
range1 = maximumHeartRate*(50/100) 
range2 = maximumHeartRate*(85/100)
print("maximum heart rate is ", maximumHeartRate)
print(" the range of the user’s target heart rate is between " , range1)
print(" and ", range2)