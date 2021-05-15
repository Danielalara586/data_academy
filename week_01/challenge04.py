# Volume Calculator
import math

def menu():
    option = int(input("""Hello and welcome to this volume calculator.
    Which shape would you like to know it's volume:
    1. Cylinder.
    2. Sphere.
    3. Triangular prism
    4. Rectangular prism
    5. Cube
    
    Please enter your option: """))

    if option == 1:
        r = float(input('Please enter the value for the radius: '))
        h = float(input('Please enter the value for the height: '))
        return volume_cylinder(r, h)
    elif option == 2:
        r = float(input('Please enter the value for the radius: '))
        return volume_sphere(r)
    elif option == 3:
        l = float(input('Please enter the value for the long side: '))
        h = float(input('Please enter the value for the high side: '))
        height = float(input('Please enter the value for the height: '))
        return volume_triangularp(l, h, height)
    elif option == 4:
        l = float(input('Please enter the value for the long side: '))
        w = float(input('Please enter the value for the width: '))
        h = float(input('Please enter the value for the height: '))
        return volume_rectangularp(l, w, h)
    elif option == 5:
        sides = float(input('Please enter value for the sides: '))
        return volume_cube(sides)
    else:
        print('Please enter a valid option.\n')
        return menu()

def volume_cylinder(radius, height):
    volume = math.pi * (radius**2) * height
    print(f'The volume of the cylinder is: {round(volume, 4)} u^3.')

def volume_sphere(radius):
    volume = (4/3) * math.pi * radius ** 3
    print(f'The volume of the sphere is: {round(volume, 4)} u^3.')

def volume_triangularp(long, high, height):
    volume = ((long * high)/2) * height
    print(f'The volume of the triangular prism is: {round(volume, 4)} u^3.')

def volume_rectangularp(long, width, height):
    volume = long * width * height
    print(f'The volume of the rectangular prism is: {round(volume, 4)} u^3.')

def volume_cube(side):
    volume = side ** 3
    print(f'The volume of the cube is: {round(volume, 4)} u^3.')

menu()

