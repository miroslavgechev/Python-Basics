name_actor = input()
points = float(input())
jury_members = int(input())

for loops in range (1, jury_members + 1):
    jury_member_name = input()
    jury_member_points = float(input())
    points += len(jury_member_name) * jury_member_points / 2
    if points >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        break

if points <= 1250.5:
    print(f"Sorry, {name_actor} you need {(1250.5 - points):.1f} more!")