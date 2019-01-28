'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

from math import pi

# pi = 3.1415
radius = 3.14
height = 5

circumference = 2 * pi * radius
circleArea = pi * radius ** 2

volume = circleArea * height
surfaceArea = (circumference * height) + (circleArea * 2)

print("volume " + str(volume))
print("surface area " + str(surfaceArea))
