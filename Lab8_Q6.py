n = int(input("Enter the number of students: "))

students = []

for _ in range(n):
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = float(input("Enter total marks out of 100: "))
    students.append({'Name': name, 'RollNo': rollno, 'Marks': marks})

max_student = max(students, key=lambda x: x['Marks'])
print("\nDetails of Student with Maximum Marks:")
print(f"Name: {max_student['Name']}, RollNo: {max_student['RollNo']}, Marks: {max_student['Marks']}")

students.sort(key=lambda x: x['Marks'], reverse=True)
for i, student in enumerate(students, start=1):
    student['Rank'] = i

print("\nStudent Records in Ascending Order of Ranks:")
for student in students:
    print(f"Rank: {student['Rank']}, Name: {student['Name']}, RollNo: {student['RollNo']}, Marks: {student['Marks']}")
