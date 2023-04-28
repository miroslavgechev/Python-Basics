
room_width = int(input())
room_length = int(input())
room_height = int(input())

cubes = room_width * room_height * room_length

has_finished_moving = False

while cubes > 0:
    boxes_moved = input()
    if boxes_moved == "Done":
        has_finished_moving = True
        break
    current_value = int(boxes_moved)
    cubes = cubes - current_value

if has_finished_moving == True and cubes > 0:
    print(f"{cubes} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(cubes)} Cubic meters more.")