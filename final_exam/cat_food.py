number_of_cats = int(input())

counter_small_cats = 0
counter_big_cats = 0
counter_very_big_cats = 0
counter_food = 0

for cats in range (number_of_cats):
    current_cat_food_intake = float(input())
    counter_food += current_cat_food_intake

    if 100 <= current_cat_food_intake < 200:
        counter_small_cats += 1
    elif 200 <= current_cat_food_intake < 300:
        counter_big_cats += 1
    elif 300 <= current_cat_food_intake < 400:
        counter_very_big_cats += 1

price_for_food = (counter_food / 1000) * 12.45

print(f"Group 1: {counter_small_cats} cats.")
print(f"Group 2: {counter_big_cats} cats.")
print(f"Group 3: {counter_very_big_cats} cats.")
print(f"Price for food per day: {round(price_for_food, 2)} lv.")