month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_apartment = nights * 65
    price_studio = nights * 50
    if 7 < nights <= 14:
        price_studio = price_studio * 0.95
    elif nights > 14:
        price_studio = price_studio * 0.7
        price_apartment = price_apartment * 0.9
elif month == "June" or month == "September":
    price_apartment = nights * 68.70
    price_studio = nights * 75.2
    if nights > 14:
        price_studio = price_studio * 0.8
        price_apartment = price_apartment * 0.9
elif month == "July" or month == "August":
    price_apartment = nights * 77
    price_studio = nights * 76
    if nights > 14:
        price_apartment = price_apartment * 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

