import math

number_of_tournaments = int(input())
initial_points = int(input())

points = initial_points

won_tournaments = 0

for tournaments in range (number_of_tournaments):
    current_tournament = input()
    if current_tournament == "W":
        points += 2000
        won_tournaments += 1
    elif current_tournament == "F":
        points += 1200
    elif current_tournament == "SF":
        points += 720

average_points = (points - initial_points) / number_of_tournaments
win_ratio = won_tournaments * 100 / number_of_tournaments

print(f"Final points: {points}")
print(f"Average points: {math.floor((average_points))}")
print(f"{win_ratio:.2f}%")
