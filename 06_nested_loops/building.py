number_of_floors = int(input())
number_of_rooms = int(input())

type_of_room = ""

for floor in range (number_of_floors, 0, -1):
    for room in range (0, number_of_rooms):
        if floor == number_of_floors:
            type_of_room = "L"
        elif floor % 2 == 0:
            type_of_room = "O"
        else:
            type_of_room = "A"
        print(f"{type_of_room}{floor}{room}", end = " ")
    print()

