# Read a given string, change the character at a given index and then print the modified string.

# Method 1
# def mutate_string(string, position, character):
#     # converts string input (s) into a list
#     s = list(string)
#     # string() at index 5 = k is replacing index 5 with k
#     s[5] = 'k'
#     s = ''.join(s)
#     return s

# Method 2
def mutate_string(string, position, character):
    modified_string = string[:position] + character + string[position + 1:]

    return modified_string


if __name__ == '__main__':
    # reading the input string
    s = input()
    # reading the position and character
    i, c = input().split()

    s_new = mutate_string(s, int(i), c)
    print(s_new)

'''Input: abracadabra'''
'''change at index 5 to character k'''
'''Time & Space Complexity: 0(n) linear - means that the alogrithims execution time grows linearly with the size of the input. As the input size increases, the algorithims running time will increase proportionally '''
