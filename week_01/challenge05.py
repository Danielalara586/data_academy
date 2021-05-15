# Changing ranges

def changing_ranges():
    print('Hello and welcome to changing ranges!')
    upper_limit = float(input('Please enter the value for the upper limit: '))
    lower_limit = float(input('Please enter the value for the lower limit: '))
    comparison_num = float(input('Please enter the value for the comparison number: '))
    in_range = False
    
    while in_range != True: 
        if comparison_num < upper_limit and  comparison_num > lower_limit:
            print(f'The number {comparison_num} is in range!')
            in_range = True 
        elif comparison_num > upper_limit:
            print(f'The number {comparison_num} is above the range!')
            in_range = False
            comparison_num = float(input('Please enter the value for the comparison number: '))  
        else:
            print(f'The number {comparison_num} is below the range!')
            in_range = False
            comparison_num = float(input('Please enter the value for the comparison number: '))

changing_ranges()