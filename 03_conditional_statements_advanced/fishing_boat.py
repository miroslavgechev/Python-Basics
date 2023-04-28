budget = int(input())
season = input()
fishermen = int(input())

price = 0

if season == "Spring":
    if fishermen <= 6:
        price = 3000 * 0.9
    elif 7 < fishermen <= 11:
        price = 3000 * 0.85
    elif fishermen >= 12:
        price = 3000 * 0.75
elif season == "Summer":
    if fishermen <= 6:
        price = 4200 * 0.9
    elif 7 < fishermen <= 11:
        price = 4200 * 0.85
    elif fishermen >= 12:
        price = 4200 * 0.75
elif season == "Autumn":
    if fishermen <= 6:
        price = 4200 * 0.9
    elif 7 < fishermen <= 11:
        price = 4200 * 0.85
    elif fishermen >= 12:
        price = 4200 * 0.75
elif season == "Winter":
    if fishermen <= 6:
        price = 2600 * 0.9
    elif 7 < fishermen <= 11:
        price = 2600 * 0.85
    elif fishermen >= 12:
        price = 2600 * 0.75

if (fishermen % 2 == 0) and (season != "Autumn"):
    price = price * 0.95

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


