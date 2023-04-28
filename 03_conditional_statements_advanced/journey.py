budget = float(input())
season = input()

price = 0
destination = ""
destination_type = ""

if budget <= 100:
    if season == "summer":
        price = budget * 0.3
    elif season == "winter":
        price = budget * 0.7
elif budget <= 1000:
    if season == "summer":
        price = budget * 0.4
    elif season == "winter":
        price = budget * 0.8
elif budget > 1000:
    price = budget * 0.9

if budget <= 100:
    destination = "Bulgaria"
elif budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

if season == "summer":
    destination_type = "Camp"
elif season == "winter":
    destination_type = "Hotel"

if destination == "Europe":
    destination_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{destination_type} - {price:.2f}")