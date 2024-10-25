import math
x1=float(input('the latitude of coordinate x1 :'))
y1=float(input('the longitude of coordinate y1 :'))
x2=float(input('the latitude of coordinate x2 :'))
y2=float(input('the longitude of coordinate y2 :'))
radius = 6371.01
distance = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print('The distance between those points is:',distance)