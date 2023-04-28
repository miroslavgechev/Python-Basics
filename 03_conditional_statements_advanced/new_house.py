flower_type = input()
flower_quantity = int(input())
budget = int(input())

flower_price = 0

if flower_type == "Roses":
    if flower_quantity > 80:
        flower_price = flower_quantity * 5 * 0.9
    else:
        flower_price = flower_quantity * 5
elif flower_type == "Dahlias":
    if flower_quantity > 90:
        flower_price = flower_quantity * 3.8 * 0.85
    else:
        flower_price = flower_quantity * 3.8
elif flower_type == "Tulips":
    if flower_quantity > 80:
        flower_price = flower_quantity * 2.8 * 0.85
    else:
        flower_price = flower_quantity * 2.8
elif flower_type == "Narcissus":
    if flower_quantity < 120:
        flower_price = flower_quantity * 3 * 1.15
    else:
        flower_price = flower_quantity * 3
elif flower_type == "Gladiolus":
    if flower_quantity < 80:
        flower_price = flower_quantity * 2.5 * 1.2
    else:
        flower_price = flower_quantity * 2.5

diff = abs(budget - flower_price)

if budget >= flower_price:
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
