number_of_locations = int(input())

for location in range (number_of_locations):
    expected_gold_per_day_current_location = float(input())
    days_at_current_location = int(input())
    total_gold_for_current_location = 0

    for days in range (days_at_current_location):
        gold_for_current_day = float(input())
        total_gold_for_current_location += gold_for_current_day

    average_gold_per_day_current_location = total_gold_for_current_location / days_at_current_location

    diff = abs(average_gold_per_day_current_location - expected_gold_per_day_current_location)

    if average_gold_per_day_current_location >= expected_gold_per_day_current_location:
        print(f"Good job! Average gold per day: {average_gold_per_day_current_location:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")