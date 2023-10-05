import re

'''
verify N is a floating point number and can start with +,- or. symbol. 
'''


def is_valid_float(string):
    # Define the regular expression pattern
    pattern = r'^[+_.]?\d+(\.\d*)?$'

    # Use re.match to check if the string matches the pattern
    if re.match(pattern, string):
        return True
    else:
        return False


# Take user input and check if it's a valid floating-point number
user_input = input()

if is_valid_float(user_input):
    print("True")
else:
    print("False")
