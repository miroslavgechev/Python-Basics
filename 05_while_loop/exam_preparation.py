allowed_fails = int(input())
fail_counter = 0

has_failed = False

task_name = input()

grade_sum = 0
task_sum = 0
task_last = ""

while task_name != "Enough":
    task_grade = int(input())
    if task_grade <= 4:
        fail_counter += 1
        if fail_counter == allowed_fails:
            has_failed = True
            break

    grade_sum += task_grade
    task_last = task_name
    task_sum += 1

    task_name = input()

average_grade = grade_sum / task_sum

if has_failed == True:
    print(f"You need a break, {fail_counter} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {task_sum}")
    print(f"Last problem: {task_last}")



