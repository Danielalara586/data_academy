# Program that calculates the area of a triangle and its type
import math

def triangleArea (a, b, c):
    if a == b and b == c:
        area = (math.sqrt(3)/4) * a**2
        print('This is an equilateral triangle and its area is: ' + str(round(area, 4)) + ' m^2') 
    elif a != b and b != c and a != c:
        s = (a + b + c)/2
        area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
        print('This is a scalene triangle and its area is: ' + str(round(area, 4)) + ' m^2') 
    else:
        if a == b and b != c:
            area = (c * math.sqrt(a*b - ((c**2)/4)))/2
            print('This is an isosceles triangle and its area is: ' + str(round(area, 4)) + ' m^2') 
        elif a == c and c != b:
            area = (b * math.sqrt(a*c - ((b**2)/4)))/2
            print('This is an isosceles triangle and its area is: ' + str(round(area, 4)) + ' m^2') 
        else:
            area = (a * math.sqrt(c*b - ((a**2)/4)))/2
            print('This is an isosceles triangle and its area is: ' + str(round(area, 4)) + ' m^2') 

a = int(input('Please enter the first side: '))
b = int(input('Please enter the second side: '))
c = int(input('Please enter the third side: '))

triangleArea(a,b,c)