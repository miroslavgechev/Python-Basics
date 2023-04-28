days = int(input())
room_type = input()
grade = input()

nights = days - 1
price = 0

if nights < 10:
    if room_type == "room for one person":
        price = nights * 18
    elif room_type == "apartment":
        price = nights * 25 * 0.7
    elif room_type == "president apartment":
        price = nights * 35 * 0.9
elif 10 <= nights <= 15:
    if room_type == "room for one person":
        price = nights * 18
    elif room_type == "apartment":
        price = nights * 25 * 0.65
    elif room_type == "president apartment":
        price = nights * 35 * 0.85
elif nights > 15:
    if room_type == "room for one person":
        price = nights * 18
    elif room_type == "apartment":
        price = nights * 25 * 0.50
    elif room_type == "president apartment":
        price = nights * 35 * 0.8

if grade == "positive":
    print(f"{price * 1.25:.2f}")
elif grade == "negative":
    print(f"{price * 0.9:.2f}")