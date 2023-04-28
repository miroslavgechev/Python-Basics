nylon = int(input())
paint = int(input())
dilutent = int(input())
man_hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint * 1.1) * 14.5
dilutent_price = dilutent * 5
bags_price = 0.4

materials_price = nylon_price + paint_price + dilutent_price + bags_price

man_hours_price = (materials_price * 0.3) * man_hours

total_price = materials_price + man_hours_price

print(total_price)