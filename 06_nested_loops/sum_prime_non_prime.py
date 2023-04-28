console_input = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0
is_non_prime = False

while console_input != "stop":
    input_to_int = int(console_input)
    if input_to_int < 0:
        print(f"Number is negative.")
        console_input = input()
        continue

    for number in range (2, input_to_int):
        if input_to_int % number == 0:
            is_non_prime = True
            break

    if is_non_prime:
        sum_non_prime_numbers += input_to_int
    else:
        sum_prime_numbers += input_to_int

    is_non_prime = False
    console_input = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")

