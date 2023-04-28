chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.4
veg_price = veg_menu * 8.15

dessert_price = (chicken_price + fish_price + veg_price) * 0.2
delivery_price = 2.5

total_price = chicken_price + fish_price + veg_price + dessert_price + delivery_price

print(f"{total_price:.2f}")
