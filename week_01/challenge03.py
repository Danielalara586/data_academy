
# Miles to Kilometers Converter

def menu():
    option = int(input("""Hello and welcome to this converter.
    Which operation would you like to make:
    1. From miles to kilometers.
    2. From kilometers to miles.
    
    Please enter your option: """))

    if option == 1:
        return miles_kilometers()
    elif option == 2:
        return kilometers_miles()
    else:
        print('Please enter a valid option.\n')
        return menu()

def miles_kilometers():
     miles = float(input('Please enter the miles: '))
     value = 1.609344
     kilometers = miles * value
     print(f'There are {round(kilometers, 4)} km in {miles} miles.')

def kilometers_miles():
    kilometers = float(input('Please enter the kilometers: '))
    value = 1.609344
    miles = kilometers / value
    print(f'There are {round(miles, 4)} miles in {kilometers} km.')

menu()