n = int(input())

current_number = 1
is_bigger_than_n = False

for rows in range (1, n+1):
    for cols in range (1, rows + 1):
        if current_number > n:
            is_bigger_than_n = True
            break
        print(f"{current_number} ", end="")
        current_number += 1
    if is_bigger_than_n:
        break
    print()