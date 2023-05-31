# A normal conditional block used to run file as a script - an additional entry point

# Print the average marks for the student name provided
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh


if __name__ == '__main__':
    n = int(input("Number of Students:"))

    student_marks = {}

    for _ in range(n):
        name, *line = input("enter name & scores:").split()
# List unpacking - assigns the other elements to line
        scores = list(map(float, line))
# Takes the values of the line and assings them to the score variable, and turns scores into a list of floats
        student_marks[name] = scores

        query_name = input()


def avg(arr):
    return sum(arr) / len(arr)


print(f'{avg(student_marks[query_name]):.2f}')
