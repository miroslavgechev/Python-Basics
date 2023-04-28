food_supply_in_g = float(input()) * 1000

food_consumption_current_day_in_g = 0
food_consumption_total_in_g = 0

input_line = input()

while input_line != "Adopted":
    food_consumption_current_day_in_g = int(input_line)
    food_consumption_total_in_g += food_consumption_current_day_in_g
    input_line = input ()

diff = abs(food_supply_in_g - food_consumption_total_in_g)

if food_supply_in_g >= food_consumption_total_in_g:
    print(f"Food is enough! Leftovers: {diff:.0f} grams.")
else:
    print(f"Food is not enough. You need {diff:.0f} grams more.")