number_of_groups = int(input())

group_musala = 0
group_monblan = 0
group_kili = 0
group_k_two = 0
group_everest = 0

total_participants = 0

for groups in range (number_of_groups):
    current_group_participants = int(input())
    total_participants += current_group_participants
    if current_group_participants <= 5:
        group_musala += current_group_participants
    elif current_group_participants <= 12:
        group_monblan += current_group_participants
    elif current_group_participants <= 25:
        group_kili += current_group_participants
    elif current_group_participants <= 40:
        group_k_two += current_group_participants
    elif current_group_participants > 40:
        group_everest += current_group_participants

print((f"{(group_musala*100/total_participants):.2f}%"))
print((f"{(group_monblan*100/total_participants):.2f}%"))
print((f"{(group_kili*100/total_participants):.2f}%"))
print((f"{(group_k_two*100/total_participants):.2f}%"))
print((f"{(group_everest*100/total_participants):.2f}%"))


