def rangoli(size):
    alphabets = [chr(ord('a') + i) for i in range(size)]

    rangoli_lines = []

    for i in range(size):
        # Create the left side of the line
        left_side = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])

        # Create the complete line by centering the left side
        line = left_side.center(4 * size - 3, '-')

        # Append the line to the list
        rangoli_lines.append(line)

    # Join the list of lines with newline characters to form the rangoli
    rangoli_pattern = '\n'.join(rangoli_lines)

    return rangoli_pattern


# Input size
size = int(input())
# Generate and print the rangoli
print(rangoli(size))
