first_number = int(input())
second_number = int(input())
magic_number = int(input())

combination_number = 0

combination_found = False

for number_one in range (first_number, second_number + 1):
    for number_two in range (first_number, second_number + 1):
        combination_number += 1
        sum = number_two + number_one
        if sum == magic_number:
            combination_found = True
            break
    if combination_found:
        break

if combination_found:
    print(f"Combination N:{combination_number} ({number_one} + {number_two} = {magic_number})")
else:
    print(f"{combination_number} combinations - neither equals {magic_number}")