import math

cat_breed = input()
cat_sex = input()

cat_life_in_cat_months = 0
is_cat_valid = True

if cat_breed == "British Shorthair":
    if cat_sex == "m":
        cat_life_in_cat_months = (13 * 12) / 6
    else:
        cat_life_in_cat_months = (14 * 12) / 6
elif cat_breed == "Siamese":
    if cat_sex == "m":
        cat_life_in_cat_months = (15 * 12) / 6
    else:
        cat_life_in_cat_months = (16 * 12) / 6
elif cat_breed == "Persian":
    if cat_sex == "m":
        cat_life_in_cat_months = (14 * 12) / 6
    else:
        cat_life_in_cat_months = (15 * 12) / 6
elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        cat_life_in_cat_months = (16 * 12) / 6
    else:
        cat_life_in_cat_months = (17 * 12) / 6
elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        cat_life_in_cat_months = (12 * 12) / 6
    else:
        cat_life_in_cat_months = (13 * 12) / 6
elif cat_breed == "Siberian":
    if cat_sex == "m":
        cat_life_in_cat_months = (11 * 12) / 6
    else:
        cat_life_in_cat_months = (12 * 12) / 6
else:
    print(f"{cat_breed} is invalid cat!")
    is_cat_valid = False

if is_cat_valid:
    print(f"{math.floor(cat_life_in_cat_months)} cat months")







