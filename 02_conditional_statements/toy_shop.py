trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = puzzles * 2.6
dolls_price = dolls * 3
bears_price = bears * 4.1
minions_price = minions * 8.2
trucks_price = trucks * 2

profit = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

total_toys = puzzles + dolls + bears + minions + trucks

if total_toys >= 50:
    profit = profit * 0.75

profit = profit * 0.9

diff = abs(trip_price - profit)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")