import math

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_height_astronauts = float(input())

ship_volume = ship_height * ship_width * ship_length
cabin_volume = (average_height_astronauts + 0.4) * 2 * 2

astronauts_allowed = math.floor(ship_volume / cabin_volume)

if 3 <= astronauts_allowed <= 10:
    print(f"The spacecraft holds {astronauts_allowed} astronauts.")
elif astronauts_allowed < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
