
# Task

# You are given a string . qA2
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
''''''

if __name__ == '__main__':
    s = input()

print(True in [char.isalnum() for char in s])
print(True in [char.isalpha() for char in s])
print(True in [char.isdigit() for char in s])
print(True in [char.islower() for char in s])
print(True in [char.isupper() for char in s])
