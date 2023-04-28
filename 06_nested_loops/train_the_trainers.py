jury_count = int(input())

presentation_name = input()

averaged_grades_total = 0
student_count = 0

while presentation_name != "Finish":
    grade_sum = 0
    for grades in range (1, jury_count + 1):
        current_grade = float(input())
        grade_sum += current_grade

    averaged_grade = grade_sum / jury_count
    averaged_grades_total += averaged_grade
    student_count += 1
    print(f"{presentation_name} - {averaged_grade:.2f}.")

    presentation_name = input()

averaged_grade_all_students = averaged_grades_total / student_count

print(f"Student's final assessment is {averaged_grade_all_students:.2f}.")