import sys

max_number = - sys.maxsize

command = input()

while command != "Stop":
    number = int(command)
    if max_number < number:
        max_number = number
    command = input()

print(max_number)