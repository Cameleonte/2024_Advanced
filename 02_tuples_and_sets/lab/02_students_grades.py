students_count = int(input())

students_dictionary = {}

for _ in range(students_count):
    data = tuple(input().split())
    student_name, grade = data[0], float(data[1])
    if student_name not in students_dictionary:
        students_dictionary[student_name] = []
    students_dictionary[student_name].append(grade)

for name, grades in students_dictionary.items():
    average_grade = sum(grades) / len(grades)
    grades_to_print = ' '.join([f"{x:.2f}" for x in grades])
    print(f'{name} -> {grades_to_print} (avg: {average_grade:.2f})')
