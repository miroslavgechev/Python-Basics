vacation_cost = float(input())
available_money = float(input())

spent_counter = 0
has_spent_too_much = False

day_counter = 0

total_savings = available_money

while vacation_cost > total_savings:
    action = input()
    action_sum = float(input())
    day_counter += 1

    if action == "spend":
        spent_counter += 1
        total_savings -= action_sum
        if total_savings < 0:
            total_savings = 0
    elif action == "save":
        spent_counter = 0
        total_savings += action_sum

    if spent_counter == 5:
        has_spent_too_much = True
        break

if has_spent_too_much == True:
    print(f"You can't save the money.")
    print(day_counter)
else:
    print(f"You saved the money for {day_counter} days.")

