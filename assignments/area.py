import math
numberOfsides = float(input('enter the number of sides of a polygon: '))
numberOflength = float(input('enter the length of sides of sides: '))
area = float(numberOfsides*numberOflength**2)/(4*math.tan((22/7)/numberOfsides))
print(area)