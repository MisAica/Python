students = {'John', 'Maria', 'David', 'Samantha'}

index = 3

student_list = []
for student in students:
    student_list.append(student)

if 0 <= index < len(student_list):
    print(student_list[index])
else:
    print("Index out of range.")
