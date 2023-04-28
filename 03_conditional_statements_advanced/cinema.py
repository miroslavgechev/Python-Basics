type = input()
rows = int(input())
columns = int(input())

price = 0

if type == "Premiere":
    price = 12
elif type == "Normal":
    price = 7.5
elif type == "Discount":
    price = 5

total_seats = rows * columns
total_price = total_seats * price

print(f"{total_price:.2f} leva")