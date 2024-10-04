student_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]

lowest_student = student_scores[0]

for student in student_scores:
    if student[1] < lowest_student[1]:
        lowest_student = student

print(lowest_student)