movie_budget = float(input())
statists_number = int(input())
statist_clothing_cost = float(input())

decor_cost = movie_budget * 0.1

statist_clothing_cost_total = statist_clothing_cost * statists_number

if statists_number > 150:
    statist_clothing_cost_total = statist_clothing_cost_total * 0.9


total_cost = statist_clothing_cost_total + decor_cost

diff = abs(movie_budget - total_cost)

if movie_budget >= total_cost:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")