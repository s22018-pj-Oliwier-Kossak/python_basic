from math import *


rad = 180/pi

degree = (pi * rad)/180

degreeValue = 360
radian = 1/3

print("degree:",degreeValue," rad",degreeValue*pi/180)
print("rad",radian," degrees",(180*radian))

print(radians(360))

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38



print("pole:", (pi*small_pizza_r**2)/10000)
print("pole:", (pi*big_pizza_r**2)/10000)
print("pole:", (pi*family_pizza_r**2)/10000)

print("price per square meter",11.50/((pi*small_pizza_r**2)/10000))
print("price per square meter",15.60/((pi*big_pizza_r**2)/10000))
print("price per square meter",22.00/((pi*family_pizza_r**2)/10000))

