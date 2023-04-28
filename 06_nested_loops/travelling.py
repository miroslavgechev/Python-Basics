
destination = input()

while destination != "End":
    budget = 0
    destination_cost = float(input())

    while budget < destination_cost:
        amount = float(input())
        budget += amount

    print(f"Going to {destination}!")
    destination = input()
