# Given the names and grades for each student in a class, store them in a
# nested list and print the name(s) of any student(s) having the second
# lowest grade
# STDInput
'''5
Harry 37.21
Berry 37.21
Tina 37.2
Akriti 41
Harsh 39 '''


if __name__ == '__main__':
 # Create an empty list to store student details
    students = []
# Input number of students and name & grade for each student
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

# find the second lowest grade/score
scores = set([student[1] for student in students])
# extracts grade of 2nd student, iterates over each student in students list
second_lowest_grade = sorted(scores)[1]

# find the student with second lowest score
second_lowest_student = [students[0]
                         for student in students if student[1] == second_lowest_grade]

# Sort the student names alphabetically
second_lowest_student.sort()

# Print the names of the students with the second lowest grade
print("Students with the second lowest grade:")
for students in second_lowest_student:
    print(students)
