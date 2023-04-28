student_name = input()
student_class = 1
counter_fails = 0
grade = 0

while counter_fails < 2:
    student_annual_grade = float (input())
    if student_annual_grade >= 4:
        grade += student_annual_grade
        if student_class >= 12:
            break
        else:
            student_class += 1
    else:
        counter_fails += 1
        continue



if counter_fails != 2:
    print(f"{student_name} graduated. Average grade: {(grade / student_class):.2f}")
else:
    print(f"{student_name} has been excluded at {student_class} grade")

