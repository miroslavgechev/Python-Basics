steps_counter = 0
steps = ""

is_home = False

while steps_counter < 10000:
    steps = input()
    if steps == "Going home":
        steps = input()
        steps_counter += int(steps)
        is_home = True
        break
    steps_counter += int(steps)

steps_diff = abs(10000 - steps_counter)

if is_home == True and steps_counter < 10000:
    print(f"{steps_diff} more steps to reach goal.")
elif steps_counter >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")




