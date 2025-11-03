student_marks = float(input('Enter marks: '))

if student_marks > 79:
    print('A')
elif student_marks >= 60 and student_marks <= 79:
    print('B')
elif student_marks >= 49 and student_marks <= 59:
    print('C')
elif student_marks >= 40 and student_marks <= 49:
    print('D')
elif student_marks >= 0 and student_marks < 40:
    print('E')