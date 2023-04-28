n = int(input())

for number in range (1111, 9999 + 1):
    counter = 0
    number_to_string = str(number)

    for symbol in range (0, len(number_to_string)):
        string_to_number = int(number_to_string[symbol])
        if string_to_number == 0:
            continue
        if n % string_to_number == 0:
            counter += 1

    if counter == 4:
        print(f"{number} ", end="")


