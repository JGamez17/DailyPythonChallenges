
# Task

# You are given a string . qA2
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
''''''

if __name__ == '__main__':
    s = input()

    # alphanumeric
    print(s.isalnum()) 
    # alphabetical 
    print(s.isalpha())
    # is lowercase
    print(s.islower())
    print(s.isupper())